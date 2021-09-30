# Create a Python list to store your grocery list
Shopping = ["Milk","Bread","Eggs","Peanut Butter","Jelly"]

# Print the grocery list
print(Shopping)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
X=Shopping.index("Peanut Butter")
Shopping[X]="Almond Butter"
print(Shopping)

# Remove "Jelly" from grocery list and print out the updated list
Shopping.remove("Jelly")
Shopping.pop(0)
print(Shopping)
Shopping.insert(0,"Milk")
Shopping.append("Almond Butter")
print(Shopping)

# Add "Coffee" to grocery list and print the updated list
Shopping.append("Coffee")
print(Shopping)

