---
name: eldlich-experience
description: 黄金国巫妖 (Eldlich) deck experience: zombie trap-control recursion loop, one-card opener, floodgate synergy, mirror and pitfalls
---
# 黄金国巫妖 (Eldlich) Deck Experience

- **Deck Identity**

- Zombie trap-control grind deck built on one boss monster: 黄金卿 黄金国巫妖 95440946, Level 10 LIGHT Zombie, 2500/2800
- Three archetype name tags verified from setcodes: 黄金国巫妖 0x1142 (Eldlich monsters), 黄金乡 0x143 (Golden Land traps), 黄金国永生药 0x2142 (Eldlixir spells and traps)
- Every engine piece works twice: once from hand or field, once from the grave, so the deck never runs out of plays
- Pure reference list 200307黄金国巫妖: 40 cards, 3x lord, 3x each of the three golden-land traps, 3x each of the three Eldlixirs, 3x 被诅咒的黄金国度 31434645, 3x 齐唱僵尸 49959355, 3x 黄金之征服王 92379223, hand traps, no extra deck
- Floodgate variants add 技能抽取 82732705, 御前试合 53334471, 群雄割据 90846359, 召唤限制器 23516703, 虚无空间 5851097, 王宫的敕命 61740673; Eldlich plays under all of them because the lord's effects resolve from hand and grave, not from the field

- **Core Mechanic: Grave Recursion Loop**

