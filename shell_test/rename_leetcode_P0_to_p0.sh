for name in $(ls):
do
    the_first=$(echo $name|cut -c1-1)
    else_name=$(echo $name|cut -c2-200)
    if [ $the_first = "P" ]; then
        #echo "p"$else_name
        mv $name $else_name
        mv $else_name "p"$else_name
    fi
done
