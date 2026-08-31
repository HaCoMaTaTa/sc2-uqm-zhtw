# One-shot v0.1 translation pipeline
$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
$root = $PSScriptRoot                          # pipeline/ (see docs/SOP_Rebuild_And_Release.md)
$repoRoot = Split-Path -Parent $root           # GitHubRepo/ (translation/, docs/ etc.)
Set-Location $root

# Coordinate with other sessions (build + package share zh-TW-addon/ and _stage/)
. "$root\_build_lock.ps1"
Enter-BuildLock

try {

# Step 0: zh-TW purity check (fail-fast on Chinese-English mix / simplified chars)
Write-Host "== Step 0: zh-TW purity check =="
python _check_zh_purity.py --strict
if ($LASTEXITCODE -ne 0) {
    throw "zh-TW purity check FAILED — fix violations before build."
}
python _check_lua_templates.py --strict
if ($LASTEXITCODE -ne 0) {
    throw "Lua template first-arg check FAILED — first args must be CJK (!StarSeed leaks English literal)."
}
python _check_line_counts.py --strict
if ($LASTEXITCODE -ne 0) {
    throw "Line-count alignment check FAILED — voice cue offsets require same line count as English source."
}
python _check_wrap_hostile.py --strict
if ($LASTEXITCODE -ne 0) {
    throw "Wrap-hostile character check FAILED — HIGH-severity FW char runs will corrupt render (see vux LIKE_BECAUSE ~~~~ bug v1.0.10)."
}
Write-Host ""

# Step 1: translate gamestrings
python translate_ui.py `
  --source "extracted\base\base\gamestrings.txt" `
  --translations "translations\gamestrings.zh-TW.json" `
  --out "zh-TW-addon\content\base\gamestrings.txt"

Write-Host ""

# Step 1b (zh-TW patch 009): append STAR_POSTFIX_ZH_BASE section (149 entries)
# Chinese star postfixes for hyperspace/interplanetary/encounter top-header.
# Requires engine patch 009 (STAR_POSTFIX_ZH_BASE constant added to gamestr.h).
# Safe with non-patched exe: extra entries are simply ignored.
python _append_star_postfix_zh.py `
  --gamestrings-json "translations\gamestrings.zh-TW.json" `
  --target-txt "zh-TW-addon\content\base\gamestrings.txt"

Write-Host ""

# Step 1c (zh-TW patch 010): star map race SoI labels
# Overrides ships/<race>/<file>.txt index 1 (race name shown on star map
# sphere-of-influence + combat/melee ship stat header) with Chinese labels.
# Pure addon shadow content — NO engine patch required. race_strings[0] and
# race_strings[2+] (ship name, captain names, description) stay English.
python _apply_race_zh_labels.py

Write-Host ""

# Step 2: translate setup menu
python translate_ui.py `
  --source "extracted\base\base\ui\setupmenu.txt" `
  --translations "translations\setupmenu.zh-TW.json" `
  --out "zh-TW-addon\content\base\ui\setupmenu.txt"

Write-Host ""

# Step 2b: translate cutscene intro (script-style TFI blocks)
python translate_intro.py `
  --source "extracted\base\base\cutscene\intro\intro.txt" `
  --translations "translations\intro.zh-TW.json" `
  --out "zh-TW-addon\content\base\cutscene\intro\intro.txt"

Write-Host ""

# Step 2b2: translate cutscene endings + game-overs (Round B · 54 TFI blocks)
# - ending/final.txt (42 blocks): SC2 主結局,老年艦長對孫兒敘事
# - gameover/deathmarch.txt (9 blocks): Kohr-Ah 統治結局 (女性 Primat 冷硬敘事)
# - gameover/defeated.txt/suicide.txt/surrendered.txt (1 each): 3 種死亡短訊
# canonical (v0.5.2 · Q1-Q9):
#   Grandfather/Grandma=爺爺/奶奶, angel=天使, Mark II=保留,
#   Chmmr crystals=查姆晶體, escape pod=逃生艙,
#   ignition key=引爆鑰匙, cleansing filth=淨化此污穢,
#   Kohr-Ah Primat=她/其後裔 (SC2 canon 女性領袖 lore)
$cutsceneFiles = @(
  @{ src="cutscene\ending\final.txt";       trans="final";        out="cutscene\ending\final.txt" },
  @{ src="cutscene\gameover\deathmarch.txt"; trans="deathmarch";  out="cutscene\gameover\deathmarch.txt" },
  @{ src="cutscene\gameover\defeated.txt";   trans="defeated";    out="cutscene\gameover\defeated.txt" },
  @{ src="cutscene\gameover\suicide.txt";    trans="suicide";     out="cutscene\gameover\suicide.txt" },
  @{ src="cutscene\gameover\surrendered.txt"; trans="surrendered"; out="cutscene\gameover\surrendered.txt" }
)
foreach ($cf in $cutsceneFiles) {
  $src = "extracted\base\base\$($cf.src)"
  $trans = "translations\$($cf.trans).zh-TW.json"
  $out = "zh-TW-addon\content\base\$($cf.out)"
  if ((Test-Path $src) -and (Test-Path $trans)) {
    python translate_intro.py `
      --source $src `
      --translations $trans `
      --out $out
    Write-Host ""
  }
}

