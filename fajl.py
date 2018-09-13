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
broj=input()
duzinaBroja=len(broj)
broj=int(broj)
milijarda=broj//1000000000
milioni=(broj//1000000)%1000
hiljade=(broj//1000)%1000
ostatak=broj%1000
if milijarda>0:
    if milijarda==1:
        b.append('jedna')
        b.append('milijarda')
    if milijarda==2 or milijarda==3 or milijarda==4:
        b.append(str(milijarda))
        b.append('milijarde')
    if milijarda>4:
        b.append(str(milijarda))
        b.append('milijardi')
if milioni>0:
    stoticeMiliona=milioni//100
    stoticeMiliona=stoticeMiliona*100
    if stoticeMiliona>0:
        stoticeMiliona=str(stoticeMiliona)
        b.append(stoticeMiliona)
    if (milioni//10)%10==1:
        deseticeMiliona=milioni%100
        deseticeMiliona=str(deseticeMiliona)
        b.append(deseticeMiliona)
        b.append('miliona')
    else:
        deseticeMiliona=(milioni//10)%10
        deseticeMiliona=deseticeMiliona*10
        if deseticeMiliona>0:
            deseticeMiliona=str(deseticeMiliona)
            b.append(deseticeMiliona)
        jediniceMiliona=milioni%10
        if jediniceMiliona>0:
            jediniceMiliona=str(jediniceMiliona)
            b.append(jediniceMiliona)
            jediniceMiliona=int(jediniceMiliona)
            if jediniceMiliona==1:
                b.append('milion')
            if jediniceMiliona>1 and jediniceMiliona<5:
                b.append('miliona')
            if jediniceMiliona>4:
                b.append('miliona')
        if jediniceMiliona==0:
            b.append('miliona')
if hiljade>0:
    stoticeHiljada=hiljade//100
    stoticeHiljada=stoticeHiljada*100
    if stoticeHiljada>0:
        stoticeHiljada=str(stoticeHiljada)
        b.append(stoticeHiljada)
    if (hiljade//10)%10==1:
        deseticeHiljada=hiljade%100
        deseticeHiljada=str(deseticeHiljada)
        b.append(deseticeHiljada)
        b.append('hiljada')
    else:
        deseticeHiljada=(hiljade//10)%10
        deseticeHiljada=deseticeHiljada*10
        if deseticeHiljada>0:
            deseticeHiljada=str(deseticeHiljada)
            b.append(deseticeHiljada)
        jediniceHiljada=hiljade%10
        if jediniceHiljada>0:
            if jediniceHiljada==1:
                b.append('jedna')
                b.append('hiljada_z')
            if jediniceHiljada>1 and jediniceHiljada<5:
                b.append(str(jediniceHiljada))
                b.append('hiljade')
            if jediniceHiljada>4:
                b.append(str(jediniceHiljada))
                b.append('hiljada')
        if jediniceHiljada==0:
            b.append('hiljada')
if ostatak>0:
    stoticeOstatka=ostatak//100
    stoticeOstatka=stoticeOstatka*100
    if stoticeOstatka>0:
        stoticeOstatka=str(stoticeOstatka)
        b.append(stoticeOstatka)
    if (ostatak//10)%10==1:
        deseticeOstatka=ostatak%100
        deseticeOstatka=str(deseticeOstatka)
        b.append(deseticeOstatka)
    else:
        deseticeOstatka=(ostatak//10)%10
        deseticeOstatka=deseticeOstatka*10
        if deseticeOstatka>0:
            deseticeOstatka=str(deseticeOstatka)
            b.append(deseticeOstatka)
        jediniceOstatka=ostatak%10
        if jediniceOstatka>0:
            b.append(str(jediniceOstatka))

for i in range(len(b)):
    if b[i] not in a:
        winsound.PlaySound(b[i] + ".wav",winsound.SND_FILENAME)
    else:
        winsound.PlaySound(a[b[i]]+".wav",winsound.SND_FILENAME)
    
