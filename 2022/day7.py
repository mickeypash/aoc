from collections import defaultdict

COMMAND_SYMBOL = "$"
TARGET_SIZE = 100000

# pre-order
# in-order
# post-order

class Tree:

    def __init__(self, name, data=None):
        self.name = name
        self.children = []
        self.data = data

def tree(): return defaultdict(tree)

if __name__ == "__main__":
    lines = open("smol7.txt").read().splitlines()

    current_dir = "/"
    root = Tree(current_dir)
    listing = False

    for line in lines:
        if "$ cd" in line:
            _, cmd, _dir = line.split(" ")

            if _dir is not "/":
                root.children.append(Tree(_dir))
            #print(f"- {_dir} (dir)")
        elif "$ ls" in line:
            listing = True
        elif "dir" in line:
            _, _dir = line.split(" ")
            if listing:
                
                #print(f"- {_dir} (dir)")
        else:
            # must be a file
            size, name = line.split(" ")
            #print(f"- {name} (file, size={size})")

    print(root)
