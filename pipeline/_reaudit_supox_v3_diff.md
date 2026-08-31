# Supox v3 vs Shipped · Rebuild-Compare Diff Report

**Race**: Supox (蘇菩族) · **Method**: v0.7 dossier-based Rebuild-Compare  
**Timestamp**: 2026-08-17 · Q&A locked (Q1B/Q2A/Q3A/Q4B/Q5A/Q6C/Q7A/Q8A/Q9A/Q10A/Q11B/Q12A)  
**Total tokens**: 93  ·  **Changed**: 29  ·  **Identical**: 64  

## Summary

| Marker | Count | Meaning |
|---|---:|---|
| 🔴 Critical | 0 | Voice/identity 重大變更 |
| 🟠 Major | 13 | canonical / 招牌 icon 更新 |
| 🟡 Minor | 16 | voice 保留 · 細節微調 |
| ✨ New | 0 | canonical 升級/招牌 icon 首次應用 |
| 🟢 Identical | 64 | 未變（Q&A 鎖定保留 shipped） |

## Decision quick-answer template

```
🔴 全 <A|B|C>
🟠 全 <A|B|C|依推薦>
🟡 全 <A|B|C|依推薦>
✨ 全 <A|B|C|依推薦>
（如有個別 override 於下方列出）
```

## 🟠 Major (13 tokens)

### `NEUTRAL_SPACE_HELLO_1`

**EN**:
```
Greetings Fellow Carbon Creature, may your roots always be well watered.
```
**A · shipped**:
```
問候，同為碳基造物的朋友，願您的根永遠得到充分灌溉。
```
**B · v3**:
```
問候您，碳基同胞。 願您的根永遠得到灌溉。
```
🟠 **推薦：B** · 碳基同胞 canonical (Q6C 招牌) · 節奏調整 dossier §六例 1 · F5 fluency: 永得→永遠得到


### `NEUTRAL_SPACE_HELLO_2`

**EN**:
```
Hello, Voyager. May the light always reach your leaves.
```
**A · shipped**:
```
哈囉，遠行者。 願光永遠照到您的葉。
```
**B · v3**:
```
哈囉，航行者。 願光永遠照到您的葉。
```
🟠 **推薦：B** · 航行者 canonical (Q6C 招牌) · F6 fluency: 永達→永遠照到


### `NEUTRAL_HOMEWORLD_HELLO_1`

**EN**:
```
Greetings Fellow Carbon Creature, may your roots always be well watered.
```
**A · shipped**:
```
問候，同為碳基造物的朋友，願您的根永遠得到充分灌溉。
```
**B · v3**:
```
問候您，碳基同胞。 願您的根永遠得到灌溉。
```
🟠 **推薦：B** · 碳基同胞 canonical (Q6C 招牌) · F5 fluency


### `NEUTRAL_HOMEWORLD_HELLO_2`

**EN**:
```
Hello, Voyager. May the light always reach your leaves.
```
**A · shipped**:
```
哈囉，遠行者。 願光永遠照到您的葉。
```
**B · v3**:
```
哈囉，航行者。 願光永遠照到您的葉。
```
🟠 **推薦：B** · 航行者 canonical (Q6C 招牌) · F6 fluency


### `UTWIG_NEARBY`

**EN**:
```
We share this region of space with the Utwig, the Wearers of Masks.
We have a strong cultural bond with the Utwig.
They have been the foundation around which we have grown our starfaring culture.
We are not only allies, but we are also friends.
You should go meet with them. They could use some excitement.
You see, they are a little depressed and morose right now.
Usually they are most festive and fun.
```
**A · shipped**:
```
共生之枝與憂特族共享此星域，那戴著面具的一族。
我方與憂特族有著堅實的文化連結。
他們是我方星際文明生長之基石。
我方不僅是盟友，也是朋友。
您應該去見他們。 他們需要一些激勵。
您看，他們現在有點沮喪與陰鬱。
通常他們是最愛慶祝、最有趣的。
```
**B · v3**:
```
共生之枝與憂特族，即面具族，共享此星域。
我方與憂特族有著堅實的文化連結。
他們是我方星際文明生長之基石。
我方不僅是盟友，也是朋友。
您應該去見他們。 他們需要一些激勵。
您看，他們現在有點沮喪與陰鬱。
通常他們是最愛慶祝、最有趣的。
```
🟠 **推薦：B** · Wearers of Masks → 面具族 canonical (Q6C 招牌) · F9 fluency: 逗號 apposition (即)


