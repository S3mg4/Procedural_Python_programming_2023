numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_value = 4
sum_of_numbers = sum(numbers[:missing_value]) + sum(numbers[missing_value+1:])
count_of_numbers = len(numbers)
new_element = sum_of_numbers / count_of_numbers
numbers[missing_value]=new_element
print("Измененный список:", numbers)
