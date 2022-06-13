from random import randint

def generate_name():
    part1 = ['an','aen','al','am','ar','as','af','at','aj','ab','ad','ban','baen','bal','bam','bar','bas','baf','bat','baj','can','caen','cal','cam','car','cas','caf','caj','cab','cad','dan','daen','dal','dam','dar','das','daf','dat','daj','jan','jaen','jal','jam','jar','jas','jaf','jat','jab','jad','kan','kaen','kal','kam','kar','kas','kaf','kat','kaj','kab','kad','ran','raen','ral','ram','ras','raf','raj','rab','rad','zan','zaen','zal','zam','zar','zas','zaf','zat','zaj','zab','zad',]
    part2 = ['jan','jas','jal','lan','lam','las','laj','lar','ral','than','thal','thaj','thaz','sal','san','sar','saj','sath',]
    part3 = ['thous','tous','tor','tal','ton','sar','izar','izod','izal','izon','izom','thia',]
    
    a,b,c = randint(0,len(part1)-1),randint(0,len(part2)-1),randint(0,len(part3)-1)
    return part1[a]+part2[b]+part3[c]

print(generate_name())