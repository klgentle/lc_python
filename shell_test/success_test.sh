#!/bin/bash
CMD="ls"
$CMD
if [ $? -eq 0 ];
then 
    echo "$CMD executed succesfully"
else
    echo "$CMD terminated unsuccesfully"
fi
