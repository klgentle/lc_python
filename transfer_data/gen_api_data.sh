# 生成两个长串
# HASE: 三行数据\n拼接，字段以,分割
# HBAP: 17行数据\n拼接，字段以,分割
# 数据尽量拼在一起，不要多次发，太麻烦了

$HASE_data="1,HASE,12312,Oct,22,22:46,123\n2,HSCN,12312,Oct,22,22:46,123\n3,HMO,12312,Oct,22,22:46,123"

curl http://192.168.5.201:8000/RPM_transfer_data/receive_data/HASE -X POST -d 'site_name=HASE' -d "site_data=1,HASE,12312,Oct,22,22:46,123
2,HSCN,12312,Oct,22,22:46,123
3,HMO,12312,Oct,22,22:46,123"

curl http://192.168.5.201:8000/RPM_transfer_data/transfer_data/HASE
