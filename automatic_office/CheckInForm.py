from docx import Document
import datetime

import os
import sys
import logging
import re
import time

#logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from automatic_office.Holiday import Holiday


class CheckInForm(object):
    """
    TODO word style
    """
    def __init__(self, year_month: str):
        # date calculate # 2019-07-26 至 2019-08-25
        if len(year_month) != 6:
            print("Please input year_month with format: YYYYMM!")
            sys.exit(1)
        self.__input_year = int(year_month[:4])
        self.__input_month = int(year_month[4:])
        self.__input_day = 25
        self.__date_start = self.calculate_date_start()
        self.__date_end = datetime.date(
            self.__input_year, self.__input_month, self.__input_day)
        self.__work_date_start = self.__date_start.strftime("%Y-%m-%d")
        self.__work_date_end = self.__date_end.strftime("%Y-%m-%d")
        self.__year_month = year_month

    def calculate_date_start(self) -> datetime.date:
        year = self.__input_year
        month = self.__input_month - 1
        day = 26
        if month == 0:
            month = 12
            year -= 1
        return datetime.date(year, month, day)

    #def calculate_date_end(self) -> datetime.date:
    #    year = self.__input_year
    #    month = self.__input_month + 1
    #    day = 25
    #    if month == 13:
    #        month = 1
    #        year += 1
    #    return datetime.date(year, month, day)

    def get_all_nature_date(self) -> list:
        """
        返回所有日期列表
        """
        all_nature_date = []
        from_date = self.__date_start
        while from_date.__le__(self.__date_end):
            all_nature_date.append(from_date)
            from_date += datetime.timedelta(1)

        return all_nature_date

    def get_all_work_date(self) -> list:
        """
        返回所有工作日列表
        """
        all_work_date = [] 
        from_date = self.__date_start
        holiday_obj = Holiday()
        while from_date.__le__(self.__date_end):
            #time.sleep(1)
            # skip holiday
            if not holiday_obj.is_holiday(from_date.strftime("%Y%m%d")):
                all_work_date.append(from_date)
            from_date += datetime.timedelta(1)
            logging.debug("----------------{0}------------".format(
                from_date.strftime("%Y%m%d")))

        return all_work_date

    def check_in_add_table(self, document: object, type: str):
        head_list = ["序号", "日期", "签到时间", "签退时间", "备注"]
        table = document.add_table(rows=1, cols=len(head_list))
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = head_list[0]
        hdr_cells[1].text = head_list[1]
        hdr_cells[2].text = head_list[2]
        hdr_cells[3].text = head_list[3]
        hdr_cells[4].text = head_list[4]
        date_str_list = []
        if type.lower() == "normal":
            date_list = self.get_all_work_date()
        elif type.lower() == "overtime":
            date_list = self.get_all_nature_date()

        for ind, date in enumerate(date_list):
            row_cells = table.add_row().cells
            row_cells[0].text = str(ind+1)
            row_cells[1].text = date.strftime("%Y-%m-%d")
            row_cells[2].text = ""
            row_cells[3].text = ""
            row_cells[4].text = ""
        return table

    def write_form(self, form_type: str):
        form_type_name_dict = {
            "overtime": "带加班",
            "normal": "正常"
        }
        document = Document(r'automatic_office\文思员工-签到表_{0}_template.docx'.format(
            form_type_name_dict.get(form_type)))
        document.add_paragraph('姓名： 					  日期：{} 至 {}'.format(
            self.__work_date_start, self.__work_date_end))

        table = self.check_in_add_table(document, form_type)
        document.save(r'automatic_office\{0}文思员工-签到表_{1}.docx'.format(
            self.__year_month, form_type_name_dict.get(form_type)))
        logging.info("Done!")


if __name__ == "__main__":
    obj = CheckInForm("201908")
    obj.write_form('overtime')
    obj.write_form('normal')
