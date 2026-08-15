---
name: dragonpendulum-experience
description: 龙剑士 (Dracoslayer) deck experience: pendulum scale engine, Draco Face-Off opener, Electrumite loop, composite bosses, halt points
---
# 龙剑士 (Dracoslayer) Deck Experience

- **Deck Identity**

- True identity: the 龙剑士 (竜剣士 / Dracoslayer) pendulum family, setcode 0xc7 in cards.cdb, not 万能龙剑士, 焰龙剑士 or 耀龙剑士 (no such names exist in the DB) and not 龙王剑士 (no such deck folder or card exists)
- Reference build: the pure 220716龙剑士灵摆 lists in the deck folder, with the modern 七音服龙剑士 230114 and the Superheavy Samurai / 异色眼 / 刻魔 hybrids 240727 and 251220 keeping the same core
- Pendulum engine, six 龙剑士 pendulum monsters, all Level 4 except 风麒麟·平行 39016067 at Level 6: 威风凛·飞马 92332424 scale 2, 光辉星·灵摆 92746535 scale 5, 卓辉星·灵摆 75195825 scale 3, 雾动轰·输力 28720123 scale 6, 点火烈·凤凰 56347375 scale 7, 风麒麟·平行 39016067 scale 2
- 龙魔王 (Dracoruler) pendulum pair, setcode 0xda: 霸道矢·灵摆 7127502 scale 5 and 魔道矢·灵摆 69512157 scale 3
- Composite bosses: 爆龙剑士 点火星·日珥 18239909 (Level 8 Synchro), 刚龙剑士 雾动星·强力 22638495 (Level 8 contact Fusion), 升龙剑士 威风星·圣骑 88722973 (Rank 4), 真龙剑士 卓辉星·拼图 34079868 (the negate boss)
- Link core: 刚炼装勇士·银金公主 24094258 (Link-2, two pendulum monsters), with 轨迹之魔术师 22125101 and 神数炼机圣 梅塔特隆 85216896 as alternate links in the builds
- 灵摆 (setcode 0xf2) support: 龙呼相争 14733538, 决斗者降临 37469904, 灵摆宝藏 26237713, 灵摆停顿 36111775, 魂之灵摆 34884015, 灵摆超量 46005939, 灵摆融合 65646587, 龙神阵·灵摆 71817640

- **Core Mechanic: Pendulum Scale Engine**

- Goal: set two scales, pendulum summon Level 4 Dracoslayers, link into 银金公主 24094258, use its destroy-and-draw to recycle scales, and finish on 真龙剑士 34079868 with a negate
- Scale pairs that summon Level 4: 威风凛·飞马 92332424 (2) with 光辉星·灵摆 92746535 or 霸道矢·灵摆 7127502 (5), 卓辉星·灵摆 75195825 (3) with scale 5 or 6, 雾动轰·输力 28720123 (6) with scale 2, 3 or 5; 风麒麟·平行 39016067 at Level 6 needs a 7 with a low scale
- 龙呼相争 14733538 is the Draco Face-Off opener: reveal one 龙剑士 pendulum and one 龙魔王 pendulum from deck, the opponent picks one and you place it in a pendulum zone or special summon it, the other goes face-up to the Extra deck, verified in script c14733538
- 威风凛·飞马 92332424 is the searcher: with another 龙剑士 or 威风妖怪 scale it adds a different 龙剑士 pendulum from deck to hand, then may destroy one of your scales
- 光辉星·灵摆 92746535 pendulum effect destroys the other scale and adds a same-name copy from deck, cycling itself through the Extra deck
- 雾动轰·输力 28720123 pendulum effect special summons the other 龙剑士 or 雾动机龙 scale to the monster zone, and when released it adds a face-up 龙剑士 or 雾动机龙 pendulum from the Extra deck to hand
- 点火烈·凤凰 56347375 is the recovery piece: its pendulum effect shuffles a face-up Extra pendulum into the deck to search a non-pendulum 龙剑士 or 点火骑士 monster, and when destroyed it special summons a 龙剑士 or 点火骑士 from deck as a Tuner
- 银金公主 24094258 loop: on link summon it adds any pendulum from deck face-up to the Extra deck, its ignition destroys a face-up card you control to add a face-up Extra pendulum to hand, and whenever one of your pendulum zone cards leaves the field it draws 1, so destroying a scale with its own ignition nets one draw plus one hand recovery
- 龙神阵·灵摆 71817640 boosts 龙剑士 monsters 300 and when destroyed adds or special summons a 龙剑士 or 龙魔王 from deck; its destroy-trigger clause needs a Dragon-race 龙剑士, none exists in the card pool, so treat that clause as dead

- **One-Card Combo**

