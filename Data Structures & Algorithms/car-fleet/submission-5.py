class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0

        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort(reverse=True)

        for i in range(len(position)):
            car_pos, car_speed = arr[i][0], arr[i][1]
            steps = (target - car_pos) / car_speed
            stack.append(steps)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)    