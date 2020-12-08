from parse import parse
from lib.helpers import log, get_strings_by_lines

tree = {}

class Bag(object):
    def __init__(self, name):
        self.name = name
        self.contains = set()
        self.children = {}
        self.parents = set()

    def __repr__(self):
        return f"\n\t{self.name} -> {list(self.contains)}, {list(self.parents)}\n"

def parse_tree():
    rules = get_strings_by_lines('7.txt')
    for rule in rules:
        specifier, contain_string = rule.split(' bags contain ')
        # Add this object to the tree if we don't know anything about it
        if specifier not in tree:
            curr_bag = Bag(specifier)
            tree[specifier] = curr_bag
        else:
            curr_bag = tree[specifier]

        for spec in contain_string.strip('.').split(', '):
            spec = spec.strip('s')
            if spec == 'no other bag':
                continue
            else:
                number, bag = parse('{:d} {} bag', spec)
                if bag in tree:
                    target_bag = tree[bag]
                else:
                    target_bag = Bag(bag)
                    tree[bag] = target_bag

                curr_bag.children[bag] = number
                curr_bag.contains.add(bag)
                target_bag.parents.add(curr_bag.name)

def part_1():
    parse_tree()

    root = tree['shiny gold']
    possible_containers = set()
    queue = [] + list(root.parents)

    while len(queue) != 0:
        log(queue)
        curr_str = queue.pop(0)
        curr_node = tree[curr_str]

        possible_containers.add(curr_str)
        for parent in list(curr_node.parents):
            if parent not in possible_containers:
                queue.append(parent)

    return len(list(possible_containers))


def recursive_get_bag_count(tree, node_str):
    total = 1
    node = tree[node_str]
    for child, count in node.children.items():
        total += count * recursive_get_bag_count(tree, child)

    return total

def part_2():
    parse_tree()
    return recursive_get_bag_count(tree, 'shiny gold') - 1
