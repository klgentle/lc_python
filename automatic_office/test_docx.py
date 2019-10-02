import unittest
import docx


class TestDocx(unittest.TestCase):
    def test_para_run(self):
        doc = docx.Document('automatic_office/文思员工-8月签到表_新模版_带加班.docx')
        # print(len(doc.paragraphs))
        # for ind, content in enumerate(doc.paragraphs):
        #    print(f"{ind}: {content.text}")

        for table in doc.tables:
            # print 第二列的内容，包括表头
            for cell in table.column_cells(1):
                print(cell.text)


if __name__ == "__main__":
    unittest.main()
