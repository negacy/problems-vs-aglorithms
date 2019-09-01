import sys
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
    def insert(self, path, handler = None):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for word in path.strip('/').split('/'):
            if word not in current_node.children:
                current_node.children[word] = RouteTrieNode()
            current_node = current_node.children[word]
        current_node.is_word = True
##assign handler
        if handler != None:
            current_node.handler = handler

    def find(self, url):
# Starting at the root, navigate the Trie to find a match for this path
# Return the handler for a match, or None for no match
        current_node = self.root

        for word in url.split('/'):
            if word not in current_node.children:
                return 
            current_node = current_node.children[word]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler= None):
    # Initialize the node with children as before, plus a handler
        self.is_word = False
        self.children = {}
        self.handler = handler
    
    #def insert(self, ...):
# Insert the node as before

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler="root handler"):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler)
         
    def add_handler(self, path, handler):
        if path == "" or handler == "":
            print("Warning: path or handler cannot be empty")
            return
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
        self.route.insert(path, handler)
    def lookup(self, path): 
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        if path == '/':
            return self.route.root.handler 
        current_node = self.route.root
        for word in path.strip('/').split('/'):
            try:
                current_node = current_node.children[word]
            except KeyError:
                return "not found handler"
        return current_node.handler 
                                                                         
    #def split_path(self, ...):
# you need to split the path into parts for
# both the add_handler and loopup functions,
# so it should be placed in a function here

# Here are some test cases and expected outputs you can use to test your implementation

###########TEST-1
# create the router and add a route
router = Router("root handler") 
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print('-'*50)
###########TEST-2
router = Router()
router.add_handler("/home/bbc/uk/local/news", "news")  # add a route
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'root handler'
print(router.lookup("/home/about/me")) # should print 'root handler'
print(router.lookup("/home/bbc/uk/local/news")) # should print 'root handler'
#############TEST-3
router = Router()
router.add_handler("", "nothing")
router.add_handler("/home", "")

