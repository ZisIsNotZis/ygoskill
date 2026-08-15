---
name: tearlaments-experience
description: 珠泪哀歌族 (Tearlaments) deck experience: mill-and-grave-fusion engine, one-card combo, extenders, halt points
---
# 珠泪哀歌族 (Tearlaments) Deck Experience

- **Deck Identity**

- Pure builds play 3x each of the four main monsters: 雷诺哈特 73956664, 塞壬人鱼 572850, 小美人鱼 37961969, 梅洛人鱼 74078255
- Fusion bosses: 水仙女人鱼 92731385, 鲁莎卡人鱼 84330567, 卡雷多哈特 28226490
- Field spells: 壹世坏-珍珠世界 77103950 (search + destroy engine), 袅袅涟歌姬的壹世坏 34225426 (extra deck mill)
- Backrow: 壹世坏奏响的哀唱 74920585 (continuous trap negate), 壹世坏清澈的残响 1329620 (counter trap), 壹世坏摩擦的爪音 38436986 (normal trap), 劈穿壹世坏的弦声 6767771 (continuous spell), 摇撼壹世坏的鼓动 60362066 (quick-play), 壹世坏涡旋的反响 33878367 (normal spell)
- All main monsters are WATER; 雷诺哈特 73956664 is the only Warrior, the rest are Aqua race
- 珠泪哀歌族型俱舍怒威族 4928565 is the Kashtira hybrid played in later builds
- 2023 builds add the Ishizu fairy engine: 古尖兵 凯尔柏克 25926710, 古卫兵 阿基多 62320425, 宿神像 凯尔多 63542003, 剑神官 姆多拉 99937011
- Variants: pure, 影依 (Shaddoll) hybrid ending on 神影依·米德拉什 94977269, and 邻家割草 11110587 60-card piles
- Historically one of the strongest decks ever; results are pile-driven, so the agent must adapt the line to whatever gets milled

- **Core Mechanic: Mill-and-Grave Fusion**

- Every main-deck Aqua Tearlaments (塞壬人鱼 572850, 小美人鱼 37961969, 梅洛人鱼 74078255) has a second effect: when sent to the GY by a card effect, fusion summon any Fusion monster using materials from your hand, field, and GY, returning the materials to the bottom of the deck in any order
- The grave fusion is a proper Fusion Summon (SUMMON_TYPE_FUSION), so on-summon effects like 水仙女人鱼 92731385 ① trigger normally
- The trigger is strict: the monster must be sent to the GY BY A CARD EFFECT; battle destruction, paying fusion materials, costs, and 简易融合 1845204's end-phase destruction do not trigger it
- 雷诺哈特 73956664 ① on Normal/Special Summon sends any other 珠泪哀歌族 monster from deck to GY, which immediately triggers its grave fusion
- 雷诺哈特 73956664 ② when sent to the GY by an effect: special summons itself (banished if it later leaves the field) and discards 1 珠泪哀歌族 card from hand, and that discarded card can trigger its own grave fusion
- 水仙女人鱼 92731385 ③ when sent to the GY by an effect mills 5 from your deck, restarting the pile chain
- The archetype setcode is 0x181 (385); 壹世坏-珍珠世界 77103950 ① on activation searches any 珠泪哀歌族 monster (or 维萨斯-斯塔弗罗斯特 56099748)
- 壹世坏-珍珠世界 77103950 ③ once per turn: when a face-up Tearlaments monster you control or a Tearlaments monster in your GY returns to the deck, destroy 1 card on the field; every grave fusion's material return to deck bottom triggers this, making each fusion a free destruction
- The grave fusion blocks GY materials under 王家长眠之谷 because the scripts apply aux.NecroValleyFilter
- 水仙女人鱼 92731385 ① searches by setcode, so it finds the 壹世坏 backrow and monsters but NOT 壹世坏-珍珠世界 77103950 (its setcode is 0)

- **One-Card Combo: 雷诺哈特**

- Starter: 雷诺哈特 73956664 in hand, searchable by 壹世坏-珍珠世界 77103950 or 增援 32807846
- Step 1: normal summon 雷诺哈特, use ① to send 梅洛人鱼 74078255 from deck to GY
- Step 2: 梅洛人鱼 ② grave fusion: 雷诺哈特 (field, Tearlaments) + 梅洛人鱼 (GY, Aqua) into 水仙女人鱼 92731385
- Step 3: 水仙女人鱼 ① search: add 壹世坏奏响的哀唱 74920585, 壹世坏涡旋的反响 33878367, or a monster like 塞壬人鱼 572850, or send 哀唱 to the GY so its GY effect searches a monster
- Step 4: 水仙女人鱼 ②: target itself, special summon another Tearlaments from hand or GY (塞壬人鱼 572850 or a second 梅洛人鱼 74078255), then send the targeted 水仙女人鱼 to the GY
- Step 5: 水仙女人鱼 ③ mills 5; the newly summoned or milled Aqua Tearlaments monsters trigger further grave fusions
- Step 6: keep fusing while materials allow, upgrading to 鲁莎卡人鱼 84330567 (水仙女人鱼 + 1 Tearlaments) and 卡雷多哈特 28226490 (雷诺哈特 + 2 Aqua)

