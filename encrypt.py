#!/usr/bin/python

import sys
import struct
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
	key = file("aes.key",'rb').read()
	data = file(sys.argv[1], 'rb').read()
	lng = len(data)
	fill = (int((lng + 15) / 16) * 16) - lng
	head = struct.pack('L',lng)
	packs = data + '\xFF' * fill
	encryptor = AES.new(key, mode)
	encrypted = encryptor.encrypt(packs)
	outfile = file(outname, 'wb')
	outfile.write(head)
	outfile.write(encrypted)
	outfile.close()

