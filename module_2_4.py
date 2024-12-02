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

print ("Primes: ", primes)
print ("Not_primes: ",not_primes)
