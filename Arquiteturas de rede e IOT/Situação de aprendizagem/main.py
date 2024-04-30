import machine 
import time 

sem_vermelho = machine.Pin(14, machine.Pin.OUT )
sem_amarelo = machine.Pin(27, machine.Pin.OUT)
sem_verde = machine.Pin(26, machine.Pin.OUT)

while True: 
  sem_verde.value(1)
  time.sleep(3)
  sem_verde.value(0)
  time.sleep(1)
  
  sem_amarelo.value(1)
  time.sleep(1)
  sem_amarelo.value(0)
  time.sleep(1)

  sem_vermelho.value(1)
  time.sleep(5)
  sem_vermelho.value(0)
  time.sleep(1)
  