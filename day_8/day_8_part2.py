
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


def tree_visibility(rows, tree_height):
    visible = 0
    if len(rows) == 0:
        return visible
    if max(rows) < tree_height:
        visible = len(rows)
    for i, tree in enumerate(rows):
        if tree >= tree_height:
            visible = i + 1
            break
    return visible


def scenic_score(trees, x, y):
    tree_height = trees[y][x]
    # if y == 3 and x == 2:
    #     import pdb; pdb.set_trace()
    # Left
    left_trees = trees[y][:x][::-1]
    left_score = tree_visibility(left_trees, tree_height)
    # Right
    if x == len(trees[y]) - 1:
        right_score = 0
    else:
        right_trees = trees[y][x + 1:]
        right_score = tree_visibility(right_trees, tree_height)
    # Top
    top_trees = [t[x] for t in trees[:y]][::-1]
    top_score = tree_visibility(top_trees, tree_height)
    # Bottom
    if y == len(trees) - 1:
        bottom_score = 0
    else:
        bottom_trees = [t[x] for t in trees[y + 1:]]
        bottom_score = tree_visibility(bottom_trees, tree_height)
    # print(f'>> {y}:{x}={tree_height}, {left_score} * {right_score} * {top_score} * {bottom_score} = {left_score * right_score * top_score * bottom_score}')
    return left_score * right_score * top_score * bottom_score


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
    score_trees = binary_copy(trees)

    for y in range(len(trees)):
        for x in range(len(trees[y])):
            score_trees[y][x] = scenic_score(trees, x, y)
    highest_scenic_score = max([max(t) for t in score_trees])

    print(f"Highest score: {highest_scenic_score}")


if __name__ == '__main__':
    main()
