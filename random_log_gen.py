import random
import string

def generator(size):
    gen = (random.choice(string.ascii_letters) for _ in range(size))
    rand_string = ''.join(gen)
    return rand_string

file_log = open('./temp_log', 'a')
strings = 10000000
current_pos = 0
while current_pos < strings:
    string_log = 'test_serv1 {0} test_log \n'.format(generator(20))
    file_log.write(string_log)
    current_pos += 1
file_log.close()

print('file ended')
