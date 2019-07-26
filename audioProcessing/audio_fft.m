% importamos o arquivo manualmente usando Import Data
% ele irá converter o arquivo em amplitudes pelo tempo amostral fs 44100
% e guardar as amplitudes em data

% comprimento do audio eh o data*frequencia, vai dar em segundos

% para ouvir o audio fazemos sound(data,fs)
%sound(data,fs);
plot(data);
lengthOfSignal = length(data);
% tf de fourier do sinal, precisamos do parametro length pra determinar o
% tamanho do nosso pi! a tf so funciona assim
x_fft = fft(data);
plot(abs(44100,x_fft));
