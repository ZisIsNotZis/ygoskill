#!/usr/bin/env python3
"""Reconcile ygo/decks/SKILL.md Collections section with the deck folders on
disk. Each deck folder foo/ with its own SKILL.md gets an alphabetical entry:
  - **[foo/](foo/SKILL.md)** — <human name> deck experience
Replaces the entire block between the "**Collections**" bullet and the
"**Conventions**" bullet. Call centrally after subagent batches finish.
"""
import os

BASE = "/home/z/.agents/skills/ygoskill/ygo/decks"
INDEX = os.path.join(BASE, "SKILL.md")
DECK_NAMES = {
    "exosister": "救祓少女 (Exosister)",
    "tearlaments": "珠泪哀歌族 (Tearlaments)",
    "shaddoll": "影依 (Shaddoll)",
    "orcust": "自奏圣乐 (Orcust)",
    "witchcrafter": "魔女术 (Witchcrafter)",
    "labrynth": "拉比林斯迷宫 (Labrynth)",    "phantomknights": "幻影骑士团 (Phantom Knights)",
    "skystriker": "闪刀姬 (Sky Striker)",
    "tenpai": "天杯龙 (Tenpai)",
    "spright": "卫星闪灵 (Spright)",
    "blueeyes": "青眼 (Blue-Eyes)",
    "hero": "英雄 (HERO)",
    "pendulummagician": "魔术师 (Pendulum Magician)",
    "traptrix": "虫惑魔 (Traptrix)",
    "rikka": "六花 (Rikka)",
    "whiteforest": "白森林 (White Forest)",
    "ryzeal": "雷火沸动 (Ryzeal)",
    "maliss": "码丽丝 (Maliss)",
    "voicelessvoice": "肃声 (Voiceless Voice)",
    "mikanko": "御巫 (Mikanko)",
    "kashtira": "俱舍怒威族 (Kashtira)",
    "runick": "神碑 (Runick)",
    "dragunity": "龙骑兵团 (Dragunity)",
    "swordsoul": "相剑 (Swordsoul)",
    "adventure": "勇者 (Adventure)",
    "bystial": "深渊之兽 (Bystial)",
    "fiendsmith": "刻魔 (Fiendsmith)",
    "assaultmode": "爆裂模式 (Assault Mode)",
    "drytron": "龙辉巧 (Drytron)",
    "evileye": "咒眼 (Evil Eye)",
    "blackwing": "黑羽 (Blackwing)",
    "spiritsoul": "灵魂 (Spirit Soul)",
    "spirit": "精灵 (Spirit)",
    "millennium": "千年 (Millennium)",
    "darklord": "堕天使 (Darklord)",
    "dd": "契约书/D·D (D/D)",
    "gunkansuship": "军贯 (Gunkan Suship)",
    "worldlegacy": "世界 (World Legacy)",
    "genex": "次世代 (Genex)",
    "zombie": "不死 (Zombie)",
    "gemini": "二重 (Gemini)",
    "sacredbeast": "三幻魔 (Sacred Beasts)",
    "unchained": "破械 (Unchained)",
    "faytale": "妖精传姬 (Faytale)",
    "dragonpendulum": "龙剑士 (Dragon Pendulum)",
    "infernity": "永火 (Infernity)",
    "machina": "机甲 (Machina)",
    "numeron": "源数 (Numeron)",
    "oddeyes": "异色眼 (Odd-Eyes)",
    "codetalker": "码语者 (Code Talker)",
    "invoked": "召唤师·阿莱斯特 (Invoked)",
    "utopia": "霍普 (Utopia)",
    "ignister": "@火灵天星 (@Ignister)",
    "yubel": "于贝尔 (Yubel)",
    "salamangreat": "转生炎兽 (Salamangreat)",
    "meklord": "机皇 (Meklord)",
    "nobleknight": "圣骑士 (Noble Knight)",
    "yosenju": "妖仙 (Yosenju)",
    "mermail": "海皇水精鳞 (Mermail)",
    "lunalight": "月光 (Lunalight)",
    "truedraco": "真龙 (True Draco)",
    "junkstardust": "废品·星尘 (Junk-Stardust)",
    "stardust": "星尘 (Stardust)",
    "dinosaur": "恐龙 (Dinosaur)",
    "abyssactor": "魔界剧团 (Abyss Actor)",
    "plunderpatroll": "海造贼 (Plunder Patroll)",
    "sunavalon": "圣天树 (Sunavalon)",
    "charmer": "灵使 (Charmer)",
    "destructionsword": "破坏之剑士 (Destruction Sword)",
    "redeyes": "真红眼 (Red-Eyes)",
    "livestwin": "直播☆双子 (Live☆Twin)",
    "cyberdragon": "电子龙 (Cyber Dragon)",
    "karakuri": "机巧 (Karakuri)",
    "zoodiac": "十二兽 (Zoodiac)",
    "herald": "宣告者 (Herald)",
    "cyberse": "电子界 (Cyberse)",
    "vendread": "复仇死者 (Vendread)",
    "predaplant": "捕食植物 (Predaplant)",
    "hieratic": "圣刻 (Hieratic)",
    "altergeist": "幻变骚灵 (Altergeist)",
    "monarch": "帝 (Monarch)",
    "qliphort": "机壳 (Qliphort)",
    "magibullet": "魔弹 (Magibullet)",
    "gemknight": "宝石骑士 (Gem-Knight)",
    "ghostrick": "鬼计 (Ghostrick)",
    "tribrigade": "铁兽 (Tri-Brigade)",
    "fabled": "魔轰神 (Fabled)",
    "performapal": "娱乐伙伴 (Performapal)",
    "sixsamurai": "六武众 (Six Samurai)",
    "darkworld": "暗黑界 (Dark World)",
    "yangzing": "龙星 (Yang Zing)",
    "dinomorphia": "恐啡肽狂龙 (Dinomorphia)",
    "mayakashi": "魔妖 (Mayakashi)",
    "subterror": "机怪虫 (Subterror)",
    "mechaphantombeast": "幻兽机 (Mecha Phantom Beast)",
    "gladiatorbeast": "剑斗兽 (Gladiator Beast)",
    "constellar": "星圣 (Constellar)",
    "icebarrier": "冰结界 (Ice Barrier)",
    "timelord": "时械神 (Timelord)",
    "madolche": "魔偶甜点 (Madolche)",
    "nekroz": "影灵衣 (Nekroz)",
    "trickstar": "淘气仙星 (Trickstar)",
    "fireking": "炎王 (Fire King)",
    "eldlich": "黄金国巫妖 (Eldlich)",
    "darkmagician": "黑魔术师 (Dark Magician)",
    "rokket": "弹丸 (Rokket)",
    "galaxyeyes": "银河眼 (Galaxy-Eyes)",
    "dragonmaid": "半龙女仆 (Dragonmaid)",
    "thunderdragon": "雷龙 (Thunder Dragon)",
    "endymion": "恩底弥翁 (Endymion)",
    "spellbook": "魔导书 (Spellbook)",
}


def main():
    decks = sorted(
        d for d in os.listdir(BASE)
        if os.path.isdir(os.path.join(BASE, d)) and os.path.isfile(os.path.join(BASE, d, "SKILL.md"))
    )
    src = open(INDEX, encoding="utf-8")
    lines = src.read().split("\n")
    src.close()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        if line.strip() == "- **Collections**":
            # consume until the Conventions bullet
            i += 1
            while i < len(lines) and lines[i].strip() != "- **Conventions**":
                # skip over any filler/blank right after Collections
                i += 1
            # emit deck links here
            for d in decks:
                name = DECK_NAMES.get(d, d)
                out.append("- **[%s/](%s/SKILL.md)** — %s deck experience" % (d, d, name))
            # the Conventions line follows naturally (we do NOT emit blank line after links)
            out.append("")
            continue
        i += 1
    open(INDEX, "w", encoding="utf-8").write("\n".join(out))
    print("index synced with deck folders:", decks)


if __name__ == "__main__":
    main()
