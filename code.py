weight = int(input("Weight: "))
unit =  input("(L)bs or (K)g : ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"{weight} pounds is equal to {converted} kilos")
else:
    converted= weight / 0.45
    print(f"{weight} kilos is equal to {converted} pounds")
