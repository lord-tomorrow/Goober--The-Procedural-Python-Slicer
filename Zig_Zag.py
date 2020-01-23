from math import *

gcode = ""
e = "0"
switch = 0
side_length = 19.6
origin_offset = 110 - side_length/2

for i in range(1, 5):
    for j in range(0, int(floor(side_length / 0.2))):
        if i % 2 != 0:
            if j < int(floor(side_length / 0.2)) * 0.5:
                f1 = j * 0.4 + origin_offset
                f2 = (j - 1) * 0.4 + origin_offset
                f3 = side_length + origin_offset - side_length
            else:
                f1 = (j - 1) * 0.4 + origin_offset - side_length
                f2 = j * 0.4 + origin_offset - side_length
                f3 = side_length + origin_offset
            square = [[f3, f1, f1, f3], [f2, f1, f3, f3], [f1, f3, f3, f1], [f3, f3, f2, f1]]
            xmul1 = square[switch][0]
            xmul2 = square[switch][1]
            ymul1 = square[switch][2]
            ymul2 = square[switch][3]
            x = "X" + str(xmul2) + " "
            y = "Y" + str(ymul2) + " "
            if switch == 3:
                switch = 0
            else:
                switch += 1

        else:
            if j < int(floor(side_length / 0.2)) * 0.5:
                f1 = j * 0.4 + origin_offset
                f2 = (j - 1) * 0.4 + origin_offset
                f3 = side_length + origin_offset - side_length
            else:
                f1 = (j - 1) * 0.4 + origin_offset - side_length
                f2 = j * 0.4 + origin_offset - side_length
                f3 = side_length + origin_offset
            square = [[f3, f1, f1, f3], [f2, f1, f3, f3], [f1, f3, f3, f1], [f3, f3, f2, f1]]
            xmul1 = square[switch][0]
            xmul2 = square[switch][1]
            ymul1 = square[switch][2]
            ymul2 = square[switch][3]
            x = "X" + str(-xmul2 + 220) + " "
            y = "Y" + str(ymul2) + " "
            if switch == 3:
                switch = 0
            else:
                switch += 1

        z = "Z" + str((i * 28) / 100) + " "
        distance = sqrt((xmul1 - xmul2) ** 2 + (ymul1 - ymul2) ** 2)
        if i == 1:
            if j != 0:
                e = str(distance * 0.08 + float(e))

        else:
            e = str(distance * 0.08 + float(e))

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"


print(str(gcode))
