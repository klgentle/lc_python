for num in {1..100}
do 
    echo -n "2^$num=" >$num.txt
    echo 2^$num | bc >>$num.txt
done
