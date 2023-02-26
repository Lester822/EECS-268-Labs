def outbreak(days):
    if days == 3:
        infected = 75
    elif days == 2:
        infected = 20
    elif days == 1:
        infected = 6
    else:
        infected = outbreak(days-3) + outbreak(days-2) + outbreak(days-1)
    return infected

day_wanted = int(input('What day do you want?: '))
print(outbreak(day_wanted))
