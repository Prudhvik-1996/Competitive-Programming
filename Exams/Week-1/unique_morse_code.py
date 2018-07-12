def genmorsecode(st):
	mc = ""
	for i in st:
		if i == 'A' or i == 'a': mc+=".-"
		elif i == 'B' or i == 'b': mc += "-..."
		elif i == 'C' or i == 'c': mc += "-.-."
		elif i == 'D' or i == 'd': mc += "-.."
		elif i == 'E' or i == 'e': mc += "."
		elif i == 'F' or i == 'f': mc += "..-."
		elif i == 'G' or i == 'g': mc += "--."
		elif i == 'H' or i == 'h': mc += "...."
		elif i == 'I' or i == 'i': mc += ".."
		elif i == 'J' or i == 'j': mc += ".---"
		elif i == 'K' or i == 'k': mc += "-.-"
		elif i == 'L' or i == 'l': mc += ".-.."
		elif i == 'M' or i == 'm': mc += "--"
		elif i == 'N' or i == 'n': mc += "-."
		elif i == 'O' or i == 'o': mc += "---"
		elif i == 'P' or i == 'p': mc += ".--."
		elif i == 'Q' or i == 'q': mc += "--.-"
		elif i == 'R' or i == 'r': mc += ".-."
		elif i == 'S' or i == 's': mc += "..."
		elif i == 'T' or i == 't': mc += "-"
		elif i == 'U' or i == 'u': mc += "..-"
		elif i == 'V' or i == 'v': mc += "...-"
		elif i == 'W' or i == 'w': mc += ".--"
		elif i == 'X' or i == 'x': mc += "-..-"
		elif i == 'Y' or i == 'y': mc += "-.--"
		elif i == 'Z' or i == 'z': mc += "--.."
	else: mc += ""
	return mc

def unique_morse_code(st_lst):
	mc_lst = []
	for i in st_lst:
		x = genmorsecode(i)
		# print i,x
		if x not in mc_lst:
			mc_lst.append(x)
	# print mc_lst
	return len(mc_lst)


l = ["gin", "zen", "gig", "msg"]
actual = unique_morse_code(l)
expected = 2
print actual == expected

l = ["a", "z", "g", "m"]
actual = unique_morse_code(l)
expected = 4
print actual == expected

l = ["bhi", "vsv", "sgh", "vbi"]
actual = unique_morse_code(l)
expected = 3
print actual == expected

l = ["a", "b", "c", "d"]
actual = unique_morse_code(l)
expected = 4
print actual == expected

l = ["hig", "sip", "pot"]
actual = unique_morse_code(l)
expected = 2
print actual == expected
