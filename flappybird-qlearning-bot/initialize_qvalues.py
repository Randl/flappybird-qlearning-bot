import json
from itertools import chain

# Script to create Q-Value JSON file, initilazing with zeros

qval = {}
# X -> [-40,-30...120] U [140, 210 ... 420]
# Y -> [-300, -240, -180] U [-170, -160... 160] U [180, 240 ... 420]
for x in chain(list(range(-40, 140, 5)), list(range(140, 421, 70))):
	for y in chain(chain(list(range(-300, -180, 60)), list(range(-180, 180, 5)), list(range(180, 421, 60)))):
			for v in range(-10, 11):
				if y > 0:
					qval[str(x) + '_' + str(y) + '_' + str(v)] = [1, 0]
				else:
					qval[str(x) + '_' + str(y) + '_' + str(v)] = [0, 1]

with open('qvalues.json', 'w') as fd:
	json.dump(qval, fd)

with open('scores.txt', 'w') as scores:
	scores.write('')
