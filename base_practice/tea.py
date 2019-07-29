resugar=1.5
rebutter=1
reflour=2.75
recookies=48
num_cookies=int(input("Enter number of cookies:"))
sugar_needed=(resugar/48)*num_cookies
butter_needed=(rebutter/48)*num_cookies
flour_needed=(reflour/48)*num_cookies
print("You need",format(sugar_needed,'.2f'),"cups of sugar,",format(butter_needed,'.2f'),"cups of butter,",format(flour_needed,'.2f'),"cups of flour.")
