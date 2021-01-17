fin=open('/home/jaej/Documents/GitWeb/thinklikeCS/words.txt')

# for line in fin:
#     word=line.strip()
#     if len(word)>20:
#         print(word)
#     else:
#         continue

#Q2==================================================

# def has_no_e(word):
#     for c in word:
#         if c=='e':
#             return False
#     return True

# print(has_no_e('fly'))
# print(has_no_e('flye'))

# if has_no_e('fly'):
#     print('fly')

# noe=0
# yese=0
# for line in fin:
#     word=line.strip()
#     print(word)
#     if has_no_e(word):
#         print(word)
#         noe+=1
#     else:
#         yese+=1
#         continue

# print((noe/(yese+noe)*100))

#Q3 Q4 Q5 Q6==================================================

def avoids(word,s):
    newword=''
    for c in word:
        if not c in s:
            newword+=c
    return newword

def uses_only(word, available):
    for letter in word: 
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    for letter in required: 
        if letter not in word:
            return False
    return True

print(avoids('abcdfes','fe'))
