import numpy as np

def parse_input(fname):
    connections = {}
    for line in open(fname):
        line = line.rstrip()
        ind = line.find('<->')
        node = int(line[:ind])
        neighbors = np.array([int(n) for n in line[ind+3:].split(',')])
        connections[node] = neighbors
    return connections

def problem12a(fname):
    connections = parse_input(fname)
    group = find_group(connections, 0)
    return len(group)

def find_group(connections, main_node):
    if main_node not in connections:
        raise RuntimeError('Main node not in set of connections.')
    # initialize list of nodes in the group
    main_group = np.array([main_node])
    ind = 0
    while ind < len(main_group):
        node = main_group[ind]
        # get nodes connected to the main node, if any
        new_nodes = connections.get(node)
        if new_nodes is not None:
            # add nodes that haven't already been added
            nodes_to_add = np.setdiff1d(new_nodes, main_group)
            main_group = np.concatenate([main_group, nodes_to_add])
        ind += 1
    return main_group

def problem12b(fname):
    connections = parse_input(fname)
    all_nodes = np.array(connections.keys())
    n_groups = 0
    while len(all_nodes) > 0:
        node = all_nodes[0]
        group = find_group(connections, node)
        all_nodes = np.setdiff1d(all_nodes, group)
        n_groups += 1  # count each distince group
    return n_groups

if __name__ == '__main__':
    # print problem12a('problem12_input.txt')
    print problem12b('problem12_input.txt')
