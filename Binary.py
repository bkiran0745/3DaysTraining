'''1.Alex gives you a positive integer N and wants you to rearrange 
the bits of the number in its binary representation such that all 
set bits are in consecutive order. Your task is to find the min possible 
number that can be formed after re-arranging the bits of the number.'''
#input  10
#output 2

#1st method

def mi(N):
    c = bin(N).count('1')
    min_v = (1<<c) - 1
    return min_v
n = int(input())
res = mi(n)
print(res)

#2nd method

n = int(input())
b = str(bin(n))[2:]
str0 = "";str1=""
for i in b:
    if i == "0":
        str0+=i
    else:
        str1+=i
res = str0+str1
k = 0;sum=0;i=len(res)-1
while i>=0:
    sum += int(res[i])*(2**k)
    k+=1;i-=1
print(sum)
print(int(res,2))

'''Alice has collection of songs represented as string S where 
each character represents a song. A playlist is the substring of 
the givenstring with exactly k number of songs. She wants to create 
a playlist that contains max number of her favourite song which is 
'a'. Your task is to find and return an integer value representing 
the max number of favourite songs that she get in single playlist

Input1: 
abcaca
3
output1: 2
Input2: 
defghugf
3
Output2: 0
'''

s = input()
n = int(input())
max = 0
for i in range(len(s)-n+1):
    c = s[i:i+n].count('a')
    if c > max:
        max = c
print(max)

'''Write a function that accepts an integer array 'arr' of size nas 
its argument. The function needs to return the index of an equilibrium 
point in the array, where the sum of elements on the left of the index 
is equal to the sum of elements on the right of the index. If no such 
point exists return -1.

Input: 7            Input: 3           
-7 1 5 2 -4 3 0           1 2 3
Output: 3           Output: -1
'''
n = int(input())
l = list(map(int,input().split()))
i = n//2
print(i)
id = -1
while i < n and i >= 0:
    if sum(l[:i]) == sum(l[i:]):
        id = i
        break
    if sum(l[:i]) < sum(l[i:]):
        i -= 1
    elif sum(l[:i]) > sum(l[i:]):
        i += 1
print(id)
