---
name: madolche-experience
description: 魔偶甜点 (Madolche) deck experience: shuffle-back Xyz ladder, one-card combo, extenders, halt points
---
# 魔偶甜点 (Madolche) Deck Experience

- **Deck Identity**

- Archetype is EARTH monsters mixing Fairy, Beast, Spellcaster, and Warrior races built on an Xyz ladder, every card carries setcode 0x71 verified from cards.cdb and scripts
- Main deck core: 玛德莲魔女 11868731, 果冻天使 34680482, 布丁妹公主 77848740, 胶凝冰糕邮递员 52404456, 热香饼猫头鹰 91350799, 千层酥猫咪 12980373, 布丁公主 74641045
- Xyz: 皇后·后冠提拉米苏 37164373 (Rank 4), 后冠草莓提拉米苏 49689480 (Rank 5), 布丁公主·巧克力布丁拼盘 44311445 (Rank 5), 教师·眼镜蛋奶酥 20343502 (Rank 4); Link: 小点猫·马卡龙猫咪 38745241 (Link-3), 新人·水果挞修女 96150936 (Link-2)
- S/T core: 城堡 14001430 field spell, 沙龙 71348837 and 券 60470713 continuous spells, 散步 68159562 and 礼仪 12940613 traps, 餐后点心 51650038 normal spell
- Repo pure builds (deck/210807, deck/191012) run 玛德莲魔女 x3, 果冻天使 x3, 布丁妹公主 x3, 胶凝冰糕 x2, 热香饼猫头鹰 x2-3, 布丁公主 x0-1, extra 皇后 x2-3, 拼盘 x2-3, 教师 x3, 水果挞修女, plus generic 天霆号阿宙斯 90448279, No.41 90590303, 访问码语者 86066372
- The task's guessed card names 待月, 磁石, and 庭院 do not exist in this database, the field spell is 城堡 14001430 and the queens are 皇后·后冠提拉米苏 37164373 plus 后冠草莓提拉米苏 49689480
- Modern variants splash Vernusylph 春化精 cards or the 2025 K9 engine (deck/250726) around this core, both beyond the scope of this document

- **Core Mechanic: Shuffle-Back Float and the Xyz Ladder**

