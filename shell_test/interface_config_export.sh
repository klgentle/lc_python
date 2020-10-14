#!/usr/bin/env bash

# output: t_itf_config/interface_id.json
# usage: sh interface_config_export.sh list*.txt

SHELL_DIR=$(cd "$(dirname "$0")";pwd)
source ${SHELL_DIR}/__config.sh

cmd=expdp

host="http://${url}:${port}/${cmd}"

filePath=/tmp/list.txt
touch filePath

for interface_id in $(cat $1)
do
   echo ${interface_id} > ${filePath}
   msg=`curl -o t_itf_config/${interface_id}.json -s --data-urlencode "filePath=$filePath" "${host}"`
done

echo "export done. ${msg}"

