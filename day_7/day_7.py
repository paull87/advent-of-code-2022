
FILE_NAME = 'input.txt'

DISK_LIMIT = 70000000
UPDATE_SPACE = 30000000


class File:
    def __init__(self, name, size):
        self.type = 'file'
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Directory:
    def __init__(self, name):
        self.type = 'dir'
        self.name = name
        self.contains = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.contains})'

    def __getitem__(self, item):
        return self.contains[item]

    def add(self, dir_object):
        if dir_object.name not in self.contains.keys():
            self.contains[dir_object.name] = dir_object

    @property
    def size(self):
        total = 0
        for file in self.contains.values():
            total += file.size
        return total


def move_to_dir(dir, path):
    current_dir = dir
    for p in path:
        current_dir = current_dir[p]
    return current_dir


def small_dirs(dir, max_size):
    output_dirs = []
    if isinstance(dir, File):
        return output_dirs
    if dir.size <= max_size:
        output_dirs.append(dir)
    for sub_dir in dir.contains.values():
        output_dirs += small_dirs(sub_dir, max_size)
    return output_dirs


def main():
    dir = Directory('root')
    current_path = []
    current_location = dir

    with open(FILE_NAME) as file:
        for command in file.readlines():
            if command.startswith('$ cd'):
                cd_comm = command.split()[-1]
                if cd_comm == '/':
                    current_path = []
                    current_location = dir
                elif cd_comm == '..':
                    current_path.pop()
                    current_location = move_to_dir(dir, current_path)
                else:
                    current_path.append(cd_comm)
                    current_location = move_to_dir(dir, current_path)

            # dir name
            elif command.startswith('dir'):
                dir_name = command.split()[-1]
                current_location.add(Directory(dir_name))
            # Must be a file
            elif not command.startswith('$'):
                size, name = command.split()
                current_location.add(File(name, int(size)))

    result = small_dirs(dir, 100000)

    result_size = sum([r.size for r in result])
    print(f"Dirs under limit: {len(result)}, sum of size: {result_size}")


if __name__ == '__main__':
    main()
