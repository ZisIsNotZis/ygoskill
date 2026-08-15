---
name: lunalight-experience
description: 月光 (Lunalight) deck experience: fusion ladder + attack-all-twice OTK engine, one-card starter, extenders, halt points
---
# 月光 (Lunalight) Deck Experience

- **Deck Identity**

- DARK Beast-Warrior fusion OTK; every main monster is Beast-Warrior and mostly DARK level 4 (银狗 35763582 is level 3, 黑羊 11317977 and 白兔 84812868 are level 2, 狼 47705572 and 虎 83190280 are LIGHT Pendulum level 4)
- Fusion ladder: 舞猫姬 51777272 (2 Lunalight) into 舞豹姬 97165977 (舞猫姬 + 1 Lunalight) into 舞狮子姬 24550676 (舞豹姬 + 2 Lunalight) into 舞狮子神姬 54701958 (舞狮子姬 + 3 Lunalight); side bosses 舞香姬 81196066 (2 Lunalight) and 舞剑虎姬 88753594 (3 Lunalight)
- Engine spells: 月光融合 87931906, 融合 24094653, 月华香 48444114, 月光舞蹈会 2344618 (field spell), 月光小夜曲舞踊 13935001 (continuous trap, the OTK enabler)
- Repo build family (all recent 月光 folders, e.g. 260228月光, 260228月光融合炎舞, 260124月光融合): 3 金狮子 8379983 + 3 黑羊 + 2 银狗 + 2 彩雏 35618217 + 翠鸟 14152693 + 黄鼬 50546208 + 狼 + 虎, splashing 铁兽战线 弗拉克杜尔 87209160 ×2 and 炎舞-「天玑」 57103969 ×3 as starters, plus 多层融合 58570206 ×2-3 and go-second boardbreakers (红色重启 23002292, 冥王结界波 54693926, 雷击 12580477, 鹰身女妖的羽毛扫 18144506)
- Extra deck: the six fusions plus generic links 转生炎兽 独角兔 60303245, 交织绵羊 50277355, S：P小夜骑士 29301450, W：P变幻舞夜 4993187 and rank 4s 魁炎星王-宋虎 96381979, No.60 刻不知之杜加雷斯 66011101

- **Core Mechanic: 月光融合 engine**

- 月光融合 87931906 fuses Lunalight monsters from hand and field; when the OPPONENT controls a monster summoned from the extra deck, it may additionally use exactly 1 Lunalight monster from your deck or extra deck as material (script c87931906 caps deck/extra materials at 1) — the go-second enabler that turns one monster into a fusion
- 月光金狮子 8379983 on normal or special summon adds any Lunalight monster from deck then discards 1; while face-up, whenever another Lunalight monster you own is sent to the graveyard it adds one of those to hand, even during the damage step — the discard loop
- 月光银狗 35763582 when sent to the graveyard by an effect special summons any Lunalight from deck and the summon is NOT negated, so summon triggers fire; while that summoned monster is face-up you cannot special summon non-Lunalight monsters from the extra deck (one-way lock on yourself)
- 月光黑羊 11317977 discards itself from hand to add a Lunalight from grave or 融合 24094653 from deck, and when used as fusion material adds a Lunalight from grave or face-up pendulum extra to hand
- 月光彩雏 35618217 once per turn sends any Lunalight from deck or extra to grave as cost and becomes that card's name as fusion material until end of turn (the name-copy that opens the ladder with 2 materials); sent to grave by an effect it recycles 融合, and when banished the opponent cannot activate effects during the battle phase that turn

- **Core Mechanic: attack-all-twice OTK**

