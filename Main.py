from Utils import *
import ByteEncoder

seed = 123
code = "Nurain"
scrambler = scrambler(seed)
audio_file1 = audio_file('CantinaBand3.wav')

scrambled_code = code #scrambler.scramble(code)
encoded_binary = ByteEncoder.hide_message_in_binary(audio_file1.get_data(), scrambled_code)
audio_file1.write_output(encoded_binary, 'test.wav')

audio_file2 = audio_file('test.wav')
print(ByteEncoder.extract_message_from_binary(audio_file2.get_data(), len(code)))