# Step 2c: translate Ur-Quan Kzer-Za dialog (SEND_MESSAGE seed)
python translate_ui.py `
  --source "extracted\base\base\comm\urquan\urquan.txt" `
  --translations "translations\urquan.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\urquan\urquan.txt"

Write-Host ""

# Step 2d: translate Cdr. Hayes (commander) first-meeting dialog
# --allow-line-mismatch: comm blocks are per-voice-segment; extra \n only affects
# visual wrapping. CJK MUST wrap short (<= 9 chars/line for AlienTextWidth=143px)
# to avoid _count_lines() infinite loop in comm.c (getLineWithinWidth can't split
# CJK "words" without spaces).
python translate_ui.py `
  --source "extracted\base\base\comm\commander\commander.txt" `
  --translations "translations\commander.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\commander\commander.txt" `
  --allow-line-mismatch

Write-Host ""

# Step 2e: translate Slylandro (斯萊族) home-world dialog
# STRICT mode: JSON preserves English \n count per token for voice-cue alignment.
# Space-wrap done inline in JSON values (see translations/slylandro.zh-TW.json).
python translate_ui.py `
  --source "extracted\base\base\comm\slylandro\slylandro.txt" `
  --translations "translations\slylandro.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\slylandro\slylandro.txt"

Write-Host ""

# Step 2f: translate Shofixti (蘇菲斯特族) Tanaka/Katana dialog
# STRICT mode: JSON preserves English \n count per token for voice-cue alignment.
# Space-wrap done inline in JSON values (see translations/shofixti.zh-TW.json).
python translate_ui.py `
  --source "extracted\base\base\comm\shofixti\shofixti.txt" `
  --translations "translations\shofixti.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\shofixti\shofixti.txt"

Write-Host ""

# Step 2g: translate Pkunk (普恩族) mystical avian dialog
# STRICT mode: JSON preserves English \n count per token for voice-cue alignment.
python translate_ui.py `
  --source "extracted\base\base\comm\pkunk\pkunk.txt" `
  --translations "translations\pkunk.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\pkunk\pkunk.txt"

Write-Host ""

# Step 2h: translate Spathi (史怕族) Fwiffo dialog
# STRICT mode: JSON preserves English \n count per token for voice-cue alignment.
python translate_ui.py `
  --source "extracted\base\base\comm\spathi\spathi.txt" `
  --translations "translations\spathi.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\spathi\spathi.txt"

Write-Host ""

# Step 2i: translate Ilwrath (蛛狂族) Dogar/Kazon cult dialog (Phase 14c Level 3)
python translate_ui.py `
  --source "extracted\base\base\comm\ilwrath\ilwrath.txt" `
  --translations "translations\ilwrath.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\ilwrath\ilwrath.txt"

Write-Host ""

# Step 2j: translate Yehat (翼哈特族) clan dialog (Phase 14c Level 3)
python translate_ui.py `
  --source "extracted\base\base\comm\yehat\yehat.txt" `
  --translations "translations\yehat.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\yehat\yehat.txt"

Write-Host ""

# Step 2k: translate Orz (歐茲族) dimensional dialog (Phase 14c Level 3, dossier-strict Orz self-ref)
python translate_ui.py `
  --source "extracted\base\base\comm\orz\orz.txt" `
  --translations "translations\orz.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\orz\orz.txt"

Write-Host ""

# Step 2l: translate Kohr-Ah (烏寬柯亞族) cleansing dialog (Phase 14c Level 3, ritual voice)
python translate_ui.py `
  --source "extracted\base\base\comm\kohrah\kohrah.txt" `
  --translations "translations\kohrah.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\kohrah\kohrah.txt"

Write-Host ""

# Step 2l1: translate Syreen (塞蓮族) home-world dialog (L3+ audit R1: 39 rewrites)
# Native 17px syreen.fon is CJK-capable — rasterized directly (no shadow redirect).
python translate_ui.py `
  --source "extracted\base\base\comm\syreen\syreen.txt" `
  --translations "translations\syreen.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\syreen\syreen.txt"

Write-Host ""

# Step 2l2: translate Arilou (阿麗露族) trans-dimensional dialog (L3+ audit R3: 13 tokens)
# Native 9px arilou.fon too small for CJK — package_zh-TW.ps1 full-redirects to computer.fon (15px).
python translate_ui.py `
  --source "extracted\base\base\comm\arilou\arilou.txt" `
  --translations "translations\arilou.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\arilou\arilou.txt"

Write-Host ""

# Step 2l3: translate Chmmr (晶智族) fused-collective dialog (L3+ audit R2: 1 token)
# Native 10px chmmr.fon too small for CJK — package_zh-TW.ps1 full-redirects to computer.fon (15px).
python translate_ui.py `
  --source "extracted\base\base\comm\chmmr\chmmr.txt" `
  --translations "translations\chmmr.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\chmmr\chmmr.txt"

Write-Host ""

# Step 2l4: translate Druuge (毒賈族) Crimson Corporation dialog (L3+ audit R3: 8 tokens)
# Uses shared micro.fon (11px) already covered by existing hybrid redirect in package_zh-TW.ps1.
python translate_ui.py `
  --source "extracted\base\base\comm\druuge\druuge.txt" `
  --translations "translations\druuge.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\druuge\druuge.txt"

Write-Host ""

# Step 2l5: translate Supox (蘇菩族) Utricularia symbiote dialog (L3+ audit R3: 15 tokens)
# Uses shared slab.fon (34px) already in $fontsToRasterize (below).
python translate_ui.py `
  --source "extracted\base\base\comm\supox\supox.txt" `
  --translations "translations\supox.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\supox\supox.txt"

Write-Host ""

# Step 2l6: translate Umgah (陰嘎族) prank/Talking Pet dialog (Round 1 · 85 tokens, v0.1)
# Native 8px umgah.fon too small for CJK — package_zh-TW.ps1 full-redirects to computer.fon (15px).
python translate_ui.py `
  --source "extracted\base\base\comm\umgah\umgah.txt" `
  --translations "translations\umgah.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\umgah\umgah.txt"

Write-Host ""

# Step 2l7: translate Safe Ones (平安族 / 史怕族最高議會) dialog (Round 1 · 143 tokens, v0.5)
# RMP has no comm.safeones.font — engine uses context-inherited font (from Fwiffo → spathi.fon 15px).
# Voice aligned with 03_Characters/Safe_Ones_High_Council.md dossier + spathi.zh-TW.json canonical.
python translate_ui.py `
  --source "extracted\base\base\comm\safeones\safeones.txt" `
  --translations "translations\safeones.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\safeones\safeones.txt"

Write-Host ""

# Step 2l8: translate Talking Pet / neo-Dnyarri dialog (Round 1 · 112 tokens, v0.1)
# Native 11px talkingpet.fon too small for CJK — package_zh-TW.ps1 full-redirects to computer.fon (15px).
# Voice per 03_Characters/Talking_Pet.md dossier: 8 modes (假身分/心靈控制/求饱賣萌/諡媚合作/貨艙抱怨/悲情敘事/諺刺辱罵/破第四道牙).
python translate_ui.py `
  --source "extracted\base\base\comm\talkingpet\talkingpet.txt" `
  --translations "translations\talkingpet.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\talkingpet\talkingpet.txt"

Write-Host ""

# Step 2l9: translate Utwig (忧特族) mask etiquette + Ultron drama dialog (Round 2 · 114 tokens, v0.1)
# Native 18px utwig.fon CJK-viable — added to $fontsToRasterize (no shadow redirect needed).
# Voice per 02_Races/Utwig.md dossier: 2 stages (Ultron 損壞們薊式哀嚢 / Ultron 修復讚美詩狂喜).
python translate_ui.py `
  --source "extracted\base\base\comm\utwig\utwig.txt" `
  --translations "translations\utwig.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\utwig\utwig.txt"

Write-Host ""

# Step 2l10: translate Mycon (麥孔族) Juffo-Wup + 深淵之子 dialog (Round 2 · 109 tokens, v0.1)
# Native 15px mycon.fon CJK-viable — added to $fontsToRasterize (no shadow redirect needed).
# Voice per 02_Races/Mycon.md dossier: 集體心智真菌/禱詞式短句/零固定人格切換 (RAMBLE_5/15/28 個體名).
python translate_ui.py `
  --source "extracted\base\base\comm\mycon\mycon.txt" `
  --translations "translations\mycon.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\mycon\mycon.txt"

Write-Host ""

# Step 2l11: translate VUX (VUX 族) ZEX menagerie + hostile hostility dialog (Round 2 · 102 tokens, v0.1)
# Voice per 02_Races/VUX.md + 03_Characters/Admiral_ZEX.md dossier: 3 stages
#   ① ZEX 諂媚變態 (32 tokens): 本將軍/吾/珍藏/極品/肉塊生物/嘻！嘻！嘻！
#   ② VUX 一般敵對 (~45 tokens): 本官/爾等/醜陋/令人反胃/嗝！噁啊！
#   ③ VUX 反諷道歉 (25 tokens): 玩家道歉 → VUX 每次不同理由拒絕 → TRUTH 破口大吐真相
# canonical: VUX (保留原文), ZEX=澤克斯, DAX=達克斯, YAX=雅克斯, ZEN DUX=禪·杜克斯
# Native 13px vux.fon — added to $fontsToRasterize (borderline CJK, similar to pkunk 14px).
python translate_ui.py `
  --source "extracted\base\base\comm\vux\vux.txt" `
  --translations "translations\vux.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\vux\vux.txt"

Write-Host ""

# Step 2l12: translate Thraddash (撻伐族) Culture Nineteen -> Culture Twenty dialog (Round 3 · 152 tokens, v0.1)
# Voice per 02_Races/Thraddash.md + Ultronomicon Culture 2-20 history: 6 stages
#   ① HOSTILE 敵對 (~35): 本族/吾等/爾等/弱者;短促句+SNORT!哼！+HARG!哈！
#   ② IMPRESSED/拜師 (~20): Great Teacher=偉大導師;極度恭敬轉折
#   ③ CULTURAL EXPERIMENTS 學風格 (~20): Polite/Rhyme(中文押韻)/Pig Latin(保原文+中譯註)/Like Us
#   ④ CULTURE NAMING (~10): 誇張莊嚴+GRUNT!嗯哼！+對玩家指名順從
#   ⑤ ALLY 常態 (~15): 揭密 Aqua Helix=蔚藍螺旋 (canonical 升級,取代舊「水螺旋」暫定)
#   ⑥ META (Ilwrath 戰爭 + OUT_TAKES ~5): 狂喜+演員抱怨定型
# canonical: Aqua Helix=蔚藍螺旋(v0.5.2 升級), Culture X=第X文化, Korgk/Reeunk/etc 音譯+首介英文
# thraddash.fon 11px too small for CJK — full-redirect to computer.fon (see package_zh-TW.ps1).
python translate_ui.py `
  --source "extracted\base\base\comm\thraddash\thraddash.txt" `
  --translations "translations\thraddash.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\thraddash\thraddash.txt"

Write-Host ""

# Step 2l13: translate Zoq-Fot-Pik (佐-佛-皮) 3合1物種對話 (Round 3 · 334 tokens, v0.1)
# Voice per 02_Races/Zoq_Fot_Pik.md + Ultronomicon (Frungy/Zebranky/guy in back):
#   三合一物種輪流發言 (Zoq=綠植冷靜/Fot=藍彈簧神經質/Pik=褐獨眼興奮愛 Frungy) + 沉默第四位
#   遊戲引擎控制動畫切換,JSON 不加前綴
# canonical (v0.5.2): Frungy=芙戎奇（Frungy）首介英文 (對齊 Phase 14c/d 廢止 dossier 保留原文),
#   The Sport of Kings=諸王之運動, Zebranky=澤布蘭基（Zebranky）, Zoq-Fot-Pik=佐-佛-皮 (3字),
#   Stinger=刺針號, 7 個體音譯首介, coreward=銀核方向 (canonical 升級 starbase 舊「核向」)
# zoqfotpik.fon 10px too small for CJK — full-redirect to computer.fon (see package_zh-TW.ps1).
python translate_ui.py `
  --source "extracted\base\base\comm\zoqfotpik\zoqfotpik.txt" `
  --translations "translations\zoqfotpik.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\zoqfotpik\zoqfotpik.txt"

Write-Host ""

# Step 2l14: translate Melnorme (梅諾商) 綠光貿易官 · 資訊/科技/燃料仲介 (Round 3 · 281 tokens, v0.1)
# Voice per 02_Races/Melnorme.md + Ultronomicon (Trade Master):
#   華麗商務敬語 (「敝方/本商行/本人」自稱,「艦長/尊貴的顧客/吾之友人」對玩家),
#   雙面性格 (拍賣師 vs 學者), 招牌 catchphrase「好好考慮,仔細考慮」,
#   於所有情境必勝之艦 (Ur-Quan devise 對譯), 拒議價時嚴詞:「不接受議價」
# canonical (v0.5.2 · Q1-Q18):
#   Q1 Excruciator=苦刑器 (canonical升級,取代舊「極痛裝置」暫定 → retrofit starbase/talkingpet/urquan),
#   Q2 Interstar Credits=星幣 (canonical升級 → retrofit Trade_Master_Greenish.md 敘述用「信用點數」),
#   Q3 Burvixese=布維族 (canonical確認 → retrofit druuge 舊「波維克塞族」),
#   Q4 Hellbore Cannon=火獄穿甲炮/Shiva Furnace=濕婆熔爐/Blaster=爆能砲/Auto-Tracking Module=自動追蹤模組,
#   Q5 Planet Lander=登陸艇/Turning Jet=轉向噴射器/Storage Bay=貨艙/Dynamo=能量發電機模組/stunray bolt-beamer gun=昏定波束槍,
#   Q6 Ochre=赭黃副官/Dramya=卓米雅/Gg=Gg族,
#   Q7 MetaChron=超時鐘/Tzo crystal=佐晶/Waiver of Damages=免責同意書,
#   Q9 Ahhh-YING! 保留原文+譯註「梅諾商冥想咒語」,
#   Q10 Fe-Fi-Fo-Fum! 保留原文+童話註「英國巨人童話台詞」,
#   Q11 Hoy!=喂！ Q12 Inter-Dimensional Fatigue (IDF)=跨維穿隙 首介全稱+縮寫,
#   Q17 Presto!=變！ LOOK OUT!=當心！ Q18 30 ENUMERATE stubs (一/二/三/.../百/千 + 與 + 零)
# melnorme 對話使用預設 commander.fon (無專屬 melnorme.fon,commander.fon 已由 computer.fon full-redirect)。
python translate_ui.py `
  --source "extracted\base\base\comm\melnorme\melnorme.txt" `
  --translations "translations\melnorme.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\melnorme\melnorme.txt"

Write-Host ""

# Step 2l15: translate Yehat Rebels (翼哈特叛軍) 反抗女皇星艦氏族 (Round 4 · 34 tokens, v0.1)
# Voice per 02_Races/Yehat.md + Ultronomicon (Cheep-Guava/Braky Girdy):
#   反抗派更悲壯抒情、稱玩家「兄弟/戰友」,蘇格蘭 ye/yer/fer → 微文言 + 頓句;
#   兩派態度:革命成功期激昂 vs HATE_PKUNK_REBEL 仍保部分保皇派恨意反應。
# canonical (v0.5.2 · Q1-Q8):
#   Q1 Cheep-Guava=奇普-瓜瓦, Q2 Veep-Kreep Clan=維普克利普氏族, Q3 Braky Girdy the First=布拉基·葛迪一世,
#   Q4 Great Beyond=蒼宇彼方, Q5 harpy Queen=鷹身女妖女皇/false Queen=偽女皇/harridan=十足的潑婦,
#   Q6 Pkunk Fury=烈憤艦 (避開 Thraddash 火炬艦撞名), Q7 Fortress Square=堡壘方陣/Dynamic Triangle=機動三角陣,
#   Q8 Primat (VUX)=總議長 (避開 Kohr-Ah Primat=總主宰混淆)
# yehatrebels 無專屬字型,使用預設 commander.fon (由 computer.fon full-redirect)。
python translate_ui.py `
  --source "extracted\base\base\comm\yehatrebels\yehatrebels.txt" `
  --translations "translations\yehatrebels.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\yehatrebels\yehatrebels.txt"

Write-Host ""

# Step 2l16: translate Slylandro Probe (斯萊探測器) 故障 Precursor 自複製採礦探針 (Round 4 · 86 tokens, v0.1)
# Voice per 02_Races/Slylandro_Probe.md + Ultronomicon:
#   Monotone loudspeaker CAPS 語調,冰冷公式化,無情感;
#   招牌反諷:「和平而來」+「拆解目標」;dossier §六 短句 + 全形句點手法。
# canonical (v0.5.2 · Q9-Q12):
#   Q9 CAPS = 短句 + 全形句點 monotone (無方括號、無標籤);
#   Q10 PROBE 2418-B = 保留 2418-B 編號原文;
#   Q11 ENACTING THIRD LAW = 執行第三定律（自保）。 [B2 括號註,Asimov 致敬 + 自解釋];
#   Q12 ENUMERATE 數字 = 中文數字 (零/一/二/.../九十/百/千) 機器廣播讀感更 monotone
# probe 無專屬字型,使用預設 commander.fon (由 computer.fon full-redirect)。
python translate_ui.py `
  --source "extracted\base\base\comm\probe\probe.txt" `
  --translations "translations\probe.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\probe\probe.txt"

Write-Host ""

# Step 2m: translate Starbase (Cdr. Hayes ongoing dialog, 267 tokens, v0.5)
# Covers: greetings, load reports, STARBASE_IS_READY intro, ABOUT_* info dumps,
# 23 STARBASE_BULLETIN_* mission bulletins, device analyses, and player options.
# Voice consistency with commander.zh-TW.json (first-meeting Hayes).
python translate_ui.py `
  --source "extracted\base\base\comm\starbase\starbase.txt" `
  --translations "translations\starbase.zh-TW.json" `
  --out "zh-TW-addon\content\base\comm\starbase\starbase.txt"