### `TAKE_ULTRON`

**EN**:
```
The Druuge, the cruel, sallow trading race who sold the device to the Utwig
called the device the `Ultron' and claimed that it would give the Utwig super-powers.
Unfortunately, the Utwig believed the Druuge and bought the Ultron.
However, the device DID make the Utwig very happy.
Of course, we didn't tell them what we REALLY thought of the Ultron
that they were vapid fools to buy a piece of junk for a planet's ransom.
We went along with the falsehood, and in doing so showed our own stupidity.
Then, one sad day a few years ago, the Utwig Proctor dropped the Ultron
during a particularly energetic and festive ritual.
Now the Utwig are morose and depressed.
They feel they cannot ever achieve greatness because they lost the powers of the Ultron.
They even gave the broken device to us, saying that they couldn't stand the sight of it anymore.
We are worried that the Utwig are so depressed that they may use their Ultimate Weapon.
Here! You take the Ultron, maybe you can do something with it.
```
**A · shipped**:
```
毒賈族，那殘忍蠟黃的貿易種族，把該裝置賣給憂特族
稱其為『厄創』並聲稱它能賦予憂特族超能力。
很不幸，憂特族相信毒賈族並買下了厄創。
然而，該裝置『確實』令憂特族非常快樂。
當然，我方沒告訴他們我方對厄創的『真正』看法
說他們是空虛的傻瓜，用一顆行星的贖金買了塊廢物。
我方順著這個謊言，如此便顯露了我方自己的愚蠢。
然後，數年前的悲傷一日，憂特族護法把厄創摔了
那時是一場特別熱鬧與歡慶的儀式。
如今憂特族陰鬱與沮喪。
他們覺得再也無法達到偉大，因為他們失去了厄創的能力。
他們甚至把壞了的裝置給了我方，說他們再也無法忍受看見它。
我方擔心憂特族如此沮喪，可能會啟用他們的終極武器。
來！ 您拿去厄創，也許您能用它做點什麼。
```
**B · v3**:
```
毒賈族，那殘忍蠟黃的貿易種族，把該裝置賣給憂特族
稱其為『厄創』並聲稱它能賦予憂特族超能力。
很不幸，憂特族相信毒賈族並買下了厄創。
然而，該裝置『確實』令憂特族非常快樂。
當然，我方沒告訴他們我方對厄創的『真正』看法
說他們是空虛的傻瓜，用一顆行星的贖金買了塊廢物。
我方順著這個謊言，如此便顯露了我方自己的愚蠢。
然後，數年前的悲傷一日，憂特監督者把厄創摔了
當時正舉行一場特別熱鬧、歡慶的儀式。
如今憂特族陰鬱與沮喪。
他們覺得再也無法達到偉大，因為他們失去了厄創的能力。
他們甚至把壞了的裝置給了我方，說他們再也無法忍受看見它。
我方擔心憂特族如此沮喪，可能會啟用他們的終極武器。
來！ 您拿去厄創，也許您能用它做點什麼。
```
🟠 **推薦：B** · 憂特族護法 → 憂特監督者 canonical (Q5A Master_Glossary L315) · Read-Aloud "當時正舉行" 修訂


### `HELLO_AFTER_KOHRAH_SPACE_2`

**EN**:
```
Hello again faunal comrade. We are spent, and must grow new bark.
```
**A · shipped**:
```
又哈囉，動物同伴。 我方精疲力竭，必須長出新樹皮。
```
**B · v3**:
```
又哈囉，動物之友。 我方精疲力竭，必須長出新樹皮。
```
🟠 **推薦：B** · faunal comrade → 動物之友 canonical (Q6C 招牌)


### `DO_THIS_AFTER_SPACE`

**EN**:
```
We are but humble plants, mere saplings in knowledge of such things.
If you seek wisdom, visit the Utwig Proctors.
```
**A · shipped**:
```
我方不過是謙卑的植物，在這類事上不過是初生幼苗。
若您尋求智慧，去拜訪憂特族護法。
```
**B · v3**:
```
我方不過是謙卑的植物，在這類事上不過是初生幼苗。
若您尋求智慧，去拜訪憂特監督者。
```
🟠 **推薦：B** · 憂特族護法 → 憂特監督者 canonical (Q5A)


### `SAMATRA`

**EN**:
```
During the battle, one of our ships intercepted a signal
from an Ur-Quan vessel to a Kohr-Ah ship.
The contents of the message was simple, `Sa-Matra'.
Immediately after receiving the broadcast, the Kohr-Ah vessel disengaged from combat
entered HyperSpace and sped off in the direction of <% comm.getStarName("the Crateris stars", "samatra") %>.
```
**A · shipped**:
```
戰鬥期間，我方一艘船艦攔截到一段訊號
從一艘烏寬族艦艇發至一艘柯亞族艦艇。
訊息內容很簡單，『薩-瑪特拉』。
收到廣播後，柯亞族艦艇立即脫離戰鬥
進入超空間並朝 <% comm.getStarName("巨爵座恆星群", "samatra") %> （the Crateris stars） 方向疾駛而去。
```
**B · v3**:
```
戰鬥期間，我方一艘船艦攔截到一段訊號
從一艘烏寬族艦艇發至一艘柯亞族艦艇。
訊息內容很簡單，『薩瑪特拉』。
收到廣播後，柯亞族艦艇立即脫離戰鬥
進入超空間並朝 <% comm.getStarName("巨爵座恆星群", "samatra") %> （the Crateris stars） 方向疾駛而去。
```
🟠 **推薦：B** · 薩-瑪特拉 → 薩瑪特拉 (cross-race v0.7 canonical · 對齊 Chmmr/Kohr-Ah/Utwig/Kzer-Za v3)


