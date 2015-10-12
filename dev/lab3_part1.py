from Crypto.Hash import SHA256

# random comment

users = {}
user_count = 0
while True:
    user_id = input('user #' + str(user_count) + ': ')
    if user_id == '':
        break
    users[user_id] = SHA256.new(str.encode(input('password: '))).hexdigest()
    user_count += 1


#Scott needs to learn how to use gitHub

#comment lol


while True:
    user_id = input('username: ')
    if user_id not in users:
        print('user not found')
        continue
    password = input('password: ')
    if users[user_id] != SHA256.new(str.encode(password)).hexdigest():
        print('login fails')
    else:
        print('login succeeds')

