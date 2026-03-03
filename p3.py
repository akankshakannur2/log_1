# Write a program to obtain the minimum number from the entered list of 

#create a list variable to take input from the user
list=input("enter the numbers:")

#seperate the list item with comma to form a proper list format
n_list=list.split()
print(n_list)

#sort the list in ascending format 
n_list.sort(reverse=False)
print(n_list)

#now the output is in list format till now, join all list element to create a single number out off
minimum = "".join(n_list)
print("the smallest number obtained:",minimum)


