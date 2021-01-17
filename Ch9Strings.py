fruit='banana'
n=fruit.count('a')
print(n)

def is_palindrome(world):
    return world[::-1]

#exercise2====================================================

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
       if not c.islower():
            return False
    return True


s='abcdef'
S='ABcdEF'
S2='ABCDE'
#print(1,any_lowercase1(s))  # checks only the 1st letter
#print(2, any_lowercase2(s)) #checks for character 'c'
#print(3,any_lowercase3(s))  #checks the last letter only
print(4,any_lowercase4(s))
#print(5,any_lowercase5(s))  #stops the moment it sees one False

print('\n')
print(4, any_lowercase4(S))

print('\n')
print(4, any_lowercase4(S2))


#exercise 5=======================================================

def rotate_word(word,n):
    
    newword=''
    for c in word:
        if c.isupper(): 
            start=ord('A')
            newc=chr((ord(c)-start+n)%26+start)
        elif c.islower():
            start=ord('a')
            newc=chr((ord(c)-start+n)%26+start)
        else:
            newc=chr(ord(c)+n)
        newword=newword+newc
    return newword
    

print(rotate_word('cheer', 20))
print(rotate_word('melon', 2))
print(rotate_word('IBM7', -1))