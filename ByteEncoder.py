from typing import *

def text_to_binary(input_text_file, output_binary_file):
    try:
        # Open the input text file in read mode and the output binary file in write mode
        with open(input_text_file, 'r') as txt_file, open(output_binary_file, 'wb') as bin_file:
            # Read the content of the text file
            content = txt_file.read()

            # Convert each character to its binary representation and join with spaces
            binary_content = ' '.join(format(ord(char), '08b') for char in content)

            # Encode the binary string to bytes and write to the binary file
            bin_file.write(binary_content.encode('utf-8'))

        print(f"Successfully converted {input_text_file} to binary representation file {output_binary_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def binary_to_text(input_binary_file, output_text_file):
    try:
        # Open the input binary file in read mode and the output text file in write mode
        with open(input_binary_file, 'rb') as bin_file, open(output_text_file, 'w') as txt_file:
            # Read the binary content and decode it to a string
            binary_content = bin_file.read().decode('utf-8')

            # Split the binary content by spaces to get each 8-bit binary character
            binary_chars = binary_content.split()

            # Convert each 8-bit binary character to the corresponding ASCII character
            text = ''.join(chr(int(b, 2)) for b in binary_chars)

            # Write the decoded text to the output file
            txt_file.write(text)

        print(f"Successfully converted binary file {input_binary_file} back to text file {output_text_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def hide_message_in_binary(byte_chars: ByteString, secret_message) -> ByteString:

    # Convert the secret message to a binary string
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_chars = ''.join(format(byte, '08b') for byte in byte_chars)
    message_length = len(binary_message)
    # Check if the binary content has enough characters to hide the message
    if message_length > len(binary_chars):
        raise ValueError("Secret message is too long to hide in the binary file.")
    # Embed the message in the LSB of each character's binary representation
    modified_binary_chars = []
    for i, binary_char in enumerate(binary_chars):
        if i < message_length:
            # Replace the last bit with the message bit
            modified_char = binary_char[:-1] + binary_message[i]
        else:
            # Keep the original binary character
            modified_char = binary_char
        modified_binary_chars.append(modified_char)
    # Join the modified binary characters and encode to binary format
    binary_str = ''.join(modified_binary_chars)
    print(binary_str[0:10])
    modified_binary_content = bytearray([int(binary_str[i:i+8], 2) for i in range(0,len(binary_str),8)])
    return modified_binary_content

def hide_message_in_binary_file(input_binary_file, output_binary_file, secret_message):
    try:
        # Convert the secret message to a binary string
        binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
        message_length = len(binary_message)

        with open(input_binary_file, 'rb') as bin_file:
            # Read the binary content and decode it to a string
            binary_content = bin_file.read().decode('utf-8')

            # Split into individual bits
            binary_chars = binary_content.split()

        # Check if the binary content has enough characters to hide the message
        if message_length > len(binary_chars):
            raise ValueError("Secret message is too long to hide in the binary file.")

        # Embed the message in the LSB of each character's binary representation
        modified_binary_chars = []
        for i, binary_char in enumerate(binary_chars):
            if i < message_length:
                # Replace the last bit with the message bit
                modified_char = binary_char[:-1] + binary_message[i]
            else:
                # Keep the original binary character
                modified_char = binary_char
            modified_binary_chars.append(modified_char)

        # Join the modified binary characters and encode to binary format
        modified_binary_content = ' '.join(modified_binary_chars).encode('utf-8')

        # Write the modified binary content to the output file
        with open(output_binary_file, 'wb') as out_bin_file:
            out_bin_file.write(modified_binary_content)

        print(f"Successfully hid the message in {output_binary_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_message_from_binary(input_binary_file, message_length):
    try:
        with open(input_binary_file, 'rb') as bin_file:
            # Read the binary content and decode it to a string
            binary_content = bin_file.read().decode('utf-8')

            # Split the binary content by spaces to get each 8-bit binary character
            binary_chars = binary_content.split()

        # Extract the least significant bit from each character up to the message length
        extracted_bits = ''.join(binary_char[-1] for binary_char in binary_chars[:message_length])

        # Convert the extracted bits to characters (8 bits at a time)
        hidden_message = ''.join(chr(int(extracted_bits[i:i + 8], 2)) for i in range(0, len(extracted_bits), 8))

        print(f"Extracted message: {hidden_message}")
        return hidden_message
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # First, convert text to binary file
    text_to_binary("input_text_file.txt", "output_binary_file.txt")

    # Hide the message
    hide_message_in_binary("output_binary_file.txt", "binary_with_hidden_message.txt", "secret")

    # Convert with message back to text
    binary_to_text("binary_with_hidden_message.txt", "output_text_file.txt")

    # Extract the hidden message
    extract_message_from_binary("binary_with_hidden_message.txt", len("secret") * 8)

