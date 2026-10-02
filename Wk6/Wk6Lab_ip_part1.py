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
    for part in (ip.split('.')):
        if not is_valid_part(part):
            return False
    return True


print(is_valid_ip('192.168.0.1'))
print(is_valid_ip('192.168.0.000'))
print(is_valid_ip('192.168.1.256'))
