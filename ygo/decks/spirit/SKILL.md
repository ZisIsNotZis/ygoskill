---
name: spirit-experience
description: 精灵 树精 (Doriado) deck experience: attribute-mixing ritual engine, one-card combo, extenders, halt points, mirror
---
# 精灵 (树精 Doriado) Deck Experience

- **Deck Identity**

- 精灵 in this card database resolves to the 树精 (Doriado) family, LIGHT Fairy monsters built around being treated as every attribute, it is not the 灵魂 Spirit monster type and not the vanilla 精灵 beatdown pile
- Main monsters: 精灵术师 树精 99414168 (Level 3 LIGHT Fairy Ritual, the 2002 original), 精灵世妃 树精 50208444 (Level 7, 2021 retrain), 精灵神后 树精 32965616 (Level 9, modern boss), 暗黑树精 62312469 (Level 4 DARK Spellcaster Pendulum)
- Ritual spells: 树精的祈祷 23965037 (summons 精灵术师 树精 only) and 精灵的祝福 37626500 (summons any LIGHT ritual monster)
- Signature payoff: 风林火山 1781310, the four-element quick-play, run at three copies in real Doriado builds
- Charmer overlap: 精灵术的使魔 45538320 and 精灵术的术使 91530236 are 灵使/凭依 (Charmer) support sharing the 精灵术 Spiritual Arts name prefix, use them as a cross-engine not as archetype core
- Ambiguity: 精灵兽 cards such as 精灵兽 雷鹰 49885567 are the Ritual Beast 灵兽 archetype, old vanillas 山之精灵 34690519, 岩石之精灵 82818645, 气象精灵 96643568, 书之精灵 68963107 form the casual 200000精灵 beatdown, and 精灵剑士 91152256 is an unrelated vanilla elf swordsman

- **Core Mechanic: Attribute Mixing**

- 精灵术师 树精 99414168 is treated as EARTH, WATER, FIRE and WIND in addition to its own LIGHT (EFFECT_ADD_ATTRIBUTE 0xf in c99414168.lua), so one monster carries all five attributes
- 风林火山 1781310 only needs face-up EARTH, WATER, FIRE and WIND monsters to exist on the field, so the all-attribute 精灵术师 树精 alone unlocks it
- 精灵神后 树精 32965616 special summons itself from hand while monsters in BOTH players' GYs cover 6 or more distinct attributes (c32965616.lua spcon scans LOCATION_GRAVE on both sides), and gains 500 ATK/DEF per distinct attribute in both GYs
- 精灵神后 树精 32965616 negates an opponent special summon and destroys it by banishing 3 monsters from your own GY, only as a direct response while the chain is empty
- 精灵世妃 树精 50208444 requires 3 or more distinct attributes in your OWN GY, and its effect ② only special summons a deck monster whose attribute is absent from both your field and your GY
- 暗黑树精 62312469 on summon stacks one EARTH, WATER, FIRE and WIND monster each from deck on top in any order, and in a pendulum zone boosts your face-up elemental monsters by 200 times your field attribute count

- **One-Card Combo: 仪式的事前准备**

- Starter: one 仪式的事前准备 13048472 in hand, nothing else required
- Step 1: activate 仪式的事前准备, add 树精的祈祷 23965037 plus 精灵术师 树精 99414168 (Pre-Prep finds the ritual spell in deck and the listed ritual monster in deck or GY)
- Step 2: activate 树精的祈祷, tribute monsters from hand or field totaling 3 or more original levels (Greater ritual proc, the ritual monster itself is only Level 3)
- Step 3: ritual summon 精灵术师 树精, which now counts as EARTH, WATER, FIRE, WIND and LIGHT simultaneously
- Step 4: activate 风林火山 1781310 whose four-attribute condition is already met, then pick destroy all opponent monsters, destroy all opponent spells and traps, discard 2 random opponent hand cards, or draw 2
- Halt point: 灰流丽 14558127 on 仪式的事前准备 or on 树精的祈祷 kills the line, and one tribute body with fewer than 3 total levels cannot perform the ritual

- **End Field One-Card**

