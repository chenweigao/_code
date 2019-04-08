def reverseWords(s):
    return " ".join([x[::-1] for x in s.split()])

s = "Let's take LeetCode contest"
print(reverseWords(s))