- 黄金卿 黄金国巫妖 95440946 effect 2 (grave, ignition, once per turn): send 1 of your field spells or traps to grave, add itself to hand, then optionally special summon 1 Zombie from hand with +1000 attack and defense and effect-destruction immunity until the opponent's end phase, script c95440946
- 黄金卿 黄金国巫妖 95440946 effect 1 (hand): discard itself plus 1 spell or trap, send 1 card on the field to grave, the deck's only targeted removal
- The golden-land traps 黄金乡的征服者 20590515 (5★ 500/1800), 黄金乡的守护者 67007102 (8★ 800/2500), 黄金乡的盗墓者 93191801 (5★ 1800/1500) activate into Zombie trap monsters and can banish themselves from the grave during either player's end phase to set a 黄金国永生药 card from deck
- The Eldlixirs banish themselves from the grave to set a 黄金乡 trap from deck: 黑化觉醒之黄金国永生药 68829754 (main phase), 白化宿命之黄金国永生药 94224458 (main phase), 红化血染之黄金国永生药 20612097 (quick effect, usable on the opponent's turn)
- 贵华黄金乡之黄金国永生药 22669793 can re-set your banished 黄金乡 or 黄金国永生药 cards, closing the banish loop
- End result: any field spell or trap is recursion fuel and any grave card is an engine piece; the deck grinds forever

- **One-Card Combo: 黑化觉醒之黄金国永生药 68829754**

- Starter: 黑化觉醒之黄金国永生药 68829754 alone in hand, no other card needed
- Step 1: activate it, special summon 黄金卿 黄金国巫妖 95440946 from deck in defense; while no Eldlich monster is on the field the summon target must be an Eldlich monster, and the lord qualifies
- Step 2: after it resolves to the grave, activate its grave effect: banish it, set 1 黄金乡 trap from deck, usually 永久辉煌的黄金乡 56984514 or 黄金乡的征服者 20590515
- Opening board: 黄金卿 2500/2800 in defense plus 1 set trap, with the banished Eldlixir fueling the next loop
- Sustain line with 被诅咒的黄金国度 31434645: pay 800 LP to search 黄金卿 95440946; discard the lord plus 1 spell or trap to send 1 card to grave (effect 1); the lord in grave sends the search spell to grave as cost (effect 2) to return to hand, and the spell's third effect mills 1 Eldlich monster or 黄金乡 card from deck, recycling the engine with no net card loss

- **End Field**

- Control board, not a combo board: 1-2 Zombie bodies, 黄金卿 黄金国巫妖 95440946 plus trap monsters, and 1-3 set traps
- 永久辉煌的黄金乡 56984514 set: counter trap that negates and destroys any monster effect or spell or trap activation by tributing a Zombie you control, once per turn
- With 技能抽取 82732705 face up the lord stays a 2500 beater and the trap monsters stay Normal Monsters while opponent on-field effects die; activate all engine effects from hand and grave under it
- 被诅咒的黄金国度 31434645 restricts your attack declarations to Zombies only while face up, keep the board all-Zombie before swinging
- 召唤限制器 23516703 caps both players at 2 special summons per turn, Eldlich normally summons 1-2 bodies per turn, activate trap monsters sparingly under it

- **Extenders**

- 愚蠢的埋葬 81439173: mill 黄金卿 黄金国巫妖 95440946 straight to grave to start the loop
- 齐唱僵尸 49959355: normal-summonable Level 3 Zombie tuner, effect 2 mills a Zombie from deck to grave and raises a monster's level by 1, the pure build runs 3 copies
- 白化宿命之黄金国永生药 94224458: special summons a Zombie from hand or grave, the best follow-up once the lord is in play
- 红化血染之黄金国永生药 20612097: special summons a Zombie from deck or grave, gives a second body the same turn
- 贵华黄金乡之黄金国永生药 22669793: pay 800 LP to become a 10★ 1500/2800 body and bounce 1 monster on the field to hand (with the lord on field), or re-set a banished 黄金乡 or 黄金国永生药 card
- 黄金之征服王 92379223: finisher trap, with a lord on field shuffle 3 different kinds of banished 黄金国永生药 cards back to deck to destroy all cards on field, or 3 kinds of banished 黄金乡 cards to halve the opponent's LP and gain the same
- 黄金狂 黄金国巫妖 74889525 (extra deck fusion builds): counts as 黄金卿 on field, cannot be destroyed by battle or card effect, tributes a Zombie to take control of an opponent monster

- **Halt Points**

- 灰流丽 14558127 stops both main openers: the special summon from deck of 黑化觉醒之黄金国永生药 68829754 and the search of 被诅咒的黄金国度 31434645
- 墓穴的指名者 24224830 and 屋敷童 73642296 hit the grave engine: the lord's recursion effect and the golden-land traps' end-phase set effects
- 增殖的G 23434538 draws 1 per special summon and the deck special summons 2-4 times per turn; under G prefer trap-monster and recursion lines over Eldlixir special summons
- The zombie-lock: after any Eldlixir resolves you can only special summon Zombies that turn; without a face-up Eldlich monster an Eldlixir may only special summon Eldlich monsters, so put the lord on field before other Zombies

- **Mirror Match: 黄金国巫妖 vs 黄金国巫妖**

- The player who keeps the grave loop running wins, use 黄金乡的盗墓者 93191801 to banish the opponent's grave 黄金国永生药 or 黄金乡 pieces, or the lord itself, before they recur
- 永久辉煌的黄金乡 56984514 negates the opponent lord's grave recursion by tributing a Zombie, the loop-killer of the mirror
- 黄金卿 黄金国巫妖 95440946 effect 1 trades 2 cards for 1, aim it at the opponent's face-up 被诅咒的黄金国度 31434645 and set 黄金乡 traps rather than their monsters
- Keep a face-up lord before resolving Eldlixirs, otherwise the special summon restriction locks you out of your key Zombie bodies
- Under 技能抽取 82732705 the duel becomes off-field recursion versus off-field recursion, whoever keeps the lord in the grave loop first wins

- **Common Mistakes**

- Never fire 黄金卿 黄金国巫妖 95440946 effect 1 without a target worth 2 cards, it discards the lord plus a spell or trap from hand
- Resolve the Eldlixir first, then the lord's effect 2 special summon: the summoned Zombie gets +1000 and effect-destruction immunity, swing with the buffed body
- Do not over-set spells and traps, the end-phase set effects and the lord's recursion cost need spell and trap zone space
- Do not activate a trap monster without a free monster zone, and each trap monster activation counts as a special summon for 召唤限制器 23516703 and 增殖的G 23434538
- After an Eldlixir do not plan non-Zombie summons that turn, the zombie-lock lasts until the end of the turn
- Do not banish your own 红化血染之黄金国永生药 20612097 wastefully, its grave effect is a quick effect, save it for the opponent's turn
- 黄金之征服王 92379223 needs 3 different card names in your banished pool, build the pool during the game instead of firing it early
