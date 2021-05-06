def compare(a,b):
    if a[0] == b[0]:
        return b[1] - a[1]
    return a[0] - b[0]
 
# 列表
envelopes = [[5,4],[6,4],[6,7],[2,3]]
 
# 指定第二个元素排序
envelopes.sort(key=compare)
print(envelopes)
