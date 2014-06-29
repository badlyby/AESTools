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
		outname = sys.argv[1]+".aes"
	key = hashlib.sha1(password+salt).digest()+ '\xAA\xBB\xCC\xDD'
	data = file(sys.argv[1], 'rb').read()
	lng = len(data)
	fill = (int((lng + 8 + 15) / 16) * 16) - lng - 8
	head = struct.pack('L',lng)
	packs = head + data + '\xFF' * fill
	encryptor = AES.new(key, mode)
	encrypted = encryptor.encrypt(packs)
	file(outname, 'wb').write(encrypted)

