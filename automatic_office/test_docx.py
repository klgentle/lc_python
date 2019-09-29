import unittest
import docx

class TestDocx(unittest.TestCase):
    def test_para_run(self):
        doc = docx.Document('文思员工-8月签到表_新模版_带加班.docx')        
        print(len(doc.paragraphas))

    

if __name__ == "__main__":
    unittest.main()