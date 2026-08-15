---
name: trickstar-experience
description: 淘气仙星 (Trickstar) deck experience: link burn loop, one-card combo, extenders, halt points
---
# 淘气仙星 (Trickstar) Deck Experience

- **Deck Identity**

- All Trickstar monsters are LIGHT Fairy, setcode 0xfb, except 阿库阿安琪儿 37405032 which is WATER and also counts as a 海晶少女 (setcode 0x12b)
- Main deck engine: 坎迪娜 61283655, 莉莉贝儿 98700941, 卡罗贝恩 98169343, 曼珠诗华 35199656, 那耳姬丝 91505214, 胡蒂 1410324, 菲沃斯 86825114, 曼德拉 22219822, 施南 59604521
- Extra deck links: 科尔奇卡 298846, 布露姆 77307161, 蒂瓦丽迪丝 14365823, 霍莉安琪儿 32448765, 斯威特戴薇儿 94626871, 布拉蒂玛丽 51011872, 诺布露安琪儿 37683441, 福克希维琪 86750474, 戴薇尔菲妮姆 3792766, 贝拉麦当娜 41302052
- Extra deck fusions: 德拉玛蒂丝 64804137, 吉她斯薇特 91272072, reachable through 淘气仙星融合 88693151 and 淘气仙星扩散融合 63181559
- Key spells: 灯光舞台 35371948, 现场演唱舞台 51208046, 灯光竞技场 63492244, 音乐节 62481203, 花冠魔法 22159429; key traps: 康乃馨转生术 21076084, 花束 99890852
- Support engine: 蓝泪的天使 91706817 and 蓝泪的处女 99176254 searched by 诺布露安琪儿 37683441 on link summon, plus burn traps 魔法筒 62279055, 破坏轮 83555666, 隐居者的猛毒药 8842266, 隐居者的大釜 91740879, 噩梦之拷问室 85562745
- Two-card search core: 坎迪娜 on normal summon adds any Trickstar card, 灯光舞台 on activation adds a Trickstar monster, field spell tutors 星球改造 73628505 and 舞台旋转 73468603 give extra access

- **Core Mechanic: Link Burn Loop**

- Every Trickstar special summon into a linked zone and every Trickstar link summon stacks 200-point burns, and 灯光舞台 35371948 adds another 200 whenever a Trickstar monster deals battle or effect damage
- 霍莉安琪儿 32448765: 200 burn per Trickstar summoned into its linked zone, all linked Trickstars are indestructible by battle and effect, and it gains ATK equal to every Trickstar effect damage it sees
- 蒂瓦丽迪丝 14365823: 200 burn on its own link summon plus 200 burn each time the opponent summons a monster, but only one 蒂瓦丽迪丝 can be face-up on your field
- 布露姆 77307161: link-1 off one Level 2 or lower Trickstar, the opponent draws 1 on its link summon, then burns opponent hand count times 200 if a linked Trickstar is destroyed
- 曼珠诗华 35199656: quick effect shows itself in hand to special summon and returns one face-up Trickstar to hand, and it burns 200 per card the opponent adds to hand, which makes it the loop recycler and the hand-draw punisher
- 音乐节 62481203: special summons 2 Trickstar tokens for link fodder and locks you into Trickstar-only summons that turn, its grave effect banishes itself to save an extra deck Trickstar from destruction
- Example burn stack: link the two 音乐节 tokens into 蒂瓦丽迪丝 inside 霍莉安琪儿's arrow deals 600 at once (蒂瓦丽迪丝 own 200, 霍莉安琪儿 zone 200, 灯光舞台 effect-damage 200)

- **One-Card Combo: 坎迪娜**

- Starter: 坎迪娜 61283655 in hand, no other cards needed
- Step 1: normal summon 坎迪娜, add 灯光舞台 35371948 from deck
- Step 2: activate 灯光舞台, add 莉莉贝儿 98700941 from deck
- Step 3: 莉莉贝儿 special summons itself because it was added to hand by an effect, not by a draw, verified in script c98700941 as not REASON_DRAW
- Step 4: link 坎迪娜 and 莉莉贝儿 into 霍莉安琪儿 32448765, no burn yet
- Step 5: activate 音乐节 62481203 to special summon 2 Trickstar tokens, this locks every further summon this turn to Trickstar monsters
- Step 6: link the 2 tokens into 蒂瓦丽迪丝 14365823 inside 霍莉安琪儿's arrow, dealing 600 burn, and every opponent summon now burns 200
- Step 7: 曼珠诗华 35199656 quick effect: show it, special summon it, return one face-up Trickstar to hand, use the bounce to pick up 坎迪娜 for a second normal summon search if it is still on field, never bounce a link monster
- Variant: search 曼珠诗华 from 灯光舞台 instead of 莉莉贝儿 when 卡罗贝恩 98169343 or another extender is already in hand, the combo still lands on the same end field

- **End Field One-Card**

- 灯光舞台 35371948 face-up with its once-per-turn lock ready to pin an opponent face-down spell or trap until the end phase
- 霍莉安琪儿 32448765 with 蒂瓦丽迪丝 14365823 in its arrow, both indestructible and burning 200 per opponent summon plus 200 per Trickstar damage
- 曼珠诗华 35199656 as the reactive body that punishes every opponent hand add, 莉莉贝儿 98700941 direct attacker with grave recursion when available
- One-card alone sets no trap, trap access comes from 蓝泪的天使 91706817 or from drawing 康乃馨转生术 21076084 and 花束 99890852
- Halt point: 灰流丽 14558127 on the 坎迪娜 search or on the 灯光舞台 add ends the line, there is no second search in the same chain

- **Extenders**