### `GOOD_HINTS`

**EN**:
```
Knowledge is the purview of the Utwig. We Supox are but the effectuators.
In truth though, we have learned a fact or two unknown to others.
We did not think anyone would care in the slightest, but since you ask, listen.
We have not fared far from our region of space, but we have explored this region thoroughly.
Of all the oddities we have found, from the firefalls of Nalnar to the servants of Mali
the truest mystery was the nature of a world we found at the <% comm.getColor("orange", "rainbow 7") %> star, <% comm.getStarName("Beta Leporis", "rainbow 7") %>.
As a general rule, we prefer not to dwell in such <% comm.swapIfSeeded("long", "pale") %>-wavelength regions
but we were on a mapping mission. That was when we found the planet.
At first we thought our scanners had failed, for they showed us a world of chromatic aspect.
Then we located the source of our malfunction... the planet itself!
Somehow the planet generates a field of unusual radiations which scramble delicate circuitry.
Though blazing hot, we attempted a landing. Before we were forced off the surface by the intense heat
we registered the presence of huge amounts of processed radioactives.
Strange, is it not?
```
**A · shipped**:
```
知識是憂特族的職掌。 我方蘇菩不過是執行者。
然事實上，我方也學到了一兩件別人不知的事實。
我方本以為不會有人在意分毫，但既然您問了，請聽。
我方離自己星域不遠，但已徹底探索了這片區域。
在我方所發現的所有奇物中，從納爾納之火瀑到馬利之僕從
最真確的謎團是我方於 <% comm.getColor("橘色", "rainbow 7") %> 恆星 <% comm.getStarName("天兔座β", "rainbow 7") %> （Beta Leporis） 找到的一顆世界之本質。
一般而言，我方偏好不居於此類 <% comm.swapIfSeeded("長", "蒼白") %> 波長區域
但我方當時在執行測繪任務。 那時我方發現了那顆行星。
起初我方以為感應器故障了，因為它們顯示我方看到一個色彩斑斕之世界。
然後我方定位到故障來源… 那行星本身！
該行星不知怎地產生一種不尋常的輻射場，擾亂精密電路。
儘管熾熱難耐，我方仍嘗試登陸。 在被強烈高溫逼離地表之前
我方記錄到大量已加工放射性物質的存在。
奇怪，不是嗎？
```
**B · v3**:
```
智慧屬憂特之領域，我方蘇菩僅為執行者。
但事實上，我方也學到了一兩件別人不知的事實。
我方本以為不會有人在意分毫，但既然您問了，請聽。
我方離自己星域不遠，但已徹底探索了這片區域。
在我方所發現的所有奇物中，從納爾納之火瀑到馬利之僕從
最真確的謎團是我方於 <% comm.getColor("橘色", "rainbow 7") %> 恆星 <% comm.getStarName("天兔座β", "rainbow 7") %> （Beta Leporis） 找到的一顆世界之本質。
一般而言，我方偏好不居於此類 <% comm.swapIfSeeded("長", "蒼白") %> 波長區域
但我方當時在執行測繪任務。 那時我方發現了那顆行星。
起初我方以為感應器故障了，因為它們顯示我方看到一個色彩斑斕之世界。
然後我方定位到故障來源…… 那行星本身！
該行星不知怎地產生一種不尋常的輻射場，擾亂精密電路。
儘管熾熱難耐，我方仍嘗試登陸。 在被強烈高溫逼離地表之前
我方記錄到大量已加工放射性物質的存在。
奇怪，不是嗎？
```
🟠 **推薦：B** · 知識是憂特族的職掌 → 智慧屬憂特之領域,我方蘇菩僅為執行者 (dossier §六例 3 招牌對憂特依賴) · 然事實上→但事實上 Read-Aloud


