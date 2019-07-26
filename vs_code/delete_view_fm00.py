import os

view_path = "/home/kl/svn/1300_编码/1301_ODSDB/RPTUSER/03Views"
new_path = "/home/kl/yx_walk/new_views"
#for folderName, subfolders, filenames in os.walk(path):
for file_name in os.listdir(view_path):
    one_file = os.path.join(view_path,file_name)
    content = ""
    with open(one_file) as f:
        content = f.read().upper()

    # test
    #if content.find('V_CHB_H_BLACKLIST_CUSTOMER_ALL') == -1:
    #    continue

    content = content.replace(';','').strip()
    # skip no FM00 views
    if content.find("'FM00'") == -1:
        continue

    # data deal
    select_ind = content.find('SELECT')
    head = content[:select_ind]
    # UNION ALL may be not stand
    selects = content[select_ind:].split('UNION ALL')
    if content.find("UNION ALL") == -1:
        selects = content[select_ind:].split('UNION')
    medium = ""
    if selects[0].find("'FH00'") > 0:
        medium = selects[0]
    else:
        medium = selects[1]
    
    # wirte file
    new_view = os.path.join(new_path,file_name)
    new_f = open(new_view,'w')
    new_f.write(head)
    new_f.write(''.join([medium,';\n']))
    new_f.close
