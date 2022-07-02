class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if 8 > len(self.password) or len(self.password) > 15:
            raise Exception('Password should be longer than 8, and less than 15')
        
        check_num = list(filter(lambda x: x.isdigit(), self.password))
        if  len(check_num) == 0:
            raise Exception('Password should contain numbers too')

        check_alpha = list(filter(lambda x: x.isalpha(), self.password))
        if len(check_alpha) == 0:
            raise Exception('Password should contain letters as well')

        check_symbol = list(filter(lambda x: x in '@#&$%!~*', self.password))
        if len(check_symbol) == 0:
            raise Exception('Your password should have some symbols')
        
        return 'Ваш пароль сохранен.'

    def __str__(self):
        pass_length = len(self.password)
        return pass_length * '*'

password = Password('we@#3fdfe')

print(password.validate())