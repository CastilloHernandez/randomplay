import os
import random

dir='e:\\temp\\'
file=random.choice(os.listdir(dir))
print file
os.startfile(dir + file)