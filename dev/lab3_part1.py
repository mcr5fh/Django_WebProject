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

<<<<<<< HEAD
<<<<<<< HEAD
#comment_Matt
=======
#hahah
=======

#Scott needs to learn how to use gitHub

>>>>>>> 0ec73ef5446257f55f52b5b5cf5e707dc035ee21
#comment lol
>>>>>>> 27e18e23105347e1d397ff98f768fafd4f89922f


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

