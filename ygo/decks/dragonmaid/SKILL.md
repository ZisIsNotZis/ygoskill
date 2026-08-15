---
name: dragonmaid-experience
description: 半龙女仆 (Dragonmaid) deck experience: tag-out engine, one-card combo, extenders, halt points
---
# 半龙女仆 (Dragonmaid) Deck Experience

- **Deck Identity**

- Every card below verified against /home/z/ygo/cards.cdb and /home/z/ygo/script — this cdb REBALANCES the archetype: all monsters are Dragon-race, attributes are split per tag pair, only the 寝室/星夜 pair is DARK, all three fusions are LIGHT
- Small maids: 蒸馏室龙女 16960120 (FIRE 3★, on summon add 1 Dragonmaid monster from deck then mandatory discard 1 Dragonmaid from hand), 寝室龙女 32600024 (DARK 4★, on summon add 1 Dragonmaid spell/trap from deck), 客厅龙女 88453933 (WIND 3★, on summon mill 1 Dragonmaid card), 育婴龙女 40398073 (EARTH 2★, on summon revive 1 4★-or-less Dragonmaid from GY), 洗衣龙女 13171876 (WATER 2★, on summon mill 3)
- Big dragons: 星夜龙女 12163590 (DARK 9★), 天风龙女 15848542 (WIND 8★), 赤焰龙女 42055234 (FIRE 8★), 苍河龙女 49575521 (WATER 7★), 地慈龙女 76782778 (EARTH 7★)
- Fusions: 耀光龙女 24799107 (LIGHT 10★, 1 Dragonmaid + 1 5★+ Dragon), 龙女管家 41232647 (LIGHT 9★, 1 Dragonmaid + 1 Dragon), 贴身龙女 48658295 (LIGHT 8★, 2 Dragonmaid same attribute different level)
- Spells/traps: 盛情 78231355, 更衣 40110009, 迎接 14625090, 送行 15754711, 整理 57416183, 休息 77515704
- This cdb has NO Dragonmaid link monster — the names 半龙女仆·双头龙, 半龙女仆龙, 半龙女仆的接待, 半龙女仆的再召 DO NOT exist here; pure builds use generic dragon links instead: 刺刀枪管龙 85289965, 天球之圣刻印 24361622, S:P小夜骑士 29301450, I:P百变莱娜 65741786, 主动撞针龙 73539069, 圣秘之龙骑士 89851827
- Reference pure build: /home/z/ygo/deck/250426半龙女仆 — maids 蒸馏室×3/寝室×3/客厅×3/育婴×2/洗衣×1, big dragons 1 each, fusions 耀光×2/龙女管家×2/贴身×2, spells 盛情×3/更衣×2/迎接×2, traps 整理×3, 超融合 48130397×2 with 凶饿毒融合龙 41209827 and 沼地的泥龙王 54757758, staples 灰流丽 14558127×3, 增殖的G 23434538×2, 墓穴的指名者 24224830×2, 无限泡影 10045474, 效果遮蒙者 97268402×2, 屋敷童 73642296, 小丑与锁鸟 94145021

- **Core Mechanic: Tag-Out Engine**

- Every small maid's ② effect fires at battle phase START: return itself to hand and special summon a specific-level big dragon from hand OR GY — the bounce is part of the effect (script: SS only if the bounce resolved and the maid reached hand), so negating or removing the maid stops the tag
- Every big dragon's ③ effect fires at battle phase END: return itself to hand and special summon its small maid from HAND only — keep a maid in hand or the big dragon strands on field
- Tag pairs share attribute and level: 洗衣龙女↔苍河龙女 (WATER 2↔7), 育婴龙女↔地慈龙女 (EARTH 2↔7), 客厅龙女↔天风龙女 (WIND 3↔8), 蒸馏室龙女↔赤焰龙女 (FIRE 3↔8), 寝室龙女↔星夜龙女 (DARK 4↔9)
- There is no battle phase on the first turn, so the tag loop is offline turn 1 — turn 1 is fusion setup plus searches
- Big dragon hand effects (discard self): 赤焰龙女 and 地慈龙女 are QUICK effects usable on the opponent's turn (+2000 ATK on 1 Dragonmaid; special summon a 4★-or-less maid from hand); 星夜龙女, 天风龙女, 苍河龙女 are IGNITION effects in your own main phase (revive 1 Dragonmaid from GY/banished; negate the on-field effects of 1 face-up monster this turn; shuffle 1 monster from either GY into the deck) — do NOT hold them as reactive handtraps
- 赤焰/天风/苍河/地慈 are immune to effect destruction while a Fusion monster is on your field; 星夜龙女 makes your Dragon fusions immune to opponent effect destruction

