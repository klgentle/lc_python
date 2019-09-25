import chardet
import codecs


def convert_file_to_utf8(filename):
    # !!! does not backup the origin file
    content = ""
    with codecs.open(filename, "rb") as f:
        content = f.read()
    source_encoding = chardet.detect(content)["encoding"]
    if not source_encoding:
        print("source_encoding??", filename)
        return
    print(source_encoding, filename)
    # utf8结果字符串是'utf-8'，utf8-bom结果是'UTF-8-SIG'。
    if source_encoding not in ("utf-8", "UTF-8-SIG"):
        content = content.decode(source_encoding, "ignore")  # .encode(source_encoding)
        with codecs.open(filename, "w", encoding="UTF-8-SIG") as f:
            f.write(content)


if __name__ == '__main__':
    #filename = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures\p_rpt_lgr001.sql"
    filename = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures\p_rpt_cif032.sql"
    convert_file_to_utf8(filename)
