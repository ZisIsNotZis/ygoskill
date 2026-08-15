---
name: unchained-experience
description: 破械 (Unchained) deck experience: destroy-and-float link engine, 娑罗摩 loop, extenders, halt points
---
# 破械 (Unchained) Deck Experience

- **Deck Identity**

- Near-pure build from deck/230422破械: core engine 3x 破械童子 阿罗汉 26236560, 2-3x 破械童子 娑罗摩 31588572, 3x 破械童子 罗鬼刹 53624265, 2-3x 破械神 萨巴拉 41165831, 1-2x 双极之破械神 1966438, 1-2x 破械神的祸灵 89019964, 1x 破械神 萨玛 88554436
- Searchers and traps: 3x 双王之械 27412542, 2-3x 破械唱导 53417695, 2-3x 破械双极 80801743, 1-2x 破械神的恸哭 54807656
- Extra deck: 2-3x 破械神 罗寂刹 67680512, 2-3x 破械神 阿罗魃 93084621, 1-3x 破械神王 阎摩 24269961, 1-2x 破械双王神 来迎 29479265, 1x 访问码语者 86066372, 1x 闭锁世界的冥神 98127546, 1x 梦幻崩影·独角兽 38342335, 1x I：P百变莱娜 65741786, 1x 天霆号 阿宙斯 90448279, 1-2x DDD 怒涛大王 决策凯撒 79559912
- Hand traps 灰流丽 14558127, 增殖的G 23434538, 幽鬼兔 59438930, 屋敷童 73642296, 原始生命态 尼比鲁 27204311, protection 墓穴的指名者 24224830 and 抹杀之指名者 65681983
- Floodgate variants run 技能抽取 82732705, 大逮捕 36975314, 群雄割据 90846359 and 激流葬 53582587 because the engine mostly activates from hand and grave
- Every 破械 monster is a Fiend; main deck attributes are FIRE (阿罗汉 26236560, 萨巴拉 41165831), WATER (罗鬼刹 53624265, 萨玛 88554436) and DARK (娑罗摩 31588572, 祸灵 89019964, 双极之破械神 1966438), and every link monster is a DARK Fiend
- Setcodes on this server are separate: 破械 is 0x130 and 破械神 is 0x1130, so 破械 search and revive effects cannot touch 破械神 monsters and vice versa

- **Core Mechanic: Destroy and Float**

- Every 破械童子 (阿罗汉 26236560, 娑罗摩 31588572, 罗鬼刹 53624265, 斯玛 31531914) floats when destroyed by battle or by another card's effect, special summoning a different 破械 monster from hand or deck, verified in scripts as a destroy trigger that excludes the card's own code
- Self-destroy is the engine: 阿罗汉 26236560 destroys one card you control to special summon itself from hand, 罗鬼刹 53624265 quick-destroys one card you control on either player's turn, 娑罗摩 31588572 Sets a 破械 card from grave then destroys one card you control
- Set-trap float: 破械双极 80801743, 破械唱导 53417695, 破械神的恸哭 54807656, 破械习合 93898740 and 破械转生 67803035 special summon a 破械 from deck when destroyed by effect while Set, and a face-down 双王之械 27412542 does the same, but a face-up 双王之械 27412542 does not float
- Destroying your own Set trap with 阿罗汉 26236560 or 罗鬼刹 53624265 produces two bodies at once: the monster special summons itself and the trap special summons a 破械 from deck, so traps Set this turn are meant to be destroyed, not activated
- 破械唱导 53417695 is removal and engine in one: destroy one face-up 破械 monster you control plus one card on the field, both sides float
- Fiend lock: after 阿罗汉 26236560, 罗鬼刹 53624265 or 斯玛 31531914 resolves its destroy effect you may only special summon Fiends until the end of the turn, and 萨巴拉 41165831 and 破械焰魔天 阎摩 94014327 lock while their summoned monsters stay face-up
- 阎摩 24269961 is the Link-2 searcher (two Fiends) that adds a 破械 monster from deck or grave on summon, 罗寂刹 67680512 is the Link-2 that includes a 破械神 as material
- Absorb summon: 罗寂刹 67680512, 阿罗魃 93084621, 破械神的祸灵 89019964 and 破械习合 93898740 link summon using the opponent's monster as material, removing it without destroying it so its float never triggers
- 罗寂刹 67680512 effect one only works during the opponent's main phase on their special-summoned monster and only makes a DARK Link-2, while 阿罗魃 93084621 and 祸灵 89019964 are your own ignition effects on any face-up monster
- 破械神的恸哭 54807656 effect one destroys a card only when you link summon a 破械 link (来迎 29479265 or 破械焰魔天 阎摩 94014327), not on 阎摩 24269961 or 罗寂刹 67680512
- 来迎 29479265 (Link-4) destroys a card after every effect destroy, after every battle destruction and in each player's end phase, turning the whole float engine into free removal

