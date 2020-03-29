import re


def test_re_pattern():
    # 正则表达需要强化，太弱了！！！

    text = "https://qpix.com;http://85.117.234.129"
    p = re.compile("(https://qpix.com|http://85.117.234.129)")
    tempList = re.findall(p, text)
    print(tempList)


test_re_pattern()
