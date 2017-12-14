import numpy as np

enum = {'n': 1, 'ne': 2, 'se': 3, 's': -1, 'sw': -2, 'nw': -3}

def problem11a(input_str):
    # print input_str
    tokens = input_str.split(',')
    origin = 0
    vals = np.array([enum[t] for t in tokens])
    counts = {}
    for val in enum.values():
        counts[val] = np.sum(vals == val)
    # cancel out steps that are exact opposites
    cancel_opposites(counts)
    # cancel out cycles
    remove_cycles(counts, [1, -2, 3])
    remove_cycles(counts, [-1, 2, -3])
    # remaining directions is at most three and do not cancel out
    # but some paths have a shorter disance than the number of steps
    # compute shortest distance
    dirs_left = [k for k, v in counts.items() if v > 0]
    if len(dirs_left) > 1:
        reduce_steps(counts, dirs_left[:2])
        if len(dirs_left) > 2:
            reduce_steps(counts, dirs_left[1:])
    total_length = np.sum([v for v in counts.values()])
    # print remaining steps
    # for key, val in counts.items():
    #     if val > 0:
    #         print key, ':', val
    return total_length

def reduce_steps(counts, dir_pair):
    enum_sum = dir_pair[0] + dir_pair[1]
    if (np.abs(enum_sum) == 1) or (np.abs(enum_sum) == 4):
        min_ind = np.argmin(np.array([counts[dir_pair[0]], counts[dir_pair[1]]]))
        counts[dir_pair[min_ind]] = 0

def cancel_opposites(counts):
    for val in range(1, 4):
        if counts[val] < counts[-val]:
            val *= -1
        counts[val] -= counts[-val]
        counts[-val] = 0

def remove_cycles(counts, cycle_vals):
    cycle_counts = np.array([counts[c] for c in cycle_vals])
    min_ind = np.argmin(cycle_counts)
    min_val = cycle_counts[min_ind]
    for c in cycle_vals:
        counts[c] -= min_val

def test_problem11a():
    print problem11a('ne,ne,ne')
    print problem11a('ne,ne,sw,sw')
    print problem11a('ne,ne,s,s')
    print problem11a('se,sw,se,sw,sw')

def count_steps(vals):
    # counts = np.zeros(6, dtype=np.uint32)
    counts = {}
    for val in enum.values():
        counts[val] = np.sum(vals == val)
    # cancel out steps that are exact opposites
    cancel_opposites(counts)
    # cancel out cycles
    remove_cycles(counts, [1, -2, 3])
    remove_cycles(counts, [-1, 2, -3])
    # remaining directions is at most three and do not cancel out
    # but some paths have a shorter disance than the number of steps
    # compute shortest distance
    dirs_left = [k for k, v in counts.items() if v > 0]
    if len(dirs_left) > 1:
        reduce_steps(counts, dirs_left[:2])
        if len(dirs_left) > 2:
            reduce_steps(counts, dirs_left[1:])
            reduce_steps(counts, dirs_left[0:3:2])
    total_length = np.sum([v for v in counts.values()])
    return total_length

def problem11b(input_str):
    # print input_str
    tokens = input_str.split(',')
    vals = np.array([enum[t] for t in tokens])
    max_steps = 0
    for ival in range(len(vals)):
        n_steps = count_steps(vals[:ival+1])
        if n_steps > max_steps:
            max_steps = n_steps
    return max_steps


if __name__ == '__main__':
    with open('problem11_input.txt') as f:
        input_str = f.readline().rstrip()
    print problem11b(input_str)