- **One-Card Combo: 蒸馏室龙女**

- Starter: 蒸馏室龙女 16960120 alone in hand, nothing else needed
- Step 1: normal summon 蒸馏室龙女, activate ① to add 赤焰龙女 42055234 from deck to hand, then the mandatory discard sends 赤焰龙女 to GY — the script discards after the search, so the just-searched card fuels the GY even with an empty hand
- Step 2: contact fusion 贴身龙女 48658295 by banishing field 蒸馏室龙女 (FIRE 3★) and GY 赤焰龙女 (FIRE 8★) — same attribute, different level, 1 from field and 1 from GY
- Step 3: 贴身龙女 ① special summons 寝室龙女 32600024 from deck
- Step 4: 寝室龙女 ① adds 更衣 40110009, 迎接 14625090 or 盛情 78231355 from deck to hand
- Step 5 option A: keep 贴身龙女 + 寝室龙女; on the opponent's standby 贴身龙女 ② shuffles them into the deck and fusion summons 耀光龙女 24799107, whose negate goes live
- Step 5 option B: activate 更衣 immediately, fusing 贴身龙女 + 寝室龙女 into 耀光龙女 (贴身龙女 fills the 5★+ Dragon material slot), gaining the negate one turn earlier but losing the standby option

- **End Field One-Card**

- 贴身龙女 48658295 + 寝室龙女 32600024 + 1 searched S/T, with 贴身龙女's standby fusion threatening 耀光龙女 24799107
- Or immediate 耀光龙女 24799107: 3500 ATK, one negate of an opponent effect per turn that also returns itself to the extra deck and special summons 龙女管家 41232647 — run one 龙女管家 per 耀光
- 耀光龙女 ① on your next standby recycles any 9★-or-less Dragonmaid from hand or GY
- Halt points: Ash Blossom 14558127 on the 蒸馏室龙女 search kills the line; Ash or 效果遮蒙者 97268402 on 贴身龙女 ① stops the deck summon; removing 贴身龙女 before the standby phase stops the fusion

- **Extender: 盛情 78231355**

- Special summons 1 Dragonmaid from hand or GY in defense, then optionally mills 1 Dragonmaid from deck with the same attribute and a different level — oath limit 1 activation per turn
- Example: with 蒸馏室龙女 in GY, 盛情 summons it from GY and mills 赤焰龙女 42055234 from deck, creating the FIRE 3★/8★ pair for 贴身龙女 48658295 without spending the normal summon
- The same-attribute-different-level mill constraint exists precisely to set up 贴身龙女 contact pairs — keep pairs attribute-matched

- **Extender: 送行 15754711**

- Targets 1 Dragonmaid you control: special summons a different-named Dragonmaid from hand in defense and returns the target to hand
- The summoned monster cannot be destroyed by battle or effects until the end of the next turn
- Swaps a used maid into the big dragon you need without waiting for the battle phase tag

- **Extender: 更衣 40110009**

- Fusion summons 1 Dragon fusion from hand/field materials: 耀光龙女 24799107 (1 Dragonmaid + 1 5★+ Dragon) or 龙女管家 41232647 (1 Dragonmaid + 1 Dragon)
- Graveyard effect: return 1 face-up Dragonmaid you control to hand and add itself back to hand — recycle it with 寝室龙女 32600024 for repeated searches
- 龙女管家 ② destroys 1 opponent monster whenever one of your face-up Dragons returns to hand, so the maid tag-outs and 更衣 bounces all become removal

- **Extender: 迎接 14625090**

- Continuous spell: your monsters gain 100 ATK/DEF per Dragonmaid you control, and with 2+ Dragonmaids on field it adds 1 Dragonmaid card from GY to hand once per turn
- When it is sent to the GY, the opponent cannot target your Dragonmaid monsters with card effects for the rest of the turn — sequence it so this trigger lands on your key turn

- **Extender: Other Engine Pieces**

- 育婴龙女 40398073 normal summon revives a 4★-or-less Dragonmaid from GY, turning one normal summon into two searches (蒸馏室龙女 + 寝室龙女)
- 客厅龙女 88453933 mills any Dragonmaid card — mill the matching big dragon (赤焰/天风) so the battle phase tag has a GY target, or mill 盛情/迎接 for GY plays
- 洗衣龙女 13171876 mills 3 to fuel 育婴龙女 revives, 迎接 adds and 贴身龙女 GY material
- 整理 57416183: trap that returns your Dragon and one opponent field/GY card to hand; its GY effect revives a Dragonmaid in defense that returns to hand at the end phase
- 休息 77515704: trap that bounces a Dragonmaid to either search any Dragonmaid card or return one opponent spell/trap to hand

