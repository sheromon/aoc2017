def problem09a(input_str):
    input_str = remove_cancellers(input_str)
    input_str = remove_garbage(input_str)
    return calculate_total_score(input_str)

def remove_cancellers(input_str):
    while True:
        ind = input_str.find('!')
        if ind == -1:
            break
        input_str = input_str[:ind] + input_str[ind+2:]
    return input_str

def remove_garbage(input_str):
    while True:
        start_ind = input_str.find('<')
        if start_ind == -1:
            break
        end_ind = input_str.find('>', start_ind)
        input_str = input_str[:start_ind] + input_str[end_ind+1:]
    return input_str

def calculate_total_score(input_str):
    total_score = 0
    level = 0
    ind = -1
    while True:
        ind += 1
        if ind >= len(input_str):
            break
        if input_str[ind] == '{':
            level += 1
        elif input_str[ind] == '}':
            total_score += level
            level -= 1
    return total_score

def test_problem09a():
    print problem09a('{}')
    print problem09a('{{{}}}')
    print problem09a('{{}, {}}')
    print problem09a('{{{},{},{{}}}}')

def problem09b(input_str):
    input_str = remove_cancellers(input_str)
    return count_garbage(input_str)

def count_garbage(input_str):
    total_length = 0
    while True:
        start_ind = input_str.find('<')
        if start_ind == -1:
            break
        end_ind = input_str.find('>', start_ind)
        input_str = input_str[:start_ind] + input_str[end_ind+1:]
        length = end_ind - start_ind - 1
        total_length += length
    return total_length

def test_problem09b():
    print problem09b('<>')
    print problem09b('<random characters>')
    print problem09b('<<<<>')
    print problem09b('<{!>}>')
    print problem09b('<!!!>>')
    print problem09b('<{o"i!a,<{i<a>')

if __name__ == '__main__':
    # test_problem09b()
    with open('problem09_input.txt') as f:
        input_str = f.readline()
    print problem09b(input_str)
