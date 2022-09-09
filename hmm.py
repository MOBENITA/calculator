import wave
ob = wave.open("output.wav", "rb")
print('NUMBERS OF CHANNELS',ob.getnchannels())
print("SAMPLE WIDTH ",ob.getsampwidth())
print("FRAME RATE",ob.getframerate())
print("NUMBER OF FRAMES",ob.getnframes())
print("PARAMETERS",ob.getparams())

time = ob.getnframes() / ob.getframerate()
print(time)

frame = ob.readframes(-1)
print(type(frame), type(frame[0]))
print(len(frame))

ob.close()

import wave
import matplotlib.pyplot as plt
import numpy as np

ob = wave.open("output.wav", "rb")
sample_freq = ob.getframerate()
n_sample = ob.getnframes()
signal_waves =77777777777777777777