- 精灵术师 树精 99414168 as the all-attribute body plus one live 风林火山 1781310 (full board wipe, hand shred or +2 draws)
- If the shared GY already covers six attributes, 精灵神后 树精 32965616 drops at 3000 or more ATK with one summon negate standing by (banish 3 from your GY)
- Optionally one set 精灵的祝福 37626500 to ritual summon another LIGHT ritual on the next turn

- **Extenders**

- 精灵世妃 树精 50208444: effect ① from hand targets 1 own GY monster and special summons both, effect ② on field special summons 1 deck monster with an attribute new to your field and GY, neither activation can be chained to
- 暗黑树精 62312469: its deck stack lines up next-draw ritual tribute fodder and feeds 精灵神后 树精 attribute diversity, and its pendulum boost applies to the all-attribute 精灵术师 树精 99414168
- 万手神 95492061: on normal or flip summon adds any ritual monster or ritual spell, tutoring 树精的祈祷 23965037 or 精灵的祝福 37626500
- 宣告者的神巫 92919429: sends a ritual monster from deck or extra deck to GY to special summon a 宣告者, dumping an attribute for 精灵神后 树精 and ending on 虹光之宣告者 79606837
- 精灵术的使魔 45538320: on summon adds a 凭依 spell or trap or 大灵术-「一轮」 38057522, changes its own attribute once per turn, and when destroyed special summons a 1500 DEF Spellcaster from deck or GY
- 精灵术的术使 91530236: discard 1, pick 2 different 灵使 monsters, 凭依装着 monsters or 凭依 spells and traps from deck, add 1 and set 1
- GY fillers 数学家 41386308, 愚蠢的埋葬 81439174 and the 光道 mill shell (光之援军 94886282, 光道弓手 费莉丝 73176465) are the fastest route to six attributes for 精灵神后 树精

- **Halt Points**

- 灰流丽 14558127 on 仪式的事前准备 13048472 or 树精的祈祷 23965037 stops the ritual line cold
- 增殖的G 23434538 draws on every 精灵世妃 树精 and 精灵神后 树精 special summon, while the ritual summon itself does not feed it
- Banish effects on your GY monsters such as 墓穴的指名者 24224830 drop 精灵世妃 树精 below 3 or 精灵神后 树精 below 6 attributes
- 次元吸引者 91800273 and other GY exclusion effects remove attributes from the shared pool, disabling both 精灵世妃 树精 and 精灵神后 树精
- 精灵神后 树精 32965616 needs 3 monsters in your own GY as cost and an empty chain, so it cannot answer a summon already chained to or after its own GY was spent
- Hand-to-field locks such as 青眼精灵龙 59822133 block both 精灵神后 树精 and 精灵世妃 树精 hand special summons

- **Mirror Match: 精灵 vs 精灵**

- Both players count the same shared GY pool, your opponent mills feed your 精灵神后 树精 32965616 and yours feed theirs
- The race to six attributes decides the game, the first 精灵神后 树精 to resolve its summon negation wins the exchange
- Banishing the opponent GY monsters with 墓穴的指名者 24224830 or similar drops their count below six while leaving yours intact
- Whoever resolves 仪式的事前准备 13048472 into the ritual first controls 风林火山 1781310 and can wipe the other side before the boss arrives
- 精灵世妃 树精 50208444 activations cannot be chained to, so the mirror answer is stopping 仪式的事前准备 or stripping the GY before it resolves

- **Common Mistakes**

- 树精的祈祷 23965037 tributes a total of 3 or more levels while 精灵的祝福 37626500 needs exactly the ritual monster level and fits any LIGHT ritual, do not confuse the two procs
- 精灵神后 树精 32965616 counts BOTH players' GYs, do not read it as own GY only, and its 3-banished-monster cost can drop your own count below the next summon threshold
- 精灵神后 树精 32965616 is special summon only, never normal summonable, do not hold it in hand waiting for a tribute
- 精灵世妃 树精 50208444 effect ② requires the chosen attribute to be missing from BOTH your field and GY, so it cannot pull a monster sharing an attribute you already milled
- 风林火山 1781310 is a quick-play whose condition counts elemental monsters anywhere on the field, use it on the opponent turn for the board wipe or hand disruption
- 暗黑树精 62312469 places the four monsters on top in your chosen order and the last placed is drawn first, plan the order around the ritual tribute
- 精灵世妃 树精 50208444 activations cannot be responded to by either player, so never fire them while your GY has fewer than 3 attributes
