import re 


def test_re_search():
    #        search_obj = re.search(pattern, string, flags=re.IGNORECASE)
    view_pattern = r"V_\w*_ALL"
    string1 = "V_DEAL_DATE,'FH00',T1.CCY,T1.OD_ALL"
    string2 = "V_ACCOUNT_M_ALL"
    if re.search(view_pattern, string1, flags=re.IGNORECASE) :
        print(f"{string1} fond")
    else:
        print(f"{string1} not find")

    if re.search(view_pattern, string2, flags=re.IGNORECASE) :
        print(f"{string2} fond")
    else:
        print(f"{string2} not find")



if __name__ == "__main__":
    test_re_search()
