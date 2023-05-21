import random
#
values = {}
values['1'] = 16
values['2.'] = 12
values['2'] = 8
#values['2-3'] = 5+(1/3)
values['4.'] = 6
values['4'] = 4
#values['4-3'] = 2+(2/3)
values['8.'] = 3
values['8'] = 2
#values['8-3'] = 1+(1/3)
values['16'] = 1
#values['32'] = 0.5
values['gallop'] = 4
#values['quarter_triplets'] = 8
#values['eighth_triplets'] = 4
#
notes = [key for key in values.keys()]
#
class Measure:
    def __init__(self,time_sig):
        time_sig = time_sig.split('/')
        self.time_sig_a = time_sig[0]
        self.time_sig_b = time_sig[1]
        self.total_length = int(self.time_sig_a) * values[self.time_sig_b]
        self.length = 0
        self.notes = []
    def generate(self):
        while self.length < self.total_length:
            num = random.randint(1,len(notes)-1)
            note = notes[num]
            if self.length + values[note] <= self.total_length:
                self.notes.append(note)
                self.length += values[note]
    def print_notes(self):
        self.measure = [f'1/{note}' if not note == 'gallop' else '1/16, 1/16, 1/8' for note in self.notes]
        self.measure = ', '.join(self.measure)
        print(f'{self.measure=}')
    
        
#
measures = int(input(f'Enter number of measures to djenerate> '))
time_sig = input(f'Enter the time signature> ')
#
for i in range(measures):
    new = Measure(time_sig)
    new.generate()
    new.print_notes()