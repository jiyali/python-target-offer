# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        queue = [(beginWord, 1)]
        word_set = set(wordList)

        while queue:
            word, depth = queue.pop(0)
            if word == endWord:
                return depth
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    word_new = word[:i] + j + word[i + 1:]
                    if word_new in word_set:
                        word_set.remove(word_new)
                        queue.append((word_new, depth + 1))
        return 0


s = Solution()
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