- **Halt Points**

- 蒸馏室龙女 16960120 search is the combo hinge — Ash Blossom 14558127 here ends the 1-card line
- 寝室龙女 32600024 search and 贴身龙女 48658295 deck special summon are the secondary Ash / 效果遮蒙者 97268402 / 无限泡影 10045474 targets
- 贴身龙女 on field is the engine hub: negate or remove it before the opponent's standby and the fusion into 耀光龙女 24799107 never happens
- The maid tag-out needs the maid to actually leave the field — 泡影/遮蒙者 on the maid or destroying it stops the big dragon
- 耀光龙女's negate is a once-per-turn quick effect; beat it by removing 耀光 first with 无限泡影 or by forcing it out, because the 龙女管家 41232647 it tags into has no negate
- The tag loop only exists during battle phases — anything that skips or ends your battle phase (turn 1, a battle-phase-ending effect, or burning your battle phase) strands your big dragon with no tag-back

- **Playing Under 增殖的G**

- The 1-card line special summons 3 times (蒸馏室, 贴身, 寝室) and the tag loop summons again every battle phase — full combo hands 3+ draws
- Compromise: stop at 蒸馏室龙女's search alone, or do 贴身龙女 + 寝室龙女 for the search and pass on the fusion
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 protect the search line from handtraps in this cdb's staple package

- **Mirror Match: 半龙女仆 vs 半龙女仆**

- First 蒸馏室龙女 16960120 resolution decides the game — handtrap the opponent's 蒸馏室/贴身, not their end board
- On your turn, discard 天风龙女 15848542 to negate the on-field effects of the opponent's 耀光龙女 24799107 or 贴身龙女 48658295 this turn, so your 更衣/盛情 resolve
- 苍河龙女 49575521 shuffles 1 monster from either GY into the deck on your main phase — strip the opponent's 育婴龙女 revive targets, 盛情 78231355 GY fuel and 贴身龙女's GY material half
- 赤焰龙女 42055234 is a quick +2000 ATK — break the 3500 耀光龙女 wall, e.g. 星夜龙女 12163590 becomes 4800
- 地慈龙女 76782778 is a quick special summon of a maid from hand — use it on your turn to extend into a second 贴身龙女 pair
- 龙女管家 41232647 ② destroys a monster every time YOUR Dragon returns to hand — your tag-outs and 更衣 bounces clear their field while yours cycle
- 超融合 48130397 with 凶饿毒融合龙 41209827 absorbs the opponent's DARK monsters (寝室龙女/星夜龙女) as materials — the mirror's biggest blowout, keep it for that

- **Common Mistakes**

- 贴身龙女 48658295 is special-summoned ONLY by its contact procedure (banish 1 matching Dragonmaid from field + 1 from GY, same attribute, different level) — its script registers a fusion-material function but an extra-deck summoning restriction leaves the contact procedure as the only way in, so 更衣 40110009 cannot fuse it (script-verified static analysis, not live-tested)
- 蒸馏室龙女's discard is mandatory — sequence it so the discarded card is one you want in the GY (the searched 赤焰龙女 is the standard choice); never discard a maid you still need for the tag-back
- The big-dragon ③ tag-back summons from HAND only, the maid ② tag-out summons from hand OR GY — keep a small maid in hand during your battle phase or the loop strands a big dragon
- 盛情 78231355 summons in defense and its mill requires same attribute + different level — a same-level or off-attribute mill breaks the 贴身龙女 pair
- Do not plan turn 1 around tag-outs — no battle phase on the first turn, turn 1 is fusion plus search
- Each 耀光龙女 negate consumes one 龙女管家 41232647 from the extra deck — the pure build runs 2/2, do not fuse the second 耀光 when no 龙女管家 remains
- 寝室龙女 searches S/T only, 蒸馏室龙女 searches monsters only, 客厅龙女 mills — use the right searcher mid-line
- This cdb rebalances attributes: only 寝室龙女/星夜龙女 are DARK and only the fusions are LIGHT, so TCG-format assumptions do not transfer — e.g. 深渊之兽 DARK/LIGHT dragon support only lines up with the 寝室/星夜 pair
