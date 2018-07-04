def get_closing_paren(sentence, opening_paren_index):

	# Find the position of the matching closing parenthesis
	openings = 0
	
	for i in range(opening_paren_index+1, len(sentence)):
		c = sentence[i]
		if c == '(':
			openings += 1
		elif c == ')':
			if openings == 0:
				return i
			else:
				openings -= 1

	raise Exception("no closings found!")

# Tests

def test_all_openers_then_closers():
	actual = get_closing_paren('((((()))))', 2)
	expected = 7
	print(actual == expected)

def test_mixed_openers_and_closers():
	actual = get_closing_paren('()()((()()))', 5)
	expected = 10
	print(actual == expected)

# def test_no_matching_closer():
#     get_closing_paren('()(()', 2)

test_all_openers_then_closers()
test_mixed_openers_and_closers()