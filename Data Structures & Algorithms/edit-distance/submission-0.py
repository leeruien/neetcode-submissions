class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #x is word w, y word 2, start from index 1
        len_1 = len(word1)
        len_2 = len(word2)
        matrix = [[0 for i in range(len_1+1)]for j in range(len_2+1)]
        for i in range(len_1):
            matrix[0][i+1] = i + 1
        for i in range(len_2):
            matrix[i+1][0] = i+1
        for i in range(1,len_2+1):
            for j in range(1,len_1+1):
                if word2[i-1] == word1[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
        return matrix[len_2][len_1]
        

        