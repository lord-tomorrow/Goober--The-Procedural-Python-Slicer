from math import *


e = "0"
switch = 0
side_length = 70
origin_offset = 110 - side_length/2
gcode = ""
inf_sl = side_length - 0.8
inf_offset = 110 - inf_sl/2

for i in range(1, 5):
    for j in range(0, 5):
        square = [[0, 1], [0, 0], [1, 0], [1, 1], [0, 1]]
        x = "X" + str(square[j][0] * side_length + origin_offset) + " "
        y = "Y" + str(square[j][1] * side_length + origin_offset) + " "
        z = "Z" + str((i * 28) / 100) + " "
        if i == 1:
            if j != 0:
                e = str(side_length * 0.08 + float(e))

            else:
                e = str(0 + float(e))

        else:
            if j != 0:
                e = str(side_length * 0.06 + float(e))

            else:
                e = str(0 + float(e))

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"

    for k in range(0, int(floor(inf_sl / 0.2))):
        if i % 2 != 0:
            if k < int(floor(inf_sl / 0.2)) * 0.5:
                f1 = k * 0.4 + inf_offset
                f2 = (k - 1) * 0.4 + inf_offset
                f3 = inf_offset
            else:
                f1 = (k - 1) * 0.4 + inf_offset - inf_sl
                f2 = k * 0.4 + inf_offset - inf_sl
                f3 = inf_sl + inf_offset
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
            if k < int(floor(inf_sl / 0.2)) * 0.5:
                f1 = k * 0.4 + inf_offset
                f2 = (k - 1) * 0.4 + inf_offset
                f3 = inf_offset
            else:
                f1 = (k - 1) * 0.4 + inf_offset - inf_sl
                f2 = k * 0.4 + inf_offset - inf_sl
                f3 = inf_sl + inf_offset
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
            if k != 0:
                e = str(distance * 0.08 + float(e))

            else:
                e = str(float(e))

        else:
            if k != 0:
                e = str(distance * 0.06 + float(e))

            else:
                e = str(float(e))

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"

print(str(gcode))
