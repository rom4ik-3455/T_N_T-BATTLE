from guns import *
import threading
################################################################################
################################################################################
################################################################################
pos=mc.player.getTilePos()
power=10
distance=18
modes=[
   [0.5,3.2],
   [0.7,2.7],
   [1.2,2],
   [2,1.7],
   [3.5,0.1]]
currentMode=modes[2]
#################################################################################
#################################################################################
#################################################################################
#AI-искуственный интелект
#own-собственость
###############################AI############################################################
tread1AI=threading.Thread(target=GUN_AI,args=(pos.x+30,pos.y+20,pos.z,pos,7,13,modes[3]))
tread2AI=threading.Thread(target=GUN_AI,args=(pos.x+30,pos.y+20,pos.z+6,pos,10,14,modes[3]))
###########################OWN##############################################################
tread3OWN=threading.Thread(target=gun,args=(pos.x+5,pos.y+20,pos.z,pos,12,17,modes[2]))
tread4OWN=threading.Thread(target=gun,args=(pos.x+5,pos.y+20,pos.z+5,pos,11,15,modes[2]))
#запускаем потоки
tread3OWN.start()
tread1AI.start()
tread2AI.start()
tread4OWN.start()
#ждем завершения потоков
tread3OWN.join()
tread1AI.join()
tread2AI.join()
tread4OWN.join()