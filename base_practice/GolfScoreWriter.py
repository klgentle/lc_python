def main():
    """
    代码修改记录：
    1、删除count=0, count+=1不需要赋值，count是变量，它的值在range里
    2、golf.file改为golf_file
    3、删除所有的,sep='', sep在的话，无法input
    4、input 修改，不能有多个,
    5、wirte修改为write,单词写错
    """
    num=int(input("Enter number of players:"))
    golf_file=open('golf.txt','w')
    for count in range(1,num+1):
        name=input("Enter name of player number {}:".format(count))
        score=input(f"Enter score of player number {count}:")
        golf_file.write(str(name)+"\n")
        golf_file.write(str(score)+"\n")
    golf_file.close()
 
main()
