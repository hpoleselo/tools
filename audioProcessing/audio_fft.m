% importamos o arquivo manualmente usando Import Data
% ele irá converter o arquivo em amplitudes pelo tempo amostral fs 44100
% e guardar as amplitudes em data

% para ouvir o audio fazemos sound(data,fs)

%fs eh frequency sample
sound(data,fs);
plot(fs,data);
% tf de fourier do sinal
%x_fft = fft(data);