Write-Host ""

# Step 2f: translate lander/energy reports (Moon Base + 32 alien installations)
# Enabled by our patched UrQuanMasters.exe (report.c strlen -> utf8StringCount).
# Uses --allow-line-mismatch since these are text reports (no voice cue timing).
$landerFiles = @(
  "moonbase",
  "urquanbase",
  # Group A (13 Precursor artifact pickup reports, v0.7 2026-08-13):
  "aquahelix",
  "burvixcaster",
  "eggcase",
  "fwiffo",
  "maidens",
  "motherark",
  "sphere",
  "spindle",
  "sundevice",
  "taalodevice",
  "ultron",
  "umgahcaster",
  "utwigbomb",
  # Group B (11 place/base reports, v0.7 2026-08-13):
  "chmmrbase",
  "chmmrhome",
  "destroyedbase",
  "earthbase",
  "precursorbase",
  "shofixtibase",
  "spathimonument",
  "syreenbase",
  "syreenvault",
  "urquanwreck",
  "zfpcolony",
  # Group C (6 ruins + large narrative reports, v0.7 2026-08-13):
  "algoliteruins",
  "androsynth_ruins",
  "burvixeseruins",
  "excavationsite",
  "ruins",
  "stele"
)
foreach ($lf in $landerFiles) {
  $src = "extracted\base\base\lander\energy\$lf.txt"
  $trans = "translations\lander\$lf.zh-TW.json"
  $out = "zh-TW-addon\content\base\lander\energy\$lf.txt"
  if ((Test-Path $src) -and (Test-Path $trans)) {
    python translate_ui.py `
      --source $src `
      --translations $trans `
      --out $out `
      --allow-line-mismatch
    Write-Host ""
  }
}

