class Solution:
    def nfa_solution(self, s: str, p: str) -> bool:
        states = ["start"]
        star = [False]
        transitions = [set([1])]
        i = 0
        while i < len(p):
            cur_state = p[i]
            has_star = False
            if i < len(p) - 1 and p[i+1] == '*':
                i += 1
                has_star = True
            i += 1
            states.append(cur_state)
            star.append(has_star)
        states.append("end")
        star.append(False)
        transitions_from = [[i - 1] for i in range(len(states))]
        for i in range(len(states)):
            if star[i]:
                transitions_from[i+1] += transitions_from[i]
                transitions_from[i].append(i)
        transitions = [set([]) for _ in range(len(states))]
        for i in range(len(states)):
            for source in transitions_from[i]:
                transitions[source].add(i)

        # print(states)
        # print(transitions)

        cur_states = transitions[0]
        for char in s:
            # print(cur_states, char)
            next_states = set([])
            for state in cur_states:
                if char == states[state] or states[state] == '.':
                    next_states = next_states.union(transitions[state])
            cur_states = next_states
        # print(cur_states)
        return len(states)-1 in cur_states

    def isMatch(self, s: str, p: str) -> bool:
        p = p.replace('?','.').replace('*','.*')
        return self.nfa_solution(s,p)
        
