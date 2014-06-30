#!/usr/bin/python

import sys
import struct
import hashlib
from Crypto.Cipher import AES

password = "123456"
salt = "7654321"
mode = AES.MODE_ECB

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 3:
		outname = sys.argv[2]
	else:
		nlen = len(sys.argv[1])
		if (nlen > 4) and (sys.argv[1][nlen-4:nlen] == ".aes"):
			outname = sys.argv[1][0:nlen-4]
		else:
			outname = sys.argv[1]+".deaes"
	key = file("aes.key",'rb').read()
	data = file(sys.argv[1], 'rb').read()
	lng = struct.unpack('L',data[0:8])[0]
	decryptor = AES.new(key, mode)
	decrypted = decryptor.decrypt(data[8:])
	file(outname, 'wb').write(decrypted[:lng])
