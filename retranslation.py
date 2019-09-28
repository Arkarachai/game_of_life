from __future__ import print_function
import string
import sys

genetic_dict = {'F': 'UUU',
                'L': 'UUA',
                'I': 'AUU',
                'M': 'AUG',
                'V': 'GUU',
                'S': 'UCU',
                'P': 'CCU',
                'T': 'ACU',
                'A': 'GCU',
                'Y': 'UAU',
                'H': 'CAU',
                'Q': 'CAA',
                'N': 'AAU',
                'K': 'AAA',
                'D': 'GAU',
                'E': 'GAA',
                'C': 'UGU',
                'W': 'UGG',
                'R': 'CGU',
                'G': 'GGU',
              #  'O': 'UAA-chre',
              #  'U': 'UGC-S+Se', #UGA-mber
                }

all_string = set(string.ascii_uppercase)
all_key = set(genetic_dict.keys())
no_available = all_string - all_key
#sequence = input('input your sequence: ')
sequence=sys.argv[1]
sequence = sequence.strip().replace(' ', '').upper()
valid_seq = True
for i in sequence:
    if i in no_available:
        print('characters {0} are not available'.format(no_available))
        valid_seq = False
        break
if valid_seq:
    print('{0} to {1}'.format(sequence, ' '.join(map(lambda x: genetic_dict[x], sequence))))
