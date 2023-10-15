numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = numbers[:4] + numbers[5:]
summary = sum(numbers_without_none)
count = len(numbers_without_none) + 1
average = summary / count


numbers[4] = average

print("Измененный список:", numbers)
