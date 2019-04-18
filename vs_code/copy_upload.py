import shutil, os
import openpyxl
import pprint
import csv


# copy upload register and upload file

def copyRegister(date_str:str):
    """ copy register """ 
    dir_name = "E:\\svn\\1300_编码\\发布登记表"
    work_tmp = "E:\\yx_walk\\common_sense\\yx_python\\tmp"
    code_bate_path = "E:\\yx_walk\\report_develop\\sky"
    target_path = os.path.join(code_bate_path, date_str+'bate')
    os.makedirs(target_path, exist_ok=True)

    csvFile = open(target_path + '\\登记表'+date_str+'.csv', 'w', newline='')
    csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
    csvWriter.writerow(['所属模块','类型（接口\报表）','程序名称','程序类型（pro\java\\rpt\sql\shell)','SVN存储目录 ','开发负责人','BA负责人','发布日期','mantis id','remarks'])

    for folderName, subfolders, filenames in os.walk(dir_name):
        for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': '+ filename)
            if filename.find(date_str) > -1:
                print(f"today filename: {filename} --------------------------") 
                whole_filename = os.path.join(folderName,filename) 
                # copy excl files
                #shutil.copy(whole_filename, work_tmp)

                # copy excel file content
                wb = openpyxl.load_workbook(whole_filename)
                sheet = wb.get_sheet_by_name('全量报表存储过程')
                countyData = {}
                print('Reading rows...')
                for row in range(2, sheet.max_row + 1):
                # Each row in the spreadsheet has data for one census tract.
                    name = sheet['C' + str(row)].value
                    if not name:
                        continue
                    file_type = sheet['D' + str(row)].value
                    path = sheet['E' + str(row)].value
                    data_list = [sheet[chr(i+ord('A')) + str(row)].value for i in range(0,10)]
                    print(f'date_list:{data_list}')
                    csvWriter.writerow(data_list)
    csvFile.close()


if __name__ == '__main__':
    copyRegister('20190418')
