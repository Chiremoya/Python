

def collatz(number):

    if(number % 2 == 0):
        print(number // 2)
        return number // 2 # we can return an expression because it evaluates to a single value
    elif(number % 2 == 1):
        result = 3 * number + 1
        print(result)
        return result

print('Enter number: ')
userInput = input()
userInput = int(userInput)

while userInput != 1:

    userInput = collatz(userInput)

