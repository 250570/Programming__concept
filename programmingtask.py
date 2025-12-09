##Task 1
#a=int(input(' Enter first number: '))
#b=int(input(' Enter second number: '))
#c=int(input(' Enter third number: '))

#if a>=b and a>=c:
  #  print(a,'is the largest number.')
#elif b>=a and b>=c:
  #  print(b,'is the largest number.')
#else:
  #  print(c,'is the largest number.')





##Task 2
#month=int(input('Enter a month number(1-12): '))
#if result==1:
   # print('jan')
#elif result==2:
 #   print('feb')
#elif result==3:
 #   print('mar')
#elif result==4:
 #   print('apr')
#elif result==5:
  #  print('may')
#elif result==6:
 #   print('jun')
#elif result==7:
 #   print('jul')
#elif result==8:
 #   print('aug')
#elif result==9:
 #   print('sep')
#elif result==10:
 #elif result==11:
   # print('nov')
#elif result==12:
  #  print('dec')
#else:
  #  print('Invalid number! Enter1-12.')



##Task 3
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print("Original values: a =", a, "b =", b)
#a, b = b, a
#print("Swapped values:  a =", a, "b =", b)




##Task 4
#age=int(input('Enter a person age: '))
#if age<12:
 #print('ticket is free')
#elif age>=12 and age<=60:
 #   membership_card=input('do the person have a member card: ')
  #  if membership_card=='yes':
   #     price=150
    #else:
     #   price=200
    #print(price)
#else:
 #   price=100
  #  print(price)


##Task 5
#units = int(input("Enter electricity usage in units: "))

#if units < 100:
  #  cost = units * 5

#elif units <= 300:
 #   cost = (100 * 5) + (units - 100) * 8

#else:   # units > 300
 #   cost = (100 * 5) + (200 * 8) + (units - 300) * 10

#print("Total Electricity Bill: Rs", cost)



##Task 6
#p1 = input("Player 1, enter your move (rock/paper/scissors): ")
#p2 = input("Player 2, enter your move (rock/paper/scissors): ")

#if p1 == p2:
  #  print("It's a tie!")
#else:
  #  if p1 == "rock":
    #    if p2 == "scissors":
     #       print("Player 1 wins! Rock breaks scissors.")
   #     else:
    #        print("Player 2 wins! Paper covers rock.")
   # else:
   #     if p1 == "paper":
     #       if p2 == "rock":
     #           print("Player 1 wins! Paper covers rock.")
     #       else:
   #             print("Player 2 wins! Scissors cut paper.")
    #    else:
     #       if p1 == "scissors":
     #           if p2 == "paper":
      #              print("Player 1 wins! Scissors cut paper.")
      #          else:
     #               print("Player 2 wins! Rock breaks scissors.")




##Task 7
#a = int(input("Enter students in class A: "))
#b = int(input("Enter students in class B: "))

#c = int(input("Enter students in class C: "))

# each desk seats 2 students
#desk_a = (a + 1) // 2
#desk_b = (b + 1) // 2
#desk_c = (c + 1) // 2

#total_desks = desk_a + desk_b + desk_c

#print("Total desks needed:", total_desks)



##Task 8
#current_floor = 5
#pressed_floor = int(input("Enter the floor you want to go to: "))

#if pressed_floor > current_floor:
  #  print("Lift should go UP")
#elif pressed_floor < current_floor:
#    print("Lift should go DOWN")
#else:
 #   print("Lift should STAY at the current floor")




##Task 9
#num = int(input("Enter a number: "))

#if num > 0:
 #   print("The number is positive.")

 #   if num % 2 == 0:
#        print("It is even.")
 #   else:
  #      print("It is odd.")

#else:
  #  print("The number is not positive.")




##Task 10
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#if a > b:
 #   print("Greater number is:", a)
#elif b > a:
 #   print("Greater number is:", b)
#else:
 #   print("Both numbers are equal.")

    # Now check if the equal number is positive, negative, or zero
  #  if a > 0:
  #      print("The number is positive.")
  #  elif a < 0:
   #     print("The number is negative.")
 #   else:
  #      print("The number is zero.")




##Task 11
#num = int(input("Enter a number: "))

#if num % 3 == 0 and num % 5 == 0:
 #   print("Fizz Buzz")
#elif num % 3 == 0:
  #  print("Fizz")
#elif num % 5 == 0:
 #   print("Buzz")
#else:
 #   print(num)





##Task 12
#import random

#num = random.randint(0, 5)   # generate a random number from 0 to 5
#print("Random number:", num)

#if num == 0:
 #   print("Flamingos turn pink from eating shrimp.")
#elif num == 1:
 #   print("The only food that doesn't spoil is honey.")
#elif num == 2:
 #   print("Shrimp can only swim backwards.")
#elif num == 3:
  #  print("A taste bud's life span is about 10 days.")
#elif num == 4:
 #   print("It is impossible to sneeze while sleeping.")
#elif num == 5:
    #print("It is illegal to sing off-key in North Carolina.")
#else:
  #  print("Invalid number")   # This never happens, but good practice





##Task 13
#total_amount = float(input("Enter total purchase amount: "))
#is_member = input("Are you a member? (True/False): ")

#if is_member.lower() == "True":
 #   is_member = True
#else:
 #   is_member = False

#if total_amount > 1000:
 #   if is_member:
  #      discount = 0.20   # 20%
 #   else:
  #      discount = 0.10   # 10%
#else:
 #   discount = 0          # No discount

#final_amount = total_amount - (total_amount * discount)

#print("Final amount to pay: Rs", final_amount)



