def main(text, part1, part2, state):
    if part1 == part2:
        state = "T"
    if part1 != part2:
        state = "F"
    print(len(text), state)
    return

state = ""

text = str(input())

part1 = text[:len(text) // 2]
part2 = text[len(text) // 2:]
part2 = part2[::-1]
main(text, part1, part2, state)