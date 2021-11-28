def getretirementage(year, month):
    if year < 1938:
        return 65, 0
    elif 1937 < year < 1943:
        return 65, (year - 1937) * 2
    elif 1942 < year < 1955:
        return 66, 0
    elif year < 1960:
        return 66, (year - 1954) * 2
    else:
        return 67, 0


def main():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']

    while True:
        year = int(input('Enter your birth year (or type -1 to exit): '))
        if year == -1:
            break

        month = int(input('Enter your birth month (in numbers, ex: 03 for March): '))

        (retage, retagemonth) = getretirementage(year, month)

        print(f'Your retirement age is {retage} years and {retagemonth} months')


if __name__ == '__main__':
    main()
