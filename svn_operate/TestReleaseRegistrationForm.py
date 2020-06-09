import openpyxl
import unittest
from ReleaseRegistrationForm import ReleaseRegistrationForm

class TestReleaseRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.reg = ReleaseRegistrationForm('20200609','','cif')
        self.__registration_file  = r'/mnt/e/svn/ODS程序版本发布登记表cif-test-20200609.xlsx'

    def test_1__getRowNumOfData(self):
        wb = openpyxl.load_workbook(self.__registration_file)
        sheet = wb.active
        num = self.reg._ReleaseRegistrationForm__getRowNumOfData(sheet)
        assert(num == 225)

    def test_2__deleteSheetBlankRow(self):
        wb = openpyxl.load_workbook(self.__registration_file)
        sheet = wb.active
        self.reg._ReleaseRegistrationForm__deleteSheetBlankRow(sheet)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

