# LIST_ = {'od' : '1a', 'dv': '2b', 'tr': '33'}
#
#
# for i, k in LIST_.items():
#     print (i, k)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

num_ch = 0  # числитель
num_zn = 0  # знаменатель
ch_zn = 0   #соотношение числителя и знаменателя
num_neprostoe = False #найдено непростое число
primes = []
not_primes =[]

for i in range(len(numbers)) :
    num_ch = numbers[i]
    num_neprostoe = False  # сбрасываем

    if  num_ch > 1:

        for k in range(1,i) :
            num_zn = numbers[k]
            if num_ch % num_zn == 0:
                num_neprostoe = True
                break
            else :
                num_neprostoe = False
                continue

        if num_neprostoe == True :
            not_primes.append(num_ch)
        else :
            primes.append(num_ch)

        #print (num_ch, "  ", num_zn, "  Neprostoe: ", num_neprostoe)

             #   if

            # num_zn = numbers [k]
            #
#
#                     if num_ch % num_zn != 0 :
#                         print("Найдено простое число:", num_ch)
#                         num_neprostoe = False  # найдено непростое число
#
#                     else:
#                         print("Найдено не простое (составное число):", num_ch)
#                         not_primes.append(num_ch)
#                         num_neprostoe = True  # найдено непростое число
#                         break
#                     print(num_ch, " num_zn: ", num_zn)
#                     primes.append(num_ch)
#                     break
#                     num_neprostoe = False
#
print ("Primes: ", primes)
print ("Not_primes: ",not_primes)
#
#
