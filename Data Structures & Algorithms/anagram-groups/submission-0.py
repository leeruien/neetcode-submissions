class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        store = {}
        cur_index = 0
        for index, string in enumerate(strs):
            sorted_str = "".join(sorted(string))
            if sorted_str in store:
                index_result = store[sorted_str]
                list_str = result[index_result]
                list_str.append(string)
                result[index_result] = list_str
            else:
                result.append([string])
                store[sorted_str] = cur_index
                cur_index += 1
        return result

        