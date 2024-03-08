def BinToDec(b):
return int(b, 2)

print("Enter the Binary Number: ", end="")
bnum = input()
dnum = BinToDec(bnum)
print("\nEquivalent Decimal Value = ", dnum)

def OctToHex(o):
return hex(int(o, 8))

print("Enter Octal Number: ", end="")
onum = input()
hnum = OctToHex(onum)
print("\nEquivalent Hexadecimal Value =", hnum[2:].upper())