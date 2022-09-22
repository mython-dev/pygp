
import random

logo = f'''
                             ____         ____       
                            |  _ \ _   _ / ___|_ __  
                            | |_) | | | | |  _| '_ \ 
                            |  __/| |_| | |_| | |_) |
                            |_|    \__, |\____| .__/ 
                                   |___/      |_|  
                        
                              VERSION-TOOL: 1.0
                          By MYTHON-DEV or MYTH-DEV
                  Instagram: @mython_dev and @hackingworld_d   

\\\ Для чего нужен генератор паролей?

\\\ Сгенерированные пароли считаются надежными, потому что они случайны. 
\\\ То есть они генерируются с использованием алгоритма.
\\\ Можно сгенерировать разные виды паролей: 
\\\ короткий и легкий (который можно даже запомнить) 
\\\ а также сложный (максимально длинная и запутанная комбинация).

'''
print(logo)

choose_length = input('Введите длину пароля: ')

password_lower = 'abcdefghijklmnopqrstuvwxyz'

password_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

nums = '1234567890'

symbols = '!@#$%^&*()'

def password():
    password = password_lower + password_upper + nums + symbols
    print_password  = "".join(random.sample(password, int(choose_length)))
    print('Ваш пароль: ' + print_password)

password()
