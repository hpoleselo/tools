import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

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
    # Number of samples in normalized_tone
    N = FS * DURATION

    yf = rfft(audio)
    xf = rfftfreq(N, 1 / FS)

    plt.plot(xf, np.abs(yf))
    plt.show()


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, FS * DURATION, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians

    
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

def main():
    # Generate a 2 hertz sine wave that lasts for 5 seconds
    x, y = generate_sine_wave(2, FS, DURATION)

    _, nice_tone = generate_sine_wave(400, FS, DURATION)
    _, noise_tone = generate_sine_wave(4000, FS, DURATION)
    noise_tone = noise_tone * 0.3

    mixed_tone = nice_tone + noise_tone
    normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

    plt.plot(normalized_tone[:1000])
    plt.show()
    analyze_audio(normalized_tone)
    write("mysinewave.wav", FS, normalized_tone)


main()
