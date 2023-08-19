sentence = "this is a common interview question"

char_repetition = {letter: sentence.count(letter)
                   for letter in sentence}

char_repetition_sorted = sorted(
    char_repetition.items(), key=lambda kv: kv[1], reverse=True)

print(
    f"'{char_repetition_sorted[0][0]}' is repeated {char_repetition_sorted[0][1]} times")
