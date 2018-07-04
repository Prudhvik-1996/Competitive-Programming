def is_valid(code):

	# Determine if the input code is valid
	lst = []
	for i in code:
		lst.append(i)
		if len(lst)>=2:
			if (lst[-1] == '}' and lst[-2] == '{') or (lst[-1] == ')' and lst[-2] == '(') or (lst[-1] == ']' and lst[-2] == '['):
				lst.pop()
				lst.pop()
		
	return lst == []

# Tests

def test_valid_short_code():
	result = is_valid('()')
	expected = True
	print(result == expected)

def test_valid_longer_code():
	result = is_valid('([]{[]})[]{{}()}')
	expected = True
	print(result == expected)

def test_mismatched_opener_and_closer():
	result = is_valid('([][]}')
	expected = False
	print(result == expected)

def test_missing_closer():
	result = is_valid('[[]()')
	expected = False
	print(result == expected)

def test_extra_closer():
	result = is_valid('[[]]())')
	expected = False
	print(result == expected)

def test_empty_string():
	result = is_valid('')
	expected = True
	print(result == expected)

test_valid_short_code()
test_valid_longer_code()
test_mismatched_opener_and_closer()
test_missing_closer()
test_extra_closer()
test_empty_string()