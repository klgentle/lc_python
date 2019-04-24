import openpyxl
import shutil, os
import time
from pprint import pprint

SVN_DIR = '/mnt/e/svn/1300_编码/'
SVN_LOG = '/mnt/e/svn/commit.log'


class Solution:
    def __init__(self):
        # copy template change excel name 
        self.regi_dir = os.path.join(SVN_DIR,'发布登记表','支付')

        file1 = os.path.join(self.regi_dir, 'ODS程序版本发布登记表(支付) -template.xlsx')
        date_str = time.strftime("%Y%m%d", time.localtime())
        date_str2 = time.strftime("%Y-%m-%d", time.localtime())
        self.file2 = os.path.join(self.regi_dir, f'ODS程序版本发布登记表(支付) -{date_str}.xlsx')
        #print(f"file2:{file2}")
        if not os.path.exists(self.file2):
            shutil.copy(file1,self.file2)

        self.comit_list = []
        self.commit_list_head = ['支付','报表']
        self.commit_list_end = ['DONGJIAN','DEVIL',date_str2,'TODO']

    def logRead(self):
        svn_log = open(SVN_LOG)
        for line in svn_log.readlines():
            if line.startswith('Sending'):
                path_file = line.split('        ')[1]
                path_list = path_file.split('/')
                #print(f"path_list:{path_list}")
                path = "/".join(path_list[:-1])
                path = '1000_编辑区/'+path
                file_list = path_list[-1].split('.')
                #print(f"file_list:{file_list}")
                file_name = file_list[0]
                file_type = file_list[-1].replace('\n','')
                row = self.commit_list_head + [file_name, file_type, path] + self.commit_list_end
                #print(f"row:{row}")
                self.comit_list.append(row)

        svn_log.close()
        #pprint(self.comit_list)    

    def logRegister(self):
        wb = openpyxl.load_workbook(self.file2)
        sheet = wb.active

        num = 0  
        print(f'{self.file2}')
        for row in range(2, sheet.max_row + 1):
            file_name = sheet['C' + str(row)].value
            if file_name:
                num += 1 
            else:
                break
        print(f"num:{num}")
        sheet.delete_rows(row+1, sheet.max_row - num)

        #print(f"max_row{sheet.max_row}")
        # TODO to write after the record from the top
        for i in self.comit_list:
            sheet.append(i)

        wb.save(filename=self.file2)


if __name__ == '__main__':
    a = Solution()
    a.logRead()
    a.logRegister()
    # todo date input
