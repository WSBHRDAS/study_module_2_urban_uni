print ("*** Подсчет количества одинаковых чисел из 3-х введенных ***")

ch1 = int(input ("Введите число 1 (первое): "))
ch2 = int(input ("Введите число 2 (второе): "))
ch3 = int(input ("Введите число 3 (третье): "))

if ch1 == ch2 and ch2 == ch3 :
    print("Все 3 (три) числа идентичны")
elif ch1 == ch2 or ch2 == ch3 or ch1 == ch3 :
    print("2 (два) числа идентичны")
else:    print("0 (нет) идентичных чисел ")
