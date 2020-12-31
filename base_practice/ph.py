print(f"please input ph value:")
ph=float(input())
print(f"input:{ph}")
if ph<7.0:
   neutral=0;base=0;acid=1
elif ph>7.0:
   neutral=0;base=1;acid=0
elif ph==7.0:
   neutral=1;base=0;acid=0

print(f"neutral={neutral};base={base};acid={acid}")
