---
name: blueeyes-experience
description: 青眼 (Blue-Eyes) deck experience: Eyes-of-Blue tuner engine, 白色少女 one-card combo, 原石/真红眼 hybrids, pitfalls
---
# 青眼 (Blue-Eyes) Deck Experience

- **Deck Identity**

- Core: 青眼白龙 89631139, a Level 8 LIGHT Dragon Normal monster with 3000 ATK, is the fusion/synchro fuel everything else feeds into, plus the Level 1 LIGHT Spellcaster Tuner "Eyes of Blue" engine (青色眼睛的贤士 8240199, 白色少女 17947697, 青色眼睛的护人 72855441, 太古的白石 71039903, 青色眼睛的巫女 36734924, 青色眼睛的少女 88241506, 青色眼睛的祭司 45644898)
- Setcode 0xdd covers 青眼 cards; setcode 0x1b9 covers the 原石 (Primsess) engine; representative decks analyzed: 250125青眼 (pure Eyes-of-Blue), 250125青眼原石 (Primsess control), 220219青眼真红眼 (Red-Eyes fusion hybrid), 251025青眼骑士 (Centurion hybrid)
- 青眼亚白龙 38517737 is the "替代" (Alternative) dragon: its name becomes 青眼白龙 while on field or in grave, and it special summons itself by revealing a 青眼白龙 from hand, so it acts as extra fusion material and extra 真正之光 fuel
- Key spells: 青色眼睛的祈祷 80326401, 真正之光 62089826, 青眼龙轰临 17725109, 光之灵堂 24382602, 龙觉醒旋律 48800175, 究极融合 71143015, 青色眼睛的威光 2783661, 毁灭之爆裂疾风弹 17655904
- Note: the names 白之预选 and 青眼的碎片 were NOT found in cards.cdb or the script pool for this build; the closest verified cards are 光之灵堂 24382602 (extra normal summon of a Level 1 Light Tuner) and 龙觉醒旋律 48800175 (search 青眼白龙), treat the two hinted names as unverified

- **Core Mechanic: Tuner Swarm into 青眼精灵龙**

- The Level 1 Light Tuners either search 青眼白龙 out of the deck, grave, or hand, or dump themselves to grave and float back when a 青眼白龙 is special summoned, feeding the one Level 8 non-tuner 青眼白龙 into a Level 9 synchro
- Central boss: 青眼精灵龙 59822133, synchro of 1 tuner plus 1 or more 青眼 non-tuners, which blocks both players from special summoning two or more monsters at the same time, negates effects activated from the grave, and once per turn can tribute itself to tag out into any Light Dragon synchro from the extra deck
- 真正之光 62089826 is a continuous trap that once per turn special summons 青眼白龙 from hand or grave, or sets a spell/trap that lists 青眼白龙 from deck, and makes your 青眼白龙 untargetable by opponent effects
- 真正之光 62089826 is a trap but the engine places it face-up (not set) via 白色少女, and in this core a face-up placed trap can be activated the same turn, so the one-card line resolves

- **One-Card Combo: 白色少女 17947697**

- Requirement: a 青眼白龙 89631139 (or 青眼亚白龙 38517737 in grave, whose name counts) available in hand or grave
- Step 1: normal summon 白色少女 17947697 and activate its effect one, sending itself to the grave as cost and placing 真正之光 62089826 face-up from deck, hand, or grave
- Step 2: activate 真正之光 effect one, special summoning 青眼白龙 89631139 from hand or grave
- Step 3: 白色少女's effect two triggers in the grave because a 青眼白龙 was special summoned, special summoning itself back
- Step 4: synchro summon 青眼精灵龙 59822133 using 白色少女 as the Level 1 tuner and 青眼白龙 as the non-tuner
- End field: 青眼精灵龙 plus face-up 真正之光, with a grave negate and a tag-out available; on the opponent turn tribute 精灵龙 to tag into 苍眼银龙 40908371 in defense, whose summon protection makes all your dragons untargetable and indestructible by effects until your second end phase
- Halt points: no 青眼白龙 in hand or grave stalls the line at 真正之光 plus 白色少女; 灰流丽 14558127 on 真正之光 activation or 白色少女's summon search stops the synchro

