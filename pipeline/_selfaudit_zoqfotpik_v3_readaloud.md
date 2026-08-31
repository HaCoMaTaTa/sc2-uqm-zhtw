# Zoq-Fot-Pik Read-Aloud Self-Audit (v0.7.1) · 2026-08-17

## 統計
- Total tokens: 334
- 命中「直譯生硬」項目: 7 (2.1%)
- 分類統計：
  - § 4.5.1 英文語序殘留 / 冗餘代詞：1 (SCOUT_HELLO1 audio-line 對齊)
  - § 4.5.2 中文語感（生硬直譯）：2 (UNDER_ATTACK7 「散亂的擊發」→「流彈」 · THANKS_FOR_RESCUE9 「話說回來，這樣的話」重複)
  - § 4.5.4 招牌詞漏套：1 (OUT_TAKES4 對齊 dossier §六 例 5「善終將戰勝惡」)
  - § 4.5.5 大聲讀測試（讀來卡舌）：3 (ALLY_WITH_US5 「錯過不起」· KOHRAH_FRENZY6 L1 「我們唯一」孤零 · KOHRAH_FRENZY8 L4 遺漏 Buppo 主體)
- 未動 tokens: 327

---

## 修訂項

### #1 · SCOUT_HELLO1 · § 4.5.5 audio-line 對齊 + § 4.5.1 語序台化

**原譯**（partial-1 clean-room 初稿）：
> 我們穿越了充滿敵意、未經標記的太空\n遠道而來\n為的是找到你。\n我們來自座標為\n〔齊格佛-葛爾爾努，阿-阿，帕霍伊-霍伊〕（佐-佛-皮自造座標系）的 <綠色> 矮星。

**自審修**：
> 我們遠道而來\n穿越充滿敵意、未經標記的太空\n才找到你。\n我們來自座標為\n〔齊格佛-葛爾爾努，阿-阿，帕霍伊-霍伊〕（佐-佛-皮自造座標系）的 <綠色> 矮星。

**類別**：§ 4.5.5 audio-line 對齊
**原因**：EN 五行順序 = "We have travelled far / through hostile, uncharted space / to find you. / We hail from the ... at coordinates / ziggerfau-gerrrnuf...". 初稿 L1 = 太空描述，會與 EN L1 audio「travelled far」錯位。改為對齊 EN 順序。

---

### #2 · UNDER_ATTACK7 · § 4.5.2 生硬直譯

**原譯**：
> ……他們偏好在強重力井附近作戰。\n他們散亂的擊發常打中我們的行星表面\n通常後果慘不忍睹。

**自審修**：
> ……他們偏好在強重力井附近作戰。\n他們的流彈常打中我們的行星表面\n通常後果慘不忍睹。

**類別**：§ 4.5.2 生硬直譯（EN "stray shots" 直搬「散亂的擊發」→ TW natural「流彈」）

---

### #3 · ALLY_WITH_US5 · § 4.5.5 大聲讀卡舌

**原譯**：
> 多好的交易，對吧？\n你絕對錯過不起！\n所以你意下如何？

**自審修**：
> 多好的交易，對吧？\n你錯過就虧大了！\n所以你意下如何？

**類別**：§ 4.5.5 大聲讀測試（「錯過不起」語序不順）· EN "You can't afford to pass it up!" → TW natural「錯過就虧大了」

---

### #4 · KOHRAH_FRENZY6 · § 4.5.5 audio-line + § 4.5.2 L1 過短孤零

**原譯**：
> 我們唯一\n可能幫得上你打敗他們的知識\n是我們從 <巨爵座> 星座\n那位特工布波那裡收到的一段殘破訊息。

**自審修**：
> 我們僅有的一項知識\n或許能助你擊敗他們\n那是一段殘破的訊息，來自我們駐 <巨爵座> 星座\n那位特工布波所發送。

**類別**：§ 4.5.5 audio-line 對齊 + § 4.5.2 L1「我們唯一」孤零僅 4 字 · EN "The only piece of knowledge we have / that may help you defeat them / is a fragment of a transmission we received / from our agent Buppo who was in the ... constellation." — 每行語義單元完整

---

### #5 · KOHRAH_FRENZY8 · § 4.5.5 L4 遺漏 Buppo 主體

**原譯**：
> 他報告說柯亞有樣東西\n「又大又危險又重要得要命」\n就在附近某個恆星系裡。\n訊號在斷之前，我們就只收到這些。

**自審修**：
> 他報告說柯亞有樣東西\n「又大又危險又重要得要命」\n就在附近某個恆星系裡。\n這是布波訊號中斷前我們收到的全部內容。

**類別**：§ 4.5.5 L4 EN 明指 "before Buppo's signal was cut off" · 初稿只寫「訊號在斷之前」丟失布波主體（不同輪拌嘴中 Buppo 已於 FRENZY7 出現，L4 應收束回 Buppo audio 而非只是抽象「訊號」）

---

### #6 · OUT_TAKES4 · § 4.5.4 招牌詞漏套（dossier §六 例 5）

**原譯**：
> 芙戎奇跟本遊戲一點關係也沒有！\n本遊戲主題是戰爭、奴役、偏執\n英雄氣概、正義，還有善必終將戰勝惡！

**自審修**：
> 芙戎奇跟本遊戲一點關係也沒有！\n本遊戲主題是戰爭、奴役、偏執\n英雄氣概、正義，還有善終將戰勝惡！

**類別**：§ 4.5.4 招牌詞漏套（dossier §六 例 5 canonical 為「善終將戰勝惡」· 初稿「善必終將」多贅字破壞 rhythm）· EN "the inevitable triumph of Good over Evil!" — 「inevitable」內建於「終將」中

---

### #7 · THANKS_FOR_RESCUE9 · § 4.5.2 重複贅詞

**原譯**：
> 話說回來，這樣的話，寧可犧牲那些朱克獸跟納夫獸，總好過犧牲我們吧？

**自審修**：
> 好啦，這樣的話，寧可犧牲那些朱克獸跟納夫獸，也不要犧牲我們，對吧？

**類別**：§ 4.5.2 中文語感（「話說回來」+「這樣的話」連續兩個「話」贅字）· EN "Well in that case, better those Jukes and Narfs than us, right?" — Well = 好啦 · 排除「話說回來」重複

---

## 未動理由摘要

- **爾** 2 次殘留（葛爾爾努 = 音譯 gag / 多爾夫 = Round 3 Q11 canonical 音譯）· 均非文言助詞 · 保留
- **兒** 1 次殘留（哥兒們 = TW natural）· 保留
- **之** 19 次殘留（諸王之運動 canonical × 2 · <捕獲>之帝國 name_4 canonical × 1 · 之前/之後/之時/之間/之一/總之 modern TW usage × 16）· 保留
- 三方拌嘴 icon 無前綴換行 · Q5 保留 shipped 慣例
- Fortunately/Unfortunately 三次翻轉 icon「幸運的是……/不幸的是……」全部保留 · Q6=A
- OUT_TAKES Did not/Did too 遞減式「才沒有！/就有！/沒有！/有！」保留 shipped · Q10=A
