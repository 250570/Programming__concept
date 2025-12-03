age=int(input('Enter a person age: '))
if age<12:
    print('ticket is free')
elif age>=12 and age<=60:
    membership_card=input('do the person have a member card: ')
    if membership_card=='yes':
        price=150
    else:
        price=200
    print(price)
else:
    price=100
    print(price)