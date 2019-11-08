import time
import sys
import os
import re
import logging

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
# 导入模块
from database.convert_file_to_utf8 import convert_file_to_utf8
from string_code.StringFunctions import StringFunctions
from decorator_test.logging_decorator import logging_begin_end

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# define constant variable
AND_DATA_AREA_PATTERN = r"\sAND\s+(\w*.)?DATA_AREA"
ON_DATA_AREA_PATTERN = r"\sON\s+(\w*.)?DATA_AREA"
WHERE_DATA_AREA_PATTERN = r"WHERE\s+(\w*.)?DATA_AREA"


class ProcedureTypeError(TypeError):
    pass


class ProcedureValueError(ValueError):
    pass


class Procedure(object):
    """ procedure deal with path, procedure file name 
    use re.sub(pattern, repl, string, flags=re.IGNORECASE) instead of str.replace()
    """

    def __init__(self, proc_name: str):
        #self.__procedure_path = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures"
        # svn bak path
        self.__procedure_path = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\98Procedures_bak_20191016"
        self.__proc_name = proc_name
        # raise error
        if not os.path.exists(
            os.path.join(self.__procedure_path, self.get_file_name())
        ):
            raise ValueError("Procedure name is incorrect!")
        self.file_to_utf8()
        self.add_schema()
        self.__date_str = time.strftime("%Y%m%d", time.localtime())
        self.__note = "-- DONGJIAN {} ".format(self.__date_str)
        # self.modify_proc_by_line()
        # skip no need
        # self.delete_no_used_code()

    def file_to_utf8(self):
        return convert_file_to_utf8(
            os.path.join(self.__procedure_path, self.get_file_name())
        )

    def get_file_name(self) -> str:
        return self.__proc_name + ".sql"

    def add_schema(self):
        """ CHANGE FROM V_, JOIN V_ TO FROM RPTUSER.V_, JOIN RPTUSER.V_ """
        proc_cont = self.read_proc_cont()
        pattern = r"(from|join)\s+(v|rpt)_"
        search_obj = re.search(pattern, proc_cont, flags=re.IGNORECASE)
        if search_obj:
            # add RPTUSER
            proc_cont = re.sub(
                pattern, r"\1 RPTUSER.\2_", proc_cont, flags=re.IGNORECASE
            )
            self.write_procedure(proc_cont)

    # @logging_begin_end
    def delete_no_used_code(self):
        """  """
        proc_cont = self.read_proc_cont()
        pattern = r"--\s*-V_SPEND_TIME\s*:=\s*V_END_TIME\s*-\s*V_ST_TIME ;(----执行时间)?"
        search_obj = re.search(pattern, proc_cont, flags=re.IGNORECASE)
        if search_obj:
            proc_cont = re.sub(pattern, r"", proc_cont, flags=re.IGNORECASE)
            self.write_procedure(proc_cont)

    @staticmethod
    def split_line_with_two_and(line: str):
        """more than one AND to add \n
            ON B1.ID = B3.ID AND B1.DATA_AREA = B3.DATA_AREA AND B1.DATA_DATE = B3.DATA_DATE
        """
        find_list = re.findall(r" AND ", line)
        if len(find_list) > 1:
            line_strip = line.strip()
            # do not split and "between add"
            if re.search("BETWEEN", line, flags=re.IGNORECASE):
                return line
            # deal with AND C.M = 1 AND C.S = 1
            if re.search(
                r"(\w*.)?M\s*=\s*(')?1(')?\s*AND\s+(\w*.)?S\s*=\s*(')?1(')?",
                line,
                flags=re.IGNORECASE,
            ):
                return line
            line = line.upper()
            if not line_strip.startswith("--") and not line_strip.startswith("WHEN"):
                line_obj = StringFunctions(line)
                second_position = line_obj.find_the_second_position(" AND ")
                logging.info("split line with two add")
                line = line_obj.str_insert(second_position, "\n")
        return line

    @staticmethod
    def delete_blank_of_job_step(line: str) -> str:
        job_step_pattern = r"\s*V_JOB_STEP\s*:=\s*(\d)+\s*;\s*"
        if re.search(job_step_pattern, line, flags=re.IGNORECASE):
            line = re.sub(
                job_step_pattern, r"V_JOB_STEP:=\1;\n", line, flags=re.IGNORECASE
            )
        return line

    # @logging_begin_end
    def modify_proc_by_line(self):
        proc_cont_list = []
        proc_file_name = self.get_file_name()
        with open(
            os.path.join(self.__procedure_path, proc_file_name), "r", encoding="UTF-8"
        ) as pro:
            proc_cont_list = pro.readlines()
        logging.info("modify proc by line")
        for i in range(0, len(proc_cont_list)):
            line = proc_cont_list[i]
            proc_cont_list[i] = self.split_line_with_two_and(line)
            # no need
            # proc_cont_list[i] = self.delete_blank_of_job_step(line)

        self.write_procedure("".join(proc_cont_list))

    def write_procedure(self, proc_cont: str):
        proc_file_name = self.get_file_name()
        with open(
            os.path.join(self.__procedure_path, proc_file_name), "w", encoding="UTF-8"
        ) as pro:
            pro.write(proc_cont)

    def read_proc_cont(self) -> str:
        proc_cont = ""
        proc_file_name = self.get_file_name()
        with open(
            os.path.join(self.__procedure_path, proc_file_name), "r", encoding="UTF-8"
        ) as pro:
            proc_cont = pro.read()  # .upper()
        return proc_cont

    @logging_begin_end
    def replace_view_with_table(self, view_dict: dict):
        proc_cont = self.read_proc_cont()
        for view, table in view_dict.items():
            view_pattern = r"(RPTUSER.)?{}".format(view)
            proc_cont = re.sub(view_pattern, table, proc_cont, flags=re.IGNORECASE)
        self.write_procedure(proc_cont)

    @staticmethod
    def data_area_check(line: str) -> bool:
        line = line.upper()
        if (
            not line.strip().startswith("--")
            and line.find("DATA_AREA") > -1
            and (
                re.search(AND_DATA_AREA_PATTERN, line, re.IGNORECASE)
                or re.search(ON_DATA_AREA_PATTERN, line, re.IGNORECASE)
                or re.search(WHERE_DATA_AREA_PATTERN, line, re.IGNORECASE)
            )
        ):
            return True
        return False

    @staticmethod
    def add_header_log(proc_cont: str, modify_content="log modify") -> str:
        """添加起始位置的log登记
        如：  V1.0   20180515 HASON       1.ADD SCHEMA
        """
        date_str = time.strftime("%Y%m%d", time.localtime())
        header_log = "  V2.0  {0} \tdongjian    {1}\n".format(date_str, modify_content)
        log_end = "+===================="
        if proc_cont.find(log_end) > -1:
            proc_cont = proc_cont.replace(log_end, header_log + log_end)
        return proc_cont

    def write_header_log(self, modify_content="log modify") -> None:
        """将添加头部log登记的内容写入文件
        """
        proc_cont = self.add_header_log(self.read_proc_cont(), modify_content)
        self.write_procedure(proc_cont)

    def data_area_replace(self, line: str) -> str:
        """ 
            按行读取，如果出现了 ON DATA_AREA, AND DATA_AREA, WHERE DATA_AREA,则进行替换，添加--
            ON, WHERE ->  ON 1=1 -- OR WHERE 1=1 -- 
            AND -> -- AND 
            ) -> \n)
        """
        try:
            if self.data_area_check(line):
                line = self.add_header_log(line, "data_area replace")
                logging.debug("data_area处理")
                line = line.upper()
                if re.search(AND_DATA_AREA_PATTERN, line, re.IGNORECASE):
                    line = re.sub(AND_DATA_AREA_PATTERN, r" --AND \1DATA_AREA", line)
                elif re.search(ON_DATA_AREA_PATTERN, line, re.IGNORECASE):
                    line = re.sub(ON_DATA_AREA_PATTERN, r" ON 1=1 --\1DATA_AREA", line)
                elif re.search(WHERE_DATA_AREA_PATTERN, line, re.IGNORECASE):
                    line = re.sub(
                        WHERE_DATA_AREA_PATTERN, r"WHERE 1=1 --\1DATA_AREA", line
                    )

                # replace line end
                if line.find(")") > -1:
                    line = line.replace(")", "\n)")
                if line.find(";") > -1:
                    line = line.replace(";", "\n;")
                if line.find("*/") > -1:
                    line = line.replace("*/", "\n*/")
                # delete line
                if line.count("\n") <= 1 and line.strip().startswith("--"):
                    line = ""
                else:
                    # line add note in the end
                    line = "".join([line[:-1], self.__note, "\n"])
        except:
            logging.error(f"line deal failed, line: {line}")

        return line

    @logging_begin_end
    def data_area_deal(self):
        """处理data_area """
        proc_cont_list = []
        proc_file_name = self.get_file_name()
        with open(
            os.path.join(self.__procedure_path, proc_file_name), "r", encoding="UTF-8"
        ) as pro:
            proc_cont_list = pro.readlines()
        proc_cont_list = [item for item in proc_cont_list]  # item.upper()
        for index, line in enumerate(proc_cont_list):
            proc_cont_list[index] = self.data_area_replace(line)

        self.write_procedure("".join(proc_cont_list))


if __name__ == "__main__":
    # proc = Procedure('p_rpt_cif022')
    proc = Procedure("p_rpt_cif063")
    # proc.modify_proc_by_line()
    proc.add_schema()
