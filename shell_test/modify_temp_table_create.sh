for table_name in $(grep -i temporary *cif* | awk -F'.sql' '{print $1}')
do
    #echo $table_name    
    filename=$table_name.sql
    dos2unix $filename

    # add delete table $table_name; in the begin
    sed -i "/create /i drop table $table_name;" $filename
    # delete "global temporary, on commit preserve rows"
    sed -i "s/global temporary //g" $filename
    sed -i "s/on commit preserve rows//g" $filename
    sed -i "s/on commit delete rows//g" $filename
done
