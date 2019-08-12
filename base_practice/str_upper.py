#str = input("Enter sentence to be capitalized:")
str = "Enter sentence to be capitalized. kllsk. lsldk. kklsdl. kkk Ull."

str_list = str.split('. ')
for i in range(0,len(str_list)):
    a=str_list[i]
    str_list[i]=a[0].upper()+a[1:]
    
str2='. '.join(str_list)
print(str2)
