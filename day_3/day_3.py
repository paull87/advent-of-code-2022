from string import ascii_letters

FILE_NAME = 'input.txt'

priority_scores = {k: i+1 for i, k in enumerate(ascii_letters)}


def split_bag(bag):
    part_size = int(len(bag) / 2)
    return bag[0:part_size], bag[part_size:]


def duplicate_items(comp_1, comp_2):
    return list(set(comp_1).intersection(set(comp_2)))


def calculate_priority_score(items):
    return sum([priority_scores[i] for i in items])


def main():
    priority_items = []

    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            comp_1, comp_2 = split_bag(rec)
            dupes = duplicate_items(comp_1, comp_2)
            priority_items += dupes

    print(f"items: {len(priority_items)}, priority_score: {calculate_priority_score(priority_items)}")


if __name__ == '__main__':
    main()
