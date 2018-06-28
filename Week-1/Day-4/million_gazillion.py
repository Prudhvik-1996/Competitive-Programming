class Trie(object):

    # Implement a trie and use it to efficiently store strings
    def __init__(self,):
        self.node = {}

    def add_word(self, word):
        node = self.node
        for c in word:
            if node.has_key(c):
                node = node[c]
            else:
                node[c] = {}
                node = node[c]
        
        if node.has_key('*'):
            return False
        node['*'] = {}
        return True

# Tests

trie = Trie()

result = trie.add_word('catch')
expected = True
print(expected == result)

result = trie.add_word('cakes')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = False
print(expected == result)

result = trie.add_word('caked')
expected = True
print(expected == result)

result = trie.add_word('catch')
expected = False
print(expected == result)

result = trie.add_word('')
expected = True
print(expected == result)

result = trie.add_word('')
expected = False
print(expected == result)