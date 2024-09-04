my_list = ()
print("Empty list: ", my_list)

my_list = [10, 20, 30, 40]
print("After adding values: ", my_list)

my_list.insert(2, 15)
print("After appending 15: ", my_list )

list_2 = [50, 60, 70]
print("list_2: ", list_2)

my_list.extend(list_2)
print("After extending with list_2: ", my_list)

del my_list[-1]
print("After removing the last element: ", my_list)

my_list.sort()
print("Sorting the list in ascending order: ", my_list)

my_list.index(30)
print("Returning index of 30: ", my_list.index(30))
