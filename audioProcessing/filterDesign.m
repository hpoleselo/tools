% Designing filters
Fs  = 48e3;
Fp  = 8e3;
Ap  = 0.01;
Ast = 80;
N = 10;
LP_IIR = dsp.LowpassFilter('SampleRate',Fs,'FilterType','IIR',...
    'DesignForMinimumOrder',false,'FilterOrder',N,...
    'PassbandFrequency',Fp,'PassbandRipple',Ap,'StopbandAttenuation',Ast);

% Trying to filter the data
y = step(LP_IIR, input);    % input would be our audio
plot(y)