- 月光舞猫姬 51777272 and 月光舞豹姬 97165977 ignition effects work only in MAIN PHASE 1 (script requires being able to enter the battle phase): the opponent's monsters cannot be destroyed by battle once each and the fusion attacks all opponent monsters twice each
- 月光小夜曲舞踊 13935001: each time you fusion summon a Lunalight fusion, special a 月光衍生物 13935002 token (DARK Beast-Warrior 2000/2000) to the opponent's field and the fusion gains 500 ATK per opponent monster — the token is a free attack target and the boost turns double swings into lethal
- 月光红狐 94919024 sent to grave by an effect sets one opponent face-up monster's ATK to 0, so 舞豹姬 two-shots it for 5600 alone
- 月光舞狮子姬 24550676 attacks twice and after each battle against a monster destroys all opponent special-summoned monsters; 月光舞狮子神姬 54701958 attacks twice, is unaffected by non-Lunalight card effects, and has a quick effect once per turn (either turn) that sends 1 Lunalight from extra to grave to destroy all opponent special-summoned monsters — after the wipe it attacks directly
- 月光狼 47705572 gives every Lunalight piercing; 月光舞剑虎姬 88753594 gains 200 ATK per Beast-Warrior in both graves and banished zones, and in grave can banish itself to give a fusion +3000 ATK
- OTK math: fuse 舞豹姬 into a 2-monster opponent field (one real monster plus the token) and it swings 3800 twice at each, lethal; fuse 舞狮子神姬 with the token boost, wipe all special-summoned monsters including the token, then attack directly twice for 8600+

- **One-Card Combo: 铁兽战线 弗拉克杜尔 87209160**

- Starter: 弗拉克杜尔 alone in hand; the final 月光融合 needs the opponent to control an extra-deck-summoned monster (or one more Lunalight in hand)
- Step 1: activate 弗拉克杜尔 87209160, discard it, send 月光银狗 35763582 from deck to grave
- Step 2: 银狗 special summons 月光金狮子 8379983 from deck
- Step 3: 金狮子 adds 月光黑羊 11317977 from deck, discards 1 (prefer 月光黄鼬 50546208, whose sent-by-effect trigger then adds 月华香 48444114 from deck)
- Step 4: discard 黑羊 to add 月光融合 87931906 from deck
- Step 5: activate 月光融合: fuse 金狮子 (field) plus 1 Lunalight from deck into 月光舞香姬 81196066
- Step 6: 舞香姬's fusion-summon trigger searches 月华香; activate it to revive 黑羊 or 银狗 from grave
- Step 7: fuse toward 舞猫姬 51777272 then 舞豹姬 97165977 and run the attack-all-twice line, or pass with 舞香姬 + 月华香 + 银狗 and 红狐 94919024 in grave as the go-first plan
- Under 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493, stop after 舞香姬 plus 月华香 (three special summons) and do not extend into the ladder

- **End Field**

- Go-second: the OTK is the end field — 舞豹姬 97165977 or 舞狮子神姬 54701958 cleared the board and dealt 8000 or more
- Go-first compromise (weak by design): 舞香姬 81196066 + face-up 月华香 48444114 + 月光舞蹈会 2344618 with 银狗 35763582 and 红狐 94919024 in grave — 银狗 negates a spell/trap activation on the field, 红狐 negates any effect targeting your face-up Lunalight and both players recover 1000
- Set 月光小夜曲舞踊 13935001 for the next turn's token boost, or use its grave effect (discard 1) to special a Lunalight from deck

- **Extenders**

- 炎舞-「天玑」 57103969 adds any level 4 or lower Beast-Warrior on activation (every Lunalight main monster) and gives your Beast-Warriors +100 ATK
- 月光彩雏 35618217 sends 舞狮子神姬 54701958 or 舞狮子姬 24550676 from the extra deck to grave and acts as that name, opening the ladder with 2-material 融合s
- 月光翠鸟 14152693 on summon discards a Lunalight to draw 1, and when sent to grave by an effect revives a level 4 or lower Lunalight in defense with negated effects — a revived 金狮子 8379983 does not search
- 月光黄鼬 50546208 recycles a face-up 月光 card to hand, specials itself from hand or grave in defense, and searches any 月光 spell or trap when sent by an effect — the 月光融合 / 月华香 / 舞蹈会 tutor
- 月光白兔 84812868 on normal summon revives a Lunalight from grave and bounces up to your face-up 月光 count of opponent spells or traps
- 月光虎 83190280 pendulum scale revives a Lunalight from grave (negated, cannot attack, destroyed at end phase); when destroyed on field it revives another
- 月光狼 47705572 pendulum scale fusion summons using monsters from your field and grave as materials, banishing them
- 月光舞蹈会 2344618 sends a Lunalight from deck to grave during the turn it was activated, and when you fusion summon adds 融合 24094653 from grave or banished zone; if you discard during that recursion, one fusion this turn may also banish grave monsters as materials
- 多层融合 58570206 fuses 3 or more materials from hand and field and, when the opponent has monsters, may banish up to that many extra deck monsters as materials at the cost of LP equal to their ATK — a second fusion spell not subject to 月光融合's once-per-turn
- 黑羊 11317977's material effect and 金狮子's grave-recycle chain into extra fusion summons; 小夜曲舞踊 13935001's grave effect is another monster special from deck

