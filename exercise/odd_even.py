def try_again():
    print('Try again: (y/n)', end=' ')
    answer = input()
    answer = answer.lower()
    return answer == 'y'

def get_category(num):
    if num == 0:
        category = 'zero'
    elif num % 2 == 0:
        category = 'even'
    else:
        category = 'odd'
    return category

while(True):
    print('Enter a number:', end=' ')
    user_input = input()

    try:
        num = int(user_input)
    except ValueError:
        print('Invalid input')
    else:
        print(num, 'is', get_category(num))

    if not try_again():
        break