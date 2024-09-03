"""
Study the following pseudocode.
CASE OF MySwitch
1: ThisChar 'a'
2: ThisChar 'y'
3: ThisChar '7'
OTHERWISE: ThisChar '*'
ENDCASE
Write pseudocode with the same functionality without using a CASE structure.

"""

my_switch = "123" 

if my_switch == 1:
    this_char = "a"
elif my_switch == 2:
    this_char = "y"
elif my_switch == 3:
    this_char = "7"
else:
    this_char = "*"

print(this_char)
