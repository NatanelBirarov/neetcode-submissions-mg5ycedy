class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}
        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in anagramGroups:
                anagramGroups[sSorted].append(s)
            else:
                anagramGroups[sSorted] = [s]
        return list(anagramGroups.values())