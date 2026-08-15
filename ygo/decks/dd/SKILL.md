---
name: dd-experience
description: D/D 地狱帝王·契约书 (D/D Contract) deck experience: contract burn engine, one-card combo, extenders, halt points
---
# D/D 地狱帝王·契约书 (D/D Contract) Deck Experience

- **Deck Identity**

- 契约书 (Dark Contract) is the Chinese name of the D/D archetype's continuous spell/trap series, not a separate archetype; the D/D deck (地狱帝王) is built around these contracts plus the D/D and D/D/D monsters
- True identity verified from cards.cdb: 契约书 cards carry setcode 0xae, D/D monsters carry 0xaf, D/D/D carry 0x10af, and the core matches 0x10af cards against 0xaf queries, so D/D/D monsters also count as D/D for effects and materials
- All 11 契约书: 地狱门的契约书 46372010, 魔神王的契约书 73360025, 魔神王的禁断契约书 10833828, 常暗的契约书 9030160, 暗魔界的契约书 45974017, 异次元的契约书 54936778, 零王的契约书 32665564, 女武神的契约书 9765723, 异形神的契约书 60168186, 误封的契约书 37209439, 特许权的契约书类 33814281; the 契约书 tag on 459 deck folders comes from any of them
- Engine opener: 开普勒 11609969 (on summon adds any 契约书 from deck) plus 地狱门的契约书 46372010 (adds any D/D monster from deck, D/D/D included)
- Main deck monsters: 拉弥亚 19580308, 俄耳托斯 72181263, 魔导贤者哥白尼 46796664, 刻度测量员 42382265, 计数测量员 5997110, 螺涡史莱姆 45206713, 死灵史莱姆 72291412, 巴风特 19808608, 夜吼怪 48210156, 狮鹫 28406301
- Extra deck bosses: 深渊王比尔伽美斯 9024198, 双晓王末法神 15939229, 咒血王赛弗里德 44852429, 怒涛大王决策凯撒 79559912, 怒涛王凯撒 3758046, 神托王达克 82956492, 赦俿王死亡机降神 46593546, 零死王零机降神 20715411, 伟次元王弧线危机神 71398055, 死伟王地狱终末神 47198668

- **Core Mechanic: 契约书 Burn and Search Loop**

- Every 契约书 deals 1000 LP damage to its owner in their own standby phase (异形神的契约书 60168186 deals 2000), so a field of three contracts costs 3000 LP per standby; 神托王 达克 82956492 converts damage you would take into LP gain
- The search loop: 开普勒 11609969 adds any 契约书 on summon, 地狱门的契约书 46372010 adds any D/D monster, and 零王的契约书 32665564 destroys a D/D card you control to summon a D/D monster from the deck
- 零死王 20715411 recursion: whenever a face-up D/D/D card or 契约书 you control is destroyed, 零死王 in the face-up extra deck special summons itself and may destroy 1 card; when destroyed on the field it moves to the pendulum zone at scale 0
- The deck is a two-card deck: the opener needs one extender card to reach the full board, and the link 2 深渊王 比尔伽美斯 9024198 turns two D/D monsters into pendulum scales
- 深渊王 比尔伽美斯 9024198 places 2 different-name D/D pendulum monsters from the deck into the pendulum zones, deals 1000 damage, and locks you into D/D-only special summons for the rest of the turn

- **One-Card Combo: 开普勒 11609969**

- Step 1: normal summon 开普勒 11609969, activate its effect to add 地狱门的契约书 46372010 from the deck
- Step 2: activate 地狱门的契约书 to add DD 拉弥亚 19580308 from the deck
- Step 3: activate 拉弥亚 from the hand by sending the face-up 地狱门的契约书 from the field to the graveyard as cost, special summon 拉弥亚 as a level 1 tuner
- Step 4: link 开普勒 and 拉弥亚 into 深渊王 比尔伽美斯 9024198, then its effect places 2 different-name D/D pendulum monsters from the deck in the pendulum zones and deals 1000 damage
- Step 5: place 零死王 零·机降神 20715411 (scale 0) and 刻度测量员 42382265 (scale 9), which together allow any level 1-8 D/D pendulum summon; after this effect only D/D monsters can be special summoned until the end of the turn
- Halt note: this one-card line ends on 比尔伽美斯 plus two scales; any second D/D or 契约书 card in hand extends into the pendulum loop and the boss plays

- **Two-Card Line: 开普勒 + 螺涡史莱姆**

- Step 1: normal summon 开普勒 11609969, search 魔神王的契约书 73360025
- Step 2: activate 魔神王的契约书 to fusion summon 神托王 达克 82956492 using 开普勒 from the field and 螺涡史莱姆 45206713 from the hand
- Step 3: banish 螺涡史莱姆 from the graveyard to special summon DD 拉弥亚 19580308 from the hand
- Step 4: synchro 拉弥亚 (level 1 tuner) with 神托王 达克 (level 7 D/D/D non-tuner) into 咒血王 赛弗里德 44852429, a once-per-turn spell/trap activation negate
- Step 5: 死灵史莱姆 72291412 in the graveyard provides a second fusion from the grave, and 魔神王的禁断契约书 10833828 specials a D/D/D from the hand then fuses using it

- **End Field**

