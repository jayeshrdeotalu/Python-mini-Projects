import random
name_int = input("Enter the names who gonna pay:")
sep_name = name_int.split()
n = len(sep_name)
ran = random.randint(0, n-1)
print(f"The person who gonna pay is {sep_name[ran]}")
