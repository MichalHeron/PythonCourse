username = input('username: ')
password = input('password: ')
print(username + ', your password ' + '*' * len(password) + ', is ' + str(len(password)) + ' letter long')

password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password {hidden_password}, is {password_length} letters long')