- **End Field**

- 鲁莎卡人鱼 84330567: once per turn quick negate of an opponent effect that includes special summoning, other Aqua monsters immune to battle destruction, and it revives itself when a fusion-summoned copy is sent to the GY by an effect
- 卡雷多哈特 28226490: returns one opponent card to the deck when special summoned and whenever an Aqua monster is sent to your GY by an effect; it cannot be used as fusion material
- 水仙女人鱼 92731385 kept on field: searches on summon and special summons a Tearlaments from hand or GY while sending a monster you control to the GY
- 壹世坏-珍珠世界 77103950 face-up: +500 ATK to fusions and Tearlaments monsters, its search, and the destroy-on-recycle engine
- Set backrow: 壹世坏奏响的哀唱 74920585 (negates an opponent effect monster, then sends 1 of your monsters to the GY), 壹世坏清澈的残响 1329620 (counter trap), 壹世坏摩擦的爪音 38436986 (flips a monster down + sends a Tearlaments from deck to GY)
- The 影依 hybrid ends on 神影依·米德拉什 94977269 (limits each player to one special summon per turn) or 神影依·七贤巨鲲魔 50907446
- Typical one-card end field: 鲁莎卡人鱼 + 卡雷多哈特 or 水仙女人鱼, 壹世坏-珍珠世界, one set trap, plus hand traps

- **Extenders**

