def middle(t):
    return t[1:-1]

def cumsum(x):
    newt=[]
    for i in range(len(x)):
        print(i)
        newt+=[sum(x[:i+1])]
    return newt

def nested_sum(t):
    summed=0
    for i in range(len(t)):
        summed+=sum(t[i])
    return summed

letters=['a', 'b', 'c', 'd']
print(middle(letters))

number=[1, 2, 3, 4, 5, 6]
print(cumsum(number))

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))


import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

#Q4===================================================
def has_duplicates(t):
    for i in range(len(t)):
        if t[i] in t[i+1:]:
            return True
        if i>0:
            if t[i] in t[:i]:
                return True
    return False

t1=[1, 1, 3, 4, 9, 5]
t2=[1, 2, 3, 4, 6, 5]

print(has_duplicates(t1))
print(has_duplicates(t2))