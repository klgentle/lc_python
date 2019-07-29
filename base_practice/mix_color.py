colors = input("Enter primary color:")
colors2 = input("Enter primary color:")
primary_colors = [colors, colors2] 
if "red" in primary_colors and "blue" in primary_colors:
    print(f"When you mix {colors} and {colors2}, you get purple.")
elif "red" in primary_colors and "yellow" in primary_colors:
    print(f"When you mix {colors} and {colors2}, you get orange.")
elif "blue" in primary_colors and "yellow" in primary_colors:
    print(f"When you mix {colors} and {colors2}, you get green.")
else:
    print("You didn't input two primary colors.")