- **One-Card Combo: 娑罗摩 Loop**

- Starter: 破械童子 娑罗摩 31588572 with a normal summon plus one 破械 card in grave, which the turn-one opener or 愚蠢的埋葬 81439173 provides
- Step 1: normal summon 娑罗摩 31588572, effect one Sets 破械唱导 53417695 from grave face-down then destroys it, 唱导 effect two special summons 破械童子 阿罗汉 26236560 from deck
- Step 2: link 娑罗摩 31588572 plus 阿罗汉 26236560 into 破械神王 阎摩 24269961, effect one adds 破械童子 罗鬼刹 53624265 to hand
- Step 3: normal summon 罗鬼刹 53624265, quick effect destroys 阎摩 24269961, 阎摩 effect two in grave banishes itself to special summon 娑罗摩 31588572 from grave, optionally destroying one card you control to trigger another float
- Step 4: link 罗鬼刹 53624265 plus 娑罗摩 31588572 into a second 阎摩 24269961 which searches again, the loop rebuilds itself on every destruction
- With 破械神 萨巴拉 41165831 or 双极之破械神 1966438 in hand the loop upgrades: 萨巴拉 41165831 destroys the 阎摩 24269961 to summon itself, the grave 阎摩 effect revives 娑罗摩 31588572, and 萨巴拉 plus 娑罗摩 link into 破械神 罗寂刹 67680512 while 萨巴拉 effect two Sets a 破械 trap from deck
- Turn-one opener, two cards: Set 破械双极 80801743, 阿罗汉 26236560 destroys it to summon itself while 双极 floats 娑罗摩 31588572 from deck, then 娑罗摩 effect one recycles 双极 80801743 from grave and destroys 阿罗汉 26236560 to float 罗鬼刹 53624265, the pair links into 阎摩 24269961 whose search provides the extra Fiend to continue into 破械神 罗寂刹 67680512 with the Set 双极 as backrow

- **End Field One-Card**

- Typical turn-one board from the pure build: 破械神 罗寂刹 67680512 and 破械神王 阎摩 24269961, one or two Set traps (破械双极 80801743, 破械唱导 53417695, 破械神的恸哭 54807656), and 双极之破械神 1966438 or 破械神 萨巴拉 41165831 in hand
- On the opponent's turn 罗寂刹 67680512 steals their special-summoned monster into a DARK Link-2, normally a second 阎摩 24269961 that searches again, and every destroyed 破械 card on your side replaces itself from deck
- 双极之破械神 1966438 in hand re-summons itself whenever a card you control is destroyed, even during the opponent's turn and the damage step, discarding one card to destroy one card on the field
- Bigger variant: 破械双王神 来迎 29479265 as the Link-4 with a live 破械神的恸哭 54807656, or 破械神双 罗寂刹 21419436 whose quick effect destroys your own Fiend to negate the opponent's just-special-summoned monster
- Xyz option: 破械神 萨巴拉 41165831 and 破械神 萨玛 88554436, both Level 6, stack into DDD 怒涛大王 决策凯撒 79559912 which negates every special-summon effect, then climb into 天霆号 阿宙斯 90448279
- Halt point: 灰流丽 14558127 on the Set-trap float or 阎摩 24269961 search leaves one monster, 增殖的G 23434538 draws on every deck special summon so the loop is cut short

