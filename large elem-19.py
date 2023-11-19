def find_largest_element(lst):
    if not lst:
        return None 
    largest = lst[0] 
    for num in lst:
        if num > largest:
            largest = num  
    return largest

# Example list
my_list = [3, 12, 45, 7, 23, 56, 8]
result = find_largest_element(my_list)
print("The largest element in the list is:", result)
