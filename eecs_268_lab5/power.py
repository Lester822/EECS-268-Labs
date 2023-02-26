def powerify(base, power):
    if power == 0:
        return 1
    else:
        return base * powerify(base, power-1)

def main():
    base = ''
    power = ''
    while not str(base).isnumeric():
        base = input('Enter Base: ')
        if base.isnumeric():
            base = int(base)
        else:
            print('The base must be numeric')
    while not str(power).isnumeric():
        power = input('Enter a Power: ')
        if power.isnumeric():
            power = int(power)
            if power >= 0:
                break
            else:
                print('The power must be greater than or equal to 0')
        else:
            print('The power must be numeric')
    print(powerify(base, power))
main()