# Step 2f2: translate lander/bio reports (v1.0.11 · vuxbeast).
# base/lander/bio/ has only 1 file (vuxbeast.txt). Was missed by v0.7 B1B/B1C
# batches — 造成玩家抓 VUX 獸時 report 全英文 (v1.0.7-1.0.10 build gap).
$landerBioFiles = @(
  "vuxbeast"
)
foreach ($lf in $landerBioFiles) {
  $src = "extracted\base\base\lander\bio\$lf.txt"
  $trans = "translations\lander\bio\$lf.zh-TW.json"
  $out = "zh-TW-addon\content\base\lander\bio\$lf.txt"
  if ((Test-Path $src) -and (Test-Path $trans)) {
    python translate_ui.py `
      --source $src `
      --translations $trans `
      --out $out `
      --allow-line-mismatch
    Write-Host ""
  }
}

# Step 3: extract all unique CJK chars from translated files
$chars = ""
foreach ($f in @(
    "zh-TW-addon\content\base\gamestrings.txt",
    "zh-TW-addon\content\base\cutscene\intro\intro.txt",
    "zh-TW-addon\content\base\cutscene\ending\final.txt",
    "zh-TW-addon\content\base\cutscene\gameover\deathmarch.txt",
    "zh-TW-addon\content\base\cutscene\gameover\defeated.txt",
    "zh-TW-addon\content\base\cutscene\gameover\suicide.txt",
    "zh-TW-addon\content\base\cutscene\gameover\surrendered.txt",
    "zh-TW-addon\content\base\comm\urquan\urquan.txt",
    "zh-TW-addon\content\base\comm\commander\commander.txt",
    "zh-TW-addon\content\base\comm\starbase\starbase.txt",
    "zh-TW-addon\content\base\comm\slylandro\slylandro.txt",
    "zh-TW-addon\content\base\comm\shofixti\shofixti.txt",
    "zh-TW-addon\content\base\comm\pkunk\pkunk.txt",
    "zh-TW-addon\content\base\comm\spathi\spathi.txt",
    "zh-TW-addon\content\base\comm\ilwrath\ilwrath.txt",
    "zh-TW-addon\content\base\comm\yehat\yehat.txt",
    "zh-TW-addon\content\base\comm\orz\orz.txt",
    "zh-TW-addon\content\base\comm\kohrah\kohrah.txt",
    "zh-TW-addon\content\base\comm\syreen\syreen.txt",
    "zh-TW-addon\content\base\comm\arilou\arilou.txt",
    "zh-TW-addon\content\base\comm\chmmr\chmmr.txt",
    "zh-TW-addon\content\base\comm\druuge\druuge.txt",
    "zh-TW-addon\content\base\comm\supox\supox.txt",
    "zh-TW-addon\content\base\comm\umgah\umgah.txt",
    "zh-TW-addon\content\base\comm\safeones\safeones.txt",
    "zh-TW-addon\content\base\comm\talkingpet\talkingpet.txt",
    "zh-TW-addon\content\base\comm\utwig\utwig.txt",
    "zh-TW-addon\content\base\comm\mycon\mycon.txt",
    "zh-TW-addon\content\base\comm\vux\vux.txt",
    "zh-TW-addon\content\base\comm\thraddash\thraddash.txt",
    "zh-TW-addon\content\base\comm\zoqfotpik\zoqfotpik.txt",
    "zh-TW-addon\content\base\comm\melnorme\melnorme.txt",
    "zh-TW-addon\content\base\comm\yehatrebels\yehatrebels.txt",
    "zh-TW-addon\content\base\comm\probe\probe.txt",
    "zh-TW-addon\content\base\lander\energy\moonbase.txt",
    "zh-TW-addon\content\base\lander\energy\urquanbase.txt",
    "zh-TW-addon\content\base\lander\energy\aquahelix.txt",
    "zh-TW-addon\content\base\lander\energy\burvixcaster.txt",
    "zh-TW-addon\content\base\lander\energy\eggcase.txt",
    "zh-TW-addon\content\base\lander\energy\fwiffo.txt",
    "zh-TW-addon\content\base\lander\energy\maidens.txt",
    "zh-TW-addon\content\base\lander\energy\motherark.txt",
    "zh-TW-addon\content\base\lander\energy\sphere.txt",
    "zh-TW-addon\content\base\lander\energy\spindle.txt",
    "zh-TW-addon\content\base\lander\energy\sundevice.txt",
    "zh-TW-addon\content\base\lander\energy\taalodevice.txt",
    "zh-TW-addon\content\base\lander\energy\ultron.txt",
    "zh-TW-addon\content\base\lander\energy\umgahcaster.txt",
    "zh-TW-addon\content\base\lander\energy\utwigbomb.txt",
    "zh-TW-addon\content\base\lander\energy\chmmrbase.txt",
    "zh-TW-addon\content\base\lander\energy\chmmrhome.txt",
    "zh-TW-addon\content\base\lander\energy\destroyedbase.txt",
    "zh-TW-addon\content\base\lander\energy\earthbase.txt",
    "zh-TW-addon\content\base\lander\energy\precursorbase.txt",
    "zh-TW-addon\content\base\lander\energy\shofixtibase.txt",
    "zh-TW-addon\content\base\lander\energy\spathimonument.txt",
    "zh-TW-addon\content\base\lander\energy\syreenbase.txt",
    "zh-TW-addon\content\base\lander\energy\syreenvault.txt",
    "zh-TW-addon\content\base\lander\energy\urquanwreck.txt",
    "zh-TW-addon\content\base\lander\energy\zfpcolony.txt",
    "zh-TW-addon\content\base\lander\energy\algoliteruins.txt",
    "zh-TW-addon\content\base\lander\energy\androsynth_ruins.txt",
    "zh-TW-addon\content\base\lander\energy\burvixeseruins.txt",
    "zh-TW-addon\content\base\lander\energy\excavationsite.txt",
    "zh-TW-addon\content\base\lander\energy\ruins.txt",
    "zh-TW-addon\content\base\lander\energy\stele.txt",
    "zh-TW-addon\content\base\lander\bio\vuxbeast.txt",
    "zh-TW-addon\content\base\ui\setupmenu.txt"
)) {
  if (Test-Path $f) {
    $chars += (Get-Content $f -Raw -Encoding UTF8)
  }
}
# Also seed with the terminology master list so future additions reuse fonts.
# Phase 12: 詞彙表已遷移到 translation/Reference_Material/
$chars += (Get-Content "$repoRoot\translation\Reference_Material\SC2-詞彙對照表.md" -Raw -Encoding UTF8)
# Also seed with Phase 8 v0.4 canonical glossary (Fixed_Terms.csv covers new v0.4 race names)
$fixedTermsCsv = "$repoRoot\translation\07_Glossary\Fixed_Terms.csv"
if (Test-Path $fixedTermsCsv) {
  $chars += (Get-Content $fixedTermsCsv -Raw -Encoding UTF8)
}

