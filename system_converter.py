print("================================")
print("        SYSTEM CONVERTER        ")
print("================================")
print("Convert a decimal number into "
      "binary, octal and hexadecimal.\n")

while True:
    num = int(input("Insert number to be converted: "))

    def binary(num):   
        nib = ""
        
        if num == 0:
            return "0"
        
        while num > 0:    
            nib += str(num % 2)  
            num //= 2  
        
        return nib[::-1]

    def oct(num):
        num = binary(num)[::-1]
        tco = ""
        count = 0
        
        while len(num)%3 != 0:
            num += "0"
        
        while count != len(num):
            sect = num[(count):(count+3)]
            div = 0
            for index, _ in enumerate(sect):
                result = int(_)*2**index
                div += result
            tco += str(div)
            count += 3
        
        return tco[::-1]

    def hex(num):
        num = binary(num)[::-1]
        hex=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "A", "B", "C", "D", "E", "F"]
        tco = ""
        count = 0
        
        while len(num)%4 != 0:
            num += "0"
        
        while count != len(num):
            sect = num[(count):(count+4)]
            div = 0
            for index, _ in enumerate(sect):
                result = int(_)*2**index
                div += result
            tco += hex[div]
            count += 4
        
        return tco[::-1]

    print(f"BIN {binary(num)}\nOCT {oct(num)}\nHEX {hex(num)}\n")