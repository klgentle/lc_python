import collections
import re
from docxtpl import DocxTemplate
tpl = DocxTemplate('test.docx')


sd = tpl.new_subdoc()
sd.add_paragraph('Drug Table :')
rows = 2
cols = 4
table = sd.add_table(rows=rows, cols=cols, style='Style1')

# header
cells = table.rows[0].cells
cells[0].text = "Gene"
cells[1].text = "Drug"
cells[2].text = "Rank"
cells[3].text = "Description"


table.cell(1, 0).text = "ALK"
table.cell(1, 1).text = "GENE1"
table.cell(1, 2).text = "GENE2"
table.cell(1, 3).text = "haha"


context = {
    'mysubdoc': sd,
}

tpl.render(context)
tpl.save('path/test.docx')
# 原文链接：https://blog.csdn.net/weixin_42670653/article/details/89670975