- No single card reaches the full end board, the engine needs a second scale or a search card, so the closest solo starter is 龙呼相争 14733538: one pendulum zone card plus one face-up Extra pendulum, or one special summoned body plus one face-up Extra pendulum
- Standard two-card opener, 龙呼相争 14733538 plus 威风凛·飞马 92332424: reveal 光辉星·灵摆 92746535 and 霸道矢·灵摆 7127502, put the opponent's pick in a pendulum zone and the other face-up in the Extra deck, set 威风凛 as the second scale, then pendulum summon Level 4 monsters including the Extra deck card
- Continue the line: activate 威风凛's search for 雾动轰·输力 28720123 or 卓辉星·灵摆 75195825 and destroy the 光辉星 scale, link two pendulum monsters into 银金公主 24094258, add a pendulum from deck to the Extra deck, then destroy a scale with 银金公主 to draw 1 and recover a face-up Extra pendulum to hand
- With 银金公主 24094258 up, re-set the recovered scales and pendulum summon again, using 魂之灵摆 34884015 to adjust both scales plus or minus 1 and later spend 3 counters for an extra pendulum summon
- 雾动轰·输力 28720123 as scale extends by special summoning the other scale, then gets released into the 真龙剑士 卓辉星·拼图 34079868 tribute line while its release effect recovers another 龙剑士 from the Extra deck

- **End Field**

- 真龙剑士 卓辉星·拼图 34079868 at 2950/2950 with one spell, trap or monster effect negate per turn, summoned by tributing one 龙剑士 monster and one 龙魔王 monster from the field
- 升龙剑士 威风星·圣骑 88722973 as a Rank 4 with an end phase search for any pendulum monster and a detach effect that special summons a face-up 龙剑士 pendulum from the Extra deck
- 刚炼装勇士·银金公主 24094258 keeping the pendulum cycle alive with a recovered scale and a drawn card each turn
- Scales that lock the opponent: 霸道矢·灵摆 7127502 negates face-up pendulum monsters in their monster zones, 魔道矢·灵摆 69512157 negates their pendulum zone cards
- 龙神阵·灵摆 71817640 giving 300 to 龙剑士 monsters, 魂之灵摆 34884015 raising pendulum monsters 300 per counter, and 灵摆停顿 36111775 as a draw-2 burst once the Extra deck holds three different pendulums
- Optional Rank 4 finishes: 深渊的潜伏者 21044178 to shut graveyard effects, No.41 泥睡魔兽 睡梦貘 90590303 in defense, No.60 刻不知之杜加雷斯 66011101 for a draw, 希望之魔术师 67865534 to extend and place itself back in a scale
- Fusion option: 霸王眷龙 凶饿毒 43387895 from two DARK pendulums 霸道矢·灵摆 7127502 and 魔道矢·灵摆 69512157, copying any monster's name and effects with piercing battle damage

- **Extenders**

- 威风妖怪·狸 31991800 normal summons into a 威风妖怪 search, and since 威风凛·飞马 92332424 counts as 威风妖怪 it tutors the deck's best searcher
- 娱乐伙伴 琴键猴 17330916 is scale 1 (becomes 4 without another 娱乐伙伴 scale) and searches a Level 4 or lower 娱乐伙伴 monster the turn it is activated
- 灵摆宝藏 26237713 adds any pendulum from deck face-up to the Extra deck, feeding 银金公主 24094258 and the 升龙剑士 88722973 detach line
- 决斗者降临 37469904 searches any 灵摆 (setcode 0xf2) pendulum monster or spell or trap while any pendulum zone is occupied, grabbing 光辉星·灵摆 92746535, 霸道矢·灵摆 7127502, 龙神阵·灵摆 71817640 or 轨迹之魔术师 22125101
- 灵摆停顿 36111775 draws 2 when three or more different face-up pendulums sit in the Extra deck, the payoff of an earlier 灵摆宝藏 26237713 or 银金公主 24094258
- 灵摆超量 46005939 special summons both scales negated and Xyz summons with them as materials, treating one level as the other, into any Rank 4
- 灵摆融合 65646587 fuses from field monsters plus both pendulum zone cards when two scales are up, making 霸王眷龙 凶饿毒 43387895 or 凶饿毒融合龙 41209827 from DARK pendulums
- 点火烈·凤凰 56347375 destroyed in battle or by effect special summons a 龙剑士 or 点火骑士 from deck as a Tuner, opening the 爆龙剑士 点火星·日珥 18239909 or 霸王眷龙 幻透翼 70771599 synchro lines
- 爆龙剑士 点火星·日珥 18239909 destroys a pendulum monster or scale and bounces a card to the deck, then special summons a 龙剑士 from deck in defense
- 刚龙剑士 雾动星·强力 22638495 contact fuses from one pendulum plus one 龙剑士 pendulum on the field, protects all your pendulum cards from destruction, and revives a 龙剑士 pendulum from hand or grave
- 超天新龙 异色眼革命龙 16306932 discarded for 500 LP searches a Level 8 or lower Dragon pendulum, and while in its own scale it destroys itself to revive a Dragon fusion, synchro or Xyz from the grave

