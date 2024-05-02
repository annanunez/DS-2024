from machine import Pin, I2C
import ssd1306
import machine
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
led1 = machine.Pin(25, machine.Pin.OUT)
led2 = machine.Pin(26, machine.Pin.OUT)

botao1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
            
largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

while True: 
  
    if botao2.value() == 0:
      led1.value(1)
      led2.value(0)
      tela.fill(0)
      tela.text('A umidade da', 0, 0)
      tela.text('sala e de ', 0, 10)
      tela.text('20% ', 0, 20)
      tela.show()
    
    elif botao1.value() == 0:
      led2.value(1)
      led1.value(0)
      tela.fill(0)
      tela.text('A temperatura', 0, 0)
      tela.text('do quarto e', 0, 10)
      tela.text('30 graus ')

      tela.show()
    
    time.sleep(0.1)
    
