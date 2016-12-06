import hashlib
import itertools

door_id = 'uqwqemis'
password = {str(i): None for i in range(8)}
for index in itertools.count():
    token = door_id + str(index)
    hashed = hashlib.md5(token.encode('utf-8')).hexdigest()
    if hashed[:5] == '00000':
        pword_index = hashed[5]
        pword_val = hashed[6]
        if pword_index not in password:
            print(pword_index, 'out of range')
            continue
        if password[pword_index]:
            print('discarding', pword_index, 'already taken')
            continue

        print('setting index', pword_index, 'to', pword_val)
        password[pword_index] = pword_val

        if None not in password.values():
            break
print(''.join(password[str(i)] for i in range(8)))
