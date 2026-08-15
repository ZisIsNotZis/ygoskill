---
name: yosenju-experience
description: 妖仙兽 (Yosenju) deck experience: hit-and-run bounce mechanics, Kama chain one-card combo, pend scales, extenders, halt points
---
# 妖仙兽 (Yosenju) Deck Experience

- **Deck Identity**

- WIND Beast-Warrior control deck, archetype setcode 0xb3, plays entirely on its own turn and leaves an empty board at the End Phase
- Core Level 4 engine: 镰壹太刀 65247798, 镰贰太刀 92246806, 镰叁太刀 28630501
- Level 4 support: 侍郎风 58981727 (search pendulum / set trap from deck), 饭纲鞭 85970321 (summon-lock + draw), 辻斩风 25244515 (ATK pump)
- Pendulum bosses: 独眼群主 21364070, 大刃祸是 93368494; scales: 左镰神柱 65025250, 右镰神柱 91420254
- Race split quirk: Level 4 engine and 木魅 23740893 are Beast-Warrior (race 32768), Level 6 support 凶旋岚 49249907 / 阎魔巳裂 39853199 / 大幽谷响 69838592 and pend bosses are Beast (race 16384), 左镰神柱 65025250 / 右镰神柱 91420254 are Rock (race 256), so 千查万别 24207889 allows one of each race
- Win plan: summon the chain on your turn, attack for damage, bounce everything to hand at End Phase, answer the opponent turn with set bounce/negate traps and floodgates
- Build eras in repo: pure stun 141011/160709 (强欲而谦虚之壶 98645731, 削命的宝札 59750328, 休息一回 24348804), modern pendulum 230422 (神颪 61884774, 千查万别 24207889), PSY-frame 210717, Fiendsmith/罪宝 hybrid 240727

- **Core Mechanic: Hit-and-Run Bounce**

