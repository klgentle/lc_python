def bat_log_template():
    bat_report_log = """
COMMIT;

V_END_TIME:=CURRENT_TIMESTAMP ;    --处理结束时间
V_SPEND_TIME:=ROUND(TO_NUMBER(TO_DATE(TO_CHAR(V_END_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')
 -TO_DATE(TO_CHAR(V_ST_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')) * 24 * 60 * 60);----执行时间

V_JOB_STEP:=1;
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME,V_SPEND_TIME,V_ERR_MSG,V_JOB_ID,'结束处理...');
COMMIT;
    """
    return bat_report_log

def add_in_second_position(content:str, target_str:str)->str:
    content_list = content.split(target_str)
    # s2 =['d', ' b ', ' c ', ' css']
    # 从第二个至最后都要加日志
    # TODO 日志编号 编号可以在最后统一重写一遍
    to_add_log_list = content_list[2:]
    # the last one no need
    log_content_list = [' '] * len(to_add_log_list)
    for i in range(0, len(to_add_log_list)-1):
        sql = to_add_log_list[i] + self.bat_log_template()
        log_content_list[i] = sql

    log_content_list[-1] = to_add_log_list[-1]
    return target_str.join(content_list[0:2] + log_content_list)


if __name__ == "__main__":
    s = "da b a c a css"
    s2 = add_in_second_position(s,'a')
    print(s2)
    
