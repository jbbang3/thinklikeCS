import time

# #Q1===================================================

# fin=open('/home/jaej/Documents/GitWeb/thinklikeCS/words.txt')
# known={}

# start_time = time.time()
# for lin in fin:
#     word=lin.strip()
#     if word not in known:
#         known[word]=1
#     elif word in known:
#         known[word]+=1
# elapsed_time = time.time() - start_time    


# #Q2===================================================
# def invert_dict(t):
#     inverse=dict()
#     for x in t:
#         inverse.setdefault(t[x],[]).append(x)
#     return inverse

# h={'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
# print(invert_dict(h))

# #Q3===================================================
# def ack(m,n):
    
#     if m==0:
#         ans=n+1
#     elif m>0 and n==0:
#         ans=ack(m-1,1)
#     elif m>0 and n>0:
#         ans=ack(m-1, ack(m,n-1))
#     return ans
# print(ack(3,4))

# cache={}

# def ack2(m,n):
#     if m==0:
#         return n+1
#     elif n==0:
#         return ack2(m-1,1)
#     elif (m,n) in cache:
#         return cache[m,n]
#     else:  
#         cache[m, n] = ack2(m-1, ack2(m, n-1))
#         return cache[m, n]

# print(cache)
# print(ack2(3,4))
# # print(ack2(3,6))

# #Q4===================================================
# def has_duplicates(t):
#     dictionary={}
#     for c in t:
#         if c in dictionary:
#             return True
#         else:
#             dictionary[c]=True
#     return False

# t1=[1, 1, 3, 4, 9, 5]
# t2=[1, 2, 3, 4, 6, 5]

# print(has_duplicates(t1))
# print(has_duplicates(t2))


#Q5===================================================
fin=open('/home/jaej/Documents/GitWeb/thinklikeCS/words.txt')

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

rotate=dict()
wordlist=list()
rotatepair=dict()

print(rotate_word('test',1))

for line in fin:
    word=line.strip()
    wordlist.append(word)

for w in wordlist:
    for i in range(25):
        testword=rotate_word(w,i+1)
        if i==0:
            rotate[w]=[testword]
        else:
            rotate[w].append(testword)


for j in range(len(wordlist)):
    test=wordlist[j]
    for k in range(25):
        if rotate[test][k] in wordlist:
            if rotatepair[test] not in rotate:
                rotatepair[test]=rotate[test][k]
            else:
                rotatepair[test].append(rotate[test][k])

print(rotatepair)