def parse_instruction(input_str, registers):
    reg_name, op, op_val, _, check_reg_name, check_op, check_val = input_str.split()
    condition = eval('registers.get(check_reg_name, 0)' + check_op + check_val)
    if condition:
        if op == 'inc':
            op_to_use = '+'
        elif op == 'dec':
            op_to_use = '-'
        val = registers.get(reg_name, 0)
        registers[reg_name] = eval('val' + op_to_use + op_val)

def problem08a(input_lines):
    registers = {}
    for line in input_lines:
        parse_instruction(line, registers)
    return max(registers.values())

def problem08b(input_lines):
    registers = {}
    max_val = 0
    for line in input_lines:
        parse_instruction(line, registers)
        if len(registers) > 0:
            max_val = max([max_val, max(registers.values())])
    return max_val

if __name__ == '__main__':
    print(problem08b(open('problem08_input.txt')))
