# import time
# while True:
#     print("test while")
#     time.sleep(1)

money = 1000
transfer = 10000

print("Check:", money<transfer)

while money < transfer:
    print('Please input transfer again')
    transfer= int(input('new transfer:'))
    if transfer > 1000000:
        print('Call manager!')
        break
    
print('transfer already if manager allowed ')