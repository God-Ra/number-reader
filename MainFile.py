import winsound

a = {'1': 'jedan',
     '2': 'dva',
     '3': 'tri',
     '4': 'cetiri',
     '5': 'pet',
     '6': 'sest',
     '7': 'sedam',
     '8': 'osam',
     '9': 'devet',
     '10': 'deset',
     '11': 'jedanaest',
     '12': 'dvanaest',
     '13': 'trinaest',
     '14': 'cetrnaest',
     '15': 'petnaest',
     '16': 'sesnaest',
     '17': 'sedamnaest',
     '18': 'osamnaest',
     '19': 'devetnaest',
     '20': 'dvadeset',
     '30': 'trideset',
     '40': 'cetrdeset',
     '50': 'pedeset',
     '60': 'sezdeset',
     '70': 'sedamdeset',
     '80': 'osamdeset',
     '90': 'devedeset',
     '100': 'sto',
     '200': 'dvjesto',
     '300': 'tristo',
     '400': 'cetristo',
     '500': 'petsto',
     '600': 'setsto',
     '700': 'sedamsto',
     '800': 'osamsto',
     '900': 'devetsto',
     '0': ''}

wordedNumber = []
number = input()
numberLength = len(number)
number = int(number)
billion = number // 1000000000
million = (number // 1000000) % 1000
thousand = (number // 1000) % 1000
remainder = number % 1000

if billion > 0:
    if billion == 1:
        wordedNumber.extend(('jedna', 'milijarda'))
    if billion == 2 or billion == 3 or billion == 4:
        wordedNumber.extend((str(billion), 'milijarde'))
    if billion > 4:
        wordedNumber.extend((str(billion), 'milijardi'))

if million > 0:
    hundredMillion = million // 100 * 100
    if hundredMillion > 0:
        wordedNumber.append(str(hundredMillion))
    if (million // 10) % 10 == 1:
        tenMillion = str(tenMillion % 100)
        wordedNumber.extend((tenMillion, 'miliona'))
    else:
        tenMillion = (million // 10) % 10
        tenMillion = tenMillion * 10
        if tenMillion > 0:
            wordedNumber.append(str(tenMillion))
        oneMillion = million % 10
        if oneMillion > 0:
            wordedNumber.append(str(oneMillion))
            if oneMillion == 1:
                wordedNumber.append('milion')
            if oneMillion > 1 and oneMillion < 5:
                wordedNumber.append('miliona')
            if oneMillion > 4:
                wordedNumber.append('miliona')
        if oneMillion == 0:
            wordedNumber.append('miliona')

if thousand > 0:
    hundredThousand = thousand // 100 * 100
    if hundredThousand > 0:
        wordedNumber.append(str(hundredThousand))
    if (thousand // 10) % 10 == 1:
        tenThousand = str(tenThousand % 100)
        wordedNumber.extend((tenThousand, 'hiljada'))
    else:
        tenThousand = (thousand // 10) % 10
        tenThousand = tenThousand * 10
        if tenThousand > 0:
            wordedNumber.append(str(tenThousand))
        oneThousand = thousand % 10
        if oneThousand > 0:
            if oneThousand == 1:
                wordedNumber.extend(('jedna', 'hiljada_z'))
            if oneThousand > 1 and oneThousand < 5:
                wordedNumber.extend((str(oneThousand), 'hiljade'))
            if oneThousand > 4:
                wordedNumber.extend((str(oneThousand), 'hiljada'))
        if oneThousand == 0:
            wordedNumber.append('hiljada')

if remainder > 0:
    hundredRemainder = remainder // 100 * 100
    if hundredRemainder > 0:
        wordedNumber.append(str(hundredRemainder))
    if (remainder // 10) % 10 == 1:
        tenRemainder = str(tenRemainder % 100)
        wordedNumber.append(tenRemainder)
    else:
        tenRemainder = (remainder // 10) % 10
        tenRemainder = tenRemainder * 10
        if tenRemainder > 0:
            wordedNumber.append(str(tenRemainder))
        oneRemainder = remainder % 10
        if oneRemainder > 0:
            wordedNumber.append(str(oneRemainder))

for i in range(len(wordedNumber)):
    if wordedNumber[i] in a:
        winsound.PlaySound(a[wordedNumber[i]] + ".wav", winsound.SND_FILENAME)
    else:
        winsound.PlaySound(wordedNumber[i] + ".wav", winsound.SND_FILENAME)
