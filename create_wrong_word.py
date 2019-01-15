alphabet = [alpha for alpha in "abcdefghijklmnopqrstuvwxyz"]

def edit_word(word):
    splits      = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes     = [a + b[1:] for a, b in splits if b]
    transposes  = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces    = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts     = [a  + c + b for a, b in splits for c in alphabet]
    pair        = set(deletes + transposes + replaces + inserts)
    return pair

wrong_word = edit_word("sloth")
print(wrong_word)
