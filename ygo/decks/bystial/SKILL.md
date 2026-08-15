---
name: bystial-engine-experience
description: 深渊之兽 (Bystial) engine experience: LIGHT/DARK grave-banish special summons, Lubellion search, Dis Pater synchro end
---
# 深渊之兽 (Bystial) Engine Experience

- **Deck Identity**

- Splash engine, not a standalone deck: seven DARK/LIGHT Dragon monsters that special summon themselves from hand by banishing a LIGHT or DARK monster from either graveyard, present in over 2400 deck folders in this repo
- Core family, all Level 6 DARK Dragon 2500 ATK with an identical hand special summon: 玛格巨龙 33854624, 德鲁伊鳞虫 06637331, 萨隆魔龙 60242223, 巴尔德鸟龙兽 72656408
- Searcher: 赫界龙 32731036, Level 8 LIGHT Dragon 2500 ATK, cannot be normal summoned, special summons itself by tributing a Level 6 or higher DARK Dragon
- Support monsters: 阿鲁伯 45005708, Level 4 DARK Dragon whose name becomes 阿不思的落胤 68468459; 白界丧失龙 69120785, Level 12 LIGHT Dragon boss
- Synchro end: 深渊之神兽 狄斯·帕忒耳 27572350, Level 10 DARK Dragon Synchro, tuner plus one or more non-tuner Dragons
- Key trap: 复烙印 34090915, the continuous trap that recycles banished LIGHT/DARK monsters and revives 深渊之兽
- Common homes in this repo: 骑士深渊之兽 (Centurion), 青眼深渊之兽, 弹丸深渊之兽龙骑兵团, 珠泪哀歌族深渊之兽, 烙印阿不思的落胤深渊之兽, 深渊之兽雷龙

- **Core Mechanic: Banish-to-Summon Hand Engine**

- Each of the four Level 6 Bystials targets 1 LIGHT or DARK monster in either player's graveyard, banishes it face-up, then special summons itself from hand, verified in scripts as targeting LOCATION_GRAVE of both players
- The effect is an IGNITION while the opponent controls no monster, but becomes a QUICK effect while the opponent controls a monster, verified as two registered effects with spcon2 checking opponent field, so these act as hand traps on the opponent's turn
- The banish is the disruption: it removes fusion material, recursion targets, and graveyard setup from either player's grave at no normal summon cost
- Each Bystial has a second effect that fires when sent from the field to the grave, verified as EVENT_TO_GRAVE with IsPreviousLocation(LOCATION_ONFIELD): 德鲁伊鳞虫 06637331 sends 1 opponent special summoned monster to grave, 萨隆魔龙 60242223 mills 1 深渊之兽 monster or 烙印 spell/trap from deck
- 巴尔德鸟龙兽 72656408 instead fires when the opponent special summons a Fusion/Ritual/Synchro/Xyz/Link monster: tribute another LIGHT/DARK you control to banish that monster
- 玛格巨龙 33854624 fires on its own special summon: a lingering end phase effect adds 1 Dragon from deck or grave except itself, and it resolves even if 玛格巨龙 left the field
- 赫界龙 32731036: tribute 1 Level 6 or higher DARK Dragon you control to special summon from hand or grave, discard it from hand to add any 深渊之兽 from deck, and once per main phase place 1 烙印 continuous spell or trap directly from deck, almost always 复烙印 34090915
- 阿鲁伯 45005708: on normal or special summon, discard 1 card, then either take control of 1 opponent field Dragon until end phase or special summon 1 Dragon from their grave to your field, then send itself to grave

- **One-Card Combo: 玛格巨龙 33854624**

- Starter: 玛格巨龙 in hand and any LIGHT or DARK monster in either graveyard, no other cards needed
- Step 1: activate its effect one targeting a grave LIGHT/DARK, banish it, special summon 玛格巨龙 as a free 2500 ATK body
- Step 2: end phase, lingering effect adds 1 Dragon from deck or grave except itself, typically 赫界龙 32731036 or 辉白龙 暴源翼龙 99234526
- Step 3: next turn, tribute 玛格巨龙 to special summon 赫界龙 32731036, discard it from hand to search a second 深渊之兽, then place 复烙印 34090915 from deck
- Result: one card became a 2500 body, a Dragon search, a second Bystial in hand, and 复烙印 face up, the full engine without spending the normal summon

- **End Field**

- 复烙印 34090915 face up: when a LIGHT/DARK monster is banished face-up, return one of them to the bottom of the deck and draw 1, once per turn, recycling the engine's own banishes into draws
- 复烙印 second effect: when the opponent normal or special summons a monster, special summon 1 深渊之兽 from your grave, once per turn and once per chain, a free revive and potential quick banish
- 深渊之神兽 狄斯·帕忒耳 27572350: effect one special summons 1 banished LIGHT/DARK monster to your field, effect two when the opponent activates a monster effect returns 1 banished card to the deck, destroying that monster if the card was yours or negating the effect if it was the opponent's
- Typical board: 1 to 2 Level 6 Bystial bodies, 复烙印 set, 赫界龙 32731036 if the line resolved, plus one or more Bystials still in hand ready to quick summon during the opponent's turn
- 白界丧失龙 69120785 as ceiling: tribute 2 深渊之兽 to special summon from hand or grave, while special summoned this way all face-up Ritual/Fusion/Synchro/Xyz/Link monster effects are negated, and if it leaves the field by the opponent's effect both players' extra decks are banished face-up until the opponent's end phase

