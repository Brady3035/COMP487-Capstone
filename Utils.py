import wave

def wav_to_bytes(wav_file):
    with wave.open(wav_file, 'rb') as wav_file:
        return wav_file.readframes(wav_file.getnframes())

byte_data = wav_to_bytes('CantinaBand3.wav')
print(byte_data)