- 现场演唱舞台 51208046: field spell that adds a Trickstar from grave on activation, then once per turn makes a token if you control a Trickstar link and once per turn makes a token if the opponent has any spell or trap zone cards, locks you into Trickstar-only summons
- 灯光竞技场 63492244: field spell that revives one link material in defense with effects negated every time you link summon a Trickstar, free bodies every link, plus a once-per-turn face-down spell or trap zone lock
- 卡罗贝恩 98169343: free special summon when your field is empty or Trickstar-only, and a hand quick effect during the damage step that sends itself to double one attacking Trickstar's base ATK
- 那耳姬丝 91505214: special summons from hand on any effect damage to you, then burns 200 per opponent monster effect activated from hand or grave
- 胡蒂 1410324: special summons from hand while a Trickstar fusion or link is on field, as link material it adds 淘气仙星融合 88693151 or 淘气仙星扩散融合 63181559
- 菲沃斯 86825114: as link material it special summons itself back from grave but is banished if it ever leaves the field, and 曼德拉 22219822: special summons when discarded and destroys a monster in the opponent's linked zone when used as link material
- 施南 59604521: discard one Trickstar to revive a Trickstar link from grave, and burns 200 per card banished from the opponent's grave
- 阿库阿安琪儿 37405032: once per duel special summons from hand or grave while a Trickstar or 海晶少女 is on field, and when used as link material it reveals the opponent's hand and face-down cards
- 花冠魔法 22159429: equip spell that revives a Trickstar from grave, then special summons a Trickstar from hand once per turn when the equipped monster deals damage
- 康乃馨转生术 21076084: banish the opponent's entire hand and they draw the same count, then a quick effect in grave that banishes itself to revive a Trickstar
- 蓝泪 engine: 蓝泪的天使 91706817 burns the target's controller's opponent by their hand count and negates the target, and its grave effect sets a normal trap from hand or deck whenever anyone takes effect damage, hand-set traps can activate that same turn so every 200 burn can become a free 魔法筒 62279055 or 康乃馨转生术
- 蓝泪的处女 99176254: destroys a monster the opponent just special summoned for half its original ATK burn while you control a link monster, and its grave effect sets a normal spell on effect damage

- **Halt Points**

- 增殖的G 23434538: the token and link chain hands the opponent a draw per summon, compress the line to the 坎迪娜 into 霍莉安琪儿 plus one link and stop
- 灰流丽 14558127 on the 坎迪娜 search, on the 灯光舞台 add, or on 音乐节 activation stops extension cold
- 无限泡影 10045474 and 效果遮蒙者 97268402 on 坎迪娜 kill the first search, on 霍莉安琪儿 or 蒂瓦丽迪丝 kill the burn stacking
- 原始生命态 尼比鲁 27204311 after the fifth summon clears the whole board, stop at three to four summons or hold 康乃馨转生术 to strip the hand before it resolves
- 音乐节 and 现场演唱舞台 locks forbid every non-Trickstar summon for the rest of the turn, never activate them before summoning 灰流丽, 蓝泪的天使, 召命之神弓-阿波罗萨 4280258, S：P小夜骑士 29301450, or 灾厄之星 提·丰 93039339

- **Mirror Match: 淘气仙星 vs 淘气仙星**

- The mirror is a burn race decided by hand control: whoever resolves 康乃馨转生术 21076084 or 蓝泪的天使 91706817 first removes the other's burn traps and extenders
- Use 灯光舞台 35371948 and 灯光竞技场 63492244 zone locks on the opponent's set 康乃馨转生术 or 花束 99890852 before they can activate them
- Your own burns trigger the opponent's 那耳姬丝 91505214 special summons and 诺布露安琪儿 37683441 destruction, sequence damage so the last burn of the turn is yours
- 布露姆 77307161's opponent-draw and 曼珠诗华 35199656's add-burn feed each other in the mirror, expect free 200s from every draw and add
- 吉她斯薇特 91272072 doubles linked Trickstar link damage and snowballs ATK on every effect damage, whoever lands it first wins the burn exchange

- **Common Mistakes**

- Do not activate 音乐节 62481203 or 现场演唱舞台 51208046 after special summoning any non-Trickstar, the whole-turn lock makes the activation illegal and the chain fizzles
- 贝拉麦当娜 41302052's effect immunity and burn both require zero linked monsters, never put anything inside its arrows
- 蒂瓦丽迪丝 14365823 is unique on field, a second one cannot be summoned
- 莉莉贝儿 98700941 only special summons when added to hand by an effect, drawing it does nothing, always fetch it with 灯光舞台 or 坎迪娜
- 霍莉安琪儿's summon burn only counts summons into its own linked zone, place every new Trickstar link inside its arrows to stack the 200s
- 曼珠诗华's bounce is mandatory on successful special summon, always keep a reusable Trickstar to pick up and never bounce a link monster to waste it
- 蓝泪的天使's burn hits the target's controller's opponent, target the opponent's monster to burn them, targeting your own burns you instead
- 康乃馨转生术 banishes the entire opponent hand and lets them draw the same count, dead against an empty hand and risky when they hold hand traps
- 布露姆's link summon gives the opponent a draw, factor it into 增殖的G math and into 曼珠诗华 add-burn value
- 福克希维琪's float only triggers if it was link summoned and pulls a link-2 or lower Trickstar, keep 霍莉安琪儿 or 布拉蒂玛丽 in the extra deck when relying on it
- 花冠魔法 destroys the equipped monster when the equip leaves the field, and its hand summon needs the equipped monster itself to deal damage
- 施南's burn punishes banishment from the opponent's grave only, it does not burn on your own 康乃馨转生术, and 科尔奇卡 298846's burn needs your Trickstar to destroy a monster by battle first
