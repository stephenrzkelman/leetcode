class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[]]
        line_spaces = [maxWidth]
        last_line_remaining = maxWidth
        for word in words:
            if len(word) <= last_line_remaining:
                lines[-1].append(word)
                last_line_remaining -= len(word) + 1
                line_spaces[-1] -= len(word)
            else:
                lines.append([word])
                last_line_remaining = maxWidth - len(word) - 1
                line_spaces.append(maxWidth - len(word))
        justified_lines = []
        for i in range(len(lines)-1):
            if len(lines[i]) == 1:
                justified_lines.append(lines[i][0] + " "*line_spaces[i])
            else:
                num_spacings = len(lines[i]) - 1
                for j in range(num_spacings):
                    lines[i][j] += " "*(line_spaces[i]//num_spacings)
                    if j < line_spaces[i] % num_spacings:
                        lines[i][j] += " "
                justified_lines.append("".join(lines[i]))
        leftover_spaces = line_spaces[-1] - (len(lines[-1]) - 1)
        justified_lines.append(" ".join(lines[-1]) + " " * leftover_spaces)
        return justified_lines

