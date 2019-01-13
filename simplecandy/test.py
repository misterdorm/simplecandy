#!/usr/bin/env python
import simplecandy
from sys import exit
import time

sc = simplecandy.SimpleCandy('192.168.101.199:7890')
########################################################

r = 10
g = 30
b = 80

# Turn on:
# sc.lightOn(r, g, b, lightNumber)
# sc.lightOn(r, g, b) turns all that color

# Turn off:
# sc.lightOff(lightNumber)
# sc.lightOff() turns all off

#for i in range(0,50):
#   sc.lightOn(50, 50, 50, i)
#   time.sleep(0.25)



## SMALL STAR PROGRAM (50 lights)##
## All different colors
sc.lightOn(30,20,0,5)
time.sleep(0.25)
sc.lightOn(13,12,21,32)
time.sleep(0.25)
sc.lightOn(6,80,16, 21)
time.sleep(0.25)
sc.lightOn(87,92,34,17)
time.sleep(0.25)
sc.lightOn(100,100,100,12)
time.sleep(0.25)
sc.lightOn(20,32,14,1)
time.sleep(0.25)
sc.lightOn(49,49,0,2)
time.sleep(0.25)
sc.lightOn(80,50,23,3)
time.sleep(0.25)
sc.lightOn(28,32,91,4)
time.sleep(0.25)
sc.lightOn(100,21,38,7)
time.sleep(0.25)
sc.lightOn(76,39,100, 8)
time.sleep(0.25)
sc.lightOn(10, 100 ,92,9)
time.sleep(0.25)
sc.lightOn(83, 29, 29, 10)
time.sleep(0.25)
sc.lightOn(33, 20,38,11)
time.sleep(0.5)
sc.lightOn(39, 39 ,29,13)
time.sleep(0.25)
sc.lightOn(28,20,19,14)
time.sleep(0.25)
sc.lightOn(28, 68,92, 15)
time.sleep(0.25)
sc.lightOn(29, 87, 67, 16)
time.sleep(0.25)
sc.lightOn(23, 39,82,18)
time.sleep(0.25)
sc.lightOn(38, 43,29,19)
time.sleep(0.25)
sc.lightOn(92,20,12,20)
time.sleep(0.25)
sc.lightOn(30,20, 23,22)
time.sleep(0.25)
sc.lightOn(93, 89,34,23)
time.sleep(0.25)
sc.lightOn(28, 0,0,24)
time.sleep(0.25)
sc.lightOn(39,20,91,25)
time.sleep(0.25)
sc.lightOn(49,39,38,26)
time.sleep(0.25)
sc.lightOn(90,50,23,27)
time.sleep(0.25)
sc.lightOn(99,49,43,28)
time.sleep(0.25)
sc.lightOn(99, 88,77,29)
time.sleep(0.25)
sc.lightOn(66,55,44,30)
time.sleep(0.25)
sc.lightOn(33,22,11,31)
time.sleep(0.25)
sc.lightOn(12,34,56,32,)
time.sleep(0.25)
sc.lightOn(12,23,34,6)
time.sleep(0.25)
sc.lightOn(45,56,67,33)
time.sleep(0.25)
sc.lightOn(78,89,90,34)
time.sleep(0.25)
sc.lightOn(1,23,34,35)
time.sleep(0.25)
sc.lightOn(39,39,20,36)
time.sleep(0.25)
sc.lightOn(023,30,30,37)
time.sleep(0.25)
sc.lightOn(92,94,38,38)
time.sleep(0.25)
sc.lightOn(38,28,28,39)
time.sleep(0.25)
sc.lightOn(20,93,29,40)
time.sleep(0.25)
sc.lightOn(94,57,94,41)
time.sleep(0.25)
sc.lightOn(10,29,38,42)
time.sleep(0.25)
sc.lightOn(47,56,10,43)
time.sleep(0.25)
sc.lightOn(29,38,47,44)
time.sleep(0.25)
sc.lightOn(29, 93,34, 45)
time.sleep(0.25)
sc.lightOn(32,99,55,46)
time.sleep(0.25)
sc.lightOn(29,28,73,47)
time.sleep(0.25)
sc.lightOn(83,47,38,48)
time.sleep(0.25)
sc.lightOn(52,32,5,49)
time.sleep(1)
sc.lightOff()
## All pink
time.sleep(2)
sc.lightOn(100,21,38)
time.sleep(3)
sc.lightOff()
time.sleep(0.25)
## Christmas tree
sc.lightOn(83,29,29,10)
time.sleep(2.5)
for i in range(0,10):
   sc.lightOn(0, 100, 0, i)
   time.sleep(0.25)
for i in range (11,19):
     sc.lightOn(0,100,0,i)
     time.sleep(0.25)
