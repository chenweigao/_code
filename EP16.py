
#  def index_words_iter(text):
#     result = []
#     if text:
#         result.append(0)
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             result.append(index + 1)
#     return result
# NOT effective way, do not use append
my_text = 'weigao chen is one of the best software engineer in the word!'


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result = list(index_words_iter(my_text))
print(result)


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('./my_text.txt', 'r') as f:
    it = index_file(f)
    # import itertools
    # results = itertools.islice(it, 0, 3)
    # print(list(results))
    print(list(it))