- 塞壬人鱼 572850: Main Phase ignition from hand: special summons itself, sends 1 monster from hand to GY (that monster's grave fusion triggers), then mills 3
- 简易融合 1845204: pay 1000 LP to fusion summon 千眼纳祭神 63519819 (steals and equips one monster, locks attacks) or directly 水仙女人鱼 92731385 (Level 5), whose ① and ② continue the line
- 壹世坏涡旋的反响 33878367: normal spell, special summons 1 珠泪哀歌族 monster (or 维萨斯-斯塔弗罗斯特 56099748) from deck or GY, then sends 1 face-up monster you control with the same race or attribute to the GY, triggering its grave fusion
- 绝海之马雷 31259606: on summon sends 1 Aqua from deck to GY; end phase tributes itself to add 1 Aqua from GY to hand
- 珠泪哀歌族型俱舍怒威族 4928565: quick effect in Main Phase, special summons itself from hand, banishes 1 俱舍怒威族 or 珠泪哀歌族 card from hand/GY, then mills 3 from either player's deck (choose your own deck in the mirror)
- 袅袅涟歌姬的壹世坏 34225426: when an Aqua-race 珠泪哀歌族 monster is sent to your GY by an effect, sends 1 Level 4 or lower Aqua from deck to GY; a non-Tearlaments monster sent this way has its effects locked this turn
- 劈穿壹世坏的弦声 6767771: when a monster is summoned while you control a Tearlaments, mills 3 and makes opponent monsters lose 500 ATK; in the GY it searches a 珠泪哀歌族 trap from the deck
- 摇撼壹世坏的鼓动 60362066: quick-play, returns 1 Spell/Trap on the field to the deck then sends 1 card from hand to GY (triggers grave fusions); in the GY it recovers a banished 珠泪哀歌族 trap
- 愚蠢的埋葬 81439173 sends any Tearlaments monster straight from deck to GY to trigger its second effect immediately
- 愚蠢的副葬 35726888 sends 壹世坏奏响的哀唱 74920585 or 壹世坏清澈的残响 1329620 to the GY to use their GY search effects
- 增援 32807846 searches 雷诺哈特 73956664 because it is a Level 4 Warrior
- 影依兽 3717252 draws 1 card when sent to the GY by a card effect, giving value from the mills
- Ishizu engine: 古尖兵 凯尔柏克 25926710 and 古卫兵 阿基多 62320425 mill 5 from both decks when sent from hand or deck to the GY, flooding the pile; 宿神像 凯尔多 63542003 and 剑神官 姆多拉 99937011 banish themselves to shuffle up to 3 cards in either GY back into the deck (rip the opponent's GY or recycle fusions); 凯尔柏克 ① also bounces one opponent special-summoned monster when a card is milled to their GY

- **Halt Points**

- 灰流丽 14558127 on 雷诺哈特 73956664 ① (the deck send) stops the standard line's first fusion, leaving only a vanilla 雷诺哈特 on field
- 灰流丽 14558127 on 水仙女人鱼 92731385 ① search or 壹世坏-珍珠世界 77103950 ① search cuts the resource generation
- 墓穴的指名者 24224830 and D.D.乌鸦 24508238 remove the key GY monster (梅洛人鱼 74078255 or 雷诺哈特 73956664) before its grave fusion resolves
- 深渊的潜伏者 21044178 (Abyss Dweller) shuts off all GY triggers while on the field, the strongest generic counter
- 次元吸引者 91800273 sends cards to banishment instead of the GY; the deck cannot play under it at all
- 王家长眠之谷 blocks GY fusion materials via the NecroValleyFilter in the scripts
- Under 增殖的G 23434538, every special summon and grave fusion gives the opponent a draw; compromise by making 水仙女人鱼 92731385 and stopping, or decline the optional grave-fusion triggers

- **Mirror Match**

- The engines are symmetric: both players' mills feed each other's GY, and 古尖兵 凯尔柏克 25926710 plus 古卫兵 阿基多 62320425 mill both decks, so careless milling hands the opponent their combo
- Whoever resolves 深渊的潜伏者 21044178 first usually wins because the opponent's grave engine dies
- 次元吸引者 91800273 is an auto-win opener in the mirror
- 墓穴的指名者 24224830 and D.D.乌鸦 24508238 hit the opponent's 雷诺哈特 73956664 or 梅洛人鱼 74078255 as soon as they reach the GY
- 卡雷多哈特 28226490 is the main removal: its spin keeps clearing the opponent's monsters while your own Aqua mills trigger it repeatedly
- 珠泪哀歌族型俱舍怒威族 4928565 mill choice: always mill your own deck, never the opponent's
- Make 鲁莎卡人鱼 84330567 on your turn so its special-summon-effect negate protects you on theirs
- 壹世坏奏响的哀唱 74920585 and 壹世坏清澈的残响 1329620 are the mirror's backrow weapons: negate the opponent's key monster effects and shuffle their cards away

- **Common Mistakes**

- The grave-fusion trigger needs "sent to GY by a card effect": battle destruction, material payment, costs, and 简易融合 1845204's end-phase destruction do not trigger it
- 卡雷多哈特 28226490 cannot be used as fusion material; never include it in a material selection
- 雷诺哈特 73956664 ②'s revived copy is banished when it leaves the field, so do not plan on it as a persistent body or material
- 雷诺哈特 73956664 ② forces a discard of a 珠泪哀歌族 card from hand: keep one available before sending it to the GY
- 小美人鱼 37961969 ① only responds to opponent monster effects activated from the field, not spells, traps, or hand-activated effects
- 壹世坏涡旋的反响 33878367 needs a face-up monster you control matching the summoned monster's race or attribute, otherwise it cannot be activated
- 水仙女人鱼 92731385 ② sends the targeted monster to the GY, so target a monster whose grave effect you want to trigger
- The grave fusion returns materials to the bottom of the deck in the order you choose; with 壹世坏-珍珠世界 77103950 active this triggers its destroy effect once per turn
- Under 增殖的G 23434538, decline the optional grave fusions to keep special summons low
- 壹世坏奏响的哀唱 74920585 must send 1 monster you control: do not activate it with an empty field, and prefer sending an Aqua Tearlaments to trigger its grave fusion
- 水仙女人鱼 92731385 ① can send the searched card to the GY instead of adding it: sending 壹世坏奏响的哀唱 74920585 or 壹世坏清澈的残响 1329620 uses their GY effects
- 劈穿壹世坏的弦声 6767771 only mills on the turn a monster is summoned while you control a Tearlaments, so time its activation with a summon
- Never mill the opponent's deck with 珠泪哀歌族型俱舍怒威族 4928565 or the Ishizu cards if it enables their grave plays
- 袅袅涟歌姬的壹世坏 34225426 locks the effects of a non-Tearlaments Aqua it sends, so do not send 绝海之马雷 31259606 or 沼地的魔神王 79109599 unless you accept losing their effects this turn

- **Naming Notes**

- The task references 世界鸣动 and 救世神眠 but neither card name exists in this codebase's cards.cdb; the "cryme" spell is 壹世坏涡旋的反响 33878367, implemented here as a Normal SPELL rather than a trap
- The "graveyard fusion" is not a card: it is the second effect of 塞壬人鱼 572850, 小美人鱼 37961969, and 梅洛人鱼 74078255
- All effects in this file were verified against the scripts in /home/z/ygo/script/c*.lua and cards.cdb; setcode 0x181 is the archetype bit used by every search filter
