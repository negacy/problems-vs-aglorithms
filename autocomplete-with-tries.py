## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        tmp = []
        for k in self.children:
            if self.children[k].is_word:
                tmp.append(suffix + k)
            tmp += self.children[k].suffixes(suffix+k)
        return tmp
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        
        current_node.is_word = True
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        if prefix == '':
            return False 
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return current_node
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
            "trie", "trigger", "trigonometry", "tripod"
            ]
for word in wordList:
    MyTrie.insert(word)

#test-1
prefixNode = MyTrie.find('a')
print(prefixNode.suffixes())#prints ['nt', 'ntagonist', 'ntonym', 'nthology']

prefixNode = MyTrie.find('f')
print(prefixNode.suffixes())#prints ['un', 'unction', 'actory']

####test-2 non existing character

prefixNode = MyTrie.find('x')
try:
    print(prefixNode.suffixes())#prints `Character not found`
except AttributeError:
    print("Character not found")
#####test-3 empty character
prefixNode = MyTrie.find(' ')
print('pref: ', prefixNode)
try:
    print(prefixNode.suffixes())#prints `Character not found`
except AttributeError:
    print("Character not found")

prefixNode = MyTrie.find('')
print('pref: ', prefixNode)
try:
    print(prefixNode.suffixes())#prints `Character not found`
except AttributeError:
    print("Character not found")
