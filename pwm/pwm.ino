//  valor de ocr2b/ocr2a é o duty cicle
//  No caso ai começa com 50%
void setup() {
  pinMode(3, OUTPUT); // saida do pwm
  //pinMode(11, OUTPUT);
  pinMode(A0, INPUT);   // entrada do sinal DC pra controlar o duty cycle
  // usando a operacao de setar os bits especificos usando a macro _BV() (bit value)
  TCCR2A = _BV(COM2A0) | _BV(COM2B1) | _BV(WGM20); // ligando o comparador para o OCR2A e limpando o comparador OCR2B, e usando PWM Phase Correct Mode
  TCCR2B = _BV(WGM22) | _BV(CS20);  // 
  OCR2A = 160;  // maximo do PWM, 80% de 256 bits
  OCR2B = 50; // teste pra testar o pwm separado, nao precisamos quando estamos lendo do ADC
  // Para inicializar o monitoramento do ADC
  Serial.begin(9600);
}


void loop() {
  
  float leituraADC = analogRead(A0);
  // Para monitorar o ADC
  Serial.println(leituraADC);
  // mapeamos os valores de 1 a 159 pois se mapeassemos de 0 a 160, em 0 nao haveria frequencia assim como em 160 tambem nao
  float valorMapeado = map(leituraADC,0,1023,1,159);  // mapeamento dos valores de 10 bits pra 8 bits (do ADC p/ uC)
  OCR2B = valorMapeado;
}
