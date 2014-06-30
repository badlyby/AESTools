#!/usr/bin/python
import random
key = ""
for i in range(0,32):
	key = key + chr(random.randint(0,255))
file("aes.key",'wb').write(key)
