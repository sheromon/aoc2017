import numpy as np

def problem10a(list_length, lengths):
    vals = np.arange(list_length)
    start_ind = 0
    skip_size = 0
    prev_start_ind = 0
    # print(vals)
    for length in lengths:
        # rearrange values so that current position is first element
        vals = np.concatenate([vals[start_ind:], vals[:start_ind]])
        prev_start_ind += start_ind
        if length > 0:
            vals[:length] = vals[length-1::-1]  # flip list section
        start_ind = length + skip_size
        start_ind = start_ind % list_length
        skip_size += 1
        fix_ind = prev_start_ind % list_length
    # reorder list (undo reordering done earlier)
    vals = np.concatenate([vals[-fix_ind:], vals[:-fix_ind]])
    return vals[0] * vals[1]

def problem10a_v2(list_length, lengths):
    vals = np.arange(list_length)
    start_ind = 0
    skip_size = 0
    # print(vals)
    for length in lengths:
        end_ind = start_ind + length
        # print 'Start ind:', start_ind
        # print 'End ind:', end_ind
        if length > 0:
            if end_ind >= length:
                delta = end_ind - length
                vals = np.concatenate([vals, vals[:delta]])
            vals[start_ind:end_ind] = vals[start_ind:end_ind][::-1]
            if delta > 0:
                vals[:delta] = vals[list_length:]
                vals = vals[:list_length]
        start_ind += length + skip_size
        start_ind = start_ind % list_length
        # print vals
        skip_size += 1
    return vals[0] * vals[1]

def test_problem10a():
    print problem10a_v2(5, [3, 4, 1, 5])

def problem10b(ascii_lengths, list_length=256):
    lengths = convert_lengths(ascii_lengths)
    lengths += [17, 31, 73, 47, 23]
    print lengths
    vals = np.arange(list_length)
    start_ind = 0
    skip_size = 0
    prev_start_ind = 0
    for iround in range(64):
        # print(vals)
        for length in lengths:
            end_ind = start_ind + length
            # print 'Start ind:', start_ind
            # print 'End ind:', end_ind
            if length > 0:
                if end_ind >= length:
                    delta = end_ind - length
                    vals = np.concatenate([vals, vals[:delta]])
                vals[start_ind:end_ind] = vals[start_ind:end_ind][::-1]
                if delta > 0:
                    vals[:delta] = vals[list_length:]
                    vals = vals[:list_length]
            start_ind += length + skip_size
            start_ind = start_ind % list_length
            # print vals
            skip_size += 1
    dense = sparse_to_dense(vals)
    result = to_hex(dense)

    return result

def convert_lengths(ascii_lengths):
    lengths = [ord(c) for c in ascii_lengths]
    return lengths

def sparse_to_dense(vals):
    n_elements = len(vals)
    n_groups = n_elements / 16
    result = np.zeros(n_groups, dtype=np.uint8)
    for igroup in range(n_groups):
        for ival in range(16):
            val = vals[igroup * 16 + ival]
            result[igroup] = result[igroup] ^ val
    return result

def to_hex(vals):
    # hex_vals = [str(hex(v))[2:] for v in vals]
    hex_vals = ['{:02x}'.format(v) for v in vals]
    result = ''.join(hex_vals)
    return result

def test_problem10b():
    print problem10b('')
    print problem10b('AoC 2017')
    print problem10b('1,2,3')
    print problem10b('1,2,4')

if __name__ == '__main__':
    # test_problem10a()
    # print problem10a(256, [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216])
    # print convert_lengths('1,2,3')
    # print sparse_to_dense([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
    # print to_hex([64, 7, 255])
    # test_problem10b()
    print problem10b('187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216')
