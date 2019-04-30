class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        if len(digits) == 0:
            return []
        dic_digit_letter = {
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': ['']
        }
        
        res = ['']
        for digit in digits:
            chars_in_dict = dic_digit_letter[digit]

            temp_res = []
            for char in chars_in_dict:
                for s in res:
                    temp_res.append(s + char)
            res = temp_res
        return res


class Solution2:

    def helper(self, digits, mappings, char, res):
        if len(digits) > 0:
            for new_char in mappings[digits[0]]:
                self.helper(digits[1:], mappings, char + new_char, res)
        else:
            if len(char) > 0:
                res.append(char)
        return res


    def letterCombinations(self, digits: str) -> 'List[str]':
        mappings = {
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': ['']
        }

        return self.helper(digits, mappings, '', [])

digits = "23"
print(Solution().letterCombinations(digits))
print(Solution2().letterCombinations(digits))