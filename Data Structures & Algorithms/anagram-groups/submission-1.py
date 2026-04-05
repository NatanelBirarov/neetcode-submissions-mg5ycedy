class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramIndices = {}
        anagramGroups = []
        i = 0
        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in anagramIndices:
                anagramGroups[anagramIndices[sSorted]].append(s)
            else:
                anagramGroups.append([s])
                anagramIndices[sSorted] = i
                i += 1
        return list(anagramGroups)