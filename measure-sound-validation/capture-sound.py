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
DURATION = 3
# Number of points
POINTS = DURATION*FS

# TODO:
# Real time fft plotting
# Run both programs over TCP/IP using handshake etc

def capture_audio():
    recording = sd.rec(int(POINTS), samplerate=FS, channels=2)
    sd.wait()  # Wait until recording is finished
    print("The recorded audio returns a 2D array with (frequency sample*duration in s) points, so it would be 2 equal columns because we chose stereo.")
    print("Shape: \n", recording.shape)
    print("Values: \n", recording)
    #write('output.wav', FS, myrecording)  # Save as WAV file
    return recording 

def analyze_audio(audio):
    # Just extract one column (mono) since it's stereo
    audio = audio[:,0]
    yf = rfft(audio)
    xf = rfftfreq(POINTS, 1 / FS)

    plt.plot(xf, np.abs(yf))
    plt.show()

    # TODO: Add phase view

def time_domain_plot(audio):
    # Play audio live
    pass

def main():
    recording = capture_audio()
    analyze_audio(recording)

main()

