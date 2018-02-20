
#name = input("What's your name? ")
#print("Nice to meet you " + name + "!")
#age = input("Your age? ")
#print("So, you are already " + str(age) + " years old, " + name + "!")

opperand = int(input('Should we 1. add or 2. subtract '))
if opperand == 1:
    print('Great! We will add two numbers.')
elif opperand == 2:
    print('Great! We will subtract two numbers.')
else:
    print('Does not compute!')

def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.'
          .format(**locals()))
