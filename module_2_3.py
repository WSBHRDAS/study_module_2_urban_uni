my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 15]

my_l_num = 0

my_l_value = my_list[my_l_num]

my_l_len = len(my_list) - 1  #длина списка, начиная с 0 (нуля)

if my_l_value < 0 :
    print("Первый же элемент со значением меньше 0: ", my_l_num + 1, "-й = ",my_l_value)
else:
    while my_l_num <= my_l_len:

        print(my_l_value)
        if my_l_num != my_l_len :
            my_l_num = my_l_num + 1
            my_l_value = my_list[my_l_num]

        if my_l_value < 0:
            print("Закончен вывод значений списка до элемента со значением меньше 0: ", my_l_num + 1, "-й = ",
                  my_l_value)
            break
        else:
            if my_l_num == my_l_len :
                print (my_list[my_l_num])
                print("Все элементы списка положительные")
                break
