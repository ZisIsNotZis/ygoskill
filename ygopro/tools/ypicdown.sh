#!/bin/bash
for i in `comm -23 <(sqlite3 cards.cdb 'select id from datas'|sort) <(ls pics|grep -o '[0-9]*'|sort)`;do
	curl -v https://cdn.233.momobako.com/ygoimg/ygopro/$i.webp!/format/webp/fw/400/quality/85 -opics/$i.webp
done
mogrify -format jpg pics/*.webp
rm pics/*.webp