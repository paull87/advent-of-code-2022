import math

FILE_NAME = 'input.txt'
MONKEY_SECTION = 7
ROUNDS = 10000
WORRY_FACTOR = 96577


class Monkey:

    def __init__(self, name, items, operation, test, true_throw, false_throw):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspections = 0
        self.worry = 1

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def throw_items(self, monkeys):
        while self.items:
            item = self.items.pop(0)
            print(f"{self.name} inspecting item [{item}]")
            item = self.inspect_item(item)
            item = self.worry_factor(item)
            print(f"{self.name} threw item [{item}]")
            if self.test_item(item):
                monkeys[self.true_throw].catch_item(item)
            else:
                monkeys[self.false_throw].catch_item(item)

    def catch_item(self, item):
        self.items.append(item)
        print(f"{self.name} caught item [{item}]")

    def inspect_item(self, item):
        self.inspections += 1
        return eval(self.operation)

    def worry_factor(self, item):
        return item % self.worry

    def test_item(self, item):
        return item % self.test == 0


def parse_monkey(data):
    data = [x.strip() for x in data]
    name = parse_name(data[0])
    items = parse_items(data[1])
    operation = parse_operation(data[2])
    test = parse_test(data[3])
    true_throw = parse_true_throw(data[4])
    false_throw = parse_false_throw(data[5])
    return Monkey(
        name=name,
        items=items,
        operation=operation,
        test=test,
        true_throw=true_throw,
        false_throw=false_throw,
    )


def parse_name(data):
    return data.replace(':', '')


def parse_items(data):
    item_string = data.split(':')[1]
    items = [int(x.strip()) for x in item_string.split(',')]
    return items


def parse_operation(data):
    operation = data.split('=')[-1]
    return operation.replace('old', 'item').strip()


def parse_test(data):
    return int(data.split()[-1])


def parse_true_throw(data):
    return int(data.split()[-1])


def parse_false_throw(data):
    return int(data.split()[-1])


def create_monkeys():
    monkeys = []

    with open(FILE_NAME) as file:
        all_data = file.readlines()
        for i in range(0, len(all_data), MONKEY_SECTION):
            data = all_data[i:i + MONKEY_SECTION]
            monkeys.append(parse_monkey(data))

    return monkeys


def get_worry_factor(monkeys):
    return math.lcm(*[x.test for x in monkeys])


def main():

    monkeys = create_monkeys()

    worry = get_worry_factor(monkeys)
    for monkey in monkeys:
        monkey.worry = worry

    for _ in range(ROUNDS):
        for monkey in monkeys:
            print(f"{monkey.name} turn")
            monkey.throw_items(monkeys)

    print("-----------------------------------------\n")
    for monkey in monkeys:
        print(f"{monkey.name} inspected {monkey.inspections} items")

    print("-----------------------------------------\n")

    most_active_monkeys = sorted(monkeys, key = lambda x: x.inspections)[-2:]

    for monkey in most_active_monkeys:
        print(f"{monkey.name} inspected {monkey.inspections} items")

    monkey_business = most_active_monkeys[0].inspections * most_active_monkeys[1].inspections
    print(f"Monkey Business: {monkey_business}")



if __name__ == '__main__':
    main()
