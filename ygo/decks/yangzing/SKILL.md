---
name: yangzing-experience
description: 龙星 (Yang Zing) deck experience: destruction float engine, Denglong turbo, extenders, halt points
---
# 龙星 (Yang Zing) Deck Experience

- **Deck Identity**

- Wyrm (幻龙族) synchro float deck: every Yang Zing monster special summons another Yang Zing from deck when destroyed, turning removal into advantage
- Setcode 0x9e (158); core main deck monsters are 光龙星-螭吻 61488417, 炎龙星-狻猊 30106950, 地龙星-狴犴 66500065, 风龙星-蒲牢 35089369, 水龙星-赑屃 2095764, 暗龙星-椒图 25935625, 魔龙星-饕餮 99946920
- Tuners are 光龙星-螭吻 61488417 (Lv1, main deck) and the synchro tuners 源龙星-望天吼 65536818 (Lv5), 邪龙星-睚眦 43202238 (Lv7), 幻龙星-嘲风 19048328 (Lv9)
- Boss synchro is 辉龙星-蚣蝮 83755611 (Lv8, requires non-tuner Wyrm materials), with 幻龙星-嘲风 19048328 as the attribute-floodgate and 邪龙星-睚眦 43202238 as the removal body
- Reference build is the near-pure 150822龙星 list: main Yang Zing engine plus 虚无空间 5851097 and 技能抽取 82732705 floodgates; modern builds splash 天威 or 相剑 Wyrms as extenders

- **Core Mechanic: Destruction Float Engine**

- Every main deck Yang Zing monster has a float effect: when destroyed by battle or card effect and sent to grave, special summon 1 other Yang Zing monster from deck (script condition: REASON_DESTROY, REASON_BATTLE+REASON_EFFECT, previous location field, previous controller you)
- Floats are trigger effects that resolve from the grave, so 技能抽取 82732705 and other field-negation do not stop them; the monsters must actually be destroyed, banish or bounce does not float
- Float positions differ: 炎龙星-狻猊 30106950, 地龙星-狴犴 66500065, 魔龙星-饕餮 99946920 summon in defense, 风龙星-蒲牢 35089369, 水龙星-赑屃 2095764, 暗龙星-椒图 25935625 summon in attack
- 光龙星-螭吻 61488417 is the engine multiplier: if destroyed, it floats a Yang Zing from deck, and while in grave it special summons itself when another Yang Zing is destroyed (self-floated copy is banished when leaving the field)
- 暗龙星-椒图 25935625 starts the loop: while it is the only monster on your field, discard 2 Yang Zing from hand to special summon 1 Yang Zing with 0 ATK and 1 with 0 DEF from deck (光龙星-螭吻 61488417 and 炎龙星-狻猊 30106950 both qualify); those two are banished at end phase, so synchro them away that turn
- The deliberate destruction loop uses 龙星的九支 57831349 (negate, return the negated card to deck, then destroy 1 other Yang Zing card you control to trigger its float), 邪龙星-睚眦 43202238 (destroy 1 face-up Yang Zing you control plus 1 opponent card), and 辉龙星-蚣蝮 83755611 (destroy 1 card you control, special summon 1 Lv4 or lower monster from your grave)
- 龙星的具象化 30398342 adds an extra deck float: when a monster you control is destroyed, special summon 1 Yang Zing from deck, once per turn, while it is face-up you may only special summon synchro monsters from the extra deck
- 龙星的气脉 43577607 scales with attributes of Yang Zing in grave: 2 attributes gives Yang Zing +500 ATK, 3 gives a destroy-replacement that sends the field spell instead (that replacement prevents the float), 4 forces opponent monsters to attack position and blocks their sets, 5 lets you send it to grave to destroy all cards on field (a mass float trigger)

- **One-Card Combo: 暗龙星-椒图 start**

