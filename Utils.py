import wave

# Uses built in wave library to pull byte code out
def wav_to_bytes(wav_file):
    with wave.open(wav_file, 'rb') as wav_file:
        return wav_file.readframes(wav_file.getnframes())

#  Cuts the header off the file, so we can have just the song data
def wavbyte_to_data(wavbyte):
    return wavbyte[44:]


byte_data = wav_to_bytes('CantinaBand3.wav')
print(byte_data)

