int valorDc = 0; 
void setup() {
  cli();//stop interrupts

  // PARA GERAR O PWM VAMOS USAR O TIMER0, OU SEJA, O TEMPORIZADOR0
  TCCR0A = 0;   // COLOCAR TODOS OS BITS DESSE REGISTRADOR PARA 0
  TCCR0B = 0;   // COLOCAR TODOS OS BITS DESSE REGISTRADOR PARA 0
  TCNT0  = 0;   // TimerCounterRegister0 initialize counter value to 0
  OCR0A = 19;   // OutputCompareRegister seta o valor maximo em que o timer TCNT0 vai contar!
  
  // SETANDO PRESCALER PARA DIVIDIR A FREQUENCIA EM 64 E HABILITANDO A COMPARACAO turn on CTC mode
  TCCR0A |= (1 << WGM01);  // SETAMOS APENAS O WGM01 COM BIT 1, QUE OLHANDO NO DATASHEET EH O QUE O ATIVA O MODO CTC
  
  // Set CS01 and CS00 bits for 64 prescaler
  TCCR0B |= (1 << CS01);  // COLOCOU BIT 1 NO CS01 E CS00 DO REGISTRADOR TCCR0B, QUE EH BASICAMENTE SETAR O PRESCALER PRA 64BITS
  // enable timer compare interrupt
  TIMSK0 |= (1 << OCIE0A);       // COLOCANDO BIT 1 NA POSICAO OCIE0A, QUE HABILITA O BIT DE INTERRUPCAO NO STATUS REGISTER, QUE EH BASICAMENTE ATIVAR
                                 // A INTERRUPCAO QUANDO O COMPARADOR CHEGAR NO VALOR DE OCR0A

                                 
  DDRD |= 0b00001000;  // SETAR O PINO 3 COMO SAIDA, DEPOIS ESCREVEMOS NO PORTD SE EH NIVEL ALTO OU BAIXO

  sei();    //allow interrupts locally
  // Habilitar a porta serial para podermos receber os dados do ADC
  Serial.begin(9600);
}


// Argumento do ISR eh dizer em qual porta ele vai ativar a interrupcao
// Dizemos aqui que a porta a que o interrupt eh sensivel eh o comparador do timer0, ou seja, toda vez que ele for verdadeiro, i.e quando o comparador contar ate 19, este sera verdadeiro
ISR(TIMER0_COMPA_vect) {
  // isso acontece na metade do periodo, assumindo q o duty cycle eh de 50%
  PORTD ^= 0b00001000;   // variando o pino 0000 1000   

  // TODO: ENTRAR COM NIVEL DC, SE FOR 5V -> 100% DUTY CYCLE
  // 1V -> 20% DO DUTY CYCLE
  // iremos trablhar como uma faixa, de 10% a 90%
  
}

void loop() {
  valorDc = analogRead(A0); //PINO23
  //Serial.println(valorDc);
  if valorDc 

}
