array_var=(1 2 3 4 5 6)
# or 
#array_var[0]="test1"
#array_var[1]="test2"
#array_var[2]="test3"
#array_var[3]="test4"
#array_var[4]="test5"
#array_var[5]="test6"

echo ${array_var[0]}
index=5
echo ${array_var[$index]}
echo ${array_var[*]}
echo "length:" ${#array_var[*]}
echo "index:" ${!array_var[*]}
