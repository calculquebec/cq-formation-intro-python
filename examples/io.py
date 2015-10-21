import math
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
infile = "numbers"
outfile = "f_numbers"

f = open(os.path.join(data_dir, infile), 'r')
g = open(os.path.join(data_dir, outfile), 'w')

def func(y):
    if y >= 0.0:
        return y**5.0*math.exp(-y)
    else:
        return 0.0

for line in f:
    line = line.split()
    x, y = float(line[0]), float(line[1])
    g.write("%g %12.5e\n" % (x,func(y)))

f.close()
g.close()