- **Two-Card Starter: 青色眼睛的祈祷 80326401**

- Activate 青色眼睛的祈祷, discard 1 card as cost, and add any spell or trap that lists 青眼白龙 plus any Level 1 Light Tuner from deck, for example 真正之光 62089826 plus 白色少女 17947697
- Then run the 白色少女 line above: normal summon 白色少女, place 真正之光, special summon 青眼白龙, revive 白色少女, synchro 青眼精灵龙 59822133
- 祈祷's grave effect banishes itself to equip any 青眼 monster from the extra deck to a face-up 青眼白龙 you control, giving it 400 attack and setting up 青眼暴君龙's alternative summon by tributing the equipped 青眼白龙

- **Extender: 青色眼睛的贤士 8240199 and 青色眼睛的护人 72855441**

- 贤士: on normal summon search any Level 1 Light Tuner from deck; from hand, discard itself and send one face-up effect monster you control to the grave to special summon 青眼白龙 from the deck
- 护人: on normal summon special summon a Level 1 Light Tuner from hand; its ignition effect sends a face-up effect monster to the grave to special summon a 青眼 monster from hand
- Both are the send-to-grave-to-cheat-青眼白龙 extenders, so 贤士 or 护人 plus any face-up effect monster (even the tuner itself) converts into an extra 青眼白龙

- **Extender: 太古的白石 71039903 and 光之灵堂 24382602**

- 太古的白石: when sent to the grave, during the end phase special summons any 青眼 monster from deck; from the grave it banishes itself to return a 青眼 monster to hand, so it is the ideal discard fodder for 抵价购物 38120068 and synchro material
- 光之灵堂: field spell granting one extra normal summon per turn of a Level 1 Light Tuner, and an ignition effect that sends a normal monster from hand or deck to grave to boost a monster by level times 100 attack and defense
- 青色眼睛的精灵 42097666, a link 1 of one Level 4 or lower Dragon or Spellcaster, searches 光之灵堂 on link summon, tributes itself to special summon a 青眼 monster from hand or grave, and locks you to Dragon-only special summons while it is on field, so link it away before non-Dragon plays

- **Extender: 原石 (Primsess) Engine**

- 原石龙 变种绿柱石龙 63198739: on normal summon set one 原石 spell or trap from deck, then tribute itself to send one normal monster from deck to grave (青眼白龙), and in your standby phase return itself from grave to hand while a normal monster is face-up on field or in grave
- 原石的皇脉 56506740: continuous spell that searches a 原石 spell or trap on activation, gives normal monsters and 原石 monsters attack equal to 300 times the number of different normal monster names in your grave, and announces one normal monster name to special summon it from hand, deck, or grave in defense
- 原石的穿光 29095457: quick-play that negates a face-up card's effects and banishes it, paying either by revealing a 原石 or normal monster from hand or by controlling a face-up normal or Level 5 plus 原石 monster, and it re-sets itself from grave while a face-up 原石 monster is on field
- 圣王的粉碎 97045737: trap that can be activated from hand while the opponent has a card on field, negating any draw or search effect and destroying the card if a trap is in your grave, then locking the opponent out of Dark, Fire, and Water monster effects for the turn if played from hand
- Pitfall: after 原石的皇脉 special summons a monster, you cannot activate effects of any of your special-summoned monsters for the rest of the turn, so use 皇脉 as the last summon of the turn, ideally only to put vanilla 青眼白龙 89631139 on board

- **Extender: 真红眼 (Red-Eyes) Hybrid**

