import unittest
import os
import sys
from os.path import dirname

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from database.ProcedureLogModify import ProcedureLogModify


class TestProcLogMod(unittest.TestCase):
    def test_set_job_step_value(self):
        proc_cont = """
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'1',V_JOB_NAME,V_SPEND_TIME,V_ERR_MSG,V_JOB_ID,'结束处理...');
"""
        except_out = """
V_JOB_STEP:=1;
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME,V_SPEND_TIME,V_ERR_MSG,V_JOB_ID,'结束处理...');
"""
        obj = ProcedureLogModify("p_rpt_cif035")
        out = obj.set_job_step_value_and_modify_insert(proc_cont)
        print(f"out:{out}")
        self.assertEqual(except_out, out)

    def test_modify_procedure_between_report_log(self):
        proc_cont = """V_ERR_MSG       := '100001输入参数[I_RUN_DATE]值为空' ;
      RAISE EX_DEAL ;
    END IF ;

    IF LENGTH(I_RUN_DATE) <> 8 THEN
      V_ERR_MSG       := '100002输入参数[I_RUN_DATE]格式错误(YYYYMMDD),输入格式为:' || I_RUN_DATE ;
      RAISE EX_DEAL ;
    END IF ;

INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'0',V_JOB_NAME,0,V_ERR_MSG,"""
        except_str = """V_ERR_MSG       := '100001输入参数[I_RUN_DATE]值为空' ;
      RAISE EX_DEAL ;
    END IF ;

    IF LENGTH(I_RUN_DATE) <> 8 THEN
      V_ERR_MSG       := '100002输入参数[I_RUN_DATE]格式错误(YYYYMMDD),输入格式为:' || I_RUN_DATE ;
      RAISE EX_DEAL ;
    END IF ;

V_JOB_STEP:=0;
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME,0,V_ERR_MSG,"""
        obj = ProcedureLogModify("p_rpt_cif035")
        out_bool = obj.is_log_exists_and_need_modify(proc_cont)
        # test pass 
        self.assertEqual(True, out_bool)
        
        out1 = obj.set_job_step_value_and_modify_insert(proc_cont)
        print(f"out:{out1}")
        self.assertEqual(except_str, out1)

        out0 = obj.modify_report_log(proc_cont)
        print(f"out:{out0}")
        self.assertEqual(except_str, out0)
        
        out = obj.modify_procedure_between_report_log(proc_cont)
        print(f"out:{out}")
        self.assertEqual(except_str, out)


if __name__ == "__main__":
    unittest.main()
