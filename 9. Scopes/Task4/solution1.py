balance = 0

def get_salary(amount):
    global balance
    balance += amount

def pay_bills(amount, log_name):
    global balance
    balance -= amount
    print(f'Вы заплатили {amount} сом за {log_name}')

def get_balance():
    print(f'У вас на счету {balance} сом')

get_salary(1000000)
get_balance()
pay_bills(450000, 'аренду дома')
get_balance()