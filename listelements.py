my_list=[]
num_elements=int(input("How many elements do you want to enter?"))
for i in range(num_elements):
    element=input(f"Enter elemnt {i+1}:")
    my_list.append(element)
print(my_list)