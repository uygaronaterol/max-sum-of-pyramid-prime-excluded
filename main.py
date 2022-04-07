# Title: Max Sum of Pyramid
# Author: Uygar Onat Erol
# Question:3
# Description: Finding maximum sum of an pyramid input file with these rules below using python as language(Learned python for this 
# question since I heard that taking input file as string is easy at python)
# 1. You will start from the top and move downwards to an adjacent number as in below.
# 2. You are only allowed to walk downwards and diagonally.
# 3. You can only walk over NON PRIME NUMBERS.
# 4. You have to reach at the end of the pyramid as much as possible.
# 5. You have to treat your input as pyramid.
import re
 
 
#Prime check
def is_not_prime(num):
    if num == 1:
        return True
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return True
 
 
#Reading the file and assigning it to array than intarray
f = open("example.txt", "r")
arr = f.read().splitlines()
f.close()
intarr = []
for i in arr:
    intarr.append(re.findall('\d+', i))
 
#Reversing array and making one more array to count the sums of different branches
intarr = intarr[::-1]
length = len(intarr)
resultarr = [[0]*length]*length
start, stop = 0, length
sum = 0
 
#finding the maximum sum with the rules
for i, a in enumerate(intarr[start:stop], start):
    if i != 0:
        for j, item in enumerate(a):
            c = int(intarr[i][j])
            a = int(intarr[i-1][j])
            b = int(intarr[i-1][j + 1])
            d = ((is_not_prime(c) and is_not_prime(a)) or (is_not_prime(c) and is_not_prime(b)))
            e = is_not_prime(c) and not is_not_prime(a)
            h = is_not_prime(c) and not is_not_prime(b)
            if d:
                if e:
                    g = int(resultarr[i - 1][j + 1])
                    resultarr[i][j] = int(c) + max(int(b), int(g))
                    sum = resultarr[i][j]
 
                elif h:
                    f = int(resultarr[i - 1][j])
                    resultarr[i][j] = int(c) + max(int(a), int(f))
                    sum = resultarr[i][j]
 
                else:
                    f = int(resultarr[i - 1][j])
                    g = int(resultarr[i - 1][j + 1])
                    resultarr[i][j] = int(c) + max(int(max(int(a), int(b))), int(max(int(f), int(g))))
                    sum = resultarr[i][j]
 
 
#print the result
print("The maximum sum of the pyramid with rules: %2d" % (sum))
 
