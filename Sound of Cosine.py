import pyaudio
import numpy as np
fs=44800;
f=1000
t=np.arange(0,2,1/fs)
y=np.cos(2*np.pi*f*t)
play=pyaudio.PyAudio()
stream = play.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
volume=0.5
stream.write(volume*y)
stream.stop_stream()
stream.close()
play.terminate()
