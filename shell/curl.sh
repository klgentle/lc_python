#!/bin/bash
#
# Send a Text Message
################################
#
# Script Variables ####
#
phone="18070265802"
#SMSrelay_url=http://textbelt.com/text
SMSrelay_url=http://textbelt.com/intl
text_message="Hello boy, have a nice day"
#
# Send text ###########
#
curl -s $SMSrelay_url -d \
number=$phone \
-d "message=$text_message" #> /dev/null
#
exit
