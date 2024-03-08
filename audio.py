import pyaudio
import wave
import sys
from encoding_message import Data_codec
import os
import time

class Audio:
    def __init__(self):
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        self.p = pyaudio.PyAudio()

        # for i in range(self.p.get_device_count()):
        #     print(self.p.get_device_info_by_index(i)["name"])

        self.CHUNK = 1024
        # 2 octect for 16 
        self.FORMAT = pyaudio.paInt16

        self.CHANNELS = 2  #2 = window
        self.RATE = 44100
        self.RECORD_SECONDS = 5        

    def record(self,file_name_wav):    
        FILENAME = file_name_wav
        # self.p = pyaudio.PyAudio()
        with wave.open(FILENAME, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)

            stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True, input_device_index=1, frames_per_buffer=1024)

            print('Recording...')
            for _ in range(0, self.RATE // self.CHUNK * self.RECORD_SECONDS):
                wf.writeframes(stream.read(self.CHUNK))
            print('Done')

            stream.close()
            self.p.terminate()

    def play(self,file_name):
        # if len(sys.argv) < 2:
        #     print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
        #     sys.exit(-1)
        wf = wave.open(file_name, 'rb')

        # with wave.open(sys.argv[1], 'rb') as wf:

        # Open stream (2)
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play samples from the wave file (3)
        while len(data := wf.readframes(self.CHUNK)): 
            stream.write(data)

        # Close stream (4)
        stream.close()

        # Release PortAudio system resources (5)
        self.p.terminate()
    
    def generator_file_name(self):
        file_name = "audio.wav"
        if os.path.exists(file_name) :   
            nom,extension = os.path.splitext(file_name)
            i=1
            while os.path.exists(f"{nom}_{i}.{extension}"):
                i+=1
            new_name = f"{nom}_{i}.{extension}"
            return new_name
        else:    
            return file_name
        
if __name__ == "__main__":
    audio = Audio()
    codec = Data_codec()
    audio.record("test1.wav")

    cod = codec.encodage_simple(None,2,"test1.wav")
    
    os.remove("test1.wav")
   

    codec.decodage_simple(cod,2,"test1.wav")
    # time.sleep(5)
    # audio.play("test1.wav")