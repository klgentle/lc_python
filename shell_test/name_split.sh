file_txt="sample.txt"
name=${file_txt%.*}
echo File name is: $name
extension=${file_txt#*.}
echo extension is: $extension
