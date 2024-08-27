str = input()
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
''' In a supermarket every product have a barcode with alphanumeric code. Consecutive numbers in the code is considered as one multi-digit number. The price of the product is sum of the numbers in the code.Write a progran to find the price of the given product

Input: 12axy44

output: 56

Input: 24ab7hg27

Output: 58'''
def barcodecongi(str):
    sum1 = 0
    i = 0
    while i < len(str):
        if i+1<len(str) and str[i].isdigit() and str[i+1].isdigit():
            sum1 += int(str[i]+str[i+1])
            i+=2
        elif str[i].isdigit():
            sum1 += int(str[i])
            i+=1
        else:
            i+=1
    return sum1
def reve(n):
    t = n
    nu = 0
    while t != 0:
        r = t % 10
        nu =nu * 10 + r
        t = t // 10
    return nu
def othbarcodecongi(str):
    sum1 = 0
    num = 0
    for i in str:
        if i.isdigit():
            num = num * 10 + int(i)
        else:
            sum1 += num
            num = 0
    sum1 += num
    return sum1