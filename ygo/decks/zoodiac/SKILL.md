---
name: zoodiac-experience
description: 十二兽 (Zoodiac) deck experience: overlay-on-top Xyz engine, one-card combo, ladder, extenders, halt points
---
# 十二兽 (Zoodiac) Deck Experience

- **Deck Identity**

- EARTH Beast-Warrior Xyz ladder deck: every Xyz monster summons onto an existing Zoodiac monster with just one material, then keeps climbing
- Main deck monsters: 鼠骑 78872731, 马剑 77150143, 蛇笞 31755044, 羊冲 4145852, 兔铳 4367330, 鸡拳 20155904, all Level 4 EARTH Beast-Warrior
- Ladder Xyz (Rank 4): 狗环 41375811, 虎炮 11510448, 猴槌 14970113, 猪弓 74393852, 龙枪 48905153, 牛犄 85115440
- Spells: 会局 46060017 (continuous), 方合 73881652, 相克 98918572 (continuous trap)
- Finishers: 天霆号 阿宙斯 90448279, 未来No.0 未来龙皇 霍普 26973555 via 未来No.0 未来皇 霍普 65305468, 黑智天至 伊里斯斐尔 64626565, 超银河眼光子龙-光子咆哮 28331069
- Consistency: 炎舞-「天玑」57103969 searches any Level 4 or lower Beast-Warrior, 会局 special summons from deck, 强欲而贪欲之壶 35261759 draws two
- Build is handtrap heavy: 灰流丽 14558127, 增殖的G 23434538, 幽鬼兔 59438930, 屋敷童 73642296, plus 欢聚友伴·茸茸长尾山雀 42141493 and 圣王的粉碎 97045737

- **Core Mechanic: Overlay-On-Top Xyz Engine**

- Every Zoodiac Xyz can be Xyz summoned once per turn onto a face-up Zoodiac monster you control other than itself, taking it as a single material (verified ovfilter plus once-per-turn flag in scripts)
- The overlaid monster keeps its own attached materials, so the material pile transfers up the ladder and grows
- Xyz monsters gain ATK and DEF equal to the sum of the stats of all Zoodiac monsters in their materials (script atkval sums the whole attached pile)
- Each main deck monster grants its host Xyz an extra effect while attached as material: 鼠骑 detaches to summon another 鼠骑 from deck or hand, 马剑 grants piercing, 蛇笞 banishes monsters it battles, 羊冲 negates a targeting Trap, 兔铳 negates a targeting Spell, 鸡拳 negates a targeting monster effect
- Material is also the resource: 龙枪 and 牛犄 detach to pop a face-up card or search a Beast-Warrior, so attaching 蛇笞 31755044 from hand on either turn extends the pile

- **One-Card Combo: 鼠骑 78872731**

- Starter: 鼠骑 in hand, no other cards needed
- Step 1: normal summon 鼠骑, its effect one sends 马剑 77150143 (or 蛇笞 31755044) from deck to graveyard
- Step 2: Xyz summon 狗环 41375811 onto 鼠骑 using the overlay rule, one material
- Step 3: activate 鼠骑 granted material effect, detach 鼠骑, special summon a second 鼠骑 from deck or hand
- Step 4: Xyz summon 虎炮 11510448 onto 狗环, then activate 虎炮 effect two, detach 狗环, attach 马剑 from graveyard under 虎炮
- Step 5: Xyz summon 龙枪 48905153 onto 虎炮, 龙枪 holds 虎炮 plus 马剑 as materials, 马剑 grants piercing and its attack reaches 1600
- Step 6: 龙枪 effect two pops one face-up card, once per turn
- Step 7: attack with 龙枪, then in Main Phase 2 Xyz summon 天霆号 阿宙斯 90448279 onto the Xyz that battled this turn, 阿宙斯 inherits the pile and wipes the field with two detaches
- Alternative ending without battle: Xyz summon 未来No.0 未来皇 霍普 65305468 onto two same-rank non-No. Xyz, then 未来No.0 未来龙皇 霍普 26973555 onto it, indestructible with a negate and control steal per material

- **End Field One-Card**

- 天霆号 阿宙斯 90448279 with two or more materials ready to send every other card to the graveyard
- 龙枪 48905153 with 马剑 77150143 attached for one pop plus piercing, or 猴槌 14970113 protecting all other Zoodiacs from targeting while it holds material
- 未来No.0 未来龙皇 霍普 26973555 with stacked materials for multiple monster effect negates and control steals
- Halt point: 灰流丽 on the 鼠骑 dump or 天玑 search stops the line, 增殖的G draws against every ladder step so stop early under it

- **Extender: 会局 46060017**

- Continuous spell, effect one once per turn: destroy one face-up card you control, special summon any Zoodiac from deck, a second normal-summon worth of bodies
- Effect two: when 会局 is destroyed by an effect, attach itself under a Zoodiac Xyz as material, growing the pile for 龙枪, 阿宙斯, or 未来No.0
- Destroy 会局 with its own effect to trigger both lines at once

