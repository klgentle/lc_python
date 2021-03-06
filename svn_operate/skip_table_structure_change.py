def skip_table_structure_change(commit_list):
    """
    如果即写了modify文件，又改了表结构，则不将表结构变更写入登记表
    """
    folder_index = 4
    has_modify = False
    modify_tables = []

    for row in commit_list:
        if row[folder_index].endswith("01Tables\\modify"):
            has_modify = True
        elif row[folder_index].endswith("01Tables"):
            modify_tables.append(row)

    if has_modify and len(modify_tables) > 0:
        # delete row in commit_list
        for row in modify_tables:
            print("Warning, skip row !!!!!!!!!!!!!!!: \n", row)
            commit_list.remove(row)

    return commit_list


if __name__ == "__main__":
    commit_list = [
        [
            "", "报表", "TMP_CIF151_DE_ADDRESSdd", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\01Tables\\modify", "Dongjian", "Gene", "20210112", "", "", "",
        ],
        [
            "", "报表", "TMP_CIF151_DE_Sdd", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\01Tables\\modify", "Dongjian", "Gene", "20210112", "", "", "",
        ],
        [
            "", "报表", "TMP_CIF151_DE_ADDRESS", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\01Tables", "Dongjian", "Gene", "20210112", "", "", "",
        ],
        [
            "CIF", "报表", "p_rpt_cif151", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\05Procedures", "Dongjian", "Gene", "20210112", "", "", "",
        ],
        [ "CIF", "报表", "p_rpt_cif911b", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\05Procedures", "Dongjian", "Gene", "20210112", "", "", "", ],
        [ "CIF", "报表", "RPT_CIF151_D", "rpt", "1000_编辑区\\1300_编码\\1370_水晶报表\\CIF", "Dongjian", "Gene", "20210112", "", "", "", ],
        [ "", "报表", "TMP_CIF151_DE_ADDRikkkESS", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\01Tables", "Dongjian", "Gene", "20210112", "", "", "", ],
        [ "", "报表", "TMP_CIF151_DEddd_ADDRESS", "sql", "1000_编辑区\\1300_编码\\1301_ODSDB\\RPTUSER\\01Tables", "Dongjian", "Gene", "20210112", "", "", "", ],
        [ "CIF", "报表", "RPT_CIF151_D_CSV", "rpt", "1000_编辑区\\1300_编码\\1370_水晶报表\\CSV格式", "Dongjian", "Gene", "20210112", "", "", "", ],
    ]

    print("commit list before delete:")
    for row in commit_list:
        print(row)
    commit_list = skip_table_structure_change(commit_list)
    print("commit list after delete:")
    for row in commit_list:
        print(row)
