#                  7. The given function has a string (str) and two characters, ch1 and ch2.
#                     Execute the function in such a way that str returns to its original string,
#                     and all the events in ch1 are replaced by ch2, and vice versa.
'''Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)'''
#Assumption
'''This string has only alphabets that are in lower case.
Example
Input:
str: apples
ch1: a
ch2: p
Output:
paales'''
def replacecharacter(str1,ch1,index,ch2):
    list1=[i for i in str1]
    res=[]
    for i in list1:
        if(i == ch1):
            i=ch2
            res.append(i)
        elif(i == ch2):
            i=ch1
            res.append(i)
        else:
            res.append(i)
    result=''.join(res)
    return result
print(replacecharacter('apples','a',2,'p'))

#******************************************#

'''You are tasked with a complex matrix operation. You will need to input the size of the matrix 
and then provide the elements of the matrix.
The main matrix must then be divided into two sub matrices one for even indexed and one for
the odd indexed elements.
Following this you are required to sort both the even and odd matrices in ascending order.
Finally you must calculate and print the sum of the second largest numbers from both the
matrices.'''
import numpy as np 
def Sumoflargest(array):
    if(len(array)>4):
        even=[]
        odd=[]
        for i in range(len(array)):
            if(i%2==0):
                even.append(array[i])
            else:
                odd.append(array[i])
        even.sort()
        odd.sort()
        return even[-2]+odd[-2]
    else:
        return "Invalid Array"
ls=np.array([1,2,3])
print(Sumoflargest(ls))
