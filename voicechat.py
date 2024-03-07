import pyaudio
import wave
# import sys
# import os

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i)["name"])

CHUNK = 1024
FORMAT = pyaudio.paInt16
# channel 2 = window
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'output.wav'

with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, input_device_index=1, frames_per_buffer=1024)

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    stream.close()
    p.terminate()
