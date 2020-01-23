from math import *


gcode = ""
e = "0"

radius = 0
cir_res = 120
origin_m = 110 - radius
cir_res_to_radians = cir_res/6/pi
size = 0.2
for i in range(1, 20):
    for j in range(0, cir_res):
        if j < 0.25/pi * cir_res:
            cir_res_to_radians = cir_res / 30 / pi

        else:
            cir_res_to_radians = cir_res / 3 / pi

        x = "X" + str(sin(j/cir_res_to_radians) * size * (radius - j) + origin_m) + " "
        y = "Y" + str(cos(j/cir_res_to_radians) * size * (radius - j) + origin_m) + " "
        z = "Z" + str((i * 28) / 100) + " "
        xmul1 = sin(j / cir_res_to_radians) * size * (radius - j) + origin_m
        xmul2 = sin((j - 1) / cir_res_to_radians) * size * (radius - j) + origin_m
        ymul1 = cos(j / cir_res_to_radians) * size * (radius - j) + origin_m
        ymul2 = cos((j - 1) / cir_res_to_radians) * size * (radius - j) + origin_m
        distance = sqrt((xmul1 - xmul2) ** 2 + (ymul1 - ymul2) ** 2)
        '''if i == 1:
            if j == 0:
                e = "0"

            else:
                e = str(distance * 0.08 + float(e))

        else:
            e = str(distance * 0.08 + float(e))'''
        e = str(distance * 0.08 + float(e))
        if distance == 0:
            e = str(float(e) + 3)

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"


print(str(gcode))
