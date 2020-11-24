import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt

#sudo apt-get install libportaudio2 in order to use sounddevice
#sudo apt-get install python3-tk

# Sample frequency
FS = 44100
# In seconds
DURATION = 5

def capture_audio():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file 


def analyze_audio(audio):
    pass


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, FS * DURATION, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


def main():
    # Generate a 2 hertz sine wave that lasts for 5 seconds
    x, y = generate_sine_wave(2, FS, DURATION)
    plt.plot(x, y)
    plt.show()

main()