- 真红眼融合 6172122 fuses a 真红眼 fusion monster using materials from hand, field, and deck as the first action of the turn, and then locks you out of all further summons that turn, so sequence it before any other summon
- Targets: 流星龙 流星黑龙 30086349 (Level 7 真红眼 plus a Level 6 Dragon, burns half a sent 真红眼's attack and revives a normal monster when it leaves the field) and 真红眼钢炎龙 44405066 (rank 7 xyz, 500 burn per opponent activation, detach to revive a 真红眼 normal)
- 真红眼暗钢龙 88264978: banishes a face-up Dragon you control to special summon itself from hand, then once per turn special summons a Dragon from hand or grave, acting as the recursion engine of the hybrid
- 真红眼黑星龙 27657173 special summons itself by sending a Level 5 or higher normal monster from hand or deck to grave, and 真红眼之魂 44397496 plus 真红眼的铠旋 39387565 revive 真红眼 monsters from the grave

- **Optional Variant: 百夫长 (Centurion) Hybrid**

- 251025青眼骑士 mixes the Eyes-of-Blue engine with 百夫长 knights such as 骑士皇 普莉梅拉·首席百夫长 8841431 and 从骑士 特露迪娅 42493140, using 红龙 63436931, which returns a Level 7 or higher synchro to the extra deck to summon a same-level Dragon synchro as if synchro summoned, to cheat out 青眼究极灵龙 89604813 and 宇宙耀变龙 21123811

- **Halt Points**

- 灰流丽 14558127: hit 青色眼睛的祈祷 80326401 activation, 贤士's search, 真正之光's special summon, or 青眼龙轰临's summon
- 无限泡影 10045474 or 效遮: hit 白色少女 17947697 or 原石龙 变种绿柱石龙 63198739 before they resolve
- 增殖的G 23434538: the deck special summons constantly, so under G either end on 青眼精灵龙 59822133 only or pass on 真正之光 62089826 without extending
- 次元吸引者 91800273: banishes grave resources, breaking 真正之光's summon, 太古的白石, and 白色少女's grave revival
- 墓穴的指名者 24224830: exiles 太古的白石 71039903 or 白色少女 17947697 from grave to cut the recursion engine

- **Mirror Match: 青眼 vs 青眼**

- Whichever player's 青眼精灵龙 59822133 resolves first wins the grave war, because its negate stops the opponent's 太古的白石, 青眼喷气龙, and 白色少女 grave effects
- Note the script has no controller check on 精灵龙's grave negate, so it can negate your own grave activations too if you chain carelessly
- 蓝眼银龙 16699558, an xyz of two Level 8 Dragons, negates all opponent face-up cards' effects on xyz summon and revives a normal monster, so whoever makes it first blanks the other's 真正之光 and 亚白龙
- 苍眼银龙 40908371 protection races matter: it must survive until its protection window to stop a 蓝眼银龙 or 真青眼究极龙 56532353 swing
- 墓穴的指名者 24224830 and 灰流丽 14558127 resolve the 白石 and 少女 exchanges before any synchro happens

- **Common Mistakes**

- Do not let 真正之光 62089826 be sent face-up from the spell and trap zone to the grave: its third effect destroys all your monsters, so keep 苍眼银龙 40908371 protection up or remove it proactively before the opponent pops it
- 真正之光's special summon needs a 青眼白龙 89631139 in hand or grave, verify one exists before activating effect one, and remember 青眼亚白龙 38517737 counts in the grave
- 青眼龙轰临 17725109 restricts you to Dragon-only special summons from the extra deck for the turn, activate it after your non-Dragon link plays
- 原石的皇脉's effect lock hits every monster you special summon that turn, including fusion, synchro, and xyz monsters, so never use it mid-combo before effect monsters that need to activate
- 青眼精灵龙's tag-out special summons in defense and destroys the monster at the end phase, so time the 苍眼银龙 tag for the opponent turn and do not rely on the tagged monster surviving
- 青色眼睛的激临 29432790 banishes your entire hand, field, and grave face-down to summon up to three 青眼白龙 from deck, and locks your summons to 青眼白龙 for the turn, so it is a last-resort all-in only
- 究极融合 71143015 shuffles its materials into the deck instead of sending them to the grave, so 太古的白石's sent-to-grave effect never triggers off it
- 苍眼银龙 requires normal monster non-tuners, so it cannot be synchro summoned with effect monster non-tuners
- 蓝眼银龙 cannot attack directly unless it has a normal monster as xyz material, and 真青眼究极龙 56532353's chain attack costs a 青眼 fusion from the extra deck, keep one in reserve
- 青色眼睛的幻出 35659410 and 青色眼睛的威光 2783661 are flexible quick actions, use them on the opponent's turn to dodge targeting or to stall attackers
