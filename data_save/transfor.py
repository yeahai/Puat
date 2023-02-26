# 2023/1/30 19:44
# 你好，夜嗨大帅比
import binascii

# String trans to Hex
def str_to_hex(string):
    str_bin = string.encode('utf-8')
    return binascii.hexlify(str_bin).decode('utf-8')

# Hex trans to String
def hex_to_str(hex_str):
    hex = hex_str.encode('utf-8')
    return binascii.unhexlify(hex).decode('utf-8')


def bin_to_ten(bin):
    ten = int(bin,2)
    return ten

def bin_to_eight(bin):
    eight = oct(bin)
    return eight

def bin_to_hex(bin):
    ten = bin_to_ten(bin)
    hex_ = hex(ten).split('0x')[1]
    return hex_

def four_to_hex(four):
    pass

def eight_to_hex(eight):
    pass

def ten_to_hex(ten):
    pass

def threeTwo_to_hex(threeTwo):
    pass

def sixFour_to_hex(sixFour):
    pass

def baseN(num,b):
    return ((num == 0) and "0") or \
           (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])



# 64






# b = "我是你"
# c = "e68891e698afe4bda0"
# a = str_to_hex(b)
# d = hex_to_str(c)
# print(a)
# print(d)
# bin = '100010001000110010011100010101'
# bin1 = '1111'
# a = bin_to_hex(bin1)

# ten_to_32 = baseN(111,64)
ten_to_64 = encode_b64("111")
# print(ten_to_32)
print(ten_to_64)
