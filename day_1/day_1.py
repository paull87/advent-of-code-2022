
FILE_NAME = 'input.txt'

elves = []

with open(FILE_NAME) as file:
    elf = 0
    for rec in file.readlines():
        rec = rec.strip()
        if rec == '':
            elves.append(elf)
            elf = 0
        else:
            elf += int(rec)

print(f"elves: {len(elves)}, max: {max(elves)}")
print(f"top 3 elves: {sorted(elves)[-3:]}, sum: {sum(sorted(elves)[-3:])}")