- **Halt Points**

- 灰流丽 14558127 on 龙呼相争 14733538, on 威风凛·飞马 92332424's search, on 决斗者降临 37469904 or on 灵摆宝藏 26237713 stops the scale setup before any pendulum summon
- 增殖的G 23434538 turns every pendulum summon and link summon into a draw for the opponent, the deck special summons five or more times per turn so it must stop at 银金公主 24094258 or play a minimal line
- 原始生命态 尼比鲁 27204311 lands on the fifth summon, which the standard line reaches after two pendulum summons plus the 银金公主 24094258 link plus the composite bosses
- 小丑与锁鸟 94145021, which the deck itself mains in the modern builds, stops every add-from-deck effect including 威风凛's search and 升龙剑士 88722973's end phase search
- 灵摆停顿 36111775 locks the turn: after it resolves the player cannot add from deck to hand and cannot draw, so it must be the last search-adjacent card of the turn
- 王家长眠之谷 47355498, mained in the 220716 hybrid list, blocks 刚龙剑士 雾动星·强力 22638495's grave revive and 超天新龙 16306932's grave revive, so the deck itself must sequence around it
- Removing both scales or 银金公主 24094258 kills the engine for the turn, no pendulum zone cards means no pendulum summon and no draw engine

- **Mirror Match: 龙剑士 vs 龙剑士**

- Whichever player resolves 龙呼相争 14733538 and 威风凛·飞马 92332424 first controls the scale game, the second player must break scales before any pendulum summon
- 霸道矢·灵摆 7127502 in scale negates the opponent's face-up pendulum monsters and 魔道矢·灵摆 69512157 negates their scales, so keep one 龙魔王 scale live at all times
- 卓辉星·灵摆 75195825 pendulum effect destroys any pendulum zone card on either side, the direct answer to an opponent's live 霸道矢 or 魔道矢 scale
- 真龙剑士 卓辉星·拼图 34079868 negate is saved for the opponent's 龙呼相争, 威风凛 search, or their own 真龙剑士 summon
- 风麒麟·平行 39016067 as a quick effect bounces one pendulum card and one opponent card to hand, removing the opponent's scale and their best monster in one chain
- Whoever resolves 升龙剑士 威风星·圣骑 88722973 first out-draws the other in the end phase, so prioritize its detach summon line in the mirror
- 王家长眠之谷 47355498 when mained blanks both sides' grave plays equally, so prefer Extra deck and scale effects in the mirror

- **Common Mistakes**

- 光辉星·灵摆 92746535 can only be material for 龙剑士 fusion, synchro or Xyz, so never use it as material for 凶饿毒融合龙 41209827 or generic Rank 4s like No.41 泥睡魔兽 90590303 and No.60 刻不知之杜加雷斯 66011101, though it can be link material for 银金公主 24094258 because link is not covered by the restriction
- 点火烈·凤凰 56347375's pendulum search only finds non-pendulum 龙剑士 or 点火骑士 monsters and the pure build runs none, so never waste the activation, its real value is the destroyed-into-Tuner special summon
- 灵摆停顿 36111775 must be last, activating it before 威风凛·飞马 92332424's search or 银金公主 24094258's recovery negates those lines for the turn
- 超天新龙 异色眼革命龙 16306932 as scale 12 forbids pendulum summoning non-Dragon monsters, which locks out every 龙剑士 pendulum, so use it as a discard searcher or pop it with its own effect instead of leaving it in scale
- 威风凛·飞马 92332424's field spell search discards a card, so activate it only when the hand can absorb the cost and grab 龙神阵·灵摆 71817640 or 天空的虹彩 27813661
- 真龙剑士 34079868 needs a 龙剑士 monster and a 龙魔王 monster on the field to tribute, 龙魔王 in the scale zone does not count, so pendulum summon 霸道矢·灵摆 7127502 or 魔道矢·灵摆 69512157 as a body before attempting the summon
- Restricted summons: the monster 升龙剑士 88722973 special summons cannot be Xyz material, 爆龙剑士 18239909's cannot be synchro material, 刚龙剑士 22638495's cannot be fusion material, so use those bodies as link material instead
- 灵摆超量 46005939 consumes both scales and summons them negated, losing the scale setup for next turn, so only use it when the Rank 4 payoff justifies it
- 银金公主 24094258's destroy targets a face-up card you control, destroying a scale triggers its own draw, but destroying 龙神阵·灵摆 71817640 instead trades the draw for a 龙剑士 or 龙魔王 search from the field spell's destruction effect
- 轨迹之魔术师 22125101's 1200 LP search locks the turn to pendulum summoning, if no pendulum summon follows your monster effects die and your scales are negated, so never search with it without a guaranteed scale line
- 龙神阵·灵摆 71817640's destroy-trigger clause needs a Dragon-race 龙剑士 which does not exist in the card pool, do not play the field spell expecting that effect, only its 300 boost and destruction search matter
