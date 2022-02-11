#Surprise your friends computer with just 6 line of python code
#You can put computer screen upside down 

import rotatescreen
import time
from time import strftime


screen = rotatescreen.get_primary_displays()
screen.rotate_to(0)
for i in range(10):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)
    