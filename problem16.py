import numpy as np


def problem16a(fname):
    moves = parse_input(fname)
    seq = init_seq(16)
    seq = dance(seq, moves)
    return seq

def parse_input(fname):
    moves = []
    with open(fname) as f:
        moves += f.readline().strip().split(',')
    return moves

def init_seq(length):
    seq = ''.join([chr(val) for val in range(97, 97 + length)])
    return seq

def dance(seq, moves):
    for move in moves:
        move_type = move[0]
        if move_type == 's':  # spin
            size = int(move[1:])
            seq = seq[-size:] + seq[:-size]
        elif move_type == 'x':  # exchange
            inds = move[1:].split('/')
            inds = [int(i) for i in inds]
            seq = exchange(seq, inds)
        elif move_type == 'p':  # partner
            progs = move[1:].split('/')
            inds = [seq.index(p) for p in progs]
            seq = exchange(seq, inds)
    return seq

def exchange(seq, inds):
    seq = list(seq)
    seq[inds[0]], seq[inds[1]] = seq[inds[1]], seq[inds[0]]
    seq = ''.join(seq)
    return seq


def test_problem16a():
    moves = ['s1', 'x3/4', 'pe/b']
    seq = init_seq(5)
    seq = dance(seq, moves)
    print seq

def iters_to_repeat(seq, moves):
    orig_seq = seq
    max_iters = int(1e9)
    n_iters = 0
    while n_iters < max_iters:
        seq = dance(seq, moves)
        # print seq
        if seq == orig_seq:
            break
        n_iters += 1
    return n_iters + 1

def one_billion_dances(seq, moves):
    n_iters_cycle = iters_to_repeat(seq, moves)
    n_iters_to_run = int(1e9) % n_iters_cycle
    for _ in range(n_iters_to_run):
        seq = dance(seq, moves)
    return seq

def test_problem16b():
    moves = ['s1', 'x3/4', 'pe/b']
    seq = init_seq(5)
    print one_billion_dances(seq, moves)

def problem16b(fname='problem16_input.txt'):
    moves = parse_input(fname)
    seq = init_seq(16)
    print one_billion_dances(seq, moves)


if __name__ == '__main__':
    # test_problem16b()
    problem16b('problem16_input.txt')