- Full board: 双晓王 末法神 15939229 (rank 8 from 零死王 20715411 plus 死讴王 恶德镇魂神 25857977) negates all other face-up card effects until the end phase, its quick effect destroys all spell and trap cards on the field, and it can set a 契约书 from the grave
- 咒血王 赛弗里德 44852429 (level 8 synchro) negates one spell/trap activation per turn on either turn, and heals 1000 LP per face-up D/D when destroyed
- 怒涛大王 决策凯撒 79559912 (rank 6) negates any effect that special summons a monster and then boosts ATK by 1800; 怒涛王 凯撒 3758046 (rank 4) searches a 契约书 when it leaves the field, enabling the overlay loop
- Backrow: 异次元的契约书 54936778 (shuffle 2 契约书 from grave to deck to banish 1 card), 常暗的契约书 9030160 (opponent cannot target, tribute, or use your monsters as fusion/synchro/xyz material while 2 D/D pendulums are in your zones), 误封的契约书 37209439 (negates field traps), 特许权的契约书类 33814281 (burn and extra-deck type-lock)
- 零死王 零·机降神 20715411 stays as a recursion threat: it returns from the face-up extra deck whenever your D/D/D or 契约书 is destroyed
- Late game: 赦俿王 死亡机降神 46593546 (rank 10) attaches the opponent's monster as material when they activate a monster effect, then returns to the pendulum zone in your standby; 伟次元王 弧线危机神 71398055 destroys 契约书 to summon 死伟王 pendulums, and as a 4-material monster negates all opponent face-up monsters and attacks all of them once

- **Extenders**

- 魔导贤者 哥白尼 46796664: on summon mills any D/D or 契约书 card from the deck, loading 死灵史莱姆 72291412, 拉弥亚 19580308, or 幽灵 33334269 for later plays
- 刻度测量员 42382265: special summons itself while any D/D pendulum card is on your field, then sets its own level to 4; its scale 9 pairs with 零死王 20715411's scale 0
- 计数测量员 5997110: discards another D/D to special summon itself, then searches a D/D monster with 0 ATK or 0 DEF such as 开普勒 11609969 or 刻度测量员 42382265
- 巴风特 19808608: changes a D/D monster's level from 1 to 8 to build ranks, locking you into D/D special summons
- 夜吼怪 48210156: on normal summon revives a D/D from the grave at 0 ATK/DEF, taking 1000 damage if that monster is destroyed; locks you into Fiend special summons
- 持枪战士 67322708: raises a D/D monster's level by the number of 契约书 cards in your field and grave, enabling rank 10 赦俿王 死亡机降神 46593546
- 死讴王 恶德镇魂神 25857977: destroys any number of your 契约书 to summon itself and adjust its level; as material it grants the summoned D/D/D a target-destroy effect that recycles a 契约书 and heals 1000
- 女武神的契约书 9765723: sends a D/D or 契约书 from hand to grave to destroy any card, and boosts your Fiends' ATK during the opponent's turn
- 零王的契约书 32665564 chains with 零死王 20715411: destroying a face-up D/D/D or 契约书 with it triggers 零死王's self-summon plus a pop
- Fusion line: 魔神王的契约书 73360025 fuses from hand and field, 魔神王的禁断契约书 10833828 specials a D/D/D from the hand then fuses with it, 螺涡史莱姆 45206713 fuses from the hand, 死灵史莱姆 72291412 fuses from the grave

- **Halt Points**

- Ash Blossom on 开普勒 11609969's search or on 地狱门的契约书 46372010's search stops the engine at the first piece
- Ash or effect veiler on 深渊王 比尔伽美斯 9024198's pendulum placement ends the line before the scales exist
- 增殖的G punishes every D/D special summon; D/D cannot play under it, so end on 开普勒 plus one 契约书 as the compromise
- 次元吸引者 91800273 or any banishing floodgate hurts badly: 拉弥亚 19580308 is banished when it leaves the field, both slimes fuse from the graveyard, and 零王的契约书 32665564 relies on grave recursion
- Ghost Ogre on the 零王的契约书 32665564 destruction step or on 零死王 20715411's revival leaves the deck without a body

- **Mirror Match: D/D vs D/D**

- The standby burns are symmetrical and stack, so 神托王 达克 82956492 is the mirror MVP: whoever lands it first turns both players' burn into their own LP gain
- 双晓王 末法神 15939229 ends the game on the spot: xyz summoning it negates all other face-up card effects including the opponent's contracts, then its quick effect clears their backrow
- 异次元的契约书 54936778 banishes the opponent's contract engine from field or grave; resolve it before they set up 零死王 20715411 recursion
- 误封的契约书 37209439 negates all field traps, so play your own trap activations before it resolves
- Whoever resolves 开普勒 11609969 plus 地狱门的契约书 46372010 first usually wins; the mirror is decided by who pushes the first search through hand traps

- **Common Mistakes**

- Do not activate spells or effects after xyz summoning 双晓王 末法神 15939229: its negation hits your own cards too until the end phase, so resolve every 契约书 search before it
- Do not sit on 常暗的契约书 9030160 with only one D/D pendulum in your zones; its protection requires 2 D/D pendulum cards in your pendulum zones
- 开普勒 11609969 used as a scale drops from 10 by 2 every standby and destroys all face-up monsters you control that are not D/D (D/D/D included) at or above the new scale, ruining hybrid pendulum piles
- Track the burn math: three 契约书 cost 3000 LP every standby and 异形神的契约书 60168186 costs 2000 alone, lethal if you forget to end on 神托王 达克 82956492
- 拉弥亚 19580308 is banished when it leaves the field, so do not waste its summon; 螺涡史莱姆 45206713 and 死灵史莱姆 72291412 fuse from the graveyard and must stay there until used
- After 零王的契约书 32665564, 深渊王 比尔伽美斯 9024198, or 巴风特 19808608 resolves, you can only special summon D/D monsters for the rest of the turn, so sequence non-D/D extenders first
- 零死王 零·机降神 20715411's scale-0 pendulum effect only works during the main phase of the turn it was activated, so do not wait a turn to place a 契约书 from the deck