- **Extenders**

- 萨隆魔龙 60242223: when sent from field to grave, mills 1 深渊之兽 monster or 烙印 spell/trap from deck, loading the grave for 复烙印 34090915 revives and future banishes
- 德鲁伊鳞虫 06637331: on death sends 1 opponent special summoned monster to grave, removing anything the opponent put out this turn including Link monsters that cannot be destroyed by battle
- 巴尔德鸟龙兽 72656408: a standing counter to extra deck summons, tributing a spare LIGHT/DARK to banish the opponent's fusion or synchro the moment it appears
- 阿鲁伯 45005708: steals an opponent Dragon or revives one from their grave, and as 阿不思的落胤 68468459 it enables 烙印融合 44362883 and 深渊龙 白界转生龙 3410461 lines in Branded mixes
- 赫界龙 32731036 is the consistency extender: any Level 6 or higher DARK Dragon on field, including a Bystial, converts into its search plus a 复烙印 34090915 from deck
- Tuners for the Level 10 ladder: 重骑士 普莉梅拉 15005145, 视界共鸣者 98396890, 魔轰神 路里 97651498; a Level 6 Bystial plus a Level 4 tuner makes 狄斯·帕忒耳 27572350
- Alternative ends: 混沌之双翼 22850702 Level 10 synchro that banishes a card on summon, 混沌之魔神 13076804 Level 8 that attacks all monsters, 天球之圣刻印 24361622 to bounce and search

- **Halt Points**

- 增殖的G 23434538: every Bystial special summon draws the opponent a card, so the engine cannot chain multiple summons while G is live
- 欢聚友伴·茸茸长尾山雀 42141493: same draw-per-summon problem as G, the engine's multiple special summons feed it heavily
- 次元吸引者 91800273: for the turn all cards sent to grave go to the banish zone instead, emptying the grave fuel the Bystials need to summon
- No LIGHT or DARK monster in either graveyard means every hand special summon effect cannot activate, a hard stop for the whole engine
- 效果遮蒙者 97268402 on 玛格巨龙 33854624 stops both the summon and the end phase search if timed on the summon effect
- 灰流丽 14558127 on 赫界龙 32731036 search or 萨隆魔龙 60242223 mill blocks the deck thinning
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 banish the Bystial from grave or hand, removing the death-trigger value and the revive target
- 深渊之兽 monsters are weak to 次元裂缝 effects beyond the engine: banished 深渊之兽 cannot return to hand for the quick summon since the effect summons from hand only

- **Mirror Match: 深渊之兽 vs 深渊之兽**

- The mirror is a race for the same grave pool: both players summon from the LIGHT/DARK monsters in either grave, so the first to banish the opponent's key grave card (fusion material, recursion target) cripples their engine
- 德鲁伊鳞虫 06637331 death triggers are the mirror's main trade: whoever sends the other's special summoned Bystial to grave first wins the body exchange
- 复烙印 34090915 is symmetric: every banish by either player draws its owner a card, and reviving from either player's grave pool means both can use the same banished cards
- 阿鲁伯 45005708 excels here, taking control of or reviving the opponent's own 深渊之兽 and turning their engine against them
- 巴尔德鸟龙兽 72656408 answers the opponent's 狄斯·帕忒耳 27572350 the moment it is summoned, before its negation can resolve
- Manage your own grave: leaving high-value LIGHT/DARK monsters in grave hands the opponent free summons, so banish your own key cards first when the mirror is live

- **Common Mistakes**

- Using the hand special summon as a slow IGNITION in your main phase when the opponent controls a monster, wasting the quick effect window that lets it disrupt on their turn
- Banishing the wrong grave card: the engine removes either player's grave, so careless targeting can strip your own fusion material or recursion instead of the opponent's
- Forgetting 德鲁伊鳞虫 06637331 and 萨隆魔龙 60242223 second effects need the card sent from the FIELD to the grave, discarding them from hand or banishing them triggers nothing
- Tributing the wrong monster for 赫界龙 32731036: it requires a Level 6 or higher DARK Dragon you control, so an untributable Level 4 like 阿鲁伯 45005708 cannot pay the cost
- Overextending under 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493: chain one Bystial and stop, do not resolve three quick summons into a wall of draws
- 复烙印 34090915 second effect is once per chain and once per turn, do not plan on two revives in one response
- 白界丧失龙 69120785 negation only applies while it was special summoned by its own tribute method, a revived or summoned copy does not negate extra deck monsters
- 狄斯·帕忒耳 27572350 effect two needs a banished card to return to deck, so keep a banished card available or the negation cannot resolve
- Setting 复烙印 34090915 through 赫界龙 32731036 uses the normal spell/trap zone, ensure a zone is free before activating the placement effect
