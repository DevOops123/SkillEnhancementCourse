class TrieNode:
    def __init__(self):
        self.children = {}
        self.top = []          # list of (node, freq) sorted
        self.word = None       # set only for terminal nodes
        self.freq = 0          # only for terminal nodes

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        stack = [node]
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            stack.append(node)
        # node is now the terminal node
        node.word = s
        node.freq += 1
        # update all prefixes (including the node itself)
        for anc in stack:
            self._update_top(anc, node, node.freq)

    def _update_top(self, node, term_node, new_freq):
        # Remove old entry if present
        for i, (n, _) in enumerate(node.top):
            if n is term_node:
                del node.top[i]
                break
        # Add new entry
        node.top.append((term_node, new_freq))
        # Sort: descending freq, then ascending word
        node.top.sort(key=lambda x: (-x[1], x[0].word))
        # Keep only top 5
        if len(node.top) > 5:
            node.top = node.top[:5]

    def get_suggestions(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return [entry[0].word for entry in node.top]