### `bye_allied_homeworld`

**EN**:
```
Goodbye Leafy Ones.
```
**A · shipped**:
```
再見，多葉之族。
```
**B · v3**:
```
再見，葉之族。
```
🟠 **推薦：B** · Leafy Ones 多葉之族 → 葉之族 canonical (Q6C 招牌)


### `GOODBYE_ALLIED_HOMEWORLD`

**EN**:
```
Farewell Friendly Folk.
```
**A · shipped**:
```
再見，友善之族。
```
**B · v3**:
```
願光永遠照到您的葉，友善同胞。
```
🟠 **推薦：B** · 再見友善之族 → 願光永遠照到您的葉,友善同胞 (Q8A May-式招牌升級 · F8 fluency: 永達→永遠照到)


### `OUT_TAKES`

**EN**:
```
Whew! I'm glad that's all over.
That was tough, playing second banana to the Utwig.
Now I'm hungry, but I'm sick and tired of sunlight, sunlight, sunlight!
I want some REAL food!!!
Like a hamburger or a steak... better yet
how about a dog!
```
**A · shipped**:
```
呼！ 真高興這一切都結束了。
當憂特族的第二把交椅還真是不容易。
現在我肚子餓了，可是我對陽光、陽光、陽光已經膩到不行了！
我要吃『真正的』食物！！！
像是漢堡或牛排… 更好的是
來隻狗如何！
```
**B · v3**:
```
呼！ 終於結束了。
當憂特族的配角很辛苦。
現在我餓了，可我受夠了陽光、陽光、陽光！
我想要『真正的』食物！！！
像漢堡或牛排…… 甚至
來條狗更棒！
```
🟠 **推薦：B** · 全採 dossier §六例 6 版本 · F4 fluency: 加『真正的』CAPS icon + 不然→甚至 (better yet 精確)


## 🟡 Minor (16 tokens)

### `HOSTILE_SPACE_HELLO_2`

