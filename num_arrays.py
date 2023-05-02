#  Write a method to determine if a given array of integers contains any duplicate elements.
def has_duplicates(array):
    new_set = set(array)
    return len(new_set) != len(array)


# Write a method that returns the first duplicate item in an array
def first_duplicate(array):
    checked_set = set()
    for i in array:
        if i in checked_set:
            return i
        else:
            checked_set.add(i)
    return -1
