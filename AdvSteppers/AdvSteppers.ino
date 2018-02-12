#include <AccelStepper.h>
#include <MultiStepper.h>
#define yPin A0
#define xPin A1
double xIn;
double yIn;
long positions[] = {1500, 2000};

MultiStepper steppers;
AccelStepper xAxis(AccelStepper::HALF4WIRE, 4, 5, 6, 7);
AccelStepper yAxis(AccelStepper::HALF4WIRE, 8, 9, 10, 11);

void setup()
{
	steppers.addStepper(xAxis);
	steppers.addStepper(yAxis);

    xAxis.setMaxSpeed(200.0);
    xAxis.setAcceleration(100.0);

    yAxis.setMaxSpeed(200.0);
    yAxis.setAcceleration(100.0);
    
}
void loop(){
	steppers.moveTo(positions);
	steppers.runSpeedToPosition();
}
/*
void nstepXY(){
	int x = xVal;
	int y = yVal;
	while (x != 0 || y != 0){
		if (x < 0){
			xAxis.step(-1);
			xPoint--;
			x++;
		}
		else if (xVal > 0){ 
			xAxis.step(1);
			xPoint++;
			x--;
			
		}
		if (y < 0){
			yAxis.step(-1);
			yPoint--;
			y++;
		}
		else if (yVal > 0){
			yAxis.step(1);
			yPoint++;
			y--;
		} 
  	}
  }
void jsInput() {
  
  yIn = analogRead(yPin);
  xIn = analogRead(xPin);
  xVal = map(xIn, 0, 1023, -200, 200);
  yVal = map(yIn, 0, 1023, -200, 200);
  r = sqrt(fabs(xVal * xVal) + fabs(yVal * yVal));
  
  if (r <= 5) r = 0;
  if (fabs(xVal) <= 10) xVal = 0;
  if (fabs(yVal) <= 10) yVal = 0;
  
  //if (time - lastTime )
  /*
  for (int i = 1; i <= 100; i++){
	xAxis.step(1);
	yAxis.step(1);
}
  for (int i = 1; i <= 100; i++){
	xAxis.step(1);
	yAxis.step(-1);
  }
  for (int i = 1; i <= 100; i++){
	xAxis.step(-1);
  }
}
*/


