from string import ascii_letters

FILE_NAME = 'input.txt'

PARTY_SIZE = 3

priority_scores = {k: i+1 for i, k in enumerate(ascii_letters)}


def create_party(file):
    party = []
    for _ in range(PARTY_SIZE):
        member = file.readline()
        if member == '':
            break
        party.append(member.strip())
    return party


def find_common_item(party):
    commons = set(party[0])
    for member in party:
        commons = commons.intersection(set(member))
    return list(commons)


def calculate_priority_score(items):
    return sum([priority_scores[i] for i in items])


def main():
    priority_items = []

    with open(FILE_NAME) as file:
        while True:
            party = create_party(file)
            if party == []:
                break
            badge_item = find_common_item(party)
            priority_items += badge_item

    print(f"items: {len(priority_items)}, priority_score: {calculate_priority_score(priority_items)}")


if __name__ == '__main__':
    main()
