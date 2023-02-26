def fibonacci_gen(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci_gen(number-1) + fibonacci_gen(number-2)

def fibonacci_verify(looking_for):
    value = 0
    index = 0
    while value < looking_for:
        print(value)
        value = fibonacci_gen(index)
        index += 1
    if value == fibonacci_gen:
        return True
    else:
        return False
    

def main():
    mode_num = input('Enter mode and value: ')
    command = mode_num.split()
    if command[0] == '-i':
        print(fibonacci_gen(int(command[1])))
    elif command[0] == '-v':
        print(fibonacci_verify(int(command[1])))