time.sleep(3)
sc.lightOff()
## Packman ghosts
time.sleep(4)
sc.lightOn(100,0,0,10)
time.sleep(0.25)
sc.lightOn(100,0,0,37)
time.sleep(0.25)
sc.lightOn(100,0,0,28)
time.sleep(0.25)
sc.lightOn(100,0,0,19)
time.sleep(0.25)
sc.lightOn(100,0,0,49)
time.sleep(3)
for i in range(0,49,):
   sc.lightOn(87, 80, 0, i)
   time.sleep(0.1)
for i in range(49,0,-1):
   sc.lightOn(0, 0, 80, i)
   time.sleep(0.1)
time.sleep(0.15)
for i in range(0,49,):
   sc.lightOn(0,80,0, i)
   time.sleep(0.1)
time.sleep(0.15)
for i in range(49,0,-1):
   sc.lightOn(80, 0, 0, i)
   time.sleep(0.1)
sc.lightOff()
## Red/white/blue star
time.sleep(3)
for i in range(0,17):
   sc.lightOn(0,0 ,80 , i)
   time.sleep(0.25)
for i in range(17,33):
   sc.lightOn(50,50,50, i)
   time.sleep(0.25)
for i in range(33,49):
   sc.lightOn(80, 0, 0, i)
   time.sleep(0.25)
time.sleep(5)
sc.lightOff()
## whole star orange
time.sleep(2)
sc.lightOn(100,53,0)
time.sleep(5)
## Manger
sc.lightOff()
for i in range(9,12):
   sc.lightOn(100,100,100, i)
   time.sleep(0.25)
for i in range(20,46):
   sc.lightOn(100,65,22, i)
   time.sleep(0.25)
time.sleep(2)
sc.lightOff()
## Each line different color
time.sleep(0.5)
for i in range(0,11):
   sc.lightOn(100, 0, 0, i)
   time.sleep(0.25)
for i in range(11,20):
   sc.lightOn(100, 53, 0, i)
   time.sleep(0.25)
for i in range(20,29):
   sc.lightOn(87, 80, 0, i)
   time.sleep(0.25)
for i in range(29,37):
   sc.lightOn(0, 80, 30, i)
   time.sleep(0.25)
for i in range(37,49):
   sc.lightOn(0, 0, 100, i)
   time.sleep(0.25)
time.sleep(2)
sc.lightOff()
## Whole thing purple
sc.lightOn(50,0,50)
time.sleep(1.25)
sc.lightOff()
## Seastar
for i in range(7,14):
   sc.lightOn(100,21,38, i)
   time.sleep(0.25)
for i in range(34,41):
   sc.lightOn(0, 0,80, i)
   time.sleep(0.25)
for i in (16,17,18,19,20,21,22):
   sc.lightOn(50,0,50, i)
   time.sleep(0.25)
for i in (43,44,45,46,47,48,49,0,1,2,3,4):
   sc.lightOn(100,53,0, i)
   time.sleep(0.25)
for i in range(25,32):
   sc.lightOn(0,50,20, i)
   time.sleep(0.25)
for i in (5,6,14,15,23,24,33,34,41,42):
   sc.lightOn(100,100,100, i)
   time.sleep(0.25)
time.sleep(2)
sc.lightOff()
## Energy
for i in range(0,49,):
   sc.lightOn(100,0,0, i)
   time.sleep(0.02)
for i in range(49,0,-1):
   sc.lightOn(100,53,0, i)
   time.sleep(0.02)
for i in range(0,49):
      sc.lightOn(83,46,38, i)
      time.sleep(0.02)
for i in range(49,0,-1):
   sc.lightOn(32,99,55, i)
   time.sleep(0.02)
time.sleep(1)
sc.lightOff()
##Bomb
for i in(49,0,47,48,10,28,37,19):
   sc.lightOn(100,0,0, i)
time.sleep(0.75)
for i in(9,11,36,38,18,20,27,29,46,1):
   sc.lightOn(100,53,0, i)
time.sleep(0.75)
for i in(8,12,35,39,17,21,45,2,26,30):
   sc.lightOn(32,99,55, i)
time.sleep(0.5)
for i in(7,13,25,31,34,40,16,22,44,3):
   sc.lightOn(83,46,38, i)
time.sleep(0.25)
for i in (14,15,32,33,6,5,4,41,42,43,23,24):
   sc.lightOn(100,100,100, i)
time.sleep(0.25)
time.sleep(1)
sc.lightOff()
# Lightning
for i in range(0,4):
    sc.lightOn(100,100,100)
    time.sleep(0.75)
    sc.lightOff()
    time.sleep(1)
## Thank you
for g in range(0,9):
    start = 0
    end = 49
    step = 1
    for color in ( (83,46,38), (83,29,29), (32,99,55), (100,21,38) ):
        start, end = end, start
        step = -step
        for i in range(start,end,step):
            sc.lightOn(color[0], color[1], color[2], i)
            time.sleep(0.02)
