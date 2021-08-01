import random
import string
len1 = int(input("Enter the length of element"))
OTP= ''
characters = string.ascii_letters+ string.digits
for i in range(len1):
  OTP = OTP + random.choice(characters)
print('OTP ',OTP)