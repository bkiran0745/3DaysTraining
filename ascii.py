#A-Z = 65 to 90
#a-z = 97 to 122
# py me:
# ord(char) --> gives ascii value of the char
# chr(value) --> gives the appropriate char
str = input()
'''Given a input string, you have to encrypt the string in such a way that 'a' becomes '2', 'z' becomes 'a' and accordingly. Note: All the characters in the given string are in lowercase

Input Format: A lowercase String

Output Format: Encrypted lowercase string.

[abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlk jihgfedcba]

Ex: Input: abcd

Output:

zyxw'''
def ss(str):
    str2 = ""
    st = ord("a")+ord("z")
    for i in str:
        str2+=chr(st-ord(i))
    return str2
'''A high profile secret agency wants to handle all messages send and receive in ciphers. They need to build a program software where every mail sent or received will be encrypted using some secr One of the formats can be as follows:

a->f, b->g, c->h....u->z ,v->a, w->b, x->c,y->d, z->e.

Note: input string only have lower case alphabets.

Input: word

output: btwi'''
def incres1(str):
    str2 = ""
    for i in str:
        if ord(i)+5 <= ord("z"):
            str2+=chr(ord(i)+5)
        else:
            str2+=chr((ord("a")+ord("z"))-ord(i)-2)
    return str2
'''Given is a string. The task is to given the sum of values of each character according to the position of the character in the alphabetical order.

Ex: a is 1st term so a=1, b is 2nd term so b=2 and so on

Input: abcd

Output: 10

Input: Man

Output: 28'''
def sumofvalue(str):
    s = 0
    for i in str:
        # print(122-ord(i))
        if ord(i) < ord("a"):
            s+=(26-(122-ord(i)))
        else:
            s+=(26-(90-ord(i)))
    return s
'''If A-0, B=1, C=A+B, D=B+C, E=C+D and so on till Z.

If a string(with only alphabets) is given as input. Find the sum of the individual character values

based on above series. Note: Both upper and lower case character should give same result.

Input:

MAN

output: 377'''
def fid(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    print(sum)
    return sum
def sumoffid(str):
    s = 0
    for i in str:
        s+=fid(ord(i)-96)
    return s
'''In a supermarket every product have a barcode with alphanumeric code.

The price of each item is product of each digits In the code write a program to find the price of the given iten.

Input:4ac52

Input: 2xy5r8

output: 40

output: 80'''
def barcode(str):
    sum1 = 1
    for i in str:
        if i.isdigit():
            sum1 *= int(i)
    return sum1
print(barcode(str))