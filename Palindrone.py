"""
Return True if the word is the same forwards and backwards
Do not use automatic methods for reversing the string

Big O : O(n)
"""
def is_palindrome(word):
    left = 0
    right = len(word)-1

    while right>left:
        if word[left]!=word[right]:
            return False
        right=right-1
        left=left+1
    return True

""" 
Open up  the file. Break into words 
print out all palindrones

Big O : O(n^2)
Read file has Big O: O(n)
check palindromes has Big O: O(n)
total O(n^2)
"""
def find_all_palindromes(file_name):
    fp = open(file_name,"r")
    for line in fp:
        line=line.strip()
        line=line.split(" ")
        for word in line:
            if is_palindrome(word):
                print(word)



#Run a few tests

if is_palindrome('racecar'):
    print('pass')
else:
    print('fail')

if is_palindrome('mom'):
    print('pass')
else:
    print('fail')

if is_palindrome('noon'):
    print('pass')
else:
    print('fail')

# find_all_palindromes("test_palin.txt")