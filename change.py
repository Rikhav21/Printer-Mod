# postprocess_lasergrbl_g1_x_s.py

import re

input_file = "input.nc"       # original LaserGRBL file
output_file = "output.gcode"  # new file for Klipper

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        line = line.rstrip()

        # Move all S<number> to their own line as S S=<number>
        matches = re.findall(r'S\d+', line)
        line_no_s = re.sub(r'S\d+', '', line).strip()

        # Prepend G1 if line starts with X or Y and does not already have G1
        if line_no_s and re.match(r'^[XY]', line_no_s):
            line_no_s = "G1 " + line_no_s

        # Write the motion line without S (if not empty)
        if line_no_s:
            f_out.write(line_no_s + "\n")

        # Write each S<number> on its own line
        for m in matches:
            number = m[1:]  # remove the 'S'
            f_out.write(f"S S={number}\n")
