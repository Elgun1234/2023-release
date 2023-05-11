def ConvertToBinary(DecimalNumber):
    BinaryString = ""
    while DecimalNumber > 0:
        Remainder = DecimalNumber % 2
        Bit = str(Remainder)
        BinaryString = Bit + BinaryString
        DecimalNumber = DecimalNumber // 2
    while len(BinaryString) < 4:
        BinaryString = '0' + BinaryString
    return BinaryString

print(ConvertToBinary(7))
print(ConvertToBinary(7).count("1"))
