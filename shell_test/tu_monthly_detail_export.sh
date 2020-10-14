#!/bin/sh
################################################################################
# Script name              : tu_monthly_detail_export.sh
# Describe                 : sh tu_monthly_detail_export.sh yyyymmdd POSITIVE 
# Autor                    : dongjian
# Version                  : v1.0
# History                  : 20201013
################################################################################  
#source /home/odsuser/.bash_profile
source $HOME/.bash_profile

ScriptName=${0##*/}

BASEPATH=$(cd `dirname $0`;pwd)
HOMEPATH=`echo $HKHOME`
#echo $HOMEPATH
HKCONFIG=${HOMEPATH}/conf/jobconfig.cfg

odsDBsid=`awk 'FS=" " {if ($0~/^odsDBsid/) print $2}' ${HKCONFIG}`
odsDBUser=`awk 'FS=" " {if ($0~/^odsDBuser/) print $2}' ${HKCONFIG}`
odsDBPwd=`awk 'FS=" " {if ($0~/^odsDBpassword/) print $2}' ${HKCONFIG}`
odsDBPassword=`source  ${HOMEPATH}/common/aes.sh dec $odsDBPwd`

LOGPATH=`awk 'FS=" " {if ($0~/^LOGPATH/) print $2}' ${HKCONFIG}`

#echo $odsDBUser
#echo $odsDBPassword

data_date=$1
type=$2

if [ $type = "POSITIVE" ]; then 
    exportFileName="cif089r1_err"
else
    exportFileName="cif089r2_err"
fi

export=`
sqlplus -S -L /nolog<<EOF >${exportFileName}.dat
connect  $odsDBUser/$odsDBPassword@$odsDBsid
set termout off;
set echo off;
set feedback off;
set heading off;
set pagesize 0;
set pages 0;
set linesize 1000;
select segment_info 
from ODSUSER.CBS_FH00_TU_MONTHLY_DET000 t
WHERE DATA_date =to_date(${data_date},'yyyymmdd')
AND ID LIKE 'CAR-${type}%';
exit;
EOF`

if [ $? -eq 0 ]; then 
    touch ${exportFileName}.ok
fi
