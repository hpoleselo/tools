import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
from pandas import DataFrame, Series

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
    #print("Values: \n", recording)
    #write('output.wav', FS, recording)
    return recording 

def analyze_audio(audio):
    # Just extract one column (mono) since it's stereo
    audio = audio[:,0]
    yf = rfft(audio)
    # Return in abs because we want the module from a complex number, despite having only real part (because of the rrft)
    yf_s = Series(abs(yf))
    
    # The band where we want to detect our signal 17-21kHz
    yf_s = yf_s[17000:21000]
    print(yf_s.nlargest(20))


    # Show on graph the correspondant point
    xf = rfftfreq(POINTS, 1 / FS)
    plt.plot(xf, np.abs(yf))
    plt.show()

def extract_correspondant_freq():
    # Return in abs because we want the module from a complex number, despite having only real part (because of the rrft)
    # Create the following magnitude:
    yf_df = DataFrame({'magnitude':abs(yf)})
    print(yf_df)
    yf_df['freq'] = ''
    yf_df['freq'] = yf_df.index
    #print(yf_df.index.name)
    #yf_df.set_index('freq', inplace=True)
    print(yf_df.loc[(yf_df['magnitude'] > 30) & (yf_df['freq'] > 10000)])
    #for col in yf_df.columns:
    #   yf_df[yf_df[col] > 30].index.tolist()
    #print(yf_df.nlargest(5,'magnitude'))

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

