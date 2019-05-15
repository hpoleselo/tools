% Takes a single input (a pure sin wave of frequency 60hz
% Then plots the fft in the frequency domain!
% Notes we should see one impulse on the frequency 60hz.

function fftWithoutNoise()
    % Period sample
    Ts = 1/Fs;
    % Length of the signal
    L = 1500;
    % Creates a signal of length 1500, meaning the vector will be 1500 long
    % Containing from 0 to 1.5 spaced with 0.001, meaning each value for t is
    % 0.001 of second, i.e milisecond.
    t = (0:L-1)*Ts;

    % Input signal parameters
    amp = 2;
    freq = 60;
    % Input signal, vm*sin(2pift)
    Sinput = amp*sin(freq*2*pi*t);

    % Plot the signal on time domain
    % Since the signal's freq is quite high, we would see too much on the graph
    % So we scale it by (1:freq)
    %plot(t,Sinput)
    plot(1000*t(1:60),Sinput(1:60))
    title('Original Signal')
    xlabel('t (ms)')
    ylabel('X(t)')

    % applying the fft to the input function
    fft_test = fft(Sinput);

    % a fft vai retornar numeros complexos, por isso o abs dela retornara a
    % magnitude do numero complexo!
    P2 = abs(fft_test/L); % fft/length of signal
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);

    % "Building" the frequency domain, i.e the x-axis! 
    f = Fs*(0:(L/2))/L;
    figure
    title('Two-sided spectrum')
    xlabel('frequency (Hz)')
    ylabel('Magnitude of the FFT')
    plot(f,P1)
end
