

ciphertext = 'iehho de cehu sxesebqju rqhi'

for i in range(0,26):
	sentence = ''
	for ch in ciphertext:
		if ch == ' ':
			new_ch = ord(ch)
		else:
			new_ch = ord(ch) - 1
		sentence += chr(new_ch)
	print(ciphertext)

	ciphertext = sentence

	print(2)

	print(1)
