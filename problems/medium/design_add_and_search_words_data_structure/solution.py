"""
Docstring for problems.medium.design_add_and_search_words_data_structure.solution

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
 
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search
"""





class WDNode:
    def __init__(self):
        self.word_end: bool = False
        self.children: dict = {}


class WordDictionary:

    def __init__(self):
        self.root: WDNode = WDNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = WDNode()
                curr = curr.children[char]

        curr.word_end = True


    def search(self, word: str) -> bool:
        curr_nodes = [self.root]

        for char in word:
            next_nodes = []
            for node in curr_nodes:
                if char == '.':
                    next_nodes.extend(node.children.values())
                else:
                    if char in node.children:
                        next_nodes.append(node.children[char])
                        
            if not next_nodes:
                return False
            
            curr_nodes = next_nodes

        return any(node.word_end for node in curr_nodes)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)