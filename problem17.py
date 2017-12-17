def step_insert(seq, ind, n_steps=3):
    if len(seq) < n_steps:
        ind = (ind + n_steps) % len(seq) + 1
    elif (ind + n_steps) >= len(seq):
        ind = n_steps - len(seq) + ind + 1
    else:
        ind += (n_steps + 1)
    seq = seq[:ind] + [len(seq)] + seq[ind:]
    return seq, ind

def problem10a(n_steps):
    seq = [0, 1]
    ind = 1
    for _ in range(2016):
        seq, ind = step_insert(seq, ind, n_steps)
        # print seq, ind
    if ind == len(seq) - 1:
        next_val = seq[0]
    else:
        next_val = seq[ind+1]
    return next_val

def fake_step_insert(istep, ind, n_steps=3):
    if istep < n_steps:
        ind = (ind + n_steps) % istep + 1
    elif (ind + n_steps) >= istep:
        ind = n_steps - istep + ind + 1
    else:
        ind += (n_steps + 1)
    return ind

def problem10b(n_steps, stop_iter):
    seq = [0, 1]
    ind = 1
    for istep in range(2, stop_iter):
        ind = fake_step_insert(istep, ind, n_steps)
        if ind == 1:
            next_val = istep
            print next_val
        # print seq, ind
    return next_val


if __name__ == '__main__':
    # print problem10a(367)
    print problem10b(3, 2018)
    print problem10b(367, int(5e7)+1)
