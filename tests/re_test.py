import unittest
import re
import os
import sys
from os.path import dirname

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from database.Procedure import Procedure

class ReTest(unittest.TestCase):
    
    #def test_re_search(self):
    #    batch_insert_pattern = r'\s*INSERT\s+INTO\s+BAT_REPORT_LOG'
    #    test_input = ['INSERT INTO BAT_REPORT_LOG', ' INSERT  INTO  BAT_REPORT_LOG', 'INSERT  INTO  BAT_REPORT_LOG']
    #    #self.assertEqual(re_batch_insert.search(test_input[0]), True)
    #    for string in test_input:
    #        if re.search(batch_insert_pattern, string):
    #            print(re.sub(batch_insert_pattern,'INSERT INTO BAT_REPORT_LOG',string))  #, flags=re.IGNORECASE
    #        else:
    #            print(0)

    #def test_re_findall(self):
    #    procedure = Procedure('p_rpt_cif032') 
    #    proc_cont = procedure.read_proc_cont()
    #    pattern = r"V_JOB_STEP\s*:=\s*\d+;"
    #    job_step_value_list = re.findall(pattern,proc_cont)
    #    print('----------------')
    #    print(job_step_value_list)
    #    pattern.replace()

    def test_str_replace(self):
        a = "abc, abc, bcd, bcd, abc"
        a = a.replace("abc","def", 1)
        print(a)

    
if __name__ == "__main__":
    unittest.main()