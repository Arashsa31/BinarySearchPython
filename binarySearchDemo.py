def binary_search(data, key):
    low = 0
    high = len(data) - 1
    middle = (low + high + 1) // 2
    location = -1

    while low <= high and location == -1:
        print(remaining_elements(data, low, high))

        print('   ' * middle, end='')
        print(' * ')

        if key == data[middle]:
            location = middle
        elif key < data[middle]:
            high = middle - 1
        else:
            low = middle + 1

        middle = (low + high + 1) // 2

    return location

def remaining_elements(data, low, high):
    return '   ' * low + ' '.join(str(s) for s in data[low:high + 1])

def main():
    data = [16, 23, 31, 35, 36, 46, 48, 52, 54, 57, 63, 76, 83, 89, 90]
    data.sort()
    print(data, '\n')

    search_key = int(input('Enter an integer value (-1 to quit): '))

    while search_key != -1:
        location = binary_search(data, search_key)

        if location == -1:
            print(f'{search_key} was not found\n')
        else:
            print(f'{search_key} found in position {location}\n')

        search_key = int(input('Enter an integer value (-1 to quit): '))

if __name__ == '__main__':
    main()
