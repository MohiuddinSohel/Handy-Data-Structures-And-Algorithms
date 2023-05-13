def insert(root, word):
    current = root
    for c in word:
        if c not in current:
            current[c] = {}
        current = current[c]
    current['#'] = word


def query(root, word):
    current = root
    count = 0
    for c in word:
        current = current[c]
    return count

#minimalistic trie
if __name__ == "__main__":
    trie = {}
    for word in words:
        insert(trie, word)