- **Halt Points**

- 灰流丽 14558127: on 金狮子 8379983's search, 黑羊 11317977's 融合 search, 舞香姬 81196066's 月华香 search, or 月光融合 87931906 when it uses the deck material clause (it special summons from the deck, so Ash applies)
- 增殖的G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493 punish the multi-special-summon line; stop at 舞香姬 or resolve 抹杀之指名者 65681983 first
- 小丑与锁鸟 94145021 stops the search chain — one 锁鸟 locks out all of 金狮子's, 黑羊's, 舞香姬's, and 黄鼬's searches for the turn
- 墓穴的指名者 24224830 on 银狗 35763582 kills the starter; 无限泡影 10045474 or 效果遮蒙者 on 金狮子 stops the search that feeds everything
- 原始生命态 尼比鲁 27204311 after the fourth summon (银狗, 金狮子, 舞香姬, 月华香 revival)
- 次元障壁 83326048 naming fusion locks the entire extra deck out

- **Mirror Match: 月光 vs 月光**

- 舞狮子神姬 54701958 is immune only to non-Lunalight effects, so the mirror's own 月光 effects still resolve against it
- 银狗 35763582's grave quick effect negates any spell or trap activation on the field, including the opponent's 月光融合 87931906 and 月光舞蹈会 2344618 — hold it for the fusion spell, it is the mirror's best defense
- 红狐 94919024's grave effect negates any effect targeting your face-up Lunalight and both players recover 1000, so pick targets carefully
- 舞剑虎姬 88753594 scales with Beast-Warriors in both graves and banished zones, so the mirror feeds it
- 彩雏 35618217 when banished forbids the opponent from activating effects during the battle phase, blanking their 银狗 and 红狐 grave defenses while you swing
- Whoever fuses 舞狮子神姬 first wins; going second, hold 霆王的闪光 6325660 or 灵王的波动 40366667 for the opponent's 月光融合 activation

- **Common Mistakes**

- Activate 舞猫姬 51777272 / 舞豹姬 97165977 attack-all effects outside Main Phase 1 — the script requires the battle phase to be enterable, so it fails in Main Phase 2
- Rely on 月光融合 87931906's deck or extra material without an opponent extra-deck-summoned monster; going first the clause is dead and real hand materials are required
- Forget the 银狗 35763582 extra-deck lock: no generic link or rank 4 plays (独角兔 60303245, 交织绵羊 50277355, S：P小夜骑士 29301450, 宋虎 96381979) while its summoned monster is face-up
- Plan 月光舞蹈会 2344618's deck-send effect on later turns — it only works during the turn the field spell was activated (flag check)
- Expect 翠鸟 14152693 and 虎 83190280 revivals to trigger effects — both negate the revived monster, so a revived 金狮子 8379983 does not search
- Send 红狐 94919024 as fusion material and miss the ATK-0 — it must be sent by an effect (愚蠢的埋葬 81439173, 翠鸟's discard, 舞蹈会, 金狮子's discard)
- Try to revive 舞狮子神姬 54701958 or 舞狮子姬 24550676 with 月华香 48444114 or 小夜曲舞踊 13935001 — both fusions require fusion summoning and cannot be special summoned otherwise
- 舞剑虎姬 88753594's +3000 requires banishing it from grave in a turn it was NOT sent there; a same-turn fused 剑虎 cannot use it
- Treat the 月光衍生物 13935002 token as harmless — it is an opponent monster that can be tributed, and removing it weakens the 舞豹姬 boost before you attack
- The DB text of 月光舞蹈会 2344618 still carries a stale cannot-be-used note, but the shipped script implements both effects — trust the script
