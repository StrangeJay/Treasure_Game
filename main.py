#Draw the boxes for the game 
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

# Ask for the box you want to mark your X
position = input("Where do you want to put the treasure? ")
 
#Convert the input to seperate integers for the column and rows selection 
columns = int(position[1])
rows = int(position[0]) 

# In python indexing starts from 1, so we have to add "-1" to the end of the selection
# to make up for the added 1 when 0 isn't being taken into consideration 
selection = map[columns -1]

# Mark the spot on the row, with X
selection[rows -1] = "X"

# Print the result
print(f"{row1}\n{row2}\n{row3}")

