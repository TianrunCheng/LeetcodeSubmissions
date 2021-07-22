// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         finger_prints = {}
#         result = []
#         curr_group = 0
        
#         for curr_str in strs:
#             sorted_str = "".join(sorted(curr_str))
#             if sorted_str not in finger_prints:
#                 finger_prints[sorted_str] = curr_group
#                 curr_group += 1
#                 group = [curr_str]
#                 result.append(group)
#             else:
#                 group_no = finger_prints[sorted_str]
#                 result[group_no].append(curr_str)
        
#         return result

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()