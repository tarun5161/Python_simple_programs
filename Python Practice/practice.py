weight = int(input("weight:"))
unit = input("(L)bs or (K)g:")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"your {converted} kilos")
else:
    converted = weight / 0.45
    print(f"your {converted} pounds")
