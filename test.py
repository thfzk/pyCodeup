y, m, d = input("(yyyy.mm.dd)입력 : ") .split(".")
m = "0" + m if len(m) == 1 else m
d = "0" + d if len(d) == 1 else d
print(f"{m}-{d}-{y}")