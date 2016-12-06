import hashlib
import itertools

door_id = 'uqwqemis'
password = ''
for index in itertools.count():
    token = door_id + str(index)
    hashed = hashlib.md5(token.encode('utf-8')).hexdigest()
    if hashed[:5] == '00000':
        print('found match')
        password += hashed[5]
        if len(password) == 8:
            print(password)
            break
