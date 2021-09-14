#!/bin/bash
PIDARRAY=()
for file in add_notes.sh array_var.sh
do
    md5sum $file &
    PIDARRAY+=("$!")
done
wait ${PIDARRAY[@]}
