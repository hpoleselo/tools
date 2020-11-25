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
# Add phase view on analyze-audio()

def capture_audio():
    recording = sd.rec(int(POINTS), samplerate=FS, channels=2)
    sd.wait()
    print("The recorded audio returns a 2D array with (frequency sample*duration in s) points, so it would be 2 equal columns because we chose stereo.")
    print("Shape: \n", recording.shape)
    print("Values: \n", recording)
    #write('output.wav', FS, recording)
    return recording 

def analyze_audio(audio):
    # Just extract one column (mono) since it's stereo
    audio = audio[:,0]
    yf = rfft(audio)
    # Return in abs because we want the module from a complex number, despite having only real part (because of the rrft)
    energy_peak = np.max(np.abs(yf))
    print("\nEnergy Peak: ", energy_peak)
    #correspondent_index = np.where(yf == energy_peak)
    # TODO: We have to threshold it because somehow the max peak is being on 0Hz
    # Use Pandas to do that (get 3 highest peak values but limit it to 1000 for magnitude)
    #yf(correspondent_index)
    #print("\nCorrespondent Frequency Peak: ", frequency_peak)
    # Show on graph the correspondant point
    xf = rfftfreq(POINTS, 1 / FS)
    plt.plot(xf, np.abs(yf))
    plt.show()

def time_domain_plot(audio):
    # Play audio live
    # Extract one channel
    audio = audio[:,0]
    # Generating info for the x-axis
    time = np.linspace(0, (len(audio)/FS), num=len(audio))
    plt.title("Audio in Time Domain:")
    plt.plot(time, audio)
    plt.show()

def main():
    recording = capture_audio()
    analyze_audio(recording)

main()

