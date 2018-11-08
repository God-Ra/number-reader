import winsound

a={'1':'jedan',
   '2':'dva',
   '3':'tri',
   '4':'cetiri',
   '5':'pet',
   '6':'sest',
   '7':'sedam',
   '8':'osam',
   '9':'devet',
   '10':'deset',
   '11':'jedanaest',
   '12':'dvanaest',
   '13':'trinaest',
   '14':'cetrnaest',
   '15':'petnaest',
   '16':'sesnaest',
   '17':'sedamnaest',
   '18':'osamnaest',
   '19':'devetnaest',
   '20':'dvadeset',
   '30':'trideset',
   '40':'cetrdeset',
   '50':'pedeset',
   '60':'sezdeset',
   '70':'sedamdeset',
   '80':'osamdeset',
   '90':'devedeset',
   '100':'sto',
   '200':'dvjesto',
   '300':'tristo',
   '400':'cetristo',
   '500':'petsto',
   '600':'setsto',
   '700':'sedamsto',
   '800':'osamsto', 
   '900':'devetsto',
   '0':''}
b=[]
number=input()
numberLength=len(number)
number=int(number)
billion=number//1000000000
million=(number//1000000)%1000
thousand=(number//1000)%1000
remainder=number%1000
if billion>0:
    if billion==1:
        b.append('jedna')
        b.append('milijarda')
    if billion==2 or billion==3 or billion==4:
        b.append(str(billion))
        b.append('milijarde')
    if billion>4:
        b.append(str(billion))
        b.append('milijardi')
if million>0:
    hundredMillion=million//100
    hundredMillion=hundredMillion*100
    if hundredMillion>0:
        hundredMillion=str(hundredMillion)
        b.append(hundredMillion)
    if (million//10)%10==1:
        tenMillion=million%100
        tenMillion=str(tenMillion)
        b.append(tenMillion)
        b.append('miliona')
    else:
        tenMillion=(million//10)%10
        tenMillion=tenMillion*10
        if tenMillion>0:
            tenMillion=str(tenMillion)
            b.append(tenMillion)
        oneMillion=million%10
        if oneMillion>0:
            oneMillion=str(oneMillion)
            b.append(oneMillion)
            oneMillion=int(oneMillion)
            if oneMillion==1:
                b.append('milion')
            if oneMillion>1 and oneMillion<5:
                b.append('miliona')
            if oneMillion>4:
                b.append('miliona')
        if oneMillion==0:
            b.append('miliona')
if thousand>0:
    hundredThousand=thousand//100
    hundredThousand=hundredThousand*100
    if hundredThousand>0:
        hundredThousand=str(hundredThousand)
        b.append(hundredThousand)
    if (thousand//10)%10==1:
        tenThousand=thousand%100
        tenThousand=str(tenThousand)
        b.append(tenThousand)
        b.append('hiljada')
    else:
        tenThousand=(thousand//10)%10
        tenThousand=tenThousand*10
        if tenThousand>0:
            tenThousand=str(tenThousand)
            b.append(tenThousand)
        oneThousand=thousand%10
        if oneThousand>0:
            if oneThousand==1:
                b.append('jedna')
                b.append('hiljada_z')
            if oneThousand>1 and oneThousand<5:
                b.append(str(oneThousand))
                b.append('hiljade')
            if oneThousand>4:
                b.append(str(oneThousand))
                b.append('hiljada')
        if oneThousand==0:
            b.append('hiljada')
if remainder>0:
    hundredRemainder=remainder//100
    hundredRemainder=hundredRemainder*100
    if hundredRemainder>0:
        hundredRemainder=str(hundredRemainder)
        b.append(hundredRemainder)
    if (remainder//10)%10==1:
        tenRemainder=remainder%100
        tenRemainder=str(tenRemainder)
        b.append(tenRemainder)
    else:
        tenRemainder=(remainder//10)%10
        tenRemainder=tenRemainder*10
        if tenRemainder>0:
            tenRemainder=str(tenRemainder)
            b.append(tenRemainder)
        oneRemainder=remainder%10
        if oneRemainder>0:
            b.append(str(oneRemainder))

for i in range(len(b)):
    if b[i] not in a:
        winsound.PlaySound(b[i] + ".wav",winsound.SND_FILENAME)
    else:
        winsound.PlaySound(a[b[i]]+".wav",winsound.SND_FILENAME)