**EN**:
```
You diandrous malefic vegetarians!
Your visage darkens our skies.
May your rotting bodies provide our nutrients for kinder generations.
We ignore you, as we ignore the pale, tasteless light of your wan home star.
```
**A · shipped**:
```
你們這些雙雄蕊的惡毒素食者！
你們的容貌暗黑我方之天空。
願你們腐朽之軀為我方更善良的世代提供養分。
我方忽視你們，如同忽視你們昏暗母星那蒼白無味的光芒。
```
**B · v3**:
```
你們這些兩雄蕊、邪惡的素食者！
你們的容貌暗黑我方之天空。
願你們腐爛的身體，為我方更仁慈的後代提供養分。
我方無視你們，如同無視你們病弱母星那蒼白無味的光線。
```
🟡 **推薦：B** · 雙雄蕊 → 兩雄蕊 (dossier §四 canonical 與 HIDEOUS_MONSTERS 對齊) · 昏暗母星→病弱母星 (dossier §四 canonical) · F1 fluency: 罵人段您們→你們


### `YEAH_SORRY`

**EN**:
```
Oh yes, we apologize for the confusion, our homeworld is also called `Earth',
or more properly `Vlik', which means `Perfectly Good and Nutritious Dirt'.
`Earth' is pretty close, is it not?
```
**A · shipped**:
```
喔對，我方對此困惑致歉，我方之母星也叫『地球』
或者更正確地說，弗利克（Vlik），意為『完美美好又營養的土壤』。
『地球』相當接近，不是嗎？
```
**B · v3**:
```
喔對，我方對這場混淆致歉，我方之母星也叫『地球』
或者更正確地說，弗利克（Vlik），意為『完美好用又營養的泥土』。
『地球』相當接近，不是嗎？
```
🟡 **推薦：B** · 此混淆 → 這場混淆 (Read-Aloud §4.5.4 冗餘書面修訂) · 完美美好又營養的土壤→完美好用又營養的泥土 (dossier canonical)


### `SYMBIOTS`

**EN**:
```
We learn and we adapt. We are symbionts.
Our first step in making friends is always to copy them.
This is our idiom.
```
**A · shipped**:
```
共生之枝學習，共生之枝適應。 我方是共生體。
我方交朋友的第一步永遠是模仿他們。
這是我方之慣用方式。
```
**B · v3**:
```
共生之枝學習，共生之枝適應。 我方是共生者。
我方交朋友的第一步永遠是模仿他們。
這是我方之慣用方式。
```
🟡 **推薦：B** · 共生體 → 共生者 (Q10A dossier §四 生命個體語感) · 共生之枝 保留 (Q1B)


### `tell_us_of_your_species`

**EN**:
```
Symbionts, how interesting! Please tell us more.
```
**A · shipped**:
```
共生體，真有趣！ 請多說一些。
```
**B · v3**:
```
共生者，真有趣！ 請多說一些。
```
🟡 **推薦：B** · 共生體 → 共生者 (Q10A · 玩家 response 對齊)


### `OUR_SPECIES`

**EN**:
```
Our kind evolved on a beautiful planet orbiting the wonderfully <% comm.getColor("green", "supox") %>-hued star, Root.
From the canopy of the great jungles to the shores of the azure seas
Our species has flowered and grown well.
Early in our evolution, we adapted to exist in symbiosis with other, hardier life, both flora and fauna,
who supplied us with nutrients while we supplied them with reproductive assistance.
```
**A · shipped**:
```
吾等蘇菩演化於一顆美麗的行星，繞著色調美妙 <% comm.getColor("綠色", "supox") %> 的恆星『根（Root）』運行。
自那大叢林的樹冠到蔚藍海的岸邊
我方一族已好好開花與成長。
我方演化早期，便適應了與其他更堅韌的生命共生存在，動植物皆然
他們提供我方養分，我方為他們提供生殖協助。
```
**B · v3**:
```
我方蘇菩演化於一顆美麗的行星，繞著色調美妙 <% comm.getColor("綠色", "supox") %> 的恆星『露特星（Root，意為「根」）』運行。
從那大叢林的樹冠到蔚藍海的岸邊
我方一族已好好開花與成長。
我方演化早期，便適應了與其他更堅韌的生命共生，動植物皆然
他們提供我方養分，我方為他們提供生殖協助。
```
🟡 **推薦：B** · 吾等蘇菩→我方蘇菩 (Q1B 廢 Phase 14c++ wenyan) · F12 fluency: Root pun 保留為「露特星(Root,意為「根」)」音義並存


