from math import *


gcode = ""
e = "0"
radius = 2.5
cir_res = 6
cir_res_to_radians = cir_res/2/pi
seperation = 10
size = 7
origin_offset = 110 - (seperation * size) / 2 + seperation / 2
temp = 220
retract_speed = 61
retract_distance = 5.7
for i in range(5, 147):
    radius = radius - (i ** 0.25)/200
    # gcode += "M104 " + str(temp - (i - 5) / 4.733) + "\n"
    for j in range(0, size):
        # retract_speed = j * 60/size + 1
        for k in range(0, size):
            # retract_distance = k * 10/size
            gcode += "G1 " + "E" + str(float(e) - retract_distance) + " F" + str(retract_speed * 60) + "\n"
            x = "X" + str(k * seperation + origin_offset + sin((cir_res - 1) / cir_res_to_radians) * radius) + " "
            y = "Y" + str(j * seperation + origin_offset + cos((cir_res - 1) / cir_res_to_radians) * radius) + " "
            z = "Z" + str((i * 28) / 100) + " "
            gcode = gcode + "G1 " + x + y + z + "F9000" + "\n"
            gcode += "G1 " + "E" + str(float(e)) + " F" + str(retract_speed * 60) + "\n"
            gcode += "G1 " + "F3000" + "\n"
            for m in range(0, cir_res):
                x = "X" + str(k * seperation + origin_offset + sin(m/cir_res_to_radians) * radius) + " "
                y = "Y" + str(j * seperation + origin_offset + cos(m/cir_res_to_radians) * radius) + " "
                z = "Z" + str((i * 28) / 100) + " "
                xmul1 = sin(m / cir_res_to_radians) * radius
                xmul2 = sin((m + 1) / cir_res_to_radians) * radius
                ymul1 = cos(m / cir_res_to_radians) * radius
                ymul2 = cos((m + 1) / cir_res_to_radians) * radius
                distance = sqrt((xmul1 - xmul2) ** 2 + (ymul1 - ymul2) ** 2)
                # if m != 0:
                e = str(distance * 0.08 + float(e))

                gcode += "G1 " + x + y + z + "E" + e + "\n"


print(str(gcode))
