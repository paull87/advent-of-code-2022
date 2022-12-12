
FILE_NAME = 'input.txt'


def setup_trees():
    trees = []

    with open(FILE_NAME) as file:
        for line in file.readlines():
            line = line.strip()
            tree_line = [int(x) for x in line]
            trees.append(tree_line)

    return trees


def binary_copy(trees):
    return [[0 for _ in t] for t in trees]


def check_visibility(trees, x, y):
    visible = 0
    # Edges
    if y in (0, len(trees) - 1) or x in (0, len(trees[y]) - 1):
        visible = 1
        return visible
    tree_height = trees[y][x]
    # Left
    if tree_height > max(trees[y][:x]):
        visible = 1
    # Right
    if tree_height > max(trees[y][x+1:]):
        visible = 1
    # Top
    if tree_height > max(t[x] for t in trees[:y]):
        visible = 1
    # Bottom
    if tree_height > max(t[x] for t in trees[y+1:]):
        visible = 1
    return visible


def export_tree(tree, name):
    output = [f"{','.join([str(i) for i in x])}\n" for x in tree]
    with open(f"{name}.csv", 'w') as file:
        file.writelines(output)


def main():

    trees = setup_trees()
    visible_trees = binary_copy(trees)

    for y in range(len(trees)):
        for x in range(len(trees[y])):
            visible_trees[y][x] = check_visibility(trees, x, y)
    total_visible = sum([sum(t) for t in visible_trees])

    print(f"Visible Trees: {total_visible}")


if __name__ == '__main__':
    main()
