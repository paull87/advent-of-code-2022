
FILE_NAME = 'input_part2.txt'


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, pair):
        if type(pair) == type(self):
            return self.first == pair.first and self.second == pair.second
        else:
            return False

    def __repr__(self):
        return "%s(%s, %s)" % (self.__class__.__name__, self.first, self.second)

    def overlaps(self, pair):
        return self.first <= pair.first <= self.second or self.first <= pair.second <= self.second or pair.first <= self.first <= pair.second or pair.first <= self.second <= pair.second

    def merge(self, pair):
        return Pair(min(self.first, pair.first), max(self.second, pair.second))

    def fully_contains(self, pair):
        return self.first <= pair.first and self.second >= pair.second


def merge_intervals(v):
    result = []
    for pair in v:
        if result == []:
            result.append(pair)
        if pair.overlaps(result[-1]):
            result[-1] = pair.merge(result[-1])
        else:
            result.append(pair)
    return result


def create_pairs(rec):
    p1, p2 = rec.split(',')
    return Pair(int(p1.split('-')[0]), int(p1.split('-')[1])), Pair(int(p2.split('-')[0]), int(p2.split('-')[1]))


def main():
    overlaps = []

    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            pair_1, pair_2 = create_pairs(rec)
            if pair_1.overlaps(pair_2):
                overlaps.append((pair_1, pair_2))
                print('overlaps>>>>', sep=None)
            print((pair_1, pair_2))

    print(f"items: {len(overlaps)}")


if __name__ == '__main__':
    main()
