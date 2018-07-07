def prepDict(stri):
	stri = stri.replace(" ","")
	stri = stri.lower()
	d = {}
	for i in stri:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	return d
def isAnagram(str1, str2):
	return prepDict(str1) == prepDict(str2)

expected = True
actual = isAnagram('anagram', 'nagaram')
print expected == actual

expected = True
actual = isAnagram('Keep', 'Peek')
print expected == actual

expected = True
actual = isAnagram('Mother In Law', 'Hitler Woman')
print expected == actual

expected = True
actual = isAnagram('School Master', 'The Classroom')
print expected == actual

expected = True
actual = isAnagram('ASTRONOMERS', 'NO MORE STARS')
print expected == actual

expected = False
actual = isAnagram('Toss', 'Shot')
print expected == actual

expected = False
actual = isAnagram('joy', 'enjoy')
print expected == actual

expected = True
actual = isAnagram('Debit Card', 'Bad Credit')
print expected == actual

expected = True
actual = isAnagram('SiLeNt CAT', 'LisTen AcT')
print expected == actual

expected = True
actual = isAnagram('Dormitory', 'Dirty Room')
print expected == actual