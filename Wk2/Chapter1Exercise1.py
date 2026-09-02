## "If a number ends in 0.5, does Python round up or down?"

## AI Answer:  Neither, consistently — Python 3 uses banker's rounding (round half to even).
## On an exact 0.5, it rounds toward the nearest even integer. The idea is to avoid the upward bias
#  you'd get from always rounding halves up.

print (round(0.5)) # 0
print (round(1.5))  # 2
print (round(2.5))  # 2
print (round(3.5))  # 4