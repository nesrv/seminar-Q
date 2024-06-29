s = "123 3.14 True string"


tp = int, float, bool, str


# res = [(tp[idx],val) for idx, val  in enumerate(s.split())]

res = [(tp[idx](val)) for idx, val  in enumerate(s.split())]


print(res)

from math import *

print (eval("log10(100)"))