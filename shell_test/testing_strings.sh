read -p "input var:" var

echo $var

if (( ${var} > 3)); then
    echo "case (()) $var>3"
else                       
    echo "case (()) ${var}<=3"
fi

# true for 4; flase for 22
if [[ "${var}" > 3 ]]; then
    echo "case [[]] $var>3"
else
    echo "case [[]] ${var}<=3"
fi
