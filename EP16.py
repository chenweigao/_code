def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

my_text = 'chen wei gao is one of the best software engineer in the word!'
result = list(index_words_iter(my_text))
print(result)