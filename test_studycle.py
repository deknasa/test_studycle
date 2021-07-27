list = []
total = 0
n = int(input('Input many numbers in array : '))
for i in range(0, n):
    bil = int(input('Number to - %d = ' % (i+1)))
    list.append(bil)

print('The Number of Input : ', list)
list.sort()
print('Sorted Number of Input : ',list)

def satu():
    total = sum(list)
    rata = total/n
    print('Average : ',rata)
    return rata

def dua():
    p = len(list)
    if p % 2 == 0:
        median1 = list[p//2]
        median2 = list[p//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list[p//2]
    print('Median : ', median)
    return median

def tiga():
    mult = 0
    for item in list:
        if mult == 0:
            mult = item
        else:
            mult *= item
    print('Multiple all number : ',mult)
    return mult

def pilih():
    word = 'Select function to run'
    print(word)
    dapat = ['Average', 'Median', 'Multiple all number', 'All']
    for i in dapat:
        print(dapat.index(i) + 1, '.', i)
    case = int(input('chose option 1,2,3 or 4 : '))
    if case == 1:
        satu()
    elif case == 2:
        dua()
    elif case == 3:
        tiga()
    elif case == 4:
        satu(), dua(), tiga()
    else:
        print('UNDEFINED INPUT !!!')
        print('')
        pilih()


if __name__ == '__main__':
    pilih()
