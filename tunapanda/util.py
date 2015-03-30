import crypt,getpass
import random
from optparse import OptionParser

## The next two fcns are from
## https://github.com/uphillian/misc/blob/master/cryptpass
def gensalt(length=8):
	ALPHA = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	salt=[]
	for i in range(length):
		salt.append(random.choice(ALPHA))
	return "".join(salt)

# 6 is sha512
def shadowcrypt(password,saltlen=8,hashalgo=6,salt=None):
	if salt == None:
		salt = gensalt(saltlen)
  	return crypt.crypt(password,'$%s$%s$' % (hashalgo,salt))
