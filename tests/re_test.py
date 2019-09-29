from database.Procedure import Procedure
import unittest
import re
import os
import sys
from os.path import dirname

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)


class ReTest(unittest.TestCase):
    def test_normalize_report_log_insert(self):
        """
        change  INSERT INTO  BAT_REPORT_LOG to INSERT INTO BAT_REPORT_LOG
        use 正则表达式
        """
        line = "INSERT  INTO  BAT_REPORT_LOG (DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)"
        # modify here
        batch_insert_pattern = r'\s*INSERT\s+INTO\s+BAT_REPORT_LOG(.*)'
        if re.search(batch_insert_pattern, line, flags=re.IGNORECASE):
            # logging.debug('deal_with_report_log_blanks')
            line = re.sub(batch_insert_pattern,
                          r'INSERT INTO BAT_REPORT_LOG\1', line, flags=re.IGNORECASE)
        print(line)
        print('test_normalize_report_log_insert end --------------------')

    # def test_re_search1(self):
    #    print('--------------------')
    #    pattern = r'(from|join)\s+(v|rpt)_'
    #    string_list = ['from v_', '\njoin v_...', 'from rpt_',
    #                   'join rpt_', 'FROM V_', 'JOIN V_', 'FROM RPT_', 'JOIN RPT_']
    #    for string in string_list:
    #        search_obj = re.search(pattern, string, flags=re.IGNORECASE)
    #        if search_obj:
    #            # add RPTUSER
    #            print(re.sub(pattern, r'\1 RPTUSER.\2_',
    #                         string, flags=re.IGNORECASE))  #
    #    print('--------------------')

    def test_re_search(self):
        batch_insert_pattern = r'\s*INSERT\s+INTO\s+BAT_REPORT_LOG'
        test_input = ['INSERT INTO BAT_REPORT_LOG',
                      ' INSERT  INTO  BAT_REPORT_LOG', 'insert  into  bat_report_log']
        #self.assertEqual(re_batch_insert.search(test_input[0]), True)
        for string in test_input:
            if re.search(batch_insert_pattern, string, flags=re.IGNORECASE):
                print(re.sub(batch_insert_pattern,
                             'INSERT INTO BAT_REPORT_LOG', string, flags=re.IGNORECASE))  #
                #print(re.sub('class', 'function', 'Class object', flags=re.IGNORECASE))
            else:
                print(string)

    # def test_re_findall(self):
    #    procedure = Procedure('p_rpt_cif032')
    #    proc_cont = procedure.read_proc_cont()
    #    pattern = r"V_JOB_STEP\s*:=\s*\d+;"
    #    job_step_value_list = re.findall(pattern,proc_cont)
    #    print('----------------')
    #    print(job_step_value_list)
    #    pattern.replace()

    def test_str_replace(self):
        a = "abc, abc, bcd, bcd, abc"
        a = a.replace("abc", "def", 1)
        print(a)


if __name__ == "__main__":
    unittest.main()
