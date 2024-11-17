from Utils import *
import ByteEncoder

seed = 123
code = "Nurain"

scrambler = scrambler(seed)
audio_file = audio_file('CantinaBand3.wav')

scrambled_code = scrambler.scramble(code)
encoded_binary = ByteEncoder.hide_message_in_binary(audio_file.get_data(), scrambled_code)
audio_file.write_output(encoded_binary, 'test.wav')