### `HIDEOUS_MONSTERS`

**EN**:
```
Arrgh, you hideous monsters, vegetarians, defilers of the leaf, uprooters.
Begone, or we shall uproot you!
```
**A · shipped**:
```
啊！ 你們這些可憎的怪物、素食者、葉之玷汙者、拔根者。
離開，否則我方要拔了你們！
```
**B · v3**:
```
啊！ 你們這些可憎的怪物、素食者、葉之玷汙者、拔根者。
走開，否則我方要把你們連根拔起！
```
🟡 **推薦：B** · F10 fluency: 罵詞退 A「葉之玷汙者」+ 保 B 動詞「走開/連根拔起」·  混合最佳


### `ALMOST_THERE`

**EN**:
```
Yes! Yes!
But, but no... it is still not quite as brightly lit as it once was.
One more repair job should do it!
```
**A · shipped**:
```
是！ 是！
但，但不… 它還沒像過去那樣明亮閃耀。
再修一次應該就好了！
```
**B · v3**:
```
是！ 是！
但，但不…… 它還沒像過去那樣明亮閃耀。
再修一次應該就好了！
```
🟡 **推薦：B** · 標點 … → …… (Q9A)


### `GREAT_DO_MORE`

**EN**:
```
Great! Great!
Oh, dear
It is true that you have repaired the Ultron... somewhat
but it is not yet in the condition which so enthralled the Utwig.
Your efforts are valid, merely incomplete.
```
**A · shipped**:
```
太好了！ 太好了！
喔，天啊
您確實修復了厄創… 一部分
但它尚未達到當年令憂特族入迷的狀態。
您的努力有效，但只是尚未完成。
```
**B · v3**:
```
太好了！ 太好了！
喔，天啊
您確實修復了厄創…… 一部分
但它尚未達到當年令憂特族入迷的狀態。
您的努力有效，但只是尚未完成。
```
🟡 **推薦：B** · 標點 … → …… (Q9A)


### `ABOUT_BATTLE`

**EN**:
```
Hello Captain.
We fought the Kohr-Ah; our buddies the Utwig did some pretty serious damage
to several fleets, but we mostly just watched helplessly.
The Ur-Quan did not seem to realize that we were helping them
and as often as not they attacked us too!
We may have delayed the outcome of the fight, but it still seems clear that the Kohr-Ah are winning.
```
**A · shipped**:
```
哈囉艦長。
我方對抗了柯亞族;我方的好夥伴憂特族對幾支艦隊
造成了相當嚴重的傷害，但我方大多只能無助地在旁觀看。
烏寬族似乎沒意識到我方是在幫他們
而且他們常常也對我方開火！
我方或許延緩了戰鬥的結果，但柯亞族顯然仍在獲勝。
```
**B · v3**:
```
哈囉艦長。
我方對抗了柯亞族； 我方的好夥伴憂特族對幾支艦隊
造成了相當嚴重的傷害，但我方大多只能無助地在旁觀看。
烏寬族似乎沒意識到我方是在幫他們
而且他們常常也對我方開火！
我方或許延緩了戰鬥的結果，但柯亞族顯然仍在獲勝。
```
🟡 **推薦：B** · 中文分號空白 icon 微調 (「;」→「； 」讀順)


### `HELLO_AFTER_KOHRAH_SPACE_1`

