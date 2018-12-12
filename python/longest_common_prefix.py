def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, _ in enumerate(zip(*strs)):
        if len(set(_)) > 1:
            return strs[0][:i]
    else:
        return min(strs)

test_strs = ["flower","flow","flight"]
print(longestCommonPrefix(test_strs))