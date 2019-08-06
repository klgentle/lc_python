def main():
    """
    num -> nums, 变量区分开来，不要混用了
    ave should not in cycle
    """
    nums=int(input("Enter the number of assets:"))
    portfolio=0.00
    try:
        record_file=open('record.txt','w')
        for num in range(1,nums+1):
            print("****** For asset",num,"******")
            name=str(input("Enter the name of the asset:"))
            while not name[0].isalpha():
                print("Asset name must start with a letter!")
                name=str(input("Enter the name of the asset:"))
            value=input("Enter the value of the asset:")
            while not value.isdigit():
                print("Asset value must be a number!")
                value=input("Enter the value of the asset:")
            value = int(value)
            portfolio+=value
            record_file.write(str(name)+"\n")

        record_file.close()
        ave=portfolio/nums
        print("The portfolio has the following",nums,"assets:")
        record_file=open('record.txt','r')
        name = record_file.readline() 
        while name !='':
            print(name,"\n\n\n",sep='')
            name = record_file.readline() 
        record_file.close()

        print("The portfolio is worth $",format(portfolio,',.2f'))
        print("The average of the asset is $",format(ave,'.2f'))
        
    except ValueError:
        print("Asset name must start with a letter!")
        print("Asset value must be a number!")

main()
