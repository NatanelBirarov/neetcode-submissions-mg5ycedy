class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        i, j = 0, len(people) - 1
        boats = 0
        if people[0] >= limit:
            return len(people)
        while i < j:
            num1 = people[i]
            num2 = people[j]
            if num1 + num2 <= limit:
                i += 1
            j -= 1
            boats += 1
        if i == j:
            boats += 1
        return boats