#write a python program to arrange the number to form a maximum number out of it.....

#take numbers as input with space seperation
list=input("Enter the numbers:").split()
print(list)

#sort the input so that it forms in ascending order
list.sort(reverse=True)
print(list)

#this gives the output in list format, but we wanted it in the single number 
#so use join() function to join all elements in the list and form a single number
max ="".join(list)
print("The maximum number formed is",max)