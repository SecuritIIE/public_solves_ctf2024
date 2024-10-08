#!/usr/bin/python

from z3 import *

# Define the 100-character array
a = [BitVec(f'a[{i}]', 8) for i in range(100)]

# Create a solver instance
s = Solver()

# Add the constraints from the program
s.add(a[40] == 50)
s.add(a[11] == 48)
s.add(a[27] == a[26])
s.add(a[19] == a[18] - 4)
s.add(a[29] == a[28] - 47)
s.add(a[12] == a[11])
s.add(a[13] == 49)
s.add(a[23] == 53)
s.add(a[10] == a[9] + 3)
s.add(a[26] == 52)
s.add(a[36] == 100)
s.add(a[25] == 51)
s.add(a[22] == a[11] + 2)
s.add(a[34] == 98)
s.add(a[30] == 97)
s.add(a[18] == 55)
s.add(a[35] == 52)
s.add(a[17] == a[16] + 2)
s.add(a[28] == 101)
s.add(a[31] == a[11] + 8)
s.add(a[21] == 48)
s.add(a[33] == 57)
s.add(a[9] == 98)
s.add(a[39] == a[11] + 1)
s.add(a[37] == 99)
s.add(a[14] == a[11] + 52)
s.add(a[16] == 54)
s.add(a[20] == a[18] + 47)
s.add(a[32] == 101)
s.add(a[24] == a[22] + 2)
s.add(a[38] == 99)
s.add(a[15] == 56)
s.add(a[41] == 125)
s.add(a[8] == 123)
s.add(a[7] == 70)
s.add(a[6] == 84)
s.add(a[5] == 67)
s.add(a[4] == 69)
s.add(a[3] == 73)
s.add(a[2] == 73)
s.add(a[1] == 83)
s.add(a[0] == 70)

# Solve the constraints
if s.check() == sat:
    model = s.model()
    solution = ''.join([chr(model[a[i]].as_long()) for i in range(42)])
    print(solution)
else:
    print("No solution found")
