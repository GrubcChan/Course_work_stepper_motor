
#include <CustomStepper.h>            
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);

CustomStepper stepper(8, 9, 10, 11); 

int example = 1, variable, variable1, rotation, button, button_prev, c, angle, angle1, angle2;                     

void setup()
{
  lcd.init();                      
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Donate 5$ to sup");
  lcd.setCursor(0,1);
  lcd.print("port the project");
  stepper.setSPR(4075.7728395);       // Устанавливаем кол-во шагов на полный оборот. Максимальное значение 4075.7728395
  Serial.begin(9600);
}

void loop()
{
  button = digitalRead(7);
  if (button == 1 && button_prev == 0)
  {
    c++;
    button_prev = 1;
  }

    if (button == 0 && button_prev == 1)
  {
    button_prev = 0;
  }
  variable = analogRead(A0);
  if(c % 2 == 0)
  {
  rotation = map(variable, 0, 1023, 5, 20);
  stepper.setRPM(rotation);                 // Устанавливаем кол-во оборотов в минуту
  if (stepper.isDone())  
  {
    stepper.setDirection(CW);         // Устанавливает направление вращения. Может принимать 3 значения: CW - по часовой, CCW - против часовой, STOP
    stepper.rotate(1);                // Устанавливает вращение на заданное кол-во оборотов
  }
  }
  else
  {
  if (stepper.isDone() && (variable > (variable1 + 10) || variable < (variable1 - 10)))
  {
    variable1 = analogRead(A0);
    
    angle2 = map (variable, 0, 1023, 0, 360);
    angle = angle2 - angle1;
    if(angle > 0)
    stepper.setDirection(CCW);
    else
    stepper.setDirection(CW);
    stepper.rotateDegrees(abs(angle));        // Поворачивает вал на заданное кол-во градусов. Можно указывать десятичную точность (например 90.5), но не принимаются отрицательные значения
    angle1 = angle2; 
  }
  }
  stepper.run();                      // Этот метод обязателен в блоке loop. Он инициирует работу двигателя, когда это необходимо
}
