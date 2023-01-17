from JFutils import *
import random

x = Map((15, 36))
x.fill_bottom()
x.seprate_row(4, (5, 4), 2)
x.seprate_row(7, (5, 4), 2)
x.seprate_row(12, (9, 3), 1)
x.set_start_pos()

for i in range(5, 36, 7):
    x.set_object((2, i), LIU_BING_REN)

for i in range(7, 36, 9):
    x.set_object((2, i), SHANG_PEN_HUO_LONG)

for i in range(1):
    x.set_object((5, random.randint(1, 36)), WU_YA)
for i in range(3):
    x.set_object((8, random.randint(1, 36)), WU_YA)    
for i in range(3, 36, 9):
    if i + 4 <= 36:
        x.set_object((5, i + random.randint(0, 4)), HUANG_SHE_TOU_GUAI)
for i in range(2, 36, 12):
    if i + 8 <= 36:
        x.set_object((13, i + random.randint(0, 8)), XIA_PEN_HUO_LONG)
    x.set_object((13, 15), XIA_PEN_HUO_LONG)
x.toxml(1)