**EN**:
```
Ah, our human friend... we are so tired... the battle so difficult...
```
**A · shipped**:
```
啊，我方的人類朋友… 我方好累… 戰鬥如此艱難…
```
**B · v3**:
```
啊，我方的人類朋友…… 我方好累…… 戰鬥如此艱難……
```
🟡 **推薦：B** · 標點 … → …… (Q9A · 3 處)


### `GENERAL_INFO_AFTER_SPACE_1`

**EN**:
```
We met the Kohr-Ah at the sides of our Utwig allies.
The destructive power of the black ships was greater than anticipated
however we did eventually develop tactics in conjunction with the Utwig
that were effective against them. We destroyed dozens of their battleships!
Alas, we lost many of our brothers to the spinning blades and the fiery ring.
```
**A · shipped**:
```
吾等蘇菩與憂特族盟友並肩迎戰柯亞族。
黑色艦艇的破壞力大於預期
然而我方最終與憂特族共同發展出戰術
對他們有效。 我方摧毀了他們數十艘戰艦！
可惜，我方失去許多兄弟於旋轉刃盤與火環之下。
```
**B · v3**:
```
我方蘇菩與憂特族盟友並肩迎戰柯亞族。
黑色艦艇的破壞力大於預期
然而我方最終與憂特族共同發展出戰術
對他們有效。 我方摧毀了他們數十艘戰艦！
可惜，我方失去許多兄弟於旋轉刃盤與火環之下。
```
🟡 **推薦：B** · 吾等蘇菩→我方蘇菩 (Q1B 廢 Phase 14c++ wenyan)


### `BATTLE_HAPPENS_1`

**EN**:
```
Fearsome, human, fearsome! We have not yet evolved tactics
which are useful against the Kohr-Ah Marauder vessels.
The dark ships launch spinning wheels of metal... we are mown down like
I don't even want to say it... and if we are fortunate enough to close with the ships
ports open up around its perimeter, jetting forth gouts of flaming plasma.
Not only do these flames melt through our hulls like a scythe
but they are also an effective defense against our glob weapon.
```
**A · shipped**:
```
可怕，人類，可怕！ 我方尚未演化出
對柯亞掠奪艦有效的戰術。
黑色艦艇發射旋轉的金屬輪盤… 我方像被鐮刀
我甚至不想說出來… 若我方有幸能接近艦艇
其周圍會打開埠口，噴出熾熱電漿。
這些火焰不僅像鐮刀般融穿我方船殼
也是我方黏團武器的有效防禦。
```
**B · v3**:
```
可怕，人類，可怕！ 我方尚未演化出
對柯亞掠奪艦有效的戰術。
黑色艦艇發射旋轉的金屬輪盤…… 我方像被鐮刀
我甚至不想說出來…… 若我方有幸能接近艦艇
其周圍會打開埠口，噴出熾熱電漿。
這些火焰不僅像鐮刀般融穿我方船殼
也是我方黏團武器的有效防禦。
```
🟡 **推薦：B** · 標點 … → …… (Q9A · 2 處)


### `FLEET_ON_WAY`

**EN**:
```
Even as we speak, the Utwig and Supox fleets streak toward <% comm.getConstellation("Horologii", "samatra") %>...
...where they hope to strike a major blow against the Kohr-Ah forces.
```
**A · shipped**:
```
此刻我方與您說話的同時，憂特族與蘇菩族艦隊正疾駛向 <% comm.getConstellation("時鐘座", "samatra") %> （Horologii）…
…他們希望對柯亞族軍力予以重擊。
```
**B · v3**:
```
此刻我方與您說話的同時，憂特族與蘇菩族艦隊正疾駛向 <% comm.getConstellation("時鐘座", "samatra") %> （Horologii）……
……他們希望對柯亞族軍力予以重擊。
```
🟡 **推薦：B** · 標點 … → …… (Q9A · 2 處)


### `can_you_help`

