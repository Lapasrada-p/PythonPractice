# money = -10
# if money >=300:
#     print("Go to japan restaurant")
# elif money == 0:
#     print("Wash dishes")
# elif money >0 and money <50:
#     print("Have dinner at home")
# else:
#     print("Please uinput number grater than zero")
# print("Then, back to learn Python")

# text = 'hellO PloY'
# print(text.title())
# print(text.upper())
# print(text.lower())

friend = ['Korkai','Khorkai','Khorhwai']

friend_dict = {'Korkai':'คุณกอไก่',
           'Khorkai':'คุณขอไข่'}

visitor = 'korkai'

if visitor in friend or visitor.title() in friend:
    print('เพื่อนเราเอง')
    if visitor in friend_dict or visitor.title() in friend_dict:
        print('Hello! '+ friend_dict[visitor.title()])
else:
    print('I dont know who are you!')
