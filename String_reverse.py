# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.


# #using string slicing
def solution(x):
    string = str(x)

    if string[0] == '-':  #checking if the first elemet is - , checking if its negative or not
        return int(f'-{string[:0:-1]}') #revese string till end avoiding 0'th elemenet
    else:
        return int(string[::-1])
#
# print(solution(-231))
# print(solution(345))
#
# #string reverse using for loop
def reverse_string(str):
    str1 = "" #empty string to store the reversed string

    for i in str:

        str1 = i + str1


    return str1

str = 'Hello'
print(f'String: {str}')
print(f'Reversed: {reverse_string(str)}')

#string reverse using while loop

str = 'Hello'
print(f'original string: {str}')

reversed_string = ""
count = len(str) # find lenght of string
while count >0:
    reversed_string += str[count-1] #save the value
    count -= 1
print(f'Reversed: {reversed_string}')


#using recursion
def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

str = 'Hello'
print(f'String: {str}')
print(f'Reversed: {reverse(str)}')
