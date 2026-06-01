class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0])
        total_energy = 0
        for task in tasks:
            total_energy = max(total_energy + task[0], task[1])
        return total_energy