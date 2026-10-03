def is_valid_part(part):
    try:
        code = int(part)
        if part[0] == '0' and len(part) > 1:
            return False
        return 0 <= code < 256
    except ValueError as ve:
        return False

# print(is_valid_part('123')), print(is_valid_part('aaa')) ,print(is_valid_part('-224')), print(is_valid_part('016')), print(is_valid_part('01')), print(is_valid_part('0')), print(is_valid_part('12')), print(is_valid_part('00'))

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True


#print(is_valid_ip('192.168.0.1'))
#print(is_valid_ip('192.168.0.000'))
#print(is_valid_ip('192.168.1.256'))
#print(is_valid_ip('192.168.1'))

def decimal_to_binary(n):
    if n == 0: return 0
    if n == 1: return 1
    next = n // 2
    digit = n % 2
    res = decimal_to_binary(next)
    return str(res) + str(digit)




#print(decimal_to_binary(34))
#print(decimal_to_binary(212))
#print(decimal_to_binary(252))

def binary_to_decimal(b:str):
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))


# Test cases
#print(decimal_to_binary(10))  # "1010"
#print(decimal_to_binary(255))  # "11111111"
#print(decimal_to_binary(1))  # "1"

def ip_to_binary(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    binary_ip = ''
    for part in parts:
        if not is_valid_part(part):
            return False
        else:
            return binary_ip + decimal_to_binary(int(part)) + '.'

    return binary_ip[:-1]



print(ip_to_binary('192.168.1.16'))