##Task 14
#earth_weight = float(input("Enter your Earth weight: "))
#planet = int(input("Enter planet number (1-7): "))

#if planet == 1:
 #   new_weight = earth_weight * 0.38
#    print("Your weight on Mercury is:", new_weight)

#elif planet == 2:
 #   new_weight = earth_weight * 0.91
 #   print("Your weight on Venus is:", new_weight)

#elif planet == 3:
 #   new_weight = earth_weight * 0.38
  #  print("Your weight on Mars is:", new_weight)

#elif planet == 4:
 #   new_weight = earth_weight * 2.53
#    print("Your weight on Jupiter is:", new_weight)

#elif planet == 5:
 #   new_weight = earth_weight * 1.07
 #   print("Your weight on Saturn is:", new_weight)

#elif planet == 6:
  #  new_weight = earth_weight * 0.89
  #  print("Your weight on Uranus is:", new_weight)

#elif planet == 7:
  #  new_weight = earth_weight * 1.14
  #  print("Your weight on Neptune is:", new_weight)

#else:
#    print("Invalid planet number")




##Task 15
#m1 = float(input("Enter marks of Subject 1: "))
#m2 = float(input("Enter marks of Subject 2: "))
#m3 = float(input("Enter marks of Subject 3: "))
#m4 = float(input("Enter marks of Subject 4: "))

#total = m1 + m2 + m3 + m4
#percentage = (total / 400) * 100

#print("Total Marks =", total)
#print("Percentage =", percentage)

#if percentage > 70:
 #   print("Grade: Distinction")
#elif percentage > 60:
 #   print("Grade: First Division")
#elif percentage > 40:
 #   print("Grade: Pass")
#else:
 #   print("Grade: Fail")



##Task 16
#cost = float(input("Enter the cost price of the bike: "))

#if cost > 100000:
 #   tax = cost * 0.15
#elif cost > 50000 and cost <= 100000:
  #  tax = cost * 0.10
#else:
  #  tax = cost * 0.05

#print("Road Tax to be paid: Rs", tax)




##Task 17
#years = float(input("Enter years of service: "))
#salary = float(input("Enter your salary: "))

#if years > 10:
 #   bonus = salary * 0.10        # 10%
#elif years >= 6:
 #   bonus = salary * 0.08        # 8%
#else:
 #   bonus = salary * 0.05        # 5%

#print("Bonus Amount: Rs", bonus)





##Task 18
#score = int(input("Enter your subject score: "))

#if score > 90:
 #   print("Congratulations! Excellent performance!")
#elif score >= 50:
 #   print("Good effort! But you should improve more.")
#else:
 #   print("You should retake the course for better understanding.")




##Task 19
#age = int(input("Enter candidate age: "))
#degree = input("Do you have a degree? (yes/no): ")

#if age >= 18:
 #   if degree.lower() == "yes":
 #       experience = float(input("Enter years of work experience: "))

 #       if experience > 3:
  #          print("Highly Eligible")
  #      elif experience >= 1:
  #          print("Eligible")
   #     else:
 #           print("Under Review")

 #   else:
  #      print("Not Eligible — Degree required.")
#else:
 #   print("Not Eligible — Must be 18 or older.")




##Task 20
#age = int(input("Enter age: "))
#gender = input("Enter gender (M/F): ")

#if age >= 18 and age < 30:
    # First age group
  #  if gender == 'M':
   #     print("Wage: 700")
  #  else:
 #       print("Wage: 750")

#elif age >= 30 and age <= 40:
    # Second age group
 #   if gender == 'M':
 #       print("Wage: 800")
 #   else:
 #       print("Wage: 850")

#else:
 #   print("Not eligible for wages.")




##Task 21
#is_valid = True
#balance = 50000
#correct_pin = 123

#pin = int(input("Enter PIN: "))

#if pin == correct_pin:      # PIN correct
 #   print("1. Withdraw")
 #   print("2. Check Balance")
 #   print("3. Exit")

  #  choice = int(input("Enter your choice: "))

  #  if choice == 1:
   #     amount = int(input("Enter amount to withdraw: "))
        
   #     if amount <= balance:
     #       balance -= amount
     #       print("Withdrawal successful. Remaining balance:", balance)
    #    else:
     #       print("Insufficient balance.")

  #  elif choice == 2:
    #    print("Your current balance is:", balance)

  #  elif choice == 3:
    #    print("Thank you for visiting")

  #  else:
   #     print("Invalid option!")

#else:
  #  print("Wrong PIN!")





##Task 22
#print("Welcome to the Magic Forest")

#choice1 = input("Do you want to go 'north' or 'south'? ")

#if choice1 == "south":
 #   print("Game Over")

#else:   
  #  choice2 = input("Do you want to 'cross the river' or 'follow the path'? ")

 #   if choice2 == "cross the river":
  #      print("Game Over")

  #  else:   
   #     choice3 = input("Choose 'fairy', 'ogre', or 'elf': ")

   #     if choice3 == "elf":
   #         print("You Win")
  #      else:
     #       print("Game Over")





##Task 23
#print("Welcome to the Haunted House")

#choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ")

#if choice1 == "downstairs":
 #   print("Game Over")

#else:  
 #   choice2 = input("Do you want to 'enter the room' or 'stay outside'? ")

 #   if choice2 == "enter the room":
  #      print("Game Over")

 #   else:  
  #      choice3 = input("Choose one: 'ghost', 'vampire', or 'werewolf': ")

 #       if choice3 == "werewolf":
   #         print("You Win")
  #      else:
   #         print("Game Over")














