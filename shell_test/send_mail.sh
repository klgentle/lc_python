#!/bin/bash

(
echo "To: klgentle@sina.com"
echo "Subject: hello"
echo "Content-Type: text/html"
echo
echo "<html><b><font size='7'>H</font>ello</b></html>"
echo
) | /usr/sbin/sendmail -t
