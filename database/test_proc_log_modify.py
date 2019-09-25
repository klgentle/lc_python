import unittest
from ProcedureLogModify import ProcedudreLogModify


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
        obj = ProcedudreLogModify('p_rpt_cif032')
        out = obj.set_job_step_value(proc_cont)
        print(f"out:{out}")
        self.assertEqual(except_out, out)


if __name__ == '__main__':
    unittest.main()