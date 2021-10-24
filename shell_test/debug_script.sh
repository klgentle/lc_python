 #!/usr/bin/env bash

function script1 {
    n=$(( RANDOM % 100 ))
    
    if [[ n -eq 42 ]]; then
       echo "Something went wrong"
       >&2 echo "The error was using magic numbers"
       rt=1
    fi
    
    echo "Everything went according to plan"
}

> /tmp/script1.log
for ((i=0; i<1000; i++));
do
    script1 >> /tmp/script1.log 2>&1
    if [[ $rt == 1 ]]; then
        cat /tmp/script1.log
        echo "run script1 $i times"
        exit 1
    fi
 
done
