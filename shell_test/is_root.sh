#!/bin/bash

if [ $UID -ne 0 ]; then
    echo Non root user. Please login as Root.
else
    echo Root User.
fi