- Requires 暗龙星-椒图 25935625 alone on field plus any 2 Yang Zing in hand to discard, so it is a three-card opener but the deck's defining line
- Step 1: normal summon 暗龙星-椒图 25935625 with no other monsters, activate its effect, discard 2 Yang Zing, special summon 光龙星-螭吻 61488417 (0 ATK) and 炎龙星-狻猊 30106950 (0 DEF) from deck in attack position
- Step 2: synchro 光龙星-螭吻 61488417 (Lv1 tuner) + 炎龙星-狻猊 30106950 (Lv4) into 源龙星-望天吼 65536818 (Lv5 tuner), whose summon effect adds 1 Yang Zing card from deck to hand, usually 龙星的九支 57831349 or 龙星的辉迹 17183908
- Step 3: synchro 源龙星-望天吼 65536818 (Lv5 tuner) + 暗龙星-椒图 25935625 (Lv2) into 邪龙星-睚眦 43202238 (Lv7 tuner); leaving the field makes 源龙星 float, special summoning 风龙星-蒲牢 35089369 (Lv1 non-tuner) from deck
- Step 4: 邪龙星-睚眦 43202238 ignition effect destroys the floated 风龙星-蒲牢 35089369 plus 1 opponent card, so 风龙星 floats into another Yang Zing from deck, choose a non-tuner such as 水龙星-赑屃 2095764 (Lv2), never float 光龙星-螭吻 61488417 here because it is a tuner and cannot be material beside the tuner 邪龙星
- Step 5: synchro 邪龙星-睚眦 43202238 (Lv7 tuner) + the floated 水龙星-赑屃 2095764 (Lv2) into 幻龙星-嘲风 19048328 (Lv9), whose summon grants the attribute lock, or skip the pop and synchro 邪龙星 (Lv7) + 风龙星-蒲牢 35089369 (Lv1) directly into 辉龙星-蚣蝮 83755611 (Lv8), whose summon effect shuffles up to 2 cards (distinct attributes among its Wyrm materials) back to the deck
- End result: 辉龙星-蚣蝮 83755611 (bounce boss) or 幻龙星-嘲风 19048328 (attribute floodgate) on field with a set 龙星的九支 57831349, opponent cards bounced, and grave set up for 龙星的辉迹 17183908
- 源龙星-望天吼 65536818 level change is a toolbox, not a combo step: dump a Wyrm to grave for 气脉 attributes and 辉迹 fuel, or change level to reach a target directly, e.g. 源龙星 (Lv5) + 地龙星-狴犴 66500065 (Lv3) is already 辉龙星-蚣蝮 83755611 (Lv8), 邪龙星-睚眦 43202238 (Lv7) + 水龙星-赑屃 2095764 (Lv2) is 幻龙星-嘲风 19048328 (Lv9)

- **End Field One-Card**

- 辉龙星-蚣蝮 83755611 (targeted bounce on summon, destroy-your-own-card plus grave revive) backed by 邪龙星-睚眦 43202238 (untargetable, pop 1 own Yang Zing plus 1 opponent card)
- Set 龙星的九支 57831349 as a counter trap that negates a monster effect or spell/trap activation, returns it to deck, then pops your own Yang Zing to float again
- Face-up 龙星的具象化 30398342 gives a second float per destruction; 技能抽取 82732705 shuts down opponent monster effects on field while the float engine keeps resolving from the grave; 虚无空间 5851097 is a lock you flip after establishing, since it stops all special summons including your own floats
- Halt point: 灰流丽 on 源龙星-望天吼 65536818 search, or on 暗龙星-椒图 25935625 effect, ends the line; Ash on the 光龙星-螭吻 61488417 float keeps the board smaller but does not stop the float engine

- **Extenders**

- 龙星的辉迹 17183908 (quick-play): shuffle 3 Yang Zing monsters from grave into deck, draw 2, once per turn, refuels the float pool
- 秘龙星-神数囚牛 58990362: pendulum monster, on pendulum summon or when destroyed adds 1 Yang Zing or Zefra spell/trap from deck to hand, searches 龙星的九支 57831349 or 龙星的具象化 30398342
- 转生龙 29143726: Lv5 generic tuner synchro in the pure extra deck, when sent to grave by an opponent effect or destroyed in battle special summons 1 monster from a grave, recycles synchro material
- 废品同调士 63977008 in the pure list gives the Lv5 synchro access: 废品同调士 63977008 (Lv3 tuner) plus 水龙星-赑屃 2095764 (Lv2) or 暗龙星-椒图 25935625 (Lv2) makes 源龙星-望天吼 65536818 (Lv5), or plus 炎龙星-狻猊 30106950 (Lv4) makes 月华龙 黑蔷薇 33698022 (Lv7)
- 月华龙 黑蔷薇 33698022, 幻层守护者 阿玛迪斯 88033975, 虹光之宣告者 79606837, 星尘龙 44508094, 冰结界之龙 三叉龙 52687916 fill the pure extra deck as generic synchro answers
- Modern hybrid extenders are Tenyi Wyrms that summon themselves, e.g. 天威龙-纯真蟠龙 98159737, 天威龙-宽恕蟠龙 87052196, 天威之龙仙女 78917791, 天威之拳僧 32519092, and the 相剑 package 相剑师-莫邪 20001443, 相剑师-泰阿 56495147 into 相剑大师-赤霄 69248256 and 相剑大公-承影 96633955
- Hybrid end boards add 装弹枪管狞猛龙 27548199, 鲜花女男爵 84815190, 幻兽机 曙光女神百头龙 44097050 climb, and 相剑暗转 14821890 as removal; the True Draco floodgate 真龙剑皇 卓辉星·拼图 21377582 (a Wyrm, immune to the card types used to tribute summon it, quick destroys by banishing a continuous spell/trap from grave) slots into 真龙龙星 hybrids
- 龙星的极致 77783947: continuous trap forcing opponent attacks, quick effect sends itself to grave to synchro summon using monsters that include at least 1 Yang Zing as material, enables battle-phase synchro
- 龙星的凶暴化 67249508: during damage calculation doubles a Yang Zing's attack and defense, then destroys it at the end of the damage step, a combat float trigger