- **Extender: 炎舞-「天玑」57103969**

- On activation searches any Level 4 or lower Beast-Warrior, which is every Zoodiac main deck monster, once per turn
- Grants all Beast-Warriors 100 attack while face up, incidental damage boost on the ladder
- Use it to fetch 鼠骑 for the combo or 蛇笞 as a hand extender

- **Extender: 蛇笞 31755044**

- Quick effect, either turn: attach itself from hand or field under a face-up Beast-Warrior Xyz as material, no cost
- Grants the host Xyz a banish-on-battle effect, removing battled monsters permanently, strong against floating monsters
- Adds a material for 龙枪 pop, 阿宙斯 wipe, or 未来No.0 negate count

- **Extender: 马剑 77150143 and 羊冲 4145852**

- 马剑 on summon discards a Zoodiac from hand to draw one, cycling dead 兔铳 or 鸡拳, and grants piercing as material
- 羊冲 when destroyed by battle or effect special summons another Zoodiac from graveyard, the grind engine that replaces itself
- 兔铳 4367330 when destroyed adds a Zoodiac from graveyard to hand, 鸡拳 20155904 shuffles one back to deck, both grant targeting negates as material

- **Extender: 方合 73881652 and 相克 98918572**

- 方合 attaches one Zoodiac from deck under a Zoodiac Xyz, in this build it is a Trap so it must be set a turn before use
- 方合 graveyard effect banishes itself, shuffles five different-name Zoodiacs from graveyard into deck and draws one
- 相克 redirects a Zoodiac Xyz cost detach to another Xyz while on field, then in graveyard banishes itself to attach one of two Zoodiac Xyz under the other, merging piles for a single tall monster

- **Halt Points**

- Stop the ladder at two special summons when 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493 is active, every overlay is a special summon
- 欢聚友伴 discards only when your field is empty, use it before building the board, it draws one per opponent special summon from deck or extra
- 圣王的粉碎 97045737 from hand negates any add-from-deck effect but locks your DARK, WATER and FIRE monster effects for the duel, so reserve it for the opponent's searches
- 无限泡影 10045474 on the 鼠骑 normal summon, 幽鬼兔 59438930 on 会局, 屋敷童 73642296 on graveyard plays like 羊冲, 虎炮 attach, and 狗环 special summon
- 禁忌的一滴 24299458 and 神之宣告 41420027 answer board breakers and key summons, 强欲而贪欲之壶 35261759 and 贪欲之壶 67169062 refill after the ladder

- **Mirror Match: 十二兽 vs 十二兽**

- Whoever resolves 鼠骑 plus 会局 first wins tempo, hold 灰流丽 and 无限泡影 for the opposing 鼠骑 summon or 会局 activation
- 龙枪's pop targets the opposing 会局 46060017 or 炎舞-「天玑」57103969 on field, removing their engine before they extend
- 猴槌 14970113 while holding material makes all other Zoodiacs untargetable, forcing the opposing 龙枪 to waste its pop on 猴槌 itself
- 蛇笞 material banishes whatever your monster battles, stripping the opposing ladder piece and its attached pile permanently
- 相克 98918572 redirects a Zoodiac Xyz detach cost to another Xyz, let 龙枪 keep its material pile for a later 阿宙斯 overlay

- **Common Mistakes**

- Do not climb past 鼠骑 before detaching it, its material effect summons the second 鼠骑 and only works while it is still attached
- 狗环 41375811 special summons from graveyard with effects negated and it cannot be Xyz material, use it as a body only
- 鼠骑 effect one triggers on normal summon only, the special summoned copy does not dump from deck again
- 方合 73881652 is a Trap in this build, set it a turn before expecting the deck attach, and its graveyard draw cannot activate the same turn it was sent
- 猪弓 74393852 needs twelve materials for its hand wipe, do not chase it, use it for direct attack only
- Attach 马剑 before overlaying 龙枪 so the piercing and attack stick, attach 蛇笞 from hand for the banish, attach 羊冲 to enable its revival if destroyed
- 未来No.0 未来皇 65305468 requires two Xyz of the same rank that are not No. monsters, 狗环 and 虎炮 both qualify
- 炎舞-「天玑」searches Level 4 or lower Beast-Warrior only, it cannot fetch 牛犄 or any Xyz
- 会局 destroyed by its own effect still triggers its attach line, and destroying any face-up card including 天玑 is a valid cost

- **Build Quirks**

- The reference pure build has no 牛犄 85115440 in the extra deck, 会局 and 天玑 replace its search role
- 方合 73881652 flagged as Trap in this card database while the OCG version is a normal spell, set it before use
- Rank 8 top of the ladder: 黑智天至 伊里斯斐尔 64626565 overlays onto any Xyz that activated no effect this turn, 超银河眼光子龙-光子咆哮 28331069 overlays onto it to negate all other face-up cards
- 天霆号 阿宙斯 90448279 overlays onto an Xyz that battled this turn once per turn and inherits its full material pile
