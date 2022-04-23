from typing import List

# List
# friend =[]
# friend.append("Somsri")
# friend.append("Somsak")
# friend.append("Somchai")
# print(friend)
# print(friend[0])
# friend.insert(0,"Sompong")
# print(friend)
# friend.insert(2, "Somkiat")
# print(friend)
# friend.insert(0, friend.pop(3))
# print(friend)
# friend.remove("Somchai")
# print(friend)
# print(friend.remove("Somkiat"))
# print(friend)
# print(friend.pop(2))
# print(friend)
# print(type(friend))

# print("----------------------------")
# #tuple
# teacher = ("Khorkai","Khorkhai", "Khorkwai")
# print(teacher)
# print(type(teacher))   #tuple cannot append, delete
# coin = (5, 1, 10, 2, 5, 1, 10, 2, 10, 10, 10, 10)
# print(coin.count(10))
# print(coin.count(5))
# print(coin.count(2))
# print(coin.count(1))

# teacher = ("Korkai","Khorkhai", "Korkwai")
# print(teacher.index("Khorkhai"))
# teacher = ("Korkai","Khorkhai", "Korkwai", "Khorkhai")
# print(teacher.index("Khorkhai"))
# print(teacher[1])
# print(teacher[-1])
# print(teacher[-2])

# character = ['A', 'Z', 'C', 'X', 'Y']
# character.sort()            #sort ถาวร
# print(character)
# character.sort(reverse=True)
# print(character)
# print(sorted(character))        #sortชั่วคราว 
# print(character)
# print(sorted(character,reverse=True))
# print(character)
# character.reverse()  #reverse ถาวร
# print(character)

character = ['Y', 'X', 'C', 'Z', 'A']
print(character)
character[2] = 'N'
print(character)
del character[2]   #delete
print(character)
for c in character:
    print(c)
for c in sorted(character):
    print(c)
    
    
print("----------------------------")

#dict
vocab = {'cat':'แมว', 'dog':'สุนัข'}
print(type(vocab))
print(vocab['cat'])
vocab = {'cat':'แมว', 'dog':'สุนัข', 'pig':{'สุกร','หมู'}}
print(vocab['pig'])
print(vocab['cat'][0])
vocab['orange'] = 'ส้ม'
print(vocab)
vocab['dog'] = {'หมา', 'สุนัข'}
print(vocab)

for v in vocab:
    print(v)

for v in vocab.items():
    print(v)

for v in vocab.keys():
    print(v)
for v in vocab.values():
    print(v)

