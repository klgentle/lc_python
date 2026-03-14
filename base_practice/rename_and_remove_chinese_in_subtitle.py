"""
remove chinese and rename subtitle

from: 小谢尔顿.Young.Sheldon.S01E01.1080p.BluRay.x265-RARBG.简英.srt
to: 小谢尔顿S01E01.srt
"""

for file in *小谢尔顿*; do 
	new_file=$(echo $file| sed 's:.Young.Sheldon.::g;s:1080p.BluRay.x265-RARBG.简英.::g')
	echo ${new_file}
	grep -Pv '[\p{Han}]' "$file" > "${new_file}"; 

done