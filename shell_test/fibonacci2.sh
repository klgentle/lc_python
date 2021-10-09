# 0 1 1 2 3 5 8
a=0
b=1
echo $a
echo $b

for i in `seq 2 10`
do
    let c=$a+$b
    echo $c
    a=$b
    b=$c
done