# Write concatenated chars to a temp file for the rasterizer
$charsFile = "$root\translations\_used_chars.txt"
$chars | Set-Content $charsFile -Encoding UTF8
Write-Host "Char pool size (bytes): $((Get-Item $charsFile).Length)"

Write-Host ""

# Step 4: rasterize fonts for all needed chars.
# CRITICAL: only rasterize fonts with reference PNG height >= 14px.
# Smaller fonts produce illegible CJK glyphs (see _analysis/_race_font_survey.py).
$fontsToRasterize = @(
  "slab.fon",          # 34 px - main menu / prominent UI text
  "slides.fon",        # 20 px - intro/ending narrative
  "urquan.fon",        # 16 px - Ur-Quan Kzer-Za dialog
  "kohrah.fon",        # 16 px - Ur-Quan Kohr-Ah dialog (Phase 14c)
  "shofixti.fon",      # 16 px - Shofixti (Tanaka/Katana) dialog
  "ilwrath.fon",       # 15 px - Ilwrath cult dialog (Phase 14c)
  "orz.fon",           # 15 px - Orz dimensional dialog (Phase 14c)
  "computer.fon",      # 15 px - computer terminal messages (borderline)
  "spathi.fon",        # 15 px - Spathi (Fwiffo) dialog
  "mycon.fon",         # 15 px - Mycon Juffo-Wup + 深淏之子 dialog (Round 2 v0.1)
  "utwig.fon",         # 18 px - Utwig mask etiquette dialog (Round 2 v0.1)
  "syreen.fon",        # 17 px - Syreen (Talana) dialog (L3+ audit)
  "pkunk.fon",         # 14 px - Pkunk mystical avian dialog
  "yehat.fon",         # 14 px - Yehat clan dialog (Phase 14c)
  "slylandro.fon",     # 14 px - Slylandro home-world dialog
  "vux.fon"            # 13 px - VUX + ZEX menagerie dialog (Round 2 v0.1;borderline CJK)
)

