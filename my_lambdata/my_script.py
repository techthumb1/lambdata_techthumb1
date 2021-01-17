# my_lambdata/my_script.py

import pandas
from trap_beat import TrapBeat
from trap_beat import Hip_Hop

print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

print("-----------------")
x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!