- **Extenders**

- 双极之破械神 1966438: free hand body whenever your card is destroyed, discard one to destroy one card, end-phase self-revival from grave, but only one special summon per turn
- 破械神 萨巴拉 41165831: quick special summon from hand by destroying your face-up Fiend or face-down card, and when sent to grave it Sets any 破械 trap from deck
- 破械神王 阎摩 24269961 in grave: when your card is destroyed, banish it to special summon any Fiend from hand or grave and optionally destroy one of your cards
- 破械神 萨玛 88554436: on field destroys one of your cards then one spell or trap, in grave destroys your Fiend or face-down card to summon itself
- 破械式鬼 萨拉 95136979: quick discard itself to special summon any Fiend from hand and destroy one of your cards, then recycles itself from grave on every destruction
- 破械冥官 篁 68625623: destroys up to three of your cards to summon itself, drawing or changing battle position or destroying one card per original type, and nukes all monsters when destroyed by effect
- 破械式鬼 斯玛 31531914: on normal summon specials a Level 4 or lower 破械 from deck then destroys one of your cards, the floated monster keeps the chain going
- 由魔界到现世的死亡导游 10802915: normal summon specials 娑罗摩 31588572 (negated) from deck, both Level 3 Fiends link into 阎摩 24269961 for a true one-card search
- 破械转生 67803035: searches 双王之械 27412542 from deck, then shuffles up to three 破械 from grave into deck to destroy the same number of your own cards
- 破械习合 93898740: uses your 破械神 link plus any face-up monster including the opponent's as material for a Fiend link summon such as 破械双王神 来迎 29479265
- 破械神双 罗寂刹 21419436: when the opponent special summons, destroy your own Fiend to negate the summoned monster, and in grave with a Link-4 or higher 破械 on field it banishes to destroy an activating monster
- 破械焰魔天 阎摩 94014327: at your end phase revives up to two Fiends destroyed this turn, and substitutes its own destruction with any face-up card on the field

- **Halt Points**

- 灰流丽 14558127 negates 双王之械 27412542 activation, 阎摩 24269961 search, and every special-summon-from-deck float (阿罗汉 26236560, 娑罗摩 31588572, 罗鬼刹 53624265, 斯玛 31531914 and all Set traps), but 阿罗汉 26236560 effect one summons from hand so Ash does nothing there
- 增殖的G 23434538 draws for every special summon and the loop specials five or more times, under it play 阿罗汉 26236560 plus one float and stop
- 屋敷童 73642296 stops grave moves: 娑罗摩 31588572 effect one, 阎摩 24269961 effect two, 破械双极 80801743 effect one, 祸灵 89019964 effect three, 萨玛 88554436 effect two and 焰魔天 阎摩 94014327 effect one
- 幽鬼兔 59438930 destroys the activating monster: on 娑罗摩 31588572 or 罗鬼刹 53624265 the float still replaces it, but on 罗寂刹 67680512 or 阿罗魃 93084621 the absorb summon fizzles
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 on 阿罗汉 26236560, 娑罗摩 31588572 or 罗鬼刹 53624265 in grave negate their destroy-floats for the turn
- 原始生命态 尼比鲁 27204311 tributes everything after five summons and tributing does not trigger the destroy-floats, keep the summon count at four or lower when it is live
- 次元吸引者 91800273 sends destroyed cards to banishment: the deck-float chain and 双极之破械神 1966438 still work, but grave-based 娑罗摩 31588572, 阎摩 24269961 and 破械双极 80801743 lines shut down

