clear all;
audio = 'ielson.wav'
% Sinput is our amplitude values and Fs the sample frequency
[Sinput,Fs] = audioread(audio);
L = length(Sinput);
Ts = 1/Fs;
t = (0:L-1)*Ts;

% Play original audio
sound(Sinput, Fs);


figure(1)
subplot(2,1,1);
% Display the original audio
plot(t, Sinput)
title('Original Signal')
xlabel('t (ms)')
ylabel('X(t)')


figure(2)
subplot(2,1,1)
freqsX = (0:L-1)*(Fs/L);
freqsReais = freqsX(1:floor(L/2));
fft_test = fft(Sinput);

% Only get the real values for the amplitude/magnitude (abs)
mag = abs(fft_test/L);
% In order to PLOT correctly we have to normalize our magnitude so it
% matches to our original signal
magNormalizada = mag(1:floor(L/2));
% Display the signal on the domain frequency (after the FFT)
plot(freqsReais, magNormalizada)

% Usamos um filtro IIR (biquad) pois a distorcao na fase nao importa
% o filtro IIR acaba precisando menos coeficientes em relacao ao FIR
Filtrinho = designfilt('bandstopiir','FilterOrder',10, ...
               'HalfPowerFrequency1',60,'HalfPowerFrequency2',61, ...
               'DesignMethod','butter','SampleRate',Fs);
fvtool(Filtrinho)
saidaFiltrada = filter(Filtrinho, Sinput);
figure(1)
subplot(2,1,2);
plot(t, saidaFiltrada);

sound(saidaFiltrada, Fs)
figure(2)
subplot(2,1,2);
fftFiltrada = fft(saidaFiltrada);
magFiltrada = abs(fftFiltrada/L);
magFiltNorm = magFiltrada(1:floor(L/2));
plot(freqsReais, magFiltNorm)