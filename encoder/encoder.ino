#include <TimerOne.h>
#include <util/atomic.h>

#define OUT_LED() DDRD |= ((1 << 2))
#define SET_LED() PORTD |= ((1 << 2))
#define CLR_LED() PORTD &= ~((1 << 2))

char * msg = "one" ;

#define START 0x2001 //10000001
#define STOP 0x1332 //01111110

#define T 20 //microsecond
#define D 1000 //micorsecond

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  pinMode(10, OUTPUT);
  digitalWrite(10,HIGH);

  
  OUT_LED();
  SET_LED();

}


// the loop routine runs over and over again forever:
void run_start_word(){

}

void run_string(){

}

void run_stop_word(){

}

void run_time_symbol(){
  float d_milli = D/1000;
  SET_LED();
  delay(d_milli);
  CLR_LED();
  delay(d_milli);
  SET_LED();
}

void loop() {
  static int i = 0;
  //if (i%10 == 0){
    run_time_symbol();
  //}
    run_start_word();
    run_string();
    run_stop_word();
    i += 1;
}