- **Mirror Match**

- Never destroy the opponent's 破械 monsters by effect, every destroyed 破械童子 阿罗汉 26236560, 娑罗摩 31588572, 罗鬼刹 53624265 and 斯玛 31531914 summons a replacement from deck for free
- Remove their monsters as link material instead: 罗寂刹 67680512, 阿罗魃 93084621, 祸灵 89019964, 破械习合 93898740 and 闭锁世界的冥神 98127546 consume the opponent's monster without destroying it so nothing floats
- Normal-summoned monsters are safe from 罗寂刹 67680512 effect one which only targets special-summoned monsters, so normal summon before extending into extra deck monsters
- 破械唱导 53417695 and 来迎 29479265 destroy a card each time they trigger, in the mirror aim the destroys at your own cards or their backrow, never at their floaters
- 双极之破械神 1966438 triggers for both players when their own cards are destroyed, so the mirror becomes a race over who chains the better float first
- Whoever resolves 罗寂刹 67680512 plus 双极之破械神 1966438 first owns the grind, every destruction of their board refills it from deck

- **Common Mistakes**

- Fiend lock: after 阿罗汉 26236560, 罗鬼刹 53624265 or 斯玛 31531914 destroys, no non-Fiend special summons for the rest of the turn, so 访问码语者 86066372 and I：P百变莱娜 65741786 must be made before the lock or not at all
- 双王之械 27412542 floats only when destroyed while Set, destroying the face-up 双王之械 with 阿罗汉 26236560 wastes the float, always destroy the Set traps instead
- Traps Set this turn cannot activate but still float when destroyed, destroying your own Set 破械双极 80801743 or 破械唱导 53417695 is the engine not a misplay
- A monster destroyed by its own effect does not float, 娑罗摩 31588572 or 罗鬼刹 53624265 destroying themselves with effect one produces nothing, destroy other cards such as the face-down monster placed by 娑罗摩 31588572
- Using 罗寂刹 67680512 or 阿罗魃 93084621 as material for their own absorb means they are not destroyed and their grave-add effect two does not trigger
- The absorb effects only make DARK Link-2 monsters, in the pure build that is essentially another 阎摩 24269961, so do not plan 阿罗魃 93084621 or 来迎 29479265 off the absorb
- 阎摩 24269961 searches only 破械 setcode 0x130 monsters, it cannot add 破械神 萨巴拉 41165831, 双极之破械神 1966438 or 破械神的祸灵 89019964 which are 破械神 setcode 0x1130
- 娑罗摩 31588572 effect one and 破械双极 80801743 effect one also only touch 破械 setcode 0x130 cards, they cannot recycle 破械神的恸哭 54807656 or summon 萨巴拉 41165831
- 破械神的恸哭 54807656 effect one triggers only on 破械 link summons, 来迎 29479265 and 破械焰魔天 阎摩 94014327, not on 阎摩 24269961, 罗寂刹 67680512 or 阿罗魃 93084621
- 双极之破械神 1966438 is limited to one special summon per turn, and the copy revived by effect three returns to the deck bottom when it leaves the field, so it cannot float or be recycled from grave
- 萨玛 88554436 and 萨拉 95136979 special summoned from grave redirect to the deck bottom when they leave, plan no grave recursion for those copies
- 破械神的祸灵 89019964 gains 300 attack per 破械 card in grave but it is 破械神 setcode so it never counts itself
- Under 技能抽取 82732705, played in several pure builds, on-field effects of 娑罗摩 31588572, 罗鬼刹 53624265 and the links are dead, but hand effects of 阿罗汉 26236560 and 萨巴拉 41165831, grave effects of 阎摩 24269961 and all destroy-floats still work
- 增殖的G 23434538: do not full-combo, every 破械 special summon from deck draws the opponent a card, the loop is the exact behavior Maxx C punishes
