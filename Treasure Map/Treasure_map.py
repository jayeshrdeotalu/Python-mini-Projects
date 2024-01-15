row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

mapping = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Enter the two digit number where you want to enter the 'x'")
map_in = input("First number is row and second is column")
row = int(map_in[0])
column = int(map_in[1])

mapping[row-1][column-1] = "x"
print(f"{row1}\n{row2}\n{row3}")