- Every main Level 4 monster returns to hand at the End Phase of the turn it was Normal Summoned; verified in each script as EFFECT_TYPE_TRIGGER_F on EVENT_PHASE+PHASE_END with EFFECT_FLAG_CANNOT_DISABLE
- The return is mandatory and cannot be negated, so the monster zone is empty when your turn ends
- 镰壹太刀 65247798, 镰贰太刀 92246806, 镰叁太刀 28630501 each grant one extra Normal Summon of another Yosenju from hand on their own Normal Summon (Duel.Summon with ignore_count, so it does not consume the normal summon and the summoned monster's own trigger fires)
- Each Kama can summon any Yosenju except itself, so one Normal Summon produces a chain of up to 4 monsters when the hand holds the trio plus 侍郎风 58981727 or 饭纲鞭 85970321
- 镰壹太刀 65247798 ignition bounce: once while face-up, if another face-up Yosenju is on your field, return 1 face-up opponent card to hand
- 镰贰太刀 92246806: direct attack with battle damage halved (900)
- 镰叁太刀 28630501: when another Yosenju you control inflicts battle damage, search 1 Yosenju card (not itself) from deck
- The engine is Normal Summons only, so 增殖的G 23434538 and special-summon floodgates do not punish the pure line

- **One-Card Combo: Kama Chain**

- Requires 镰壹太刀 65247798 plus 镰贰太刀 92246806 and 镰叁太刀 28630501 in hand; one Normal Summon action yields the full board (Yosenju is not a solo-starter deck, a second Yosenju in hand is always needed)
- Step 1: Normal Summon 镰壹太刀 65247798, resolve its effect to Normal Summon 镰贰太刀 92246806 from hand
- Step 2: 镰贰太刀 92246806 effect Normal Summons 镰叁太刀 28630501
- Step 3: 镰叁太刀 28630501 effect Normal Summons a fourth Yosenju from hand: 侍郎风 58981727 for a pendulum search, 饭纲鞭 85970321 for a draw, or 辻斩风 25244515 for pumps
- Step 4: battle phase — 镰贰太刀 92246806 direct attack 900, 镰壹太刀 65247798 1600, 镰叁太刀 28630501 1500
- Step 5: 镰叁太刀 28630501 searches any Yosenju card on 镰贰太刀 92246806 battle damage; 镰壹太刀 65247798 bounces 1 face-up opponent card
- Step 6: End Phase — all four monsters return to hand, net hand advantage +2 or better
- Option before End Phase: Xyz the Level 4s into rank 4 (No.39 希望皇 霍普 84013237 into 闪光No.39 希望皇 霍普·电光皇 56832966, or No.41 泥睡魔兽 睡梦貘 90590303); Xyz materials do not return
- Variant starter: 凶旋岚 49249907 Normal Summon special summons any Yosenju from deck, but the special-summoned monster does not trigger its own on-Normal-Summon effect

- **End Field**

- Monsters: none (all returned) unless kept: 大幽谷响 69838592 stays (no return effect, sticky wall), a rank-4 Xyz stays, and tribute-summoned 阎魔巳裂 39853199 or 凶旋岚 49249907 stay (their return applies only when special summoned)
- Pendulum scales: 左镰神柱 65025250 (scale 3) and 右镰神柱 91420254 (scale 5) placed by 神颪 61884774 survive until the opponent End Phase; 独眼群主 21364070 used as a scale returns to hand at your End Phase
- Backrow: 妖仙兽的秘技 54903668 (negate monster effect or spell/trap activation), 妖仙兽的居太刀风 10612222 (bounce up to 2 while your field is empty), 妖仙大旋风 79861914 (bounce when your Yosenju return, pay 800 LP), 妖仙乡的眩晕风 62681049 (return to deck instead, needs a Level 6+ Yosenju), floodgates 千查万别 24207889, 烈风之结界像 73356503, 休息一回 24348804
- 妖仙大旋风 79861914 triggers on your own End Phase returns, so it bounces 1 opponent card every turn for free

- **Extenders**

- 木魅 23740893: tribute itself to put 3 妖仙 counters on 修验的妖社 27918963, or banish itself from grave for one extra Yosenju Normal Summon this turn (deepens the Kama chain)
- 修验的妖社 27918963: each Yosenju Normal/Special Summon adds 1 counter; remove 1 for +300 ATK to your Yosenju, remove 3 to add any Yosenju card from deck or grave to hand
- 饭纲鞭 85970321: discard from hand to lock — for the rest of the turn the opponent cannot chain card effects to Yosenju summon triggers; on field it draws 1
- 辻斩风 25244515: discard during the damage step for +1000 ATK on a battling Yosenju, or ignition +1000 ATK on the field
- 神颪 61884774: with no monsters on your field, add a Level 5+ Yosenju (大刃祸是 93368494, 独眼群主 21364070) or place 左镰神柱 65025250 and 右镰神柱 91420254 into pendulum zones; afterwards no non-Yosenju special summons this turn
- 侍郎风 58981727: on summon with another Yosenju on field, search a Yosenju Pendulum monster; ignition once per turn: shuffle 1 face-up Yosenju card into deck to set 妖仙大旋风 79861914 or 妖仙乡的眩晕风 62681049 from deck
- 妖仙兽的风祀 54880296: with 3+ different-named Yosenju monsters, return all your Yosenju cards to hand then draw until 5 in hand
- 炎舞-「天玑」 57103969: search any Level 4 Beast-Warrior (any Kama, 侍郎风 58981727, 饭纲鞭 85970321, 辻斩风 25244515), the deck's main searcher
- 独眼群主 21364070 ATK snowball: every time your card effect returns a card to hand or deck (Kama bounces, 妖仙大旋风 79861914, End Phase returns), all your Yosenju gain +500 ATK

- **Halt Points**

- Effect Veiler or 无限泡影 10045474 on a Kama summon trigger stops the chain at one monster
- 灰流丽 14558127 cannot hit the Kama extra-summon effect (CATEGORY_SUMMON is outside its negate list) but does hit 侍郎风 58981727 search, 镰叁太刀 28630501 search, 神颪 61884774 add, 凶旋岚 49249907 deck special summon, 修验的妖社 27918963 search, 炎舞-「天玑」 57103969 search
- 奈落的落穴 29401950 destroys any Kama on summon (all 1500+ ATK); 激流葬 53582587 wipes the entire chain because every body is a Normal Summon
- 神之宣告 41420027 and 神之通告 40605147 negate the first Normal Summon itself and kill the chain before it starts
- 增殖的G 23434538 is useless against the pure Normal-Summon chain, but modern builds that pendulum summon 独眼群主 21364070 or 大刃祸是 93368494 or use the Fiendsmith/罪宝 package do feed it
- 妖仙兽的居太刀风 10612222 and 神颪 61884774 require an empty monster zone, so a lingering 大幽谷响 69838592 or Xyz monster blocks them
- 削命的宝札 59750328 quirks: battle damage becomes 0 (kills the 镰叁太刀 28630501 search), no special summons that turn, and the End Phase hand discard swallows the returned Kamas

- **Mirror Match**

- Both sides run the same Kama chain; the race is decided by who resolves 妖仙兽的居太刀风 10612222 (bounce up to 2, live on an empty field) and 妖仙兽的秘技 54903668 first
- Never deal battle damage while the opponent has 镰叁太刀 28630501 face-up — every point of damage is a free search for them; remove the Kama 3 or skip the battle phase first
- 镰壹太刀 65247798 bounce only hits face-up cards, so the mirror rewards keeping your own cards face-up and stripping theirs
- 妖仙大旋风 79861914 bounces when your own monster returns, answering the opponent's End Phase recursion with a free bounce every turn
- 妖仙乡的眩晕风 62681049 redirects both players' returned monsters to the deck, denying both sides their End Phase hand recursion
- A 独眼群主 21364070 board (2000 ATK plus the +500 snowball) outclasses the Kama swarm in damage races, and 右镰神柱 91420254 forces the opponent to attack into it

- **Common Mistakes**

- Do not rely on 妖仙兽的秘技 54903668 while any non-Yosenju face-up monster is on your field — its condition fails
- Do not activate 削命的宝札 59750328 and then need battle damage for the 镰叁太刀 28630501 search, damage is 0 that turn
- 妖仙大旋风 79861914 pays 800 LP and destroys itself at your End Phase when unused, track the cost
- 神颪 61884774 locks out non-Yosenju special summons for the turn, never follow it with Fiendsmith or 罪宝 plays
- 大刃祸是 93368494 and 独眼群主 21364070 can only be special summoned by pendulum summon; the default range of 左镰神柱 65025250 (3) and 右镰神柱 91420254 (5) is Level 4 only, use the 右镰神柱 or 独眼群主 scale-11 effect to reach Level 6 or 8
- Do not run 妖仙乡的眩晕风 62681049 in a pure Kama build — it needs a Level 6+ Yosenju on field to activate
- The End Phase return is mandatory and cannot be dodged; do your rank-4 Xyz in Main Phase 2 before it, or accept the empty board
- 镰壹太刀 65247798 bounce needs a second face-up Yosenju on your field and is once while face-up, do not fire it when it is the only monster
- Use the fourth link of the chain for value: the last Kama summons 侍郎风 58981727 or 饭纲鞭 85970321 instead of a fourth attacker
- 灰流丽 14558127 stops your searches, not your summons — bait it with 炎舞-「天玑」 57103969 before the 侍郎风 58981727 search
