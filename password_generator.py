import random
import string

length = int (input('Enter the lenght of the password u want! '))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for i in range(length))
print ('Your password is: ', password)

