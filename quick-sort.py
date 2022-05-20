#Quick sort practice from Udacity course "Data Structures and Algorithms in Python"
#Input a list and output a sorted list

def quicksort(array):
    check = 0
    pivot = len(array)-1-check
    while pivot != check:
        if array[pivot] < array[check]:
            array.insert(pivot+1,array[check])
            pivot -= 1
            print(array)
            array.pop(check)
            print(array)
            array.insert(check,array[pivot-1])
            array.pop(pivot)
            print(array)
        else:
            pivot -= 1
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
#      [21, 4, 1, 3, 9, 20, 25, 6, 14, 21]
#      [6, 4, 1, 3, 9, 20, 25, 14, 21, 21]
print quicksort(test)