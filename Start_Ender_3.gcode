M104 S215 ;start warming extruder
M105 ; check extruder temp
M109 S215 ; wait for extruder to heat
M82 ;absolute extrusion mode
M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration
M203 X500.00 Y500.00 Z10.00 E50.00 ;Setup machine max feedrate
M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk
M220 S100 ;Reset Feedrate
M221 S100 ;Reset Flowrate
G28 ;Home
G92 E0 ;Reset Extruder
G92 E-6
G92 E0 ;Reset Extruder
G1 Z2.0 F3000 ;Move Z Axis up
G1 F1500 ;Set speed
G1 X100.0 Y100.0 Z0.28 E0
G1 E6
G92 E0 ;Reset Extruder


;PASTE GCODE HERE 


G28; home
