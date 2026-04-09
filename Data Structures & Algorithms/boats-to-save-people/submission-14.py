class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0] * (max(people) + 1)
        for num in people:
            count[num] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        res = [0] * len(people)
        for i in range(len(people) - 1, -1, -1):
            v = people[i]
            res[count[v] - 1] = v
            count[v] -= 1
        
        print(res)
        i, j = 0, len(people) - 1
        boats = 0
        if res[0] >= limit:
            return len(res)
        while i < j:
            num1 = res[i]
            num2 = res[j]
            if num1 + num2 <= limit:
                i += 1
            j -= 1
            boats += 1
        if i == j:
            boats += 1
        return boats

        # people.sort()
        # i, j = 0, len(people) - 1
        # boats = 0
        # if people[0] >= limit:
        #     return len(people)
        # while i < j:
        #     num1 = people[i]
        #     num2 = people[j]
        #     if num1 + num2 <= limit:
        #         i += 1
        #     j -= 1
        #     boats += 1
        # if i == j:
        #     boats += 1
        # return boats