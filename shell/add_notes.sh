#!/bin/bash
for f in P_RPT_REM101R.sql P_RPT_REM105R.sql P_RPT_REM107R.sql P_RPT_REM109R.sql P_RPT_REM115R.sql P_RPT_REM116R.sql P_RPT_REM117R.sql P_RPT_REM118R.sql P_RPT_REM121B.sql P_RPT_REM121R.sql P_RPT_REM122B.sql P_RPT_REM122CH.sql P_RPT_REM122C.sql P_RPT_REM122DH.sql P_RPT_REM122D.sql P_RPT_REM122R.sql P_RPT_REM123R.sql P_RPT_REMI010R.sql P_RPT_REMI020R.sql P_RPT_REMO010R.sql P_RPT_REMOR07.sql
    do
    #sed -i '/+================*============/i V1.3    20190617    DONGJIAN    change debit_amount to amount_debited' $f
    dos2unix $f
    done
