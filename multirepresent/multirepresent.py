#by j1nj1
#github:j1nj1CL@qq.com
#qq:j1nj1cl1
def read_binary_file_and_convert(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return convert_binary_data_to_formats(binary_data)

def convert_input_to_binary(input_data, format_type):
    try:
        if format_type == 'Format 1':
            return input_data.encode('utf-8')
        elif format_type == 'Format 2':
            return bytes.fromhex(input_data)
        elif format_type == 'Format 3':
            return bytes.fromhex(input_data.replace(' ', ''))
        elif format_type == 'Format 4':
            return bytes.fromhex(input_data.replace('0x', '').replace(' ', ''))
        elif format_type == 'Format 5':
            return bytes.fromhex(input_data.replace('0x', '').replace(',', ''))
        elif format_type == 'Format 6':
            return bytes(input_data, 'latin-1')
        else:
            raise ValueError("Invalid format type")
    except ValueError as e:
        raise ValueError(f"Invalid input for the specified format: {e}")


def convert_binary_data_to_formats(binary_data):
    try:
        direct_output = binary_data.decode('utf-8')
    except UnicodeDecodeError:
        direct_output = 'Unable to decode binary data to a string'
    hex_str_plain = binary_data.hex().upper()
    hex_str_spaced = ' '.join(f'{byte:02X}' for byte in binary_data)
    hex_str_prefixed = ' '.join(f'0x{byte:02X}' for byte in binary_data)
    hex_str_prefixed_comma = ','.join(f'0x{byte:02X}' for byte in binary_data)
    hex_str_escaped = ''.join(f'\\x{byte:02X}' for byte in binary_data)

    return {
        'Format 1': direct_output,
        'Format 2': hex_str_plain,
        'Format 3': hex_str_spaced,
        'Format 4': hex_str_prefixed,
        'Format 5': hex_str_prefixed_comma,
        'Format 6': hex_str_escaped
    }


def convert_and_print_formats(format_number='Format 1', file_path=None, input_data=None):
    if file_path:
        output = read_binary_file_and_convert(file_path)
    elif input_data:
        binary_data = convert_input_to_binary(input_data, format_number)
        output = convert_binary_data_to_formats(binary_data)
    else:
        raise ValueError("Either file path or input data must be provided")
    length = len(output['Format 2'].replace(' ', '')) // 2 
    print(f"Input Format Number: {format_number}")
    print(f"Length: {length} (0x{length:X})\n")
    for key in sorted(output.keys()):
        print(f"{key}:\n{output[key]}\n")


# Format 1:Hello
# Format 2:48656C6C6F
# Format 3:48 65 6C 6C 6F
# Format 4:0x48 0x65 0x6C 0x6C 0x6F
# Format 5:0x48,0x65,0x6C,0x6C,0x6F
# Format 6:\x48\x65\x6C\x6C\x6F


input_data = "313233"
input_format = 'Format 2' 
#file_path = '1.bin'
convert_and_print_formats(input_format, input_data=input_data)
#convert_and_print_formats(file_path=file_path)