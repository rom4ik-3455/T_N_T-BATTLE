import time
import random
import mcpi.minecraft as minecraft
import mcpi.block as block 
import minecraftstuff
mc=minecraft.Minecraft.create()
#создаём функции)
def checkHit(x,y,z):
#определяем касание
    events=mc.events.pollBlockHits()
    for i in events:
        epos=i.pos
        if x==epos.x and y==epos.y and z==epos.z:
            return True
            
def gun(x,y,z,pos,power,distance,currentMode):
#создаём TNT пушку и список
    gun_blocks = [
        minecraftstuff.ShapeBlock(-1,2,0,block.GOLD_BLOCK.id),
        minecraftstuff.ShapeBlock(0,1,0,block.DIAMOND_BLOCK.id),
        minecraftstuff.ShapeBlock(1,1,0,block.WATER.id),
        minecraftstuff.ShapeBlock(6,1,0,block.DIAMOND_BLOCK.id),
        minecraftstuff.ShapeBlock(2,2,0,152)
    ]
    for i in range(6):
        gun_blocks.append(minecraftstuff.ShapeBlock(0+i,0,0,block.DIAMOND_BLOCK.id))
        gun_blocks.append(minecraftstuff.ShapeBlock(0+i,1,1,block.DIAMOND_BLOCK.id))
        gun_blocks.append(minecraftstuff.ShapeBlock(0+i,1,-1,block.DIAMOND_BLOCK.id))
    gun_pos=pos.clone()
    gun_pos.x=x
    gun_pos.y=y
    gun_pos.z=z
    minecraftstuff.MinecraftShape(mc,gun_pos,gun_blocks)
#создание бесконечного цикла
    while True:
        time.sleep(0.1)
        if checkHit(x-1,y+2,z)==True:
            mc.setBlock(x+4,y+1,z,block.DIAMOND_BLOCK.id)
            #Создание запала. 
            for i in range(distance):
                mc.setBlock(x+2,y+1,z,block.TNT.id)     
            mc.setBlock(x+5,y+2,z,152)
            #Даем запалу гореть определенное количество времени.
            time.sleep(currentMode[0])# 0.5 0.7 1.2  2   3.5
            #Ставим снаряд.
            for i in range(power):
              mc.setBlock(x+5,y+1,z,block.TNT.id)
            #Открываем 1 заслонку, чтобы вода протекла 
            time.sleep(currentMode[1])# 3.2  2.7   2.8 2  1.7   0.1
            mc.setBlock(x+4,y+1,z,0)
            #Открываем ствол пушки
            time.sleep(0.1)
            mc.setBlock(x+6,y+1,z,0)

            #закрываем ствол назад. Откат
            time.sleep(1)
            mc.setBlock(x+5,y+2,z,0)
            mc.setBlock(x+6,y+1,z,block.DIAMOND_BLOCK.id)
                        
def GUN_AI(x,y,z,pos,power,distance,currentMode):
    gun_blocks = [
        minecraftstuff.ShapeBlock(1,2,0,block.GOLD_BLOCK.id),
        minecraftstuff.ShapeBlock(0,1,0,block.DIAMOND_BLOCK.id),
        minecraftstuff.ShapeBlock(-1,1,0,block.WATER.id),
        minecraftstuff.ShapeBlock(-6,1,0,block.DIAMOND_BLOCK.id),
        minecraftstuff.ShapeBlock(-2,2,0,152)
    ]
    for i in range(6):
        gun_blocks.append(minecraftstuff.ShapeBlock(-i,0,0,block.DIAMOND_BLOCK.id))
        gun_blocks.append(minecraftstuff.ShapeBlock(-i,1,1,block.DIAMOND_BLOCK.id))
        gun_blocks.append(minecraftstuff.ShapeBlock(-i,1,-1,block.DIAMOND_BLOCK.id))
    gun_pos=pos.clone()
    gun_pos.x=x
    gun_pos.y=y
    gun_pos.z=z
    minecraftstuff.MinecraftShape(mc,gun_pos,gun_blocks)
#создание бесконечного цикла
    while True:
        time.sleep(1)
        if random.randint(1,5)==1:
            mc.setBlock(x-4,y+1,z,block.DIAMOND_BLOCK.id)
            #Создание запала. 
            for i in range(distance):
                mc.setBlock(x-2,y+1,z,block.TNT.id)     
            mc.setBlock(x-5,y+2,z,152)
            #Даем запалу гореть определенное количество времени.
            time.sleep(currentMode[0])# 0.5 0.7 1.2  2   3.5
            #Ставим снаряд.
            for i in range(power):
              mc.setBlock(x-5,y+1,z,block.TNT.id)
            #Открываем 1 заслонку, чтобы вода протекла 
            time.sleep(currentMode[1])# 3.2  2.7   2.8 2  1.7   0.1
            mc.setBlock(x-4,y+1,z,0)
            #Открываем ствол пушки
            time.sleep(0.1)
            mc.setBlock(x-6,y+1,z,0)

            #закрываем ствол назад. Откат
            time.sleep(1)
            mc.setBlock(x-5,y+2,z,0)
            mc.setBlock(x-6,y+1,z,block.DIAMOND_BLOCK.id)            