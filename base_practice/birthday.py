keepgoing="y"
while keepgoing=="y":
    birthyear=int(input("Enter year of birth:"))
    while birthyear<1900 or birthyear>2018:
        print("You need to enter a year before 2019 and after 1899.\n")
        birthyear=int(input("Enter another value:"))
    else:
        money=100/(1+0.025)**(2018-birthyear)
        print("$100 in 2018 was worth $",format(money,'.2f'),"in",birthyear,"\n")
    keepgoing=input("Do you want to enter another year(y for yes)?")