**EN**:
```
Two leaves pull water from the same root.
```
**A · shipped**:
```
兩片葉從同一根汲水。
```
**B · v3**:
```
雙葉共汲於一根。
```
🟡 **推薦：B** · 兩片葉從同一根汲水 → 雙葉共汲於一根 (dossier §四 招牌隱喻 canonical)


### `HOW_HELP`

**EN**:
```
Such wisdom! Your meanings run deep, we ponder their significance.
Ah, yes! You wish us to give you assistance... such as our fighting ships!
```
**A · shipped**:
```
多麼智慧！ 您言意深遠，我方沉思其意義。
啊，是了！ 您希望我方給您協助… 例如我方之戰艦！
```
**B · v3**:
```
多麼智慧！ 您言意深遠，我方沉思其意義。
啊，是了！ 您希望我方給您協助…… 例如我方之戰艦！
```
🟡 **推薦：B** · 標點 … → …… (Q9A)


### `DONT_NEED`

**EN**:
```
Yet, you seem to possess a fleet in concert with your need.
We will reserve what few ships we have left for our final defense against the Kohr-Ah.
```
**A · shipped**:
```
然，您似乎已擁有一支與您需求相稱的艦隊。
我方將保留剩下的少數艦艇，用於我方對抗柯亞族的最後防禦。
```
**B · v3**:
```
然而，您似乎已擁有一支與您需求相稱的艦隊。
我方將保留剩下的少數艦艇，用於我方對抗柯亞族的最後防禦。
```
🟡 **推薦：B** · 然, → 然而, (Read-Aloud §4.5.1 意連詞 更現代)


## 🟢 Identical / Preserved (64 tokens · Q&A locked)

- `HOSTILE_SPACE_HELLO_1`
- `ALLIED_HOMEWORLD_HELLO_1`
- `ALLIED_HOMEWORLD_HELLO_2`
- `ALLIED_HOMEWORLD_HELLO_3`
- `ALLIED_HOMEWORLD_HELLO_4`
- `i_am`
- `WE_ARE_SUPOX`
- `my_ship`
- `OUR_SHIP`
- `from_alliance`
- `FROM_SUPOX`
- `are_you_copying`
- `why_copy`
- `plants_arent_intelligent`
- `PROVES_WERE_SPECIAL`
- `anyone_around_here`
- `what_relation_to_utwig`
- `UTWIG_ALLIES`
- `whats_wrong_with_utwig`
- `BROKE_ULTRON`
- `whats_ultron`
- `what_do_i_do_now`
- `FIX_IT`
- `thanks_now_we_eat_you`
- `got_fixed_ultron`
- `GOOD_GIVE_TO_UTWIG`
- `look_i_repaired_lots`
- `look_i_slightly_repaired`
- `where_get_repairs`
- `ANCIENT_RHYME`
- `bye_neutral`
- `GOODBYE_NEUTRAL`
- `HELLO_BEFORE_KOHRAH_SPACE_1`
- `HELLO_BEFORE_KOHRAH_SPACE_2`
- `HELLO_DURING_KOHRAH_SPACE_1`
- `HELLO_DURING_KOHRAH_SPACE_2`
- `whats_up_after_space`
- `GENERAL_INFO_AFTER_SPACE_2`
- `what_now_after_space`
- `bye_after_space`
- `GOODBYE_AFTER_SPACE`
- `whats_up_before_space`
- `GENERAL_INFO_BEFORE_SPACE_1`
- `GENERAL_INFO_BEFORE_SPACE_2`
- `what_now_before_space`
- `DO_THIS_BEFORE_SPACE`
- `bye_before_space`
- `GOODBYE_BEFORE_SPACE`
- `how_went_war`
- `how_goes_war`
- `BATTLE_HAPPENS_2`
- `learn_new_info`
- `NO_NEW_INFO`
- `what_now_homeworld`
- `HOPE_KILL_EACH_OTHER`
- `UP_TO_YOU`
- `HAVE_4_SHIPS`
- `give_info`
- `how_is_ultron`
- `ULTRON_IS_GREAT`
- `name_1`
- `name_2`
- `name_3`
- `name_4`