- **Halt Points**

- Ash Blossom on 暗龙星-椒图 25935625 or 源龙星-望天吼 65536818 stops the main line before the synchro; the deck has no searchable engine recovery beyond 秘龙星-神数囚牛 58990362
- 增殖的G punishes the float chain and the multiple synchro summons, commit to a small line such as 源龙星-望天吼 65536818 plus set 龙星的九支 57831349 under it
- 次元吸引者 and grave-banishing effects break the engine because every float resolves from the grave; 技能抽取 82732705 does not, floats still resolve
- Cards that banish instead of destroy, or bounce instead of destroy (辉龙星-蚣蝮 83755611 mirror usage), deny the floats, remove with destruction or fight the synchro summons directly
- 虚无空间 5851097 in your own deck blocks all special summons including your floats, activate it only after the loop is done or as a stall, and remember it self-destructs when a card is sent from deck to grave

- **Mirror Match: 龙星 vs 龙星**

- Never destroy the opponent's Yang Zing monsters with destruction effects, each pop hands them a free float from deck, bounce or return to deck instead, 辉龙星-蚣蝮 83755611 bounce is the mirror removal
- Destroying your own Yang Zing is the advantage play: 邪龙星-睚眦 43202238 pops your own monster plus theirs to double the float economy in your favor
- 幻龙星-嘲风 19048328 decides the mirror: while synchro summoned it blocks the opponent from activating effects of monsters whose attributes match its Yang Zing materials, choose materials covering LIGHT/DARK/FIRE/EARTH/WIND/WATER
- First 龙星的九支 57831349 wins the counter-trap fight, chain it to their 源龙星-望天吼 65536818 search or 暗龙星-椒图 25935625 summon
- 龙星的气脉 43577607 attribute count matters, keep Yang Zing of different attributes in grave to unlock the board wipe and the attack-position lock

- **Common Mistakes**

- 暗龙星-椒图 25935625 requires being the only monster on your field, do not normal summon or special summon anything else before activating it
- 椒图-summoned 光龙星-螭吻 61488417 and 炎龙星-狻猊 30106950 are banished at the end phase, synchro them away during the same turn
- Do not use the self-floated copy of 光龙星-螭吻 61488417 as synchro material, that copy is banished when it leaves the field
- 源龙星-望天吼 65536818 can only be special summoned once per turn, never attempt a second copy in one turn
- 源龙星 level-change cost sends 1 Wyrm from deck to grave, it does not have to be a Yang Zing, send 风龙星-蒲牢 35089369 or any Wyrm to set up grave attributes
- 辉龙星-蚣蝮 83755611 requires non-tuner Wyrm materials, generic non-Wyrm synchros cannot be its non-tuner, and its bounce count is the number of distinct attributes among its Wyrm materials
- 幻龙星-嘲风 19048328 attribute lock only covers attributes of its Yang Zing materials, non-Yang Zing materials contribute no lock
- 龙星的具象化 30398342 restricts extra deck summons to synchro only while face-up, do not plan Xyz, Link, Fusion, or pendulum-from-extra plays under it
- 龙星的九支 57831349 needs another Yang Zing card on the field after it destroys one, keep a Yang Zing on board or the destroy part fizzles
- 龙星的气脉 43577607 destroy-replacement sends the field spell instead, that replacement means your monster is not destroyed and does not float, do not waste it when you want the float
- 龙星的凶暴化 67249508 destroys the boosted monster at damage step end, it is a deliberate float setup, not a beater protection
- Do not chain 增殖的G against a full Yang Zing line, the float chain plus synchro summons will outdraw you, commit small instead

- **Build Quirks**

- The reference pure list (150822龙星) plays 技能抽取 82732705, harmless to the float engine because floats resolve from the grave, and 虚无空间 5851097 as a post-combo lock, remember it blocks your own special summons and self-destructs when a card goes from deck to grave
- 秘龙星-神数囚牛 58990362 is the only main deck searcher for 龙星 spell/traps, it is a pendulum so it needs the pendulum zones and restricts pendulum summons to Yang Zing and Zefra monsters
- Pure Yang Zing has no one-card full combo, the 暗龙星-椒图 25935625 line needs 2 discardable Yang Zing, hybrid Tenyi monsters like 天威龙-纯真蟠龙 98159737 and 天威之龙仙女 78917791 provide the modern one-card starters
- 转生龙 29143726, 废品同调士 63977008 and 月华龙 黑蔷薇 33698022 are generic Dragon/Fiend extras, they are not Yang Zing and do not float, use them only as synchro bridges
