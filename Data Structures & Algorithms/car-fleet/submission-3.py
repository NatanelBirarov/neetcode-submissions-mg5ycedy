class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0

        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort(reverse=True)

        for p, s in arr:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)    