- Every main-deck Madolche monster floats: destroyed by the opponent it shuffles itself into the deck instead of staying in the graveyard, verified in each script as REASON_DESTROY plus GetReasonPlayer equals the opponent
- The graveyard is a fuel pool, not a final resting place: 皇后·后冠提拉米苏 37164373 detaches 1 material to shuffle 1-2 Madolche from your graveyard into the deck and shuffle the same number of opponent cards on field into the deck
- The ladder: 皇后·后冠提拉米苏 37164373 overlays into either 后冠草莓提拉米苏 49689480 (quick effect only on the opponent's turn) or 布丁公主·巧克力布丁拼盘 44311445 (transfers materials, and with 布丁公主 as material special summons from the deck whenever a Madolche returns from graveyard to deck)
- 城堡 14001430 is the field enabler: on activation it shuffles all Madolche monsters from your graveyard into the deck, gives every Madolche +500 ATK and DEF, and redirects any Madolche monster effect that would send your Madolche from graveyard to deck into a send to hand instead
- With 城堡 14001430 up, 皇后·后冠提拉米苏 37164373 becomes bounce the opponent's card plus put your Madolche into hand, and the hand-return feeds 券 60470713 and 沙龙 71348837
- 券 60470713: when a Madolche card returns to hand or deck by an effect, add a Madolche monster from the deck to hand, or special summon it instead while a face-up Madolche Fairy is on the field
- 沙龙 71348837: grants an extra normal summon for Madolche and, on the same return event, sets one Madolche spell or trap from the deck
- On a return event both 沙龙 71348837 and 券 60470713 trigger, put 沙龙 first on the chain so a 胶凝冰糕邮递员 52404456 special summoned by 券 resolves its when effect without missing timing

- **One-Card Combo: 果冻天使 34680482**

- Hand: 果冻天使 34680482 alone, no other cards needed
- Step 1: normal summon 果冻天使, activate its effect, release it as cost to special summon 布丁妹公主 77848740 from the deck, the released 果冻天使 in the graveyard is the queen's fuel
- Step 2: 布丁妹公主 on special summon special summons 布丁公主 74641045 from the deck with its level reduced by 1 from 5 to 4, and locks you to Madolche-only special summons for the turn
- Step 3: Xyz the two level 4 monsters into 皇后·后冠提拉米苏 37164373
- Step 4: detach 1 material, target 果冻天使 in the graveyard, shuffle it into the deck and shuffle one opponent card on the field into the deck
- Step 5: overlay 皇后·后冠提拉米苏 into 后冠草莓提拉米苏 49689480, ending on a 2600 ATK monster with a quick bounce for the opponent's turn
- With 城堡 14001430 active, step 4 sends 果冻天使 to hand instead of the deck, so the line ends with the starter back in hand
- The line is exactly 4 special summons, under the 5-summon threshold of 尼比鲁 27204311

- **End Field One-Card**

- 后冠草莓提拉米苏 49689480 with one material, on the opponent's turn it detaches to shuffle 1-2 Madolche from the graveyard into the deck and shuffle the same number of opponent field cards into the deck
- 城堡 14001430 face-up granting +500 ATK and DEF, plus 果冻天使 34680482 back in hand or a 券 60470713 search
- Extended builds add 教师·眼镜蛋奶酥 20343502 for monster-effect immunity and graveyard shuffle disruption, 小点猫·马卡龙猫咪 38745241 for a search plus hand special summon, and 散步 68159562 or 礼仪 12940613 set from the deck by 沙龙 71348837

- **Extenders**

- 沙龙 71348837 extra normal summon lets 玛德莲魔女 11868731 resolve twice, each normal summon searching any Madolche monster
- 热香饼猫头鹰 91350799 banishes any one monster from your graveyard to special summon a Madolche from the deck, and being a Beast itself lets the summoned 胶凝冰糕邮递员 52404456 search a Madolche spell or trap
- 千层酥猫咪 12980373 on normal summon special summons a Madolche from hand, and is the second Beast that turns on 胶凝冰糕邮递员 52404456
- 面包干管家 48252330 on normal summon while another Madolche is face-up searches any field spell, tutoring 城堡 14001430
- 丘与发芽的春化精 9350312 discards itself plus one card to search a Vernusylph and special summon an Earth monster from the graveyard, reviving 布丁妹公主 77848740 to trigger her effect again
- 森与觉醒的春化精 36745317 discards itself to send an Earth monster from the deck to the graveyard and special summon an Earth from the graveyard, creating queen fuel
- 小点猫·马卡龙猫咪 38745241 on link summon searches any Madolche card, its ignition shuffles a graveyard monster into the deck to special summon a Madolche from hand, then locks non-Madolche monster activations for the turn
- 新人·水果挞修女 96150936 while pointing to a face-up Madolche makes your Madolche spells and traps indestructible and untargetable, and replaces its own destruction by shuffling a Madolche from the graveyard into the deck
- 餐后点心 51650038 bounces two face-up effect monsters including at least one Madolche, then special summons a Madolche from hand or extra deck with attack at most their combined base attack, and from the graveyard attaches itself to your Xyz monster when a Madolche returns from graveyard to deck
- 散步 68159562 from the graveyard banishes itself to attach one Madolche from hand, deck, or graveyard to a face-up Madolche Xyz, refilling 皇后·后冠提拉米苏 37164373 or 后冠草莓提拉米苏 49689480 material

- **Halt Points**

- 灰流丽 14558127 stops the critical searches and summons: 玛德莲魔女 11868731, 果冻天使 34680482, 布丁妹公主 77848740 deck summon, 胶凝冰糕邮递员 52404456, and 小点猫·马卡龙猫咪 38745241
- 增殖的G 23434538 taxes every special summon, and the one-card line alone special summons 4 times
- 屋敷童 73642296 negates the graveyard shuffle effects the engine depends on, hitting 皇后·后冠提拉米苏 37164373 and 城堡 14001430
- 墓穴的指名者 24224830 on 果冻天使 34680482 in the graveyard removes the queen's fuel
- 尼比鲁 27204311 only fires on extended lines that pass five special summons, the basic one-card line stops at four
- Macro-style effects that banish instead of destroying kill the queen, 城堡 14001430, and 散步 68159562 value entirely
- 布丁妹公主 77848740 requires an empty graveyard to special summon itself from hand, any prior graveyard play or discarded hand trap blocks the line
- After resolving 布丁妹公主 field effect, only Madolche monsters can be special summoned for the rest of the turn, so generic extra deck plays must come before it

- **Mirror Match: 魔偶甜点 vs 魔偶甜点**

- The first 皇后·后冠提拉米苏 37164373 that resolves usually wins, its bounce removes the opponent's ladder pieces before they overlay
- 教师·眼镜蛋奶酥 20343502 shuffles 1-2 cards from either player's graveyard, use it to strip the opponent's Madolche fuel so their queen has nothing to shuffle
- 散步 68159562 negates the opponent's 后冠草莓提拉米苏 49689480 quick bounce, and 教师·眼镜蛋奶酥 20343502 makes your own queen immune to their monster effects
- Force any card into the opponent's graveyard before their turn so their 布丁妹公主 77848740 cannot special summon from hand, while keeping your own graveyard empty
- The player who resolves 增殖的G 23434538 first forces the other to either stop special summoning or feed draws

- **Common Mistakes**

- Detach from 皇后·后冠提拉米苏 37164373 before overlaying into 后冠草莓提拉米苏 49689480, the bounce is once per turn and is lost if skipped
- 布丁公主·巧克力布丁拼盘 44311445 is the legacy line, it needs 布丁公主 74641045 as material and a graveyard-to-deck return to fire, current builds prefer 后冠草莓提拉米苏 49689480
- 布丁公主 74641045 is level 5, only 布丁妹公主 77848740 level reduction makes it a level 4 for the rank 4 ladder
- Search spells mid-combo with 胶凝冰糕邮递员 52404456, 散步 68159562 and 礼仪 12940613 are traps and cannot activate the turn they are searched
- Normal summon 玛德莲魔女 11868731 first only with 沙龙 71348837 up, otherwise it consumes the summon the starter needs
- Use 城堡 14001430 activation to clear Madolche from the graveyard before the 布丁妹公主 77848740 hand summon, but a non-Madolche monster in the graveyard still blocks it
- Monsters special summoned by 果冻天使 34680482 shuffle into the deck at your next end phase, always turn them into Xyz material before then
- Resolve 沙龙 71348837 before 券 60470713 on the return chain, the reverse order makes 胶凝冰糕邮递员 52404456 miss its when timing
- 皇后·后冠提拉米苏 37164373 counts the opponent cards to shuffle by the number of Madolche that actually left the graveyard, and the 城堡 14001430 hand redirect keeps that count at one per card