# CJK-capable fonts NOT yet rasterized (add when translating those races):
#   utwig.fon (18px), mycon.fon (15px)
# Small fonts CANNOT host CJK (would be unreadable):
#   starcon.fon (7px), label.fon (10px), tiny*.fon (7px),
#   commander.fon (9px), player.fon (10px), playmenu.fon (11px),
#   arilou.fon (9px), chmmr.fon (10px), thraddash.fon (11px), etc.
#   These are handled via full-redirect in package_zh-TW.ps1 (arilou/chmmr → computer.fon).

foreach ($f in $fontsToRasterize) {
  $refPath = "extracted\base\base\fonts\$f"
  if (-not (Test-Path $refPath)) {
    Write-Host "  skip: $f not in reference" -ForegroundColor DarkGray
    continue
  }
  python rasterize_font.py `
    --ref-font $refPath `
    --ttf "C:\Windows\Fonts\NotoSansTC-VF.ttf" `
    --chars-file $charsFile `
    --extra-padding 0 `
    --out "zh-TW-addon\content\base\fonts\$f" 2>&1 |
    Select-String -Pattern "Reference:|Rasterized:|Weight" | ForEach-Object { "  $($_.Line)" }
}
# NOTE: --extra-padding 0 removes 1px of horizontal padding per glyph.
# Combined with kerndat's CharSpace=1, adjacent CJK glyphs sit ~1 canvas px
# apart (was ~4-5px with default padding=1, which looked like large spaces
# on-screen at 2x scale). Original ASCII PNGs are preserved by the rasterizer
# (only CJK codepoints get regenerated).

# Extra: shrink ASCII space (U+0020) glyph in dialog fonts. CJK translations
# use space-delimited chunks as word-wrap hints, but the default 5-6 px space
# makes chunk boundaries visually gappy. Reducing to 2 px is safe.
python _scripts\shrink_cjk_dialog_space_glyph.py 2>&1 |
    ForEach-Object { "  $_" }

# Regenerate the SpaceJunkFrame[18/21] override PNGs that widen the lander
# report cell grid from 5x5 to 8x10 (so CJK glyphs get breathing room).
# Untracked by git (.gitignore excludes content/), so must be regenerated
# every build. Missing => moonbase report re-cramps + report.c adaptive
# cell patch falls back to 5x5 which overlaps CJK 8x8 glyphs.
Write-Host ""
Write-Host "==== nav/orbitbackground override for lander report cells ====" -ForegroundColor Cyan
python _scripts\make_report_cells.py 2>&1 | ForEach-Object { "  $_" }

# Extra: small CJK glyphs via Fusion Pixel 8px TTF.
# 8px design fits perfectly: ink ~7 rows, PC_MENU_HEIGHT=8 → 1 row natural gap.
# Ink aligns with highlight rect (which is 7 rows tall).
# Feeds the "hybrid" font-shadow mode in package_zh-TW.ps1 for the
# PC-mode menu (starcon.fon, PC_MENU_HEIGHT=8 slots).
Write-Host ""
Write-Host "==== Small-CJK rasterization (Fusion 8px, aligns with highlight) ====" -ForegroundColor Cyan
$smallCjkOut = "zh-TW-addon\_intermediate\cjk-fusion-gap"
$fusionTtf = "_downloads\fusion-pixel-8px\fusion-pixel-8px-proportional-zh_hant.ttf"
Remove-Item $smallCjkOut -Recurse -Force -ErrorAction SilentlyContinue
python rasterize_font.py `
  --ref-font "extracted\base\base\fonts\label.fon" `
  --ttf $fusionTtf `
  --font-size 8 `
  --png-height 10 `
  --latin-bottom 9 `
  --chars-file $charsFile `
  --no-aa `
  --aa-threshold 96 `
  --out $smallCjkOut 2>&1 |
  Select-String -Pattern "Reference:|Rasterized:|Weight|OVERRIDDEN|latin_" | ForEach-Object { "  $($_.Line)" }

# Extra 2: Fusion Pixel 10px CJK for tiny.bold.fon (lander pickup text).
# Larger 10px design gives better readability for mineral names during
# planet exploration. Only used by tiny.bold.fon shadow (see package script).
Write-Host ""
Write-Host "==== Extra CJK (Fusion 10px, for lander/pickup) ====" -ForegroundColor Cyan
$largeCjkOut = "zh-TW-addon\_intermediate\cjk-fusion10-normal"
$fusion10Ttf = "_downloads\fusion-pixel-10px\fusion-pixel-10px-proportional-zh_hant.ttf"
Remove-Item $largeCjkOut -Recurse -Force -ErrorAction SilentlyContinue
python rasterize_font.py `
  --ref-font "extracted\base\base\fonts\label.fon" `
  --ttf $fusion10Ttf `
  --font-size 10 `
  --png-height 10 `
  --chars-file $charsFile `
  --no-aa `
  --aa-threshold 96 `
  --out $largeCjkOut 2>&1 |
  Select-String -Pattern "Reference:|Rasterized:|Weight|OVERRIDDEN|latin_" | ForEach-Object { "  $($_.Line)" }

Write-Host ""
Write-Host "==== v0.1 addon 檔案清單（依目錄） ====" -ForegroundColor Cyan
Get-ChildItem "zh-TW-addon\content" -Recurse -File |
  Group-Object DirectoryName |
  Sort-Object Name |
  ForEach-Object { "  {0}  {1} files" -f $_.Name.Substring($_.Name.IndexOf("content") + 8), $_.Count }

} finally {
    Exit-BuildLock
}

