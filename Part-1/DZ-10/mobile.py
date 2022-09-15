def check_phone(phone):
    operators_codes = ('067', '097', '050', '066', '099', '063', '093')
    correct_len = 10
    return len(phone) == correct_len and phone[0:3] in operators_codes

def get_operator(phone):
    operator_K = ('067', '097')
    operator_V = ('050', '066', '099')
    operator_L = ('063', '093')

    code = phone[0:3]

    if code in operator_K:
        return 'K'
    elif code in operator_V:
        return 'V'
    elif code in operator_L:        
        return 'L' 
    else:
        return None
def print_error(error_code, phone):
    if error_code == 1:
        print('Operator not supported -', phone)
    elif error_code == 2:
        print('Incorrect phone', phone)
source_file = 'E:\Git\GOIteens_PY_10\Homework\DZ-10\phones.txt'

K_file = 'E:\Git\GOIteens_PY_10\Homework\DZ-10\phones-K.txt'
V_file = 'E:\Git\GOIteens_PY_10\Homework\DZ-10\phones-V.txt'
L_file = 'E:\Git\GOIteens_PY_10\Homework\DZ-10\phones-L.txt'

K_file = open(K_file, 'a')
V_file = open(V_file, 'w')
L_file = open(L_file, 'w')

files = {'K': K_file, 'L': L_file, 'V': V_file}

delimiter = '\n'

try:
    with open(source_file, 'r') as f:
        while True: 
            phone = f.readline().rstrip(delimiter)
            if not phone: 
                break
            phone.rstrip(delimiter)
            if(check_phone(phone)):
                operator = get_operator(phone)
                if operator:
                    handle = files[operator]
                    handle.write(phone+delimiter)
                else:
                    print_error(1, phone)
            else:
                print_error(2, phone)

finally:
    for handle in files.values():
        handle.close()