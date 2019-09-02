#!/bin/bash
for f in $(ls)
    do
    dos2unix $f
    done
