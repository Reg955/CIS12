sec=1
min=60*sec
hr = min*60
km=1
mile=1.61


a = min*42 + sec*42
print(a)
d = km/mile*10
print(d)

pace = a/d
print(pace)
minpace = pace/60
print(minpace)

hrpace = d / (a / (1*hr))
print(hrpace)
print(6.211180124223602 / (2562 / 3600))

# 1) 2562 seconds
# 2) 6.211180124223602 miles
# 3) 412.482 sec/mile
# 4) 6.874700000000001 min/mile
# 5) 8.727
