
def insert_linebreak(s, max_length=20):
    # Initialize an empty list to hold the lines
    lines = []
    start = 0

    while start < len(s):
        # Determine the end of the current line
        end = start + max_length

        # If the end exceeds the string length, take the rest of the string
        if end >= len(s):
            lines.append(s[start:])
            break

        # Find the nearest space before or at the max_length
        break_point = end
        while break_point > start and s[break_point] != ' ':
            break_point -= 1

        # If no space was found, look forward for the next space
        if break_point == start:
            break_point = end
            while break_point < len(s) and s[break_point] != ' ':
                break_point += 1
            if break_point == len(s):  # No space found; break at max_length
                break_point = end

        # Add the line to the list, excluding the space where the break occurs
        lines.append(s[start:break_point])
        start = break_point + 1  # Move start to the next character after the space

    return '\n'.join(lines)

# extra functions
# def insert_linebreak(s, max_length=20):
#     if len(s) <= max_length:
#         return s
#
#     # Find the nearest space before or at max_length
#     break_point = max_length
#     while s[break_point] != ' ' and break_point > 0:
#         break_point -= 1
#
#     if break_point == 0:
#         break_point = max_length
#         while s[break_point] != ' ' and break_point > 0:
#             break_point += 1
#         # return s  # No space found; return the original string
#
#     # Insert line break
#     return s[:break_point] + '\n' + s[break_point + 1:]