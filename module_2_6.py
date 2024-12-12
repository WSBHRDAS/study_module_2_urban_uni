print ("Слишком древний шифр")
print ("--------------------")

ryad_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

ryad_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

str1 = ""
str2 = ""

for c3_20 in range (len(ryad_1)) :
    str2 = ""
    str1 =  str(ryad_1[c3_20])
    print (str1," :")
    for i in range (len(ryad_2)) :
        for j in range (len(ryad_2)) :
            if j > i :
                if (ryad_1[c3_20]) % (i+j+2) == 0 :
                    str2 += str(i+1)+str(j+1)+","
                    # print(str2)
    print (str2)