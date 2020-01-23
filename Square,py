e = "0"
square = [[0, 1], [0, 0], [1, 0], [1, 1]]
side_length = 29.2
x = "X" + str(square[3][0] * side_length + 95.4) + " "
y = "Y" + str(square[3][1] * side_length + 95.4) + " "
z = "Z" + str((1 * 28) / 100) + " "
gcode = "G1 " + x + y + z + "\n"
for i in range(1, 2):
    for j in range(0, 4):
        x = "X" + str(square[j][0] * side_length + 95.4) + " "
        y = "Y" + str(square[j][1] * side_length + 95.4) + " "
        z = "Z" + str((i * 28) / 100) + " "
        if i == 1:
            e = str(((side_length * 80) + float(e)*1000)/1000)
        else:
            e = str(((side_length * 64) + float(e) * 1000) / 1000)

        gcode = gcode + "G1 " + x + y + z + "E" + e + "\n"


print(str(gcode))
