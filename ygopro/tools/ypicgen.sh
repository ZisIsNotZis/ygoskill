#!/bin/bash
NAMESZ=${NAMESZ:-25}
NAMEY=${NAMEY:-55}
if [ "$NAME2" ];then
	NAMESZ=15
	NAMEY=44
fi
set -e
sqlite3 cards.cdb "select
case when type&0x2then'spell'when type&0x4then'trap'when type&0x80then'ritual'when type&0x40then'fusion'when type&0x2000then'synchro'when type&0x800000then'xyz'when type&0x1000000then'peffect'when type&0x4000000then'link'when type&0x4000then'token'when type&0x20then'effect'else'normal'end,
name,
concat(iif(type&0x6,'empty ',''),iif(attribute&0x1,'earth ',''),iif(attribute&0x2,'water ',''),iif(attribute&0x4,'fire ',''),iif(attribute&0x8,'wind ',''),iif(attribute&0x10,'light ',''),iif(attribute&0x20,'dark ',''),iif(attribute&0x40,'devine ','')),
case when type&0x1then level else 1 end,
case when type&0x800000then'starb'when type&0x4000000then'starb'when type&0x82=0x82then'spell_ritual'when type&0x10000then'spell_quickplay'when type&0x20002=0x20002then'spell_continuous'when type&0x40000then'spell_equip'when type&0x80000then'spell_field'when type&0x2then'spell_normal'when type&0x20000then'trap_continuous'when type&0x100000then'trap_counter'when type&0x4then'trap_normal'else'star'end,
datas.id,
case when type&0x6then''when race&0x1then'【战士'when race&0x2then'【魔法使'when race&0x4then'【天使'when race&0x8then'【恶魔'when race&0x10then'【不死'when race&0x20then'【机械'when race&0x40then'【水'when race&0x80then'【炎'when race&0x100then'【岩石'when race&0x200then'【鸟兽'when race&0x400then'【植物'when race&0x800then'【昆虫'when race&0x1000then'【雷'when race&0x2000then'【龙'when race&0x4000then'【兽'when race&0x8000then'【兽战士'when race&0x10000then'【恐龙'when race&0x20000then'【鱼'when race&0x40000then'【海龙'when race&0x80000then'【爬虫类'when race&0x100000then'【念动力'when race&0x200000then'【幻神兽'when race&0x400000then'【创造神'when race&0x800000then'【幻龙'when race&0x1000000then'【电子界'else'【幻想魔'end,
case when type&0x6then''when type&0x1000then'/调整】'when type&0x200then'/灵魂】'else'】'end,
replace(desc,char(10),''),
case when type&0x1then atk else''end,
case when type&0x1then def else''end
from datas join texts on datas.id=texts.id;"|while IFS='|' read -r type name att lv lvtype id race sp desc atk def;do
	if ! [ -a pics/$id.jpg ];then
		echo $id
		convert -font WenquanYi-Micro-Hei textures/card_$type.webp \
		-pointsize $NAMESZ -antialias -annotate +30+$NAMEY "`sed 's:\(\S\{20\}\):\1\n:g'<<<$name`" \
		-fill gold -antialias -annotate +28+$((NAMEY-2)) "`sed 's:\(\S\{20\}\):\1\n:g'<<<$name`" \
		`j=330;for i in $att;do echo -n textures/att_$i.webp -geometry +$j+27 -composite\ ;let j-=25;done` \
		\( `[ -a pico/$id.* ]&&echo pico/$id.*||ls pico/*|sort -R|head -1` -filter Box -resize 300x300\! \) -geometry +50+108 -composite \
		-pointsize 10 -fill black -annotate +30+443 "`sed 's:\(\S\{35\}\):\1\n:g'<<<"$race$sp$desc"`" \
		-pointsize 15 -antialias -annotate +249+542 "$atk" \
		-antialias -annotate +331+542 "$def" \
		-gravity NorthEast `for((i=0,j=40;i<$((lv&15));i+=1,j+=25));do echo -n textures/$lvtype.webp -geometry +$j+70 -composite\ ;done` \
		pics/$id.jpg
	fi
done
