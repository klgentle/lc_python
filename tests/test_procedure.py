import unittest
import os
import sys
from os.path import dirname

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from database.Procedure import Procedure


class TestProcedure(unittest.TestCase):
    def test_deal_with_report_log_blanks(self):
        a = Procedure('p_rpt_cif035')
        line1 = " INSERT  INTO  BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        line2 = " INSERT INTO    BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        line3 = "INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        except_line = "INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        self.assertEqual(a.deal_with_report_log_blanks(line1), except_line)
        self.assertEqual(a.deal_with_report_log_blanks(line2), except_line)
        self.assertEqual(a.deal_with_report_log_blanks(line3), except_line)

    def test_deal_with_report_log_blanks2(self):
        a = Procedure('p_rpt_cif035')
        line1 = "(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        self.assertEqual(a.deal_with_report_log_blanks(line1), line1)
        
if __name__ == "__main__":
    unittest.main()