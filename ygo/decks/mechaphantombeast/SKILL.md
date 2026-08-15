---
name: mechaphantombeast-experience
description: 幻兽机 (Mecha Phantom Beast) deck experience: token engine, one-card combo, extenders, halt points
---
# 幻兽机 (Mecha Phantom Beast) Deck Experience

- **Deck Identity**

- Archetype: 幻兽机 (Mecha Phantom Beast), setcode 0x101b, nearly every card WIND Machine; this build is a token-spam synchro deck, there is no fusion line
- Main deck core: level 1-4 幻兽机 monsters with three tuners — 暴风雪莺 31480215 (Lv1), 猎户座飞狮 72291078 (Lv2), 蓝冲高角羚 67489919 (Lv3)
- Main deck non-tuners: 绳狼 67922702, 黑猎鹰 4417407, 猛禽大盗龙 31533704, 倾转翼马 94973028, 鹞式狮豹兽 20368763, 同温层仓鼠 66200210, 追踪海龟 76902476, 长尾隐形鳐 30811116, 航空飞鸟 16943770, 全球剑齿虎 15335853, 雷电貂 44026393, plus level 7 加里宁狮鹫 41329458
- Extra deck engine: 曙光女神百头龙 44097050 (link-2), 哥萨克龙 22110647 (rank 7), 协和金翅鸟 53451824 (Lv7), 鲁斯兰枪蛇 26949946 (Lv9), 加速同调士 37675907 (Lv5 tuner), 流星登龙 68431965 (Lv7 tuner), 鲜花女男爵 84815190, 幻透翼同调龙 82044279, links 梦幻崩影·凤凰 2857636, 梦幻崩影·独角兽 38342335, 梦幻崩影·狮鹫 65330383, 刺刀枪管龙 85289965, 访问码语者 86066372, 双穹之骑士 阿斯特拉姆 21887175
- Spells and traps: 垂直着陆 904185, 紧急起飞 83054225, 空中补给 70875955, 弹幕回避 6260554, handtraps 灰流丽 14558127, 幽鬼兔 59438930, 无限泡影 10045474
- Near-pure decklists verified: /home/z/ygo/deck/210522幻兽机 (modern Auroradon build) and /home/z/ygo/deck/191123幻兽机 (pure grind build adding 死者苏生 83764718 and 活死人的呼声 97077563)
- Build quirk: one variant plays 机械复制术 63995093 on 长尾隐形鳐 30811116 (100 ATK) or 追踪海龟 76902476 (500 ATK) to flood level 3s, plus 暴走斗君 14342283 which gives attack-position tokens +1000 ATK and battle protection

- **Core Mechanic: Token Engine and Tribute Fuel**

- 幻兽机衍生物 token: WIND Machine level 3, 0 ATK / 0 DEF; every token id in cards.cdb aliases to 31533705, and core card_is_code matches aliases, so any filter checking 幻兽机衍生物 accepts every token
- Tokens are 幻兽机 (setcode 0x101b), so they are legal non-tuner synchro material for 鲁斯兰枪蛇 26949946 and 蓝冲高角羚 67489919, and legal release fodder for 哥萨克龙 22110647, 加里宁狮鹫 41329458, 弹幕回避 6260554, 紧急起飞 83054225 and 垂直着陆 904185
- Shared passive engine on most main deck monsters, verified in scripts such as c4417407.lua: this card's level is raised by the total level of all 幻兽机衍生物 you control (each token is +3), and while you control a token this card cannot be destroyed by battle or card effect
- Tribute 1 token for a one-shot effect: 猛禽大盗龙 31533704 searches a 幻兽机 from deck, 黑猎鹰 4417407 changes an opponent monster to face-up defense (quick effect, either player's turn), 全球剑齿虎 15335853 banishes one card from either graveyard, 长尾隐形鳐 30811116 destroys a spell or trap, 同温层仓鼠 66200210 revives a 幻兽机 from graveyard, 绳狼 67922702 gains 800 ATK during the damage step
- Tribute 2 tokens: 倾转翼马 94973028 destroys and banishes one opponent card; 曙光女神百头龙 44097050 releases 2 monsters to special summon a 幻兽机 from deck, see the combo below
- Token generators: 绳狼 67922702 on normal summon (mandatory), 黑猎鹰 4417407 on attack declare (mandatory), 猛禽大盗龙 31533704 doubles any token summon (once per turn), 猎户座飞狮 72291078 when sent to the graveyard, 同温层仓鼠 66200210 when flipped face-up (2 tokens), 倾转翼马 94973028 when special summoned while another 幻兽机 is face-up (2 tokens), 鹞式狮豹兽 20368763 when one of your monsters is released for another card's effect (once per turn), 航空飞鸟 16943770 by banishing another 幻兽机 from the graveyard, 加里宁狮鹫 41329458 by discarding a 幻兽机 from hand, 蓝冲高角羚 67489919 from the graveyard when your field is empty and the opponent has a monster, 雷电貂 44026393 by discarding 1 card, 哥萨克龙 22110647 by detaching 1 material (2 tokens), 曙光女神百头龙 44097050 on link summon (3 tokens), 空中补给 70875955 once per turn, 垂直着陆 904185 by releasing any number of wind non-token monsters

- **One-Card Combo: 绳狼**

- Starter: 绳狼 67922702 in hand, no other card needed; 雷电貂 44026393 with 1 discard is an equivalent start
- Step 1: normal summon 绳狼 67922702, its mandatory effect special summons 1 幻兽机衍生物
- Step 2: link summon 曙光女神百头龙 44097050 using 绳狼 and the token, both are Machine
- Step 3: 曙光女神百头龙's link summon trigger special summons 3 幻兽机衍生物, then locks you out of link summons until the end of the turn, synchro and xyz remain legal
- Step 4: 曙光女神百头龙's ignition effect releases 2 tokens to special summon 猎户座飞狮 72291078 from the deck
- Step 5: synchro 加速同调士 37675907 with 猎户座飞狮 (level 2 tuner) and 1 token (level 3), 猎户座飞狮 sent to the graveyard summons 1 more token
- Step 6: banish 猎户座飞狮 72291078 from the graveyard for an extra normal summon of a 幻兽机 from hand, this needs a second card, the strict one-card line ends here
- Pure one-card end field: 曙光女神百头龙 44097050 plus 加速同调士 37675907 plus 1 幻兽机衍生物, with 加速同调士's quick synchro available during the opponent's main phase

- **End Field**

- One-card line: 曙光女神百头龙 44097050 (2100 ATK link-2, can release 1 card to destroy any 1 card) + 加速同调士 37675907 + 1 token
- Best extended end: 流星登龙 68431965 (level 7 tuner) + 1 token, quick synchro into 鲜花女男爵 84815190 (level 10 omni-negate) during the opponent's main phase; 流星登龙 can first dump a lower-level monster to adjust its own level
- 协和金翅鸟 53451824 (level 7) makes every token indestructible by battle and effect, the token-wall end
- 鲁斯兰枪蛇 26949946 (level 9) releases any number of tokens on summon to make the opponent discard the same number of random cards, makes all other 幻兽机 indestructible, and sets a quick-play spell from deck when destroyed by the opponent
- 哥萨克龙 22110647 (rank 7) detaches 1 material to make 2 tokens every turn and tributes 1 幻兽机 to destroy a card, a self-sustaining 2600 ATK wall while a token exists
- Set 弹幕回避 6260554 with tokens on board as a counter-trap negate for the opponent's turn

- **Extenders**

- 猛禽大盗龙 31533704: every token special summoned while it is face-up summons another token (once per turn), then tribute 1 token to add any 幻兽机 monster from deck to hand; with 空中补给 70875955 it produces 2 tokens plus a search every turn
- 倾转翼马 94973028: special summoned while another 幻兽机 is face-up (including 曙光女神百头龙 44097050) makes 2 tokens, then tributes 2 tokens to destroy and banish an opponent card
- 垂直着陆 904185: releases any number of wind non-token monsters to special summon the same number of tokens, converting leftover 幻兽机 monsters into synchro fuel, and triggers 鹞式狮豹兽 20368763 once
- 紧急起飞 83054225: while the opponent has more monsters than your non-token monsters, release any number of tokens to special summon the same number of 幻兽机 from deck, they return to the deck at the end phase so use them as material first
- 空中补给 70875955: one free token per turn from a continuous trap, combines with 猛禽大盗龙 31533704; pay its end-phase release cost or lose the trap
- 猎户座飞狮 72291078: banish it from the graveyard for an extra normal summon, and its sent-to-graveyard token makes every synchro material use profitable
- 同温层仓鼠 66200210: when flipped it makes 2 tokens, then tribute 1 token to revive a 幻兽机 from the graveyard, the grind-loop piece
- 蓝冲高角羚 67489919: from the graveyard, when your field is empty and the opponent controls a monster, banish it to make 1 token
- 黑猎鹰 4417407 plus 猛禽大盗龙 31533704: 黑猎鹰 attacking makes a token, both become level 7 (4 + 3), then xyz into 哥萨克龙 22110647

- **Halt Points**

- 增殖的G 23434538: every token and monster summon draws a card and the line special summons more than 8 times, stop after 绳狼 67922702 or do not commit 曙光女神百头龙 44097050
- 原始生命态 尼比鲁 27204311: the one-card line passes 5+ summons before 加速同调士 37675907, and tributing tokens on the chain feeds it further
- 灰流丽 14558127: negates 曙光女神百头龙 44097050's token trigger (it is optional), 猛禽大盗龙 31533704's search, and 倾转翼马 94973028's token trigger
- 幽鬼兔 59438930 destroys 空中补给 70875955, 无限泡影 10045474 negates 曙光女神百头龙 44097050 or 猛禽大盗龙 31533704 before their effects resolve
- 次元吸引者 91800273 and graveyard removal kill the recursion of 猎户座飞狮 72291078, 同温层仓鼠 66200210 and 蓝冲高角羚 67489919
- 紧急起飞 83054225 is dead whenever the opponent's monster count is not higher than your non-token count, hold it for later turns against empty boards

- **Mirror Match: 幻兽机 vs 幻兽机**

- The player who resolves 曙光女神百头龙 44097050 first wins the token race, the loser should answer with 弹幕回避 6260554 instead of contesting tokens
- 黑猎鹰 4417407's quick effect flips the opponent's 黑猎鹰 4417407 to defense, denying its attack-declare token, and flips any 幻兽机 out of attack position
- 长尾隐形鳐 30811116 destroys the opponent's 空中补给 70875955 and 弹幕回避 6260554 before they snowball
- 弹幕回避 6260554 negates 紧急起飞 83054225, 垂直着陆 904185 and 空中补给 70875955 at the cost of all your tokens, only worth it when the opponent's play is bigger than yours
- 全球剑齿虎 15335853 banishes 猎户座飞狮 72291078 and 同温层仓鼠 66200210 from the opponent's graveyard, cutting their recursion and level plays
- 倾转翼马 94973028 destroy-and-banish removes 幻兽机 permanently so 同温层仓鼠 66200210 and 活死人的呼声 97077563 cannot bring them back
- 协和金翅鸟 53451824 is the mirror breaker, whoever keeps it face-up has indestructible tokens and dominates the damage race
- Do not release tokens while the opponent has 鹞式狮豹兽 20368763 face-up, every release gives them a token

- **Common Mistakes**

- 雷电貂 44026393's material lock: after its effect only 幻兽机 monsters may be used as fusion/synchro/xyz/link material for the turn, do not plan to use 灰流丽 14558127 or 幽鬼兔 59438930 as materials afterwards
- 蓝冲高角羚 67489919's synchro restriction: only Machine synchros, and the other materials must be 幻兽机 from hand or field, so it cannot make 鲜花女男爵 84815190 (Warrior) or 幻透翼同调龙 82044279 (Dragon)
- 暴风雪莺 31480215 locks you to wind-only special summons for the rest of the turn after being used as Machine synchro material, 灰流丽 14558127 is fire and cannot be summoned afterwards
- 全球剑齿虎 15335853 cannot attack while any non-幻兽机 monster is in your graveyard, keep the graveyard clean or treat it as a defender
- 紧急起飞 83054225's special summoned monsters return to the deck at the end phase, use them as material first and never count on their graveyard effects
- 空中补给 70875955 forces a release of 1 token or 幻兽机 at every end phase, skipping it destroys the trap, do not leave it up with an empty field
- 曙光女神百头龙 44097050 locks link summons for the turn after its token effect, plan synchro and xyz, do not try to climb into 访问码语者 86066372 in the same turn
- Token levels count toward synchro and xyz levels, compute +3 per token, for example 黑猎鹰 4417407 with 1 token is level 7 and pairs with another level 7 for 哥萨克龙 22110647
- 流星登龙 68431965's dump locks that monster's effects for the turn, do not dump 猎户座飞狮 72291078 and then expect its graveyard token
- 协和金翅鸟 53451824's revival releases all your tokens and only returns a level 4 or lower 幻兽机 from the graveyard, do not let it die with an empty board
- 弹幕回避 6260554 releases all your tokens as cost, only chain it when the negate trades favorably
- 垂直着陆 904185 releases wind non-token monsters, do not sacrifice monsters you still need as synchro material this turn
