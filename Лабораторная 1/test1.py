numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = numbers.index(None)
stroka1 = numbers[:index]
stroka2 = numbers[index+1:]
sum_strok = stroka1+stroka2
srednee_arifm = sum(sum_strok)/len(numbers)
numbers[index] = srednee_arifm
print("Измененный список:", numbers)
