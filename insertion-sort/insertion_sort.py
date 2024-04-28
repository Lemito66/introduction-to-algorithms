def insertion_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        j = i
        while j > 0 and list_of_numbers[j-1] > list_of_numbers[j]:
            list_of_numbers[j -1], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[j-1]
            j -= 1
    return list_of_numbers


print(insertion_sort([5, 2, 4, 6, 1, 3]))  # [1, 2, 3, 5, 6]
