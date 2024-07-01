s = "123 3.14 True string"


tp = int, float, bool, str


# res = [(tp[idx],val) for idx, val  in enumerate(s.split())]

# res = [(tp[idx](val)) for idx, val  in enumerate(s.split())]


# print(res)

# from math import *

# print (eval("log10(100)"))


data = 2,7,2021


match data:
    case 1,7,2024 | 2025:
        print("1 июля в этом или в следующем году")
    case 1, 7, _:
        print("1 июля")
    case *_, 2024:
        print("В этом году")
    case _, _, year:
        print(year,'год')
    case _:
        print("Неправильный ввод")