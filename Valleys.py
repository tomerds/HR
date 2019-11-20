def countingValleys(n, s):
    U = 'U'
    D = 'D'
    level = valley = 0
    for i in s:
        if(i == U):
            level += 1
            if(level == 0):
                valley += 1
        else:
            level -= 1
            print(level)

    return valley


print(countingValleys(8, 'UDDDUDUU'))
