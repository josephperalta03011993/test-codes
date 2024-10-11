def main():
    
    # LOOP
    # Count from zero to nine by one.
    #for i in range(10):
    #    print(i)
    
    # Count from five to nine by one.
    #for i in range(5, 10):
    #    print(i)

    # Count from zero to eight by two.
    #for i in range(0, 10, 2):
    #    print(i)

    # Count from 100 down to 70 by three.
    #for i in range(100, 69, -3):
    #    print(i)

    # Create a list of color names.
    colors = ["red", "yellow", "blue"]

    # Create a list of color names.
    for color in colors:
        print(color)
    print() # print empty line

    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        color = colors[i]
        print(color)

    print()
    # BREAK
    sum = 0
    for i in range(10):
        number = float(input("Please input a number: "))
        if number == 0:
            break
        sum += number
    print(f"Sum: {sum}")

    # WHILE LOOP
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]

    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")

    # variable and reference 
    # a reference does not copy the value, but rather
    # references to the same list
    list_one = [1,2,3]
    list_two = list_one
    print(f"List 1: {list_one} \nList 2: {list_two}")
    list_one.append(4)
    print(list_two)

def compare_lists(list1, list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.
    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)
    # Begin at the first index (0) and repeat until the
    # computer finds two elements that are not equal or
    # until the computer reaches the end of the shortest
    # list, whichever comes first.
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]
        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break
        # Add one to the index variable.
        i += 1
    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1
    return i

# COMPOUND LIST (list inside a list)
# These are the indexes of each
# element in the inner lists.
YEAR_PLANTED_INDEX = 0
HEIGHT_INDEX = 1
GIRTH_INDEX = 2
FRUIT_AMOUNT_INDEX = 3
# Create a compound list that stores inner lists.
apple_tree_data = [
    # [year_planted, height, girth, fruit_amount]
    [2012, 2.7, 3.6, 70.5],
    [2012, 2.4, 3.7, 81.3],
    [2015, 2.3, 3.6, 62.7],
    [2016, 2.1, 2.7, 42.1]
]
# Retrieve one inner list from the compound list.
one_tree = apple_tree_data[2]
# Retrieve one value from the inner list.
height = one_tree[HEIGHT_INDEX]
# Print the tree's height.
print(f"height: {height}")

if __name__ == "__main__":
    main()