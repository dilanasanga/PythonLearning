
# min_len = min(len(s) for s in string)
# #print(string[0][1])
# common_prefix = ""

# for i in range(min_len):
#         current_char = string[0][i]
#         for strings in string:
#                 if string[i] != current_char:
#                     print(common_prefix)
#         common_prefix = common_prefix + current_char
# print(common_prefix)

class Solution(object):
    def longestCommonPrefix(self, string):
        if not string:
            return ""  # If the input list is empty, there is no common prefix.

        # Find the shortest string in the list (the minimum length determines the common prefix length).
        min_len = min(len(s) for s in string)
        
        common_prefix = ""
        for i in range(min_len):
            # Compare the current character of all strings with the character at the same position in the first string.
            current_char = string[0][i]
            for string in string:
                if string[i] != current_char:
                    return common_prefix  # If characters don't match, return the common prefix found so far.
            
            common_prefix += current_char  # If characters match, add the character to the common prefix.
        
        return common_prefix
string = ['flower', 'flip', 'flight', 'flash']    
new_Solution = Solution()
new_Solution.longestCommonPrefix(string)    