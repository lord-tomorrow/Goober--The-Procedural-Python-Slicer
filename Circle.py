from math import *


gcode = ""
e = "0"

radius = 10
cir_def = 59
origin_m = 110 - radius
cirdeftorad = cir_def/2/pi
for i in range(1, 2):
    for j in range(0, cir_def):
        x = "X" + str(sin(j/cirdeftorad) * radius + origin_m) + " "
        y = "Y" + str(cos(j/cirdeftorad) * radius + origin_m) + " "
        z = "Z" + str((i * 28) / 100) + " "
        xmul1 = sin(j / cirdeftorad) * radius + origin_m
        xmul2 = sin((j + 1) / cirdeftorad) * radius + origin_m
        ymul1 = cos(j / cirdeftorad) * radius + origin_m
        ymul2 = cos((j + 1) / cirdeftorad) * radius + origin_m
        distance = sqrt((xmul1 - xmul2) ** 2 + (ymul1 - ymul2) ** 2)
        if i == 1:
            if j == 0:
                bro = 1+1
            else:
                e = str(distance * 0.08 + float(e))

        else:
            e = str(distance * 0.08 + float(e))

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"


print(str(gcode))
