import enum

# loop by number
print("------print number------")
for i in range(5):
    print(i+1)
    
print('-----------')
food = ['noodles','tokbokki','shabu','hamburger']

for j in food:
    print(j)
    
friend = {'Korkai':'คุณกอไก่',
           'Khorkai':'คุณขอไข่'}
# show key
print("------key------")
for f in friend:
    print(f)
    
# show items
print("------items------")
for k,v in friend.items():
    print('key: ',k)  
    print('value: ',v) 
    
# show key only
print("------key------")
for f in friend.keys():
    print(f)
    
# show value only
print("------value------")
for f in friend.values():
    print(f)
    
# order
print("------order------")
for i,f in enumerate(friend, start=1000):
    print(i,f)
    
# ต้องการลำดับสำหรับ dict
print("------order for dict------")
for i,f in enumerate(friend.items()):
    print(i,f)
    
# ต้องการลำดับสำหรับ dict แยก key
print("------order for dict but separate key------")
for i,(k,v) in enumerate(friend.items()):
       print(i,k,v)