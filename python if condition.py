age = 15

if age >= 15:
    print('you are a man')
else:
    print('go out you are a kid!')





number=input('How old are you ? \n ')
if int(number) >= 15:
        print('you are man')
else : 
        print('you are kid')





sis=input('Do you have siblings ? \n ')
if str(sis)== 'yes':
    print('you are donkey')
elif sis=='i dont know':
    print('you are dick')
else :
    print('fuck you')



sis=input (' do you have sisters')
if str(sis)== 'yes':
  print('you are donkey')
elif sis=='i dont know':
  print('you are dick')
elif sis=='no':
  print('you typed no, So go to hell man!')
else:
  print('fuck you')


first_input = float(input("Enter the first number: "))
second_input = float(input("Enter the second number: "))
third_input = float(input("Enter the third number: "))

if first_input >= second_input and first_input >= third_input:
  print('The Largest number is from first ' + str(first_input))
elif second_input >= first_input and second_input >= third_input:
  print('The Largest number is from second ' + str(second_input))
else:
  print('The Largest number is from third ' + str(third_input))



number=int (input(' Guess my number ? \n '))
if number>0:
    print('positive')
elif number<0:
    print('negative')
else:
    print('number is zero')
