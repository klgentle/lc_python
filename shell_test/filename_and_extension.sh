file=$0
echo 'file is: '$0

filename=${file%.*}
echo "filename is: $filename"

extension=${file##*.}
echo "extension is: $extension"
