class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp = stack.pop()
                res[prev_temp[1]] = i - prev_temp[1]

            stack.append((temp, i))

        return res