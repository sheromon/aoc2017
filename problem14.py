import numpy as np

def knot_hash(ascii_lengths, list_length=256):
    # mostly cut-and-pasted code from problem10
    lengths = convert_lengths(ascii_lengths)
    lengths += [17, 31, 73, 47, 23]
    # print lengths
    vals = np.arange(list_length)
    start_ind = 0
    skip_size = 0
    prev_start_ind = 0
    for iround in range(64):
        for length in lengths:
            end_ind = start_ind + length
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
    # hex_vals = [hex(v) for v in vals]
    hex_vals = ['{:02x}'.format(v) for v in vals]
    hex_vals = ''.join(hex_vals)
    return hex_vals

def to_binary(hex_vals):
    bin_array = np.empty([32, 4])
    for irow, h in enumerate(hex_vals):
        bin_str = '{:04b}'.format(int(h, 16))
        bin_array[irow] = np.array([int(b) for b in bin_str])
    bin_array = np.reshape(bin_array, -1)
    return bin_array

def problem14a(key):
    grid = np.empty([128, 128], dtype=np.uint8)
    for irow in range(128):
        mod_key = key + '-' + str(irow)
        hex_vals = knot_hash(mod_key)
        bin_array = to_binary(hex_vals)
        grid[irow] = bin_array
    print grid[:8, :8]
    print np.sum(grid)
    return grid

def problem14b(key):
    grid = problem14a(key)
    region_grid = np.zeros_like(grid, dtype=np.uint32)
    region_id = 1
    row = np.array([0], dtype=np.uint32)
    col = np.empty(0, dtype=np.uint32)
    while row < len(grid):
#         print 'Processing row', row[0]
        cols = np.nonzero((grid[row] == 1) & (region_grid[row] == 0))[1]
#         print cols
        if len(cols) == 0:
            row += 1
            continue
        for init_col in cols:
            if region_grid[row, init_col] != 0:
                continue
            col = np.array([init_col])
            fill_region(row, col, region_id, grid, region_grid)
            # print 'Region {:d} filled'.format(region_id)
#             print region_grid
            region_id += 1
    print region_grid[:8, :8]
    return region_id - 1


def fill_region(row, col, region_id, grid, region_grid):
    while len(col) > 0:
        # print 'Row:', row, 'Col:', col
        region_grid[row, col] = region_id
        neighbors = np.array([[row-1, row, row, row+1],
                              [col, col-1, col+1, col]])
        valid_inds = np.all((neighbors >= 0) & (neighbors < len(grid)), axis=0)
        neighbors = neighbors[:, valid_inds]
        row = row[1:]
        col = col[1:]
        if not np.any(valid_inds):
            continue
        new_rows, new_cols = check_neighbors(neighbors, grid, region_grid)
        if len(new_rows) == 0:
            continue
        region_grid[new_rows, new_cols] = region_id
        row = np.append(row, new_rows)
        col = np.append(col, new_cols)
        row_col = np.reshape(np.stack([row, col]), [2, -1])
        row_col = np.vstack({tuple(entry) for entry in row_col.T}).T
        row, col = np.vsplit(row_col, 2)

def check_neighbors(neighbors, grid, region_grid):
    row, col = np.vsplit(neighbors, 2)
    grid_inds = (grid[row, col] == 1) & (region_grid[row, col] == 0)
    return row[grid_inds], col[grid_inds]

if __name__ == '__main__':
    # print problem14b('flqrgnkx')
    print problem14b('jxqlasbh')
