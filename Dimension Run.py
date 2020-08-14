from pygame import * 
from random import *
from math import *

global developerMode, gameKeys, gameLives, introIsOn, easterEggIsOn, X, Y, VY, XCONST, ONGROUND, RAPID, move, frame, endGameDialogue, tracker
mixer.init() #initialzing mixer

developerMode = False #allows you to enter levels using numbers and prevents you from taking damage

gameKeys = [1,2,3,4] #keys for each level 
gameLives = 5 #players master lives
introIsOn = True #if the player finished the game introduction
endGameDialogue = False #if the player reached the final dialogue
easterEggIsOn = True #if the player got the easter egg
tracker = 0 #tracks the wave of the fire level

RAPID = 0 #the cool down time between each bullet the player shoots
move = 0 #the set of sprites that fit the players move
frame = 0 #each frame of a set of sprites

print("Dimension Run\nDeveloped by Majd Hailat, Alex MacKay & Rohan Talukdar")
if developerMode is True:
    print("Developer mode is enabled")

def deadScreen(level): #screen that shows when the player dies
    global gameLives, gameKeys, lives, easterEggIsOn
    youDiedBG=image.load("images/youDiedBG.png").convert() #loading images
    gameOverBG=image.load("images/gameOver.png")
    gameHeartPic=image.load("images/gameHeart.png").convert_alpha()
    keyPic=image.load("images/key.png")
    returnToLobbyBTN=Rect(375,500,500,60) #return to lobby button
    retryBTN=Rect(500,400,250,60) #retry button

    gameLives -= 1 #subtracting a game life
    running = True #setting running to true
    myClock=time.Clock() #starting clock
    while running: #main loop
        for evt in event.get(): #event listener
            if evt.type==QUIT: #checking if the player quit the window
                return("exit") #closing window
        mx,my = mouse.get_pos() #getting mouse pos
        mb = mouse.get_pressed() #getting mouse press
        
        if gameLives<=0: #checking if the player lost all the game lives (game over -> has to retsrat)
            screen.blit(gameOverBG,(0,0)) #adding bg
            draw.rect(screen,(0,0,0),returnToLobbyBTN,5) #adding return to lobby button
            if returnToLobbyBTN.collidepoint(mx,my): #checking if the mouse is on the button
                draw.rect(screen,(255,255,255),returnToLobbyBTN,5) #changing color of the button 
                if mb[0]==1: #checking if the button was presses
                    gameKeys=[1,2,3,4] #resetting keys
                    gameLives=5 #resetting game lives
                    easterEggIsOn=True #resetting easter egg
                    return("lobby") #returning the lobby
        else: #the player still has game lives
            screen.blit(youDiedBG,(0,0)) #adding bg
            displayGameLives(gameHeartPic) #displaying players lives
            displayGameKeys(keyPic) #displaying keys
            draw.rect(screen,(0,0,0),returnToLobbyBTN,5) #adding return to lobby button
            draw.rect(screen,(0,0,0),retryBTN,5) #adding retry button
            if retryBTN.collidepoint(mx,my): #checking if the mouse is on the button
                draw.rect(screen,(255,255,255),retryBTN,5) #changing color of the button 
                if mb[0]==1: #checking if the retry button was presses
                    if level=="lobbyDead": #checking which level the player was in previously and returning the player to that level 
                        return("lobby") 
                    elif level==1:
                        return("door1")
                    elif level==2:
                        return("door2")
                    elif level==3:
                        return("door3")
                    elif level==4:
                        return("door4")
                    elif level=="1Complete":
                        return("level1Complete")
                    elif level=="3Complete":
                        return("level3Complete")
            if returnToLobbyBTN.collidepoint(mx,my): #checking if the mouse is on the button
                draw.rect(screen,(255,255,255),returnToLobbyBTN,5) #changing color of the button 
                if mb[0]==1: #checking if the return to lobby button was presses
                    return("lobby") #returning the lobby
        
        display.flip() #showing screen
        myClock.tick(60) #ticking clock

def gameComplete(): #screen that comes up when the player beats the game
    global introIsOn, endGameDialogue, gameLives, gameKeys, easterEggIsOn, tracker
    gameCompleteBG = image.load("images/youwinbg.png") #loading bg
    exitBTN = Rect(410, 505, 410, 60) #exit game button
    restartGameBTN = Rect(465, 405, 305, 60) #restart game button

    running = True #setting running to true
    myClock = time.Clock() #starting clock
    while running: #main loop
        for evt in event.get(): #event listener
            if evt.type == QUIT: #checking if player has quit the window
                return ("exit") #closing window
        mx, my = mouse.get_pos() #getting mouse pos
        mb = mouse.get_pressed() #getting mouse press

        screen.blit(gameCompleteBG, (0, 0)) #adding bg
        draw.rect(screen, (0, 0, 0), restartGameBTN, 5) #adding restart button
        draw.rect(screen, (0, 0, 0), exitBTN, 5) #adding exit button
        if restartGameBTN.collidepoint(mx, my): #checking if the mouse is on the button
            draw.rect(screen, (255, 255, 255), restartGameBTN, 5) #chaning button color
            if mb[0] == 1: #checking if the restart button has been pressed
                introIsOn = True #resetting intro
                endGameDialogue = False #resetting end dialgue
                gameKeys = [1, 2, 3, 4] #resetting keys
                gameLives = 5 #resetting game lives
                easterEggIsOn = True #resetting easter egg
                tracker = 0 #resetting lava waver tracker
                return ("lobby") #returning lobby

        if exitBTN.collidepoint(mx, my): #checking if the mouse is on the button
            draw.rect(screen, (255, 255, 255), exitBTN, 5) #changing button color
            if mb[0] == 1: #checking if the exit button has been pressed
                return ("exit") #closing window

        display.flip() #showing screen
        myClock.tick(60) #ticking clock

def easterEgg(): #easter egg has been found screen
    global gameLives 
    easterEggBG = image.load("images/easterEgg.png") #loading bg
    returnToLobbyBTN = Rect(375, 500, 500, 64) #return to lobby btn

    gameLives+=1 #increasing game lives (thats the easter egg)
    running = True #running is true
    myClock = time.Clock() #setting clock
    while running: #main loop
        for evt in event.get(): #event listener
            if evt.type == QUIT: #checking if the player quit the game
                return ("exit") #closing window
        mx, my = mouse.get_pos() #getting mouse pos
        mb = mouse.get_pressed() #getting mouse clicks

        screen.blit(easterEggBG,(0,0)) #adding bg
        draw.rect(screen, (0, 0, 0), returnToLobbyBTN, 5) #adding btn
        if returnToLobbyBTN.collidepoint(mx, my): #checking if the mouse is on the btn
            draw.rect(screen, (255, 255, 255), returnToLobbyBTN, 5) #changing btn color
            if mb[0] == 1: #checking if the return to lobby btn has been presses
                return ("lobby") #returning lobby

        display.flip() #showing screen
        myClock.tick(60) #ticking clock

def ESCMenu(): #instructions and help menu
    ESCMenuBG = image.load("images/ESCMenu.png") #loading bg
    exitBTN = Rect(185, 590, 270, 70) #exit btn
    returnToLobbyBTN = Rect(640, 590, 435, 70) #return to lobby btn

    running = True #running is true
    myClock = time.Clock() #starting clock
    while running: #main loop
        for evt in event.get(): #event listener
            if evt.type == QUIT: #checking if the player quit the game
                return ("exit") #closing window
        mx, my = mouse.get_pos() #getting mouse pos
        mb = mouse.get_pressed() #getting mouse clicks

        screen.blit(ESCMenuBG, (0, 0)) #adding bg
        draw.rect(screen, (0, 0, 0), returnToLobbyBTN, 5) #adding return to lobby btn
        draw.rect(screen, (0, 0, 0), exitBTN, 5) #adding exit button
        if returnToLobbyBTN.collidepoint(mx, my): #checking if the mouse is on the button
            draw.rect(screen, (255, 255, 255), returnToLobbyBTN, 5) #changing the color of the button
            if mb[0] == 1: #checking if the return to lobby button has been presses
                return ("lobby") #returning lobby

        if exitBTN.collidepoint(mx, my): #checking if mouse is on the btn
            draw.rect(screen, (255, 255, 255), exitBTN, 5) #changing btn color
            if mb[0] == 1: #checking if the btn has been presses
                return ("exit") #closing window

        display.flip() #showing screen
        myClock.tick(60) #ticking clock

def lobby(): #main lobby
    global X, Y, VY, XCONST, ONGROUND, RAPID, lives, introIsOn, gameKeys, developerMode, musicLevel, gameLives, easterEggIsOn, endGameDialogue, move
    global finalBossJumpTimer2, FX, FY, finalBossMove, finalBossFrame, finalBossDirection, finalBossJumpTimer, finalBossDirectionChangeTimer, finalBossTempDirection, isFinalBossJumping, finalBossJumpDirection, finalBossRapid, isFinalBossMoving, finalBossLives, finalBossSpeed, isFinalBossMovingAway
    X = 350 #player x coordinate
    Y = 350 #player y coordinate
    VY = 0 #player vert velocity
    
    speed = 10 #bullet speed
    bullets = [] #bullets list
    
    portalFrame = -1 #frame of portal animation
    dialogueFrame = 0 #dialogue frame
    finalDialogueFrame = 0 #final dialogue frame

    freezePlayer = False #if the movement of the player is suspended
    finalFight = False #if the final boss fight is on

    explosionFrame = 0 #frame of the portal explosion animation
    explosionFrameCount = 0
    portalsExploded = False #if portal explosion animation has been played
    explosionPositions=[[150,220],[360,220],[540,130],[735,220]] #position of explosion animations
    
    FX = 615 #BOSS X coordinate
    FY = 355 #BOSS Y coordinate
    finalBossLives = 20 #boss lives
    finalBossSpeed = 0 #boss movement speed
    finalBossMove = 0 #the set of sprites that fit the dads move
    finalBossFrame = 0 #each frame of a set of sprites
    finalBossDirection = "right" #direction the dad is facing
    finalBossDirectionChangeTimer = 100 #counter to generate a new movement for the dad
    finalBossTempDirection = None #temporairly holds the dads direction
    isFinalBossJumping = False #when dad is jumping
    finalBossJumpDirection = "up" #direction of boss vertical movement
    finalBossJumpTimer = 0 #timer
    finalBossJumpTimer2 = 0
    isFinalBossMoving = False #is dad moving
    isFinalBossMovingAway = False #is dad moving away from the player
    deathAnimationTimer = 0 #dad death animation timer

    finalBossBulletSpeed = 10 #boss bullet speed
    finalBossBullets = [] #boss bullets
    finalBossRapid = 0 #the cool down time between each bullet the boss shoots

    musicName=["music/Roman Heuser - Requiem Of Souls [Epic Music - Dark Action Atmospheric].mp3","music/apocolypseMusic.mp3","music/HYPERDRIVE - Epic Powerful Futuristic Music MixEpic Sci-Fi Hybrid Music.mp3",
               "music/steampunkMusic.mp3","music/fireMusic.mp3"] #list of music files

    lobbyBackground = image.load("images/lobbyBackground.png").convert() #loading images
    lobbyBackground = transform.smoothscale(lobbyBackground, screen.get_size())
    gameHeartPic=image.load("images/gameHeart.png").convert_alpha()
    keyPic=image.load("images/key.png")
    ePic=image.load("images/E.png")
    ePic=transform.scale(ePic,(24,24))
    playerPic=[addPics("all characters",13,15),
      addPics("all characters",25,27)]
    dadPics = [addPics("all characters", 16,18),
        addPics("all characters", 28, 30)]
    portalPics=[addPics("portals",1,3),
      addPics("portals",4,6),
    addPics("portals",7,9),
    addPics("portals",10,12)]
    pizzaPic=image.load("images/pizza.png")
    indicatorPics = image.load("images/indicator.png")
    explosionPics=addPics("explosion",1,5)
    for pic in explosionPics:
        explosionPics[explosionPics.index(pic)]=transform.scale(pic,(90,90))
    deathPics=[]
    for i in range(1,5):
        deathPics.append(image.load("death/death%s.png"%(i)))
    speechPics=[]
    for i in range(1,7):
        speechPics.append(image.load("speech/speech%s.png"%(i)))
    finalSpeechPics=[]
    for i in range(1,6):
        finalSpeechPics.append(image.load("finalspeech/speech%s.png"%(i)))
    for p in portalPics:
        for i in p:
            portalPics[portalPics.index(p)][p.index(i)]=transform.scale(portalPics[portalPics.index(p)][p.index(i)],(130,130))

    plats = [[Rect(50, 415, 1500, 1)], [Rect(120, 310, 145, 1)], [Rect(330, 310, 145, 1)], [Rect(510, 220, 145, 1)],
             [Rect(700, 310, 145, 1)]] #plat rectangles
    portalRects = [[Rect(150, 220, 80, 80), 130, 200], [Rect(360, 220, 80, 80), 340, 200],
                   [Rect(540, 130, 80, 80), 520, 110], [Rect(735, 220, 80, 80), 715, 200]] #portal rectangles
    triggerDialogueRect = Rect(550, 330, 100, 100) #rectangle that trigers the dialogue when tha player collides with

    if len(gameKeys) == 0: #checking if the player beat every level
        lobbyBackground = image.load("images/lobbyBackgroundFinal.png").convert() #loading new background
        lobbyBackground = transform.smoothscale(lobbyBackground, screen.get_size()) #transforming background to fit screen
        endGameDialogue = True #starting end game dialogue

    mixer.music.load(musicName[0]) #loading music
    mixer.music.play(-1) #playing music
        
    running=True #running is true
    myClock=time.Clock() #starting clock
    while running: #main loop
        playerRect=Rect(X,Y+8,30,58) #player rect
        mx,my = mouse.get_pos() #getting mouse pos
        mb = mouse.get_pressed() #getting mouse clicks
        for evt in event.get():#event listener
            if evt.type==QUIT: #checking if player quit the game
                return("exit") #closing window

            if evt.type == MOUSEBUTTONUP and endGameDialogue == False and freezePlayer: #checking that the player can interact with the start of the game dialogue
                if mb[0] == 1: #player clicked
                    dialogueFrame += 1 #moving dialogue frame
                if dialogueFrame >= 6: #checking if the dialogue is over
                    introIsOn = False #turning off intro
                    freezePlayer = False #unfreezing player movement

            if evt.type == MOUSEBUTTONUP and endGameDialogue and freezePlayer: #checking that the player can interact with the end of the game dialogue
                if mb[0] == 1: #player clicked
                    finalDialogueFrame += 1 #moving dialogue frame
                if finalDialogueFrame > 4: #checking if the dialogue is over
                    endGameDialogue = False #turning off end game dialogue
                    finalFight = True #starting final fight
                    gameLives = 8 #resetting game lives
                    freezePlayer = False #unfreezing player
                    mixer.music.load("music/finalFightMusic.mp3") #loading music
                    mixer.music.play() #playing music

        keys=key.get_pressed() #getting key presses
        if keys[K_ESCAPE]: #escape key
            return("ESCMenu") #retruning escape menu
        if developerMode == True: #checking if developer mode is enabled
            if keys[K_1]: #checking which level has been called and returning that level
                return("door1")
            elif keys[K_2]:
                return("door2")
            elif keys[K_3]:
                return("door3")
            elif keys[K_4]:
                return("door4")
            elif keys[K_6]:
                return("level1Complete")
            elif keys[K_7]:
                return("level2Complete")
            elif keys[K_8]:
                return("level3Complete")
            elif keys[K_9]:
                return("level4Complete")
            elif keys[K_0]:
                finalFight = True

        if Y > 750: #checking if the player fell into the easter egg hole 
            if finalFight == False: #checking that the final fight is off
                if easterEggIsOn: #checking if the player has not goten the easter egg yet
                    easterEggIsOn = False #disabling easter egg
                    return ("easterEgg") #returning easter egg screen
                else: #the player has goten the easter egg
                    return ("deadScreenLobby") #returning dead screen
            else: #final fight is on
                gameLives -= 1 #removing life
                X = 350 #resetting player x and y coordinate
                Y = 350

        if gameLives == 0: #checking if the player lost all lived
            gameLives = 9 #resetting lives {make them 9 because the dead screen function takes away 1 life when called so it will actually give the player 8}
            return ("deadScreenLobby") #returning dead screen

        portalFrame = portalFrame + 0.2 #increasing frame counter
        if portalFrame >= 3:  # slowing down animation
            portalFrame = 0  # 1 is the first frame for the animation (0 is idle)

        if freezePlayer == False: #checking if the player should not be frozen 
            movePlayer(playerPic) #calling movement function
        checkCollision(plats) #calling collision function

        #DRAW SCENE
        screen.blit(lobbyBackground,(0,0)) #adding bg
        screen.blit(indicatorPics,(0,645)) #adding indicator that tells the player to open escape menu for help

        if portalsExploded == False: #checking if the portals have not exploded
            screen.blit(portalPics[0][int(portalFrame)],(portalRects[0][1],portalRects[0][2])) #adding portal animations  #level 1 (post apo)
            screen.blit(portalPics[2][int(portalFrame)],(portalRects[1][1],portalRects[1][2]))                            #level 2 (space)
            screen.blit(portalPics[3][int(portalFrame)],(portalRects[2][1],portalRects[2][2]))                            #level 3 (steam punk)
            screen.blit(portalPics[1][int(portalFrame)],(portalRects[3][1],portalRects[3][2]))                            #level 4 (lava)
        try: 
            screen.blit(playerPic[move][int(frame)],(X,Y)) #adding player image
        except:
            screen.blit(playerPic[0][int(0)],(X,Y)) 
        
        if finalFight == False: #checking if final fight is off
            displayGameKeys(keyPic) #calling display game key function
        displayGameLives(gameHeartPic) #calling display game lives function

        if finalFight: #checking if final fight is on 
            finalBoss(bullets,dadPics) #calling final boss function
            finalBossShoot(finalBossBulletSpeed, finalBossBullets) #calling final boss shooting function
            shoot(speed, bullets, plats) #calling player shooting function

        if finalFight == False and finalBossLives > 0: #checking if final fight is off and the boss is alive
            screen.blit(dadPics[finalBossMove][int(finalBossFrame)], (FX, FY)) #adding boss image

        if finalBossLives > 0 and finalFight: #checking if final fight is on and the boss is alive
            dadHealthRect = Rect(30, 15, finalBossLives * 20, 15) #boss health bar
            draw.rect(screen,(255,100,100),(30,15,400,15)) #drawing red health bar beneath the boss health bar so when the boss health decreases the green health turns red
            draw.rect(screen,(100,255,100),dadHealthRect) #drawing boss health bar

        if finalBossLives <= 0: #checking if the boss is dead
            finalFight = False #turning off final fight
            deathAnimationTimer += 0.2 #increasing death animation counter
            if int(deathAnimationTimer) < 4: #checking that the animation is not over
                screen.blit(deathPics[int(deathAnimationTimer)],(FX,365+deathAnimationTimer*4)) #adding animation 
            else: #animation is over
                if FX+50>=1250 or FX+50<=0: #checking if the boss is on the edges of the screen
                    FX=1100 #reassigning boss x coordinate
                screen.blit(pizzaPic, (FX, 330)) #adding pizza picture instead of boss picture
                pizzaRect=Rect(FX+50, 380, 30, 30) #pizza rect
                if playerRect.colliderect(pizzaRect): #checking if the player collided with pizza
                    return("gameComplete") #returning game complete screen

        for p in portalRects: #itterating through portal rects
            if playerRect.colliderect(p[0]) and introIsOn==False and ((portalRects.index(p)+1) in gameKeys): #checking if player collides with portal and the intro is done and the level has not been finished
                screen.blit(ePic,(p[1]+50,p[2]-30)) #adding e image
                if keys[K_e]: #checking if the player pressed e
                    try: 
                        mixer.music.load(musicName[portalRects.index(p)+1]) #loading specific level music
                        mixer.music.play(-1)
                    except:
                        mixer.music.load(musicName[0])
                        mixer.music.play(-1)
                    return("door%s"%(portalRects.index(p)+1)) #returning that specific level
                    
        if playerRect.colliderect(triggerDialogueRect) and introIsOn: #checking if the dialogue should start
            screen.blit(speechPics[dialogueFrame],(0,570)) #adding dialogue images
            freezePlayer = True #freezing player
            if Y<358: #moving the player to the ground if hes in the air
                Y+=10

        if endGameDialogue: #checking if the end game dialogue is on 
            if portalsExploded == False: #checking if the portals are still up
                if explosionFrameCount >= 10: #checking if the animation is over
                    explosionFrame+=1 #moving animation frame
                    explosionFrameCount=0 #resetting animation
                else: #animation is not over
                    explosionFrameCount+=1 #moving animation frame
                for pos in explosionPositions: #itterating through explosion position list 
                    screen.blit(explosionPics[explosionFrame],(pos[0],pos[1])) #adding explosion animation at specified pos and frame
                if explosionFrame>=4: #checking if animation is half over
                    portalsExploded=True #setting portal exploded to true
            if X >= 820: #checking if player position is within the range to turn the final boss towards the player
                finalBossMove = 1 #turning final boss towards the player by changing animation move
            if X >= 880: #checking if player is in pos to turn the player towards final boss
                screen.blit(finalSpeechPics[finalDialogueFrame],(0,570)) #adding dialogue
                freezePlayer = True #freezing player
                move=0 #turning player towards the boss by changing move
                if Y < 358: #checking if the player is not on the groud
                    Y+=10 #moving the player to the ground
        
        display.flip() 
        myClock.tick(60)

def door1():
    global player, X, Y, VY, ONGROUND, XCONST, RAPID, offset, lives, gameLives
    X=400
    Y=410
    VY=0
    XCONST=400
    lives=5
    bullets=[]
    speed=10
    
    level1Background = image.load("images/level1Back.png").convert() #loading images
    heartPic=image.load("images/heart.png").convert_alpha()
    platformPic=image.load("images/platform.png")
    playerPic=[addPics("all characters",13,15),
      addPics("all characters",25,27)]
    zombiePic=[addPics("all characters",19,21),
      addPics("all characters",31,33)]
    batPic=[addPics("bats",10,12),
      addPics("bats",4,6)]
    batPoopPic=image.load("images/poop.png")
           
    zombies=[[randint(1900,5000),420,randint(1,3),randint(2,5),-1,-1,-1] for j in range (22)]#[X,Y,HEALTH,SPEED,NEWMOVE,MOVE,FRAME]
    bats=[[randint(1900,5000),randint(316,340),randint(1,2),randint(5,8),-1,-1,-1,True,-500,-500] for j in range (8)]#[X,Y,HEALTH,SPEED,NEWMOVE,MOVE,FRAME,IS POOPING,POOP X COORDINATE, POOP Y COORIDNATE]

    platXvals1 = []#THESE LISTS WILL HOLD THE RANDOM X VALUES OF THE PLATFORMS
    platXvals2 = []
    platXvals3 = []
    for i in range(0,3): #for loop start to add random platform pos to lists
        platXvals1.append(randint(400,1540)) #appending random plat pos to list 
        platXvals2.append(randint(1820,3980))
        platXvals3.append(randint(4260,5200))
    #checking if platforms overlap --> making new platforms
    while (Rect(platXvals1[0],380,95,4)).colliderect(Rect(platXvals1[1],380,95,4)): #while platforms collide
        platXvals1=[] #clearing plat pos list
        for i in range(0,3): #for loop start to add random platform pos to lists
            platXvals1.append(randint(400,1540)) #appending random plat pos to list 
    while (Rect(platXvals2[0],380,95,4)).colliderect(Rect(platXvals2[1],380,95,4)): #repeating same thing for second set of plats
        platXvals2=[]
        for i in range(0,3):
            platXvals2.append(randint(1820,3980))

    running=True
    myClock=time.Clock()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed() #getting key preeses
        if keys[K_ESCAPE]: #checking if escape key has been pressed
            return ("ESCMenu") #returning esc menu

        offset = XCONST - X #getting offset
        playerRect = Rect(X + offset, Y + 8, 30, 58) #player hit box
        plats = [[Rect(offset, 485, 1675, 2), -500, -500], [Rect(offset + 1820, 485, 2310, 2), -100, -100],
                 [Rect(offset + 4275, 485, 10000, 2), -100, -100],  # ground plats
                 [Rect(offset + platXvals1[0], 380, 95, 4), offset + platXvals1[0], 380], #other plats using coordiantes generated above
                 [Rect(offset + platXvals1[1], 380, 95, 4), offset + platXvals1[1], 380],
                 [Rect(offset + platXvals2[0], 380, 95, 4), offset + platXvals2[0], 380],
                 [Rect(offset + platXvals2[1], 380, 95, 4), offset + platXvals2[1], 380],
                 [Rect(offset + platXvals3[0], 380, 95, 4), offset + platXvals3[0], 380]]

        #PLAYER DIED
        if lives<=0: #checking if player died
            return("deadScreen1") #returning dead screen
        #PLAYER BEAT THE LEVEL 
        if X>=4900: #checking if player is at the end of the map
            fade = Surface((1250, 666)) #starting screen fade animation
            fade.fill((255,255,255))
            for alpha in range(0, 300):
                fade.set_alpha(alpha)
                screen.blit(level1Background,(offset,0))
                screen.blit(playerPic[move][int(frame)],(XCONST,Y))
                screen.blit(fade, (0,0))
                display.update()
                time.delay(1)
            mixer.music.load("music/End Of Silence - Blood Moon (feat. Alexa Ray) [Epic Music - Epic Female Vocal - Battle Music].mp3") #loading music
            mixer.music.play(-1) #playing music
            return("level1Complete") #returning level boss fight
        #PLAYER FELL INTO THE PIT
        if Y>=650: #checking if player is beneath ground
            if developerMode==False: #checking if developer mode is disabled
                lives-=1 #reducing lives
            Y=375 #resetting player y coordinate
            if move==1: #checking wither the player was coming from the left or right side of the pit based on move
                X-=300 #resetting player x coordinate
            else:
                X+=300

        movePlayer(playerPic) #calling functions
        checkCollision(plats)
        moveEnemies(zombies,zombiePic)
        moveEnemies(bats,batPic)
        checkMobCollision(zombies,bullets,30,58,False,0,[])
        checkMobCollision(bats,bullets,18,22,False,0,[])

        #DRAW SCENE
        screen.blit(level1Background,(offset,0)) #drawing bg
        displayLives(heartPic) #calling display lives function
        screen.blit(playerPic[move][int(frame)],(XCONST,Y)) #adding player image
        shoot(speed, bullets, plats) #calling shooting function
        for p in plats: #itterating through plat list
            screen.blit(platformPic,(p[1],p[2])) #adding platform pics
        for m in zombies: #itterating through zombie list
            screen.blit(zombiePic[m[5]][int(m[6])],(offset+m[0],m[1])) #adding zombie pics
        for b in bats: #itterating through bat list
            screen.blit(batPic[b[5]][int(b[6])],(offset+b[0],b[1])) #adding bat pics
        #POOP MECHANICS
            if b[0]<=X+5 and b[0]>=X-5 and b[7]==True: #checking if the bat is above the player and that the bat has not already pooped
                b[8]=b[0] #setting the poop coordiantes based on the bats current coordinates
                b[9]=b[1]
                b[7]=False #bat should not poop again
            b[9]+=2.5 #moving poop down
            screen.blit(batPoopPic,(b[8]+offset,b[9])) #adding poop pic
            poopRect=Rect(b[8]+offset,b[9],17,16) #poop hit box
            if b[9]>=480: #checking if the poop hit thr ground
                b[7]=True #pooping is allowed again
            if poopRect.colliderect(playerRect): #checking if poop hit the player
                bats.remove(b) #deleting poop and the bat cuz im too lazy to create seperate list for the poopies
                if developerMode==False: #checking if developer mode is off
                    lives-=1 #reducing lives
        display.flip()  
        myClock.tick(60)

def level1Complete():
    global gameKeys, player, X, Y, VY, ONGROUND, XCONST, RAPID, lives, offset,gameLives
    global bossX, bossY, bossAction, bossRapid, batCounter
    offset=0
    X=400
    Y=410
    VY=0
    XCONST=400
    bullets=[]
    speed=10
    lives=5

    bossX=700 #boss x coordinate
    bossY=900 #boss y coordinate
    bossHandX=0 #boss hand x coordinate
    bossHandX2=-300 #second boss hand x coordiante
    bossHandY=700 #boss hand y coordinate
    bossLives=100 #boss lives
    bossNewMove=-1 #boss animation vals
    bossMove=-1
    bossFrame=-1
    bossAction=1 #boss action keeps track of what phase the boss is in as each phase gets harder

    bossBullets=[] #boss bullet list
    bossBatBullets=[] #boss bat bullet list
    bossRapid=60 #cool down between each of the boss's shots
    enemyBulletSpeed=10 #boss bullet speed
    counter=0 

    startHandCounter=0
    handCounter=0
    handHitCounter=0
    bossHand=False
    getHand=False
    batCounter=0

    bossHorizontalMovement="left" #hor direction
    bossVerticalMovement="up" #vert direction
    keyY=300 #key y coordiante
    direction="down" #key vert direction

    lvl1CompleteBG=image.load("images/level1Back.png").convert() #laoding images
    heartPic=image.load("images/heart.png").convert_alpha()
    keyPic = image.load("images/key.png")
    playerPic=[addPics("all characters",13,15),
      addPics("all characters",25,27)]
    boss1Pic=[addPics("boss",3,4)]
    bossFirePic=image.load("boss/boss007.png")
    bossHandPic=[addPics("boss",1,2)]
    bossBatPic=[addPics("boss",10,11)]
    batBullet1=image.load("boss/boss008.png")#left
    batBullet2=image.load("boss/boss009.png")#right
    
    bossBat=[[randint(0,1250),randint(-10000,-100),randint(2,3),randint(1,2),0,0,0,randint(60,240),randint(30,130)] for j in range (5)]#[X,Y,HEALTH,SPEED,NEWMOVE,MOVE,FRAME,rapid, bat y ending pos]
    plats=[[Rect(0,480,1250,2),-500,-500]]#ground plat
           
    running=True
    myClock=time.Clock()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")

        keyRect = Rect(800, keyY, 75, 75) #key hit box
        playerRect = Rect(X, Y + 8, 30, 58) #player hit box

        if lives<=0: #checking if the player is dead
            return("deadScreen1Complete") #returning dead screen

        if bossMove==bossNewMove: #animation
            bossFrame=bossFrame+0.2
            if bossFrame>=len(boss1Pic[bossMove]): #slowing down animation
                bossFrame=0 #1 is the first frame for the animation (0 is idle)
        elif bossNewMove!=-1:
            bossMove=bossNewMove
            bossFrame=1
        
        for b in bullets: #itterating through bullet list
            bulletRect=Rect(int(b[0]),int(b[1]),7,7) #bullet hit box
            if bulletRect.colliderect(bossRect): #checking if bullet collides with boss
                bossLives-=1 #reducing boss lives
                bullets.remove(b) #removing bullet
###############
        if bossAction==1: #checking boss action
            if bossY>=120: #checking if the boss has yet to come from underground
                bossY-=2 #moving boss up
            if bossLives<=90: #checking if the boss has lost enough health to move to stage 2
                bossAction=2 #moving to stage 2
###############
        if bossAction==2: #checking if its stage 2
            if bossHorizontalMovement=="left": #checking boss direction
                counter+=0.1 #increasing timer
                bossX-=1 #moving boss left
                if counter>=40: #checking if counter is done
                    counter=0 #resetting counter
                    bossHorizontalMovement="Right" #changing direction
            if bossHorizontalMovement=="Right":
                counter+=0.1
                bossX+=1
                if counter>=40:
                    counter=0
                    bossHorizontalMovement="left"
                    
            if bossHand==False: #checking if boss hands are not on screen
                startHandCounter+=0.1 #increasing counter
            if startHandCounter>=20: #checking counter
                bossHandX=randint(0,1150) #generating random hand x coordinate
                bossHand=True #boss hands is now true
                startHandCounter=0 #resetting counter
            if bossHand==True: #checking if boss hands are on 
                handCounter+=0.1 #increasing counter
                if bossHandY>320: #checking if hands are not fully up
                    bossHandY-=3 #moving hands up
                if handCounter>=20: #checking counter
                    if bossHandY<700: #checking if boss hands are not fully down
                        bossHandY+=10 #moving hands down
                    else: #boss hands are back down
                        handCounter=0#resetting counter
                        bossHand=False #boss hands false
            bossHandRect=Rect(bossHandX,bossHandY,97,357) #boss hand hit box
            if bossHandRect.colliderect(playerRect) and handHitCounter==0: #checking if boss hands collide with player and the hit cooldown is over
                if developerMode==False: #checking developer mode
                    lives-=1 #reducing lives
                handHitCounter=100 #resetting cool down
            if handHitCounter>0: #checking if cooldown started
                handHitCounter-=1 #reducing cooldown
            if bossLives<=70: #checking boss health
                bossAction=3 #moving to stage 3
###############
        if bossAction==3: #checking if its stage 3
            moveEnemies(bossBat,bossBatPic) #calling functions
            enemyShoot(enemyBulletSpeed,bossBatBullets,bossBat,False)
            checkMobCollision(bossBat,bullets,47,73,False,0,[])
            counter+=0.1 #increasing counter

            if bossVerticalMovement=="up" and bossY>0: #checking boss direction and making sure the boss is not at the edge of screen
                bossY-=1 #moving boss 
            elif bossVerticalMovement=="down" and bossY+200<480: 
                bossY+=1
            if bossHorizontalMovement=="right" and bossX+180<1250:
                bossX+=1
            elif bossHorizontalMovement=="left" and bossX>0:
                bossX-=1
            if bossY==0:
                bossVerticalMovement="down"
            if bossY+200==480:
                bossVerticalMovement="up"
            if bossX+180==1250:
                bossHorizontalMovement="left"
            if bossX==0:
                bossHorizontalMovement="right"  
            if counter>=20: #checking counter
                vertRand=randint(0,1) #this code is bad lmfao0ooooo0o000o0o00
                horRand=randint(0,1)
                if vertRand==0:
                    bossVerticalMovement="down"
                if vertRand==1:
                    bossVerticalMovement="up"
                if horRand==0:        
                    bossHorizontalMovement="right"
                if horRand==1:                   
                    bossHorizontalMovement="left"
                counter=0
            if bossHand==False: #same as stage 1 boss hands 
                startHandCounter+=0.1 
            if startHandCounter>=20: 
                bossHandX=randint(0,1150) 
                bossHandX2=randint(0,1150) 
                bossHand=True 
                startHandCounter=0
            if bossHand==True:
                handCounter+=0.1
                if bossHandY>320:
                    bossHandY-=3
                if handCounter>=20:
                    if bossHandY<700:
                        bossHandY+=10
                    else:
                        handCounter=0
                        bossHand=False
            bossHandRect=Rect(bossHandX,bossHandY,97,357)
            bossHandRect2=Rect(bossHandX2,bossHandY,97,357)
            if (bossHandRect.colliderect(playerRect) or bossHandRect2.colliderect(playerRect)) and handHitCounter==0:
                if developerMode==False:
                    lives-=1
                handHitCounter=100
            if handHitCounter>0:
                handHitCounter-=1
            if bossLives<=0:
                bossAction=4
###############
        movePlayer(playerPic) #calling functions
        checkCollision(plats)
        #DRAW SCENE
        screen.blit(lvl1CompleteBG,(-4500,0)) #adding bg
        displayLives(heartPic) #display lives function
        screen.blit(playerPic[move][int(frame)], (X, Y)) #adding player pic
        shoot(speed,bullets,plats) #shoot function
        #BOSS HEALTH BAR
        if bossLives>0: #checking if boss is alive
            bossHealthRect = Rect(30, 15, bossLives * 5, 15) #boss health bar
            draw.rect(screen,(255,100,100),(30,15,500,15))
            draw.rect(screen,(100,255,100),bossHealthRect)
        #BOSS IS DEAD
        if bossAction==4: #checkink if boss is dead
            bossRect=Rect(-2000,-2000,184,216) #boss hit box
            if (1) in gameKeys: #checking if level has not been beaten yet
                if direction=="down": #moving key
                    keyY+=0.5
                    if keyY>=330:
                        direction="up"
                elif direction=="up":
                    keyY-=0.5
                    if keyY<=300:
                        direction="down"
                screen.blit(keyPic,(800,keyY))
                if playerRect.colliderect(keyRect): #checking if player collides with key
                    gameKeys.remove(1) #remvoving key from list
                    return("lobby") #returning lobby
        #BOSS IS ALIVE
        elif bossAction!=4: #checking if boss is alives
            bossRect=Rect(bossX,bossY,184,216) #boss hit box
            enemyShoot(enemyBulletSpeed, bossBullets, None, True) #boss shoot function
            screen.blit(boss1Pic[bossMove][int(bossFrame)],(bossX,bossY)) #adding boss pic
            for l in bossBullets: #itterating through boss bullets         
                screen.blit(bossFirePic,(int(l[0]),int(l[1]))) #adding bullets to screen
            for l in bossBatBullets: #itterating through bat bullets
                if l[0]>=X: #checking bullet direction
                    screen.blit(batBullet1,(int(l[0]),int(l[1]))) #adding appropriate bullet image
                elif l[0]<X:
                    screen.blit(batBullet2,(int(l[0]),int(l[1])))
            if bossAction==2 and bossHand: #checking boss action and if boss hands are on
                screen.blit(bossHandPic[bossMove][int(bossFrame)],(bossHandX,bossHandY)) #adding hand pics
            if bossAction==3 and bossHand:
                screen.blit(bossHandPic[bossMove][int(bossFrame)],(bossHandX,bossHandY))
                screen.blit(bossHandPic[bossMove][int(bossFrame)],(bossHandX2,bossHandY))
            if bossAction==3: #checking boss action
                for b in bossBat: #itterating through bats list
                    screen.blit(bossBatPic[bossMove][int(bossFrame)],(b[0],b[1])) #adding bat images
                    if b[1]<b[8]: #checking if bats have not come down yet
                        b[1]+=5   #movinf bats down
        
        display.flip()  
        myClock.tick(60)

def door2():
    global player, X, Y, VY, ONGROUND, XCONST, RAPID, offset, lives, gameLives
    X=400
    Y=300
    VY=0
    XCONST=400
    lives=5
    bullets=[]
    enemyBullets=[]
    speed=10#bullet speed
    enemyBulletSpeed=10 #enemy bullet speed
    isBoostOn=False #if speed boost is on
    boostTime=0 #timer till boost turns off
    boost=[] #boost list
    asteroidTimer = 0 #timer

    level2Background = image.load("images/level2Background.png").convert() #loading images
    heartPic=image.load("images/heart.png").convert_alpha()
    boostPic=image.load("images/boost.png")
    playerPic=[[image.load("spaceship/spaceship001.png")],[image.load("spaceship/spaceship002.png")],[image.load("spaceship/spaceship003.png")]]
    asteroidPic=image.load("images/asteroid.png").convert_alpha()
    enemyspaceshipPic=image.load("images/enemyspaceship.png")
    megashooterPic=image.load("images/megashooter.png")
    
    enemyspaceship=[[randint(1000,15360),randint(0,660),randint(1,3),randint(2,4),-1,-1,-1] for j in range (75)]#[X,Y,HEALTH,SPEED,-1,-1,-1]
    megashooter=[[randint(5000,15360),randint(0,660),2,randint(3,5),-1,-1,-1,60] for j in range (50)]#[X,Y,HEALTH,SPEED,-1,-1,-1,rapid]
    usedAsteroids = [] #active asteroids
    running=True
    myClock=time.Clock()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")

        offset = XCONST - X #offset
        if move == 0: #checking the players direction and changing hit box size
            playerRect = Rect(XCONST, Y, 73, 33)
        elif move == 1:
            playerRect = Rect(XCONST, Y, 63, 44)
        elif move == 2:
            playerRect = Rect(XCONST, Y, 63, 44)

        #PLAYER DIED
        if lives<=0: 
            return("deadScreen2")
        #PLAYER BEAT THE LEVEL 
        if X>=14500:
            fade = Surface((1250, 720))
            fade.fill((255,255,255))
            for alpha in range(0, 300):
                fade.set_alpha(alpha)
                screen.blit(level2Background,(offset,0))
                screen.blit(playerPic[0][0],(XCONST,Y))
                screen.blit(fade, (0,0))
                display.update()
                time.delay(1)
            return("level2Complete")
        # SPEED BOOST TIMER
        if isBoostOn: #checking if boost is on
            lives = keepLives #not allowing player to take damage
            boostTime += 0.1 #increasing timer
            if boostTime <= 4: #checking if boost is on
                X += 40 - (boostTime * 5) #moving player based on how long the boost has been on
            elif boostTime <=5.5: #checking if the boost is over --> not boosting the player but also preventing player from taking damage for a small period of time after
                pass 
            else: #boos is over
                isBoostOn = False #turning boost off
                boostTime = 0 #resetting boost timer
            
        movePlayer(playerPic) #calling functions
        moveEnemies(enemyspaceship,enemyspaceshipPic)
        moveEnemies(megashooter,megashooterPic)
        checkMobCollision(enemyspaceship,bullets,60,56,False,0,[])
        checkMobCollision(megashooter,bullets,47,60,True,randint(1,10),boost)
            
        #DRAW SCENE
        screen.blit(level2Background,(offset,0))
        displayLives(heartPic)
        screen.blit(playerPic[move][0],(XCONST,Y))
        shoot(speed,bullets,[])
        enemyShoot(enemyBulletSpeed,enemyBullets,megashooter,False)
        #SPWANING BOOSTS
        for b in boost: #itterating through boost list
            if b[2]=="speed": #checking if its a speed boost
                screen.blit(boostPic,(b[0]+offset,b[1])) #adding boost image
                boostRect=Rect(b[0]+offset,b[1],52,50) #boost hit box
                if playerRect.colliderect(boostRect): #checking if player got boost
                    boost.remove(b) #removing boost
                    isBoostOn=True #boss is on
                    keepLives=lives #temporary lives to prevent player from taking damage
            elif b[2]=="extraLife": #checking if its an extra life boost
                screen.blit(heartPic,(b[0]+offset,b[1])) #adding pic
                extraLifeRect=Rect(b[0]+offset,b[1],50,47) #hit box
                if playerRect.colliderect(extraLifeRect): #checking if player got the life
                    boost.remove(b) #removing boost
                    lives+=1 #increasing lives
        for e in enemyspaceship: #itterating through mobs and adding images
            screen.blit(enemyspaceshipPic,(e[0]+offset,e[1]))
        for m in megashooter:
            screen.blit(megashooterPic,(m[0]+offset,m[1]))

        asteroidTimer += 1 #increasing timer
        if asteroidTimer >= 30: #checking timer
            try: 
                usedAsteroids.append([randint(X-400,X+1000),(-40),randint(-10,10)]) #adding asteroid to active asteroid list
            except:
                pass
            asteroidTimer = 0 #resetting timer
        for a in usedAsteroids: #itterating through active asteroids
            a[0]+=a[2] #moving asteroids
            a[1]+=abs(a[2])
            screen.blit(asteroidPic,(a[0]+offset,a[1])) #adding pic
            asteroidRect=Rect(a[0]+offset, a[1],30,23) #hit box
            if playerRect.colliderect(asteroidRect): #checking collision
                if developerMode==False: 
                    lives-=1 #decreasing lives
                try:
                    usedAsteroids.remove(a) #removing asteroid
                except:
                    pass
            if a[1]>720: #checking if asteroid is off screen
                try:
                    usedAsteroids.remove(a)#removing asteroid
                except:
                    pass
            for b in bullets: #itterating through bullets
                bulletRect=Rect(int(b[0]),int(b[1]),7,7) #bullet rect
                if asteroidRect.colliderect(bulletRect): #checking ig player shot asteroid
                    bullets.remove(b) #removing bullet
                    try:
                        usedAsteroids.remove(a) #removing asteroid
                    except:
                        pass

        display.flip()
        myClock.tick(60)

def level2Complete():
    global gameKeys, player, X, Y, VY, ONGROUND, XCONST, RAPID, gameLives
    X=400
    Y=410
    VY=0
    XCONST=400
    keyY=250
    direction="down"
    
    lvl2CompleteBG=image.load("images/level2Background.png").convert() #loading images
    keyPic = image.load("images/key.png")
    playerPic=[[image.load("spaceship/spaceship001.png")],[image.load("spaceship/spaceship002.png")],[image.load("spaceship/spaceship003.png")]]
                   
    running=True
    myClock=time.Clock()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")
            
        keyRect=Rect(800,keyY,75,75) #key hit box
        playerRect=Rect(X,Y,63,44) #player hit box
         
        movePlayer(playerPic) #move player function
        screen.blit(lvl2CompleteBG,(-14100,0)) #adding bg
        screen.blit(playerPic[move][0],(X,Y)) #adding player pic
        if (2) in gameKeys: #moving key
            if direction=="down":
                keyY+=0.5
                if keyY>=270:
                    direction="up"
            elif direction=="up":
                keyY-=0.5
                if keyY<=250:
                    direction="down"
            screen.blit(keyPic,(800,keyY))
            if playerRect.colliderect(keyRect):
                gameKeys.remove(2)
                return("lobby")
        
        display.flip()  
        myClock.tick(60)

def door3():
    global gameLives, lives, X, Y, VY, ONGROUND, XCONST, RAPID, hitFrames, offset, thunderPositions
    X=400
    Y=300
    VY=0
    XCONST=400
    lives=5
    bullets=[]
    speed=10#bullet speed
    hitFrames=50
    leverFlipped=False

    sawPositions=[2450,2950,1100,1900,4050,5100]#starting positions of saws
    sawDirections=[True,False,True,False,True,False]#true is moving right, false is left
    sawFrameCount=0
    laserPositions=[[3594,67],[4375,361],[4423,361],[4709,361],[4756,361],[5018,361],[5066,361]]#where the stationary lasers are
    laserFrameCount=0#all frameCount variables from here on is the timer that triggers every 3 instances or so to increase
    #the current frame of an animation
    currentLaserFrame=0#the current frame of an animation
    laserTimer=0#the timer for the timed lasers at the end of the level
 
    thunderFrame=0
    thunderFrameCount=0
    thunderPositions=[]#positions will be added and removed from this list
    thunderSecondCount=0
    activeThunder=False#to control when a lightning strike is being added

    portalFrame=0
    portalFrameCount=0

    #most animations use the same set of similar variables (current frame, frameCount, etc), so refer
    #to the laser variables for their use
    
    heartPic=image.load("images/heart.png").convert_alpha()
    level3Background=image.load("images/level3Background.png").convert()
    level3Background=transform.smoothscale(level3Background,(7348,720))
    playerPic=[addPics("all characters",13,15),
      addPics("all characters",25,27)]
    sawPics=[image.load("saw/sawPic.png"),image.load("saw/sawPic2.png")]
    sawPics[0]=transform.smoothscale(sawPics[0],(120,55))
    sawPics[1]=transform.smoothscale(sawPics[1],(120,55))
    ePic=image.load("images/E.png")
    ePic=transform.scale(ePic,(24,24))
    leverPics=[image.load("lever/lever1.png"),image.load("lever/lever2.png")]
    leverPics[0]=transform.smoothscale(leverPics[0],(80,80))
    leverPics[1]=transform.smoothscale(leverPics[1],(80,80))
    thunderPics=addPics("thunder",1,17)
    laserPics=[addPics("laser",0,11) for i in range(4)]
    portalPics=addPics("portals",7,9)

    #rescale some small stuff to fit appropriately
    for pic in portalPics:
        portalPics[portalPics.index(pic)]=transform.smoothscale(portalPics[portalPics.index(pic)],(125,125))
    for pic in thunderPics:
        thunderPics[thunderPics.index(pic)]=transform.smoothscale(thunderPics[thunderPics.index(pic)],(120,655))
    for pic in thunderPics[:10]:
        thunderPics[thunderPics.index(pic)]=transform.flip(thunderPics[thunderPics.index(pic)],False,True)
    for pics in laserPics:
        for pic in pics:
            laserPics[laserPics.index(pics)][pics.index(pic)] = transform.rotate(pic, 90)
    pics = laserPics[0]
    for pic in pics:
        laserPics[laserPics.index(pics)][pics.index(pic)] = transform.smoothscale(pic, (40, 210))
    pics = laserPics[1]
    for pic in pics:
        laserPics[laserPics.index(pics)][pics.index(pic)] = transform.smoothscale(pic, (40, 275))
    
    running=True
    myClock=time.Clock()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")
        
        if lives<=0:#if dead
            return("deadScreen3")

        offset = XCONST - X
        plats = [[Rect(offset, 600, 5511, 10)], [Rect(offset, 375, 775, 7)], [Rect(offset + 780, 375, 10, 250)],
                 [Rect(offset + 2375, 415, 15, 250)], [Rect(offset + 2375, 415, 605, 10)],
                 [Rect(offset + 2980, 240, 10, 179)], [Rect(offset + 2980, 240, 430, 20)],
                 [Rect(offset + 3113, 490, 195, 15)], [Rect(offset + 3108, 490, 15, 150)],
                 [Rect(offset + 3295, 490, 17, 150)], [Rect(offset + 3385, 378, 12, 250)],
                 [Rect(offset + 3385, 378, 195, 10)], [Rect(offset + 3580, 255, 7, 125)],
                 [Rect(offset + 3580, 255, 90, 7)], [Rect(offset + 3510, 28, 155, 7)],
                 [Rect(offset + 3510, 2, 7, 25)], [Rect(offset + 3660, 2, 5, 25)], [Rect(offset + 3670, 255, 7, 120)],
                 [Rect(offset + 3675, 356, 245, 7)],
                 [Rect(offset + 3920, 356, 7, 250)], [Rect(offset + 4025, 0, 20, 200)],
                 [Rect(offset + 4025, 30, 205, 12)], [Rect(offset + 4225, 0, 7, 30)],
                 [Rect(offset + 4025, 196, 205, 7)], [Rect(offset + 4350, 300, 130, 12)],
                 [Rect(offset + 4685, 300, 130, 12)], [Rect(offset + 4993, 300, 130, 12)],
                 [Rect(offset + 5290, 435, 7, 180)], [Rect(offset + 5290, 435, 130, 7)], [Rect(offset, -5, 5511, 7)],
                 [Rect(offset + 4015, 450, 7, 180)],[Rect(offset + 3925, 448, 90, 7)]]
        #all the floors, walls, and ceilings of the level

        sawFrameCount += 1
        if hitFrames < 50:#this is so you can only get hit by a saw every 5/6 of a second
            hitFrames += 1
        if laserTimer >= 120:#switch which lasers are active
            laserTimer = 0
        else:
            laserTimer += 1

        movePlayer(playerPic)
        checkCollision(plats)

        #DRAW SCENE
        screen.blit(level3Background,(offset,0))
        displayLives(heartPic)
        checkObjectCollision(sawPositions, laserPositions, laserTimer, leverFlipped, thunderFrame)

        for ind in range(6):#every saw position
            if ind<2:
                if sawDirections[ind]==True:#if the saw is moving right
                    sawPositions[ind]+=3#move it to the right
                    if sawPositions[ind]>=2950:#if they go too far
                        sawDirections[ind]=False#make it start to go left
                elif sawDirections[ind]==False:#if moving left
                    sawPositions[ind]-=3#move left
                    if sawPositions[ind]<=2450:#if it goes too far left
                        sawDirections[ind]=True#make it go right
            elif ind<4:# 3 ifs here for the 3 sets of saws that each have their own
                #movement boundaries
                if sawDirections[ind]==True:
                    sawPositions[ind]+=3
                    if sawPositions[ind]>=1900:
                        sawDirections[ind]=False
                elif sawDirections[ind]==False:
                    sawPositions[ind]-=3
                    if sawPositions[ind]<=1100:
                        sawDirections[ind]=True
            else:
                if sawDirections[ind]==True:
                    sawPositions[ind]+=3
                    if sawPositions[ind]>=5100:
                        sawDirections[ind]=False
                elif sawDirections[ind]==False:
                    sawPositions[ind]-=3
                    if sawPositions[ind]<=4050:
                        sawDirections[ind]=True
            if sawFrameCount<=2:
                screen.blit(sawPics[0],(offset+sawPositions[ind],550))
            else:#swap between the 2 frames of the saw
               screen.blit(sawPics[1],(offset+sawPositions[ind],550))
            if sawFrameCount==4:
                sawFrameCount=0

        if leverFlipped==False:
            screen.blit(leverPics[0],(offset+2430,540))
            screen.blit(laserPics[0][currentLaserFrame],(offset+laserPositions[0][0],laserPositions[0][1]))
            #only show the laser if the switch is off
        else:
            screen.blit(leverPics[1],(offset+2430,540))

        screen.blit(portalPics[portalFrame],(offset+4055,65))
        screen.blit(playerPic[move][int(frame)], (XCONST, Y))
        
        keys=key.get_pressed()
        if 2420<=X<=2505 and Y>460 and ONGROUND:# if the player is standing next to the lever
            if keys[K_e]:#if the player interacts
                leverFlipped=True#flip the lever
            if leverFlipped==False:
                screen.blit(ePic,(offset+2455,495))
        if 4050<X<4150 and 65<Y<200:#if the player is next to the portal
            screen.blit(ePic,(offset+4100,40))
            if keys[K_e]:
                fade = Surface((1250, 720))#fade to the next level
                #slowly increase the alpha (decrease the transparancy) of the white to give
                #a  fading effect
                fade.fill((255,255,255))
                for alpha in range(0, 300):
                    fade.set_alpha(alpha)
                    screen.blit(level3Background,(offset,0))
                    screen.blit(fade, (0,0))
                    display.update()
                    time.delay(1)
                mixer.music.load("music/steampunkBoss.mp3")
                mixer.music.play(-1)
                return("level3Complete")
                
        if laserTimer<60:#when to show which of the timed lasers
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[1][0],laserPositions[1][1]))
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[2][0],laserPositions[2][1]))
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[5][0],laserPositions[5][1]))
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[6][0],laserPositions[6][1]))
        else:
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[3][0],laserPositions[3][1]))
            screen.blit(laserPics[1][currentLaserFrame],(offset+laserPositions[4][0],laserPositions[4][1]))


        #progressing a bunch of timers
        if laserFrameCount>=3:
            currentLaserFrame+=1
            laserFrameCount=0
        else:
            laserFrameCount+=1
        if currentLaserFrame>=12:
            currentLaserFrame=0

        if portalFrameCount>=3:
            portalFrameCount=0
            portalFrame+=1
        else:
            portalFrameCount+=1
        if portalFrame>=3:
            portalFrame=0

        if activeThunder==True:# if a lightning is on the screen, do the timer stuff
            if thunderFrameCount>=5:
                thunderFrame+=1
                thunderFrameCount=0
            else:
                thunderFrameCount+=1
            if thunderFrame>=16:#if the lightning is done
                thunderFrame=0
                activeThunder=False
                thunderPositions=[]#remove that position from the list

        if thunderSecondCount>=120:#add a lightning every 2 seconds
            thunderSecondCount=0
            xPosition=randint(X-300,X+500)#random position near the player
            thunderPositions.append(xPosition)#add the position
            activeThunder=True
        else:
            thunderSecondCount+=1

        for thunderPos in thunderPositions:#blit a lightning at every position in the list
            screen.blit(thunderPics[thunderFrame],(offset+thunderPos,-40))
               
        display.flip()
        myClock.tick(60)

def level3Complete():
    global gameKeys, gameLives, player, X, Y, VY, ONGROUND, XCONST, lives, energySpeeds, energyFrameCounts, energyFrames
    offset=0
    X=400
    Y=410
    VY=0
    XCONST=400
    lives=5

    currentBossFrame=0#just used to make the boss float a bit
    bossFrameCount=0
    bossAlive=True
    bossHealth=100

    keyY=375#pos of key
    direction="down"

    objectTimers=[240,240,240,240,240]#all objects start ready to be interacted with
    objectCurrentFrames=[0,0,0,0,0]#each object needs its own frame and frame timer
    objectFrameCounts=[0,0,0,0,0]
    #             T1, T2, L1, L2, L3

    leverPositions=[[-10,220],[490,67],[969,210]]

    thunderFrame=0
    thunderFrameCount=0
    thunderPositions=[]#same deal as the lightning in the previous function
    thunderSecondCount=0
    activeThunder=False

    hitFrames=50#like the saws in the last function; used so the energy balls
    #can only hit you every 5/6 of a second

    cannonLaser=False
    cannonLaserFrame=0
    cannonLaserCount=0
    cannonCount=0#lets the animation play twice before finishing

    leftTurret=False
    rightTurret=False
    explodedTurret=False#will get rid of the right turret eventually
    explodedTurretDelay=0#waits a second after getting to half health to destroy the turret

    fireballFrames=[0,0]
    fireballFrameCounts=[0,0]
    fireballCounts=[0,0]#lets the animations play a few times before stopping
    fireballPositions=[[150,315],[787,315]]#starting positions

    explosionFrame=0
    explosionFrameCount=0
    leftExplosion=False
    rightExplosion=False
    turretExplosion=False

    energyFrames=[]#all these have to be empty lists because multiple energy balls will exist at once
    energyFrameCounts=[]
    energyPositions=[]
    energyTimer=0
    energySpeeds=[]#directions and speeds will change based on orientation of player from arm cannon

    bossFireBallTimer=0#how often it will shoot a fireball
    bossFireBallY=200
    bossFireBallVY=-6 #fireball speed
    bossFireBallX=390

    bossFireBall2X = 600
    doubleFireBall = False#ebentually starts to shoot two fireballs at once

    background=image.load("images/industrialEnd2.png").convert()
    background=transform.smoothscale(background,(999,720))
    heartPic=image.load("images/heart.png").convert_alpha()
    keyPic = image.load("images/key.png")
    playerPic=[addPics("all characters",13,15),
      addPics("all characters",25,27)]
    cannonPic=image.load("laser/cannon.png")
    cannonPic=transform.smoothscale(cannonPic,(150,75))
    cannonPic=transform.rotate(cannonPic,90)
    bossFireBallPic=image.load('images/bossFireBall.png')
    explosionPics=addPics("explosion",1,5)
    #rescale some stuff to fit the game better
    for pic in explosionPics:
        explosionPics[explosionPics.index(pic)]=transform.scale(pic,(60,60))
    laserPics=addPics("laser",0,11)
    for pic in laserPics:
        laserPics[laserPics.index(pic)] = transform.rotate(pic, 90)
    for pic in laserPics:
        laserPics[laserPics.index(pic)]=transform.smoothscale(pic,(30,200))
    fireballPics=[addPics("fireball",1,4) for i in range(2)]
    for pics in fireballPics:
        for pic in pics:
            fireballPics[fireballPics.index(pics)][pics.index(pic)]=transform.scale(pic,(50,30))
    for pics in fireballPics:
        for pic in pics:
            fireballPics[fireballPics.index(pics)][pics.index(pic)]=transform.rotate(pic,30)
    pics=fireballPics[1]
    for pic in pics:
        pics[pics.index(pic)]=transform.flip(pic,True,False)
    energyPics=addPics("energy",1,8)
    for pic in energyPics:
        energyPics[energyPics.index(pic)]=transform.smoothscale(pic,(50,55))
    
    ############### loading pics here that would normally be already loaded in door3 ish
    ePic=image.load("images/E.png")
    ePic=transform.scale(ePic,(24,24))

    leverPics=[[image.load("lever/lever1.png"),image.load("lever/lever2.png")] for i in range(3)]
    for pics in leverPics:
        for pic in pics:
            leverPics[leverPics.index(pics)][pics.index(pic)]=transform.scale(pic,(40,40))
    leverPics[0][0]=transform.rotate(leverPics[0][0],270)
    leverPics[0][1]=transform.rotate(leverPics[0][1],270)
    leverPics[2][0]=transform.rotate(leverPics[2][0],90)
    leverPics[2][1]=transform.rotate(leverPics[2][1],90)
    #rotating every lever pic to where it should be

    thunderPics=addPics("thunder",1,17)
    for pic in thunderPics:
        thunderPics[thunderPics.index(pic)]=transform.smoothscale(thunderPics[thunderPics.index(pic)],(120,680))
    for pic in thunderPics[:10]:
        thunderPics[thunderPics.index(pic)]=transform.flip(thunderPics[thunderPics.index(pic)],False,True)
    ############

    roboBossFrames=addPics("roboBoss",1,19)
    for pic in roboBossFrames:
        roboBossFrames[roboBossFrames.index(pic)]=transform.smoothscale(roboBossFrames[roboBossFrames.index(pic)],(500,400))

    turretFrames=[addPics("turret",1,18) for i in range(2)]
    for pics in turretFrames:
        for pic in pics:
            turretFrames[turretFrames.index(pics)][pics.index(pic)]=transform.smoothscale(turretFrames[turretFrames.index(pics)][pics.index(pic)],(100,100))
    pics=turretFrames[1]
    for pic in pics:
        pics[pics.index(pic)]=transform.flip(pics[pics.index(pic)],True,False)

    plats=[[Rect(0, 600, 1000, 10)],[Rect(0, 420, 180, 180)],
           [Rect(817, 420, 180, 180)],[Rect(999, 0, 30, 600)],
           [Rect(-10,0, 10, 600)],[Rect(0, 290, 70, 17)],
           [Rect(929, 281, 100, 17)],[Rect(110, 165, 130, 18)],[Rect(740, 170, 135, 18)],
           [Rect(350, 95, 335, 18)]]
    #the walls, ceilings, and floors of the level
           
    running=True
    myClock=time.Clock()
    while running:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type==QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")

        playerRect = Rect(X, Y + 8, 30, 58)
        keyRect = Rect(450, keyY, 75, 75)

        if lives<=0:
            return("deadScreen3Complete")

        movePlayer(playerPic)
        if X>966:#set a movement boundary for the player
            X=966
        checkCollision(plats)
        
        #DRAW SCENE
        screen.blit(background,(0,0))
        displayLives(heartPic)
        checkBoss3Collision(energyPositions,thunderFrame,thunderPositions, hitFrames)

        if bossAlive==True:
            screen.blit(roboBossFrames[currentBossFrame],(250,150))

        keys=key.get_pressed()
        ############# displaying E
        if bossAlive:#only use mechanics if boss is alive
            if 60<X<140 and Y>350 and objectTimers[0]==240:#if by the left turret
                screen.blit(ePic,(80,335))
                if keys[K_e]:#use the left turret
                    objectTimers[0]=0#reset the cooldown on the turret so it cant be used again for a while
                    leftTurret=True#left turret is firing
            elif 830<X<910 and Y>350 and objectTimers[1]==240 and explodedTurret==False:
                screen.blit(ePic,(890,335))
                if keys[K_e]:
                    objectTimers[1]=0
                    rightTurret=True
            elif 0<=X<25 and 220<Y<240 and objectTimers[2]==240:#if by the left lever
                screen.blit(ePic,(15,185))#blit the e key above the player's head to let them know how to interact
                if keys[K_e]:#flip the lever
                    objectTimers[2]=0#start the cooldown that will reset the lever to off after a couple seconds
            elif 945<X<999 and 210<Y<230 and objectTimers[4]==240:
                screen.blit(ePic,(960,175))
                if keys[K_e]:
                    objectTimers[4]=0
            elif 470<X<520 and 30<Y<40 and objectTimers[3]==240:
                screen.blit(ePic,(500,30))
                if keys[K_e]:
                    objectTimers[3]=0
            
        ############
        screen.blit(turretFrames[0][objectCurrentFrames[0]],(75,330))
        if explodedTurret==False:#only show right turret if it hasnt exploded
            screen.blit(turretFrames[1][objectCurrentFrames[1]],(820,330))
        screen.blit(cannonPic,(460,480))
        if leftTurret:#show fireballs if a turret is active
            screen.blit(fireballPics[0][fireballFrames[0]],(fireballPositions[0]))
        if rightTurret:
            screen.blit(fireballPics[1][fireballFrames[1]],(fireballPositions[1]))

        screen.blit(playerPic[move][int(frame)], (X, Y))
        if hitFrames<50:
            hitFrames+=1

        if bossFrameCount>=3:
            bossFrameCount=0
            currentBossFrame+=1
        else:
            bossFrameCount+=1
        if currentBossFrame>=18:
            currentBossFrame=0

        for i in range(5):#progress the timers for all of the interactive objects
            if objectTimers[i]<240:
                objectTimers[i]+=1
                if objectFrameCounts[i]>=3:
                    objectFrameCounts[i]=0
                    if i<3:
                        if objectCurrentFrames[i]<17:
                            objectCurrentFrames[i]+=1
                else:
                    objectFrameCounts[i]+=1
            else:
                objectCurrentFrames[i]=0

        ######## BOSS FIRE BALLS THAT SHOOT FROM HIS HEAD
        if bossFireBallTimer<=30:
            bossFireBallTimer+=0.1

        if bossFireBallTimer>=30 and bossAlive==True:#shoot a fireball
            bossFireBallY+=bossFireBallVY#move the fireball into the air
            screen.blit(bossFireBallPic,(bossFireBallX, bossFireBallY))
            bossFireBallRect=Rect(bossFireBallX,bossFireBallY,35,35)#use this to check for collision
            if doubleFireBall==True:#add another fireball if it is shooting 2
                screen.blit(bossFireBallPic, (bossFireBall2X, bossFireBallY))
                bossFireBallRect2 = Rect(bossFireBall2X, bossFireBallY, 35, 35)
            else:
                bossFireBallRect2=Rect(-100,-100,1,1)#just add one

            if bossFireBallY<-150:
                bossFireBallX+=randint(-250,250)#move to the left or right a bit
                bossFireBall2X+=randint(-250,250)
                bossFireBallVY=10
            if bossFireBallY>=600 or bossFireBallRect.colliderect(playerRect) or bossFireBallRect2.colliderect(playerRect):
                #if it hits the player or goes out of the screen
                bossFireBall2X=600#reset the positions and remove the fireball
                bossFireBallX=390
                bossFireBallY=200
                bossFireBallTimer=0
                bossFireBallVY =-6

            if bossFireBallRect.colliderect(playerRect) or bossFireBallRect2.colliderect(playerRect):#take a damage if hit
                if developerMode==False:
                    lives-=1
        ########

        #health bar
        if bossHealth>0:#green bar gets shorter as boss takes damage
            bossHealthRect = Rect(30, 20, bossHealth * 5, 15)
            draw.rect(screen,(255,100,100),(30,20,500,15))
            draw.rect(screen,(100,255,100),bossHealthRect)

        for leverPos in leverPositions:
            if objectTimers[leverPositions.index(leverPos)+2]<240:#if the lever has been flipped
                if leverPositions.index(leverPos)<2:#the first frame for one lever looks like the second frame for another
                    #because theyre flipped
                    screen.blit(leverPics[leverPositions.index(leverPos)][0],leverPos)
                else:
                    screen.blit(leverPics[leverPositions.index(leverPos)][1],leverPos)
                draw.circle(screen,(0,255,0),(leverPos[0]+20,leverPos[1]-7),5)#green circle to show its on
            else:
                if leverPositions.index(leverPos)<2:
                    screen.blit(leverPics[leverPositions.index(leverPos)][1],leverPos)
                else:
                    screen.blit(leverPics[leverPositions.index(leverPos)][0],leverPos)
                draw.circle(screen,(255,0,0),(leverPos[0]+20,leverPos[1]-7),5)#red circle to show its off

        if objectTimers[2]<240 and objectTimers[3]<240 and objectTimers[4]<240 and bossAlive:#if all levers are flipped
            objectTimers[2]=objectTimers[3]=objectTimers[4]=240#turn the levers off
            cannonLaser=True#the middle laser fires

        if cannonLaser:
            if cannonLaserCount>=3:#do the frame timer stuff if the cannon is active
                cannonLaserCount=0
                cannonLaserFrame+=1
                bossHealth-=0.36#slowly bring the boss' health down a bit for each frame to make it look constant
            else:
                cannonLaserCount+=1
            if cannonLaserFrame>=11:
                cannonCount+=1
                cannonLaserFrame=0
            if cannonCount==2:
                cannonCount=0
                cannonLaser=False
            screen.blit(laserPics[cannonLaserFrame],(483,315))

        if leftTurret:#if left turret is firing
            fireballPositions[0][0]+=4#move the fireball toward the boss
            fireballPositions[0][1]-=1
            if fireballFrameCounts[0]>=3:
                fireballFrames[0]+=1
                fireballFrameCounts[0]=0
            else:
                fireballFrameCounts[0]+=1
            if fireballFrames[0]==3:#reset animation
                fireballFrames[0]=0
                if fireballCounts[0]<=3:
                    fireballCounts[0]+=1
                else:#if the animation has played 3 times
                    leftTurret=False#get rid of the fireball and reset positions
                    leftExplosion=True
                    fireballCounts[0]=0
                    fireballPositions[0]=[150,315]
                    bossHealth-=4

        if rightTurret:
            fireballPositions[1][0]-=4
            fireballPositions[1][1]-=1
            if fireballFrameCounts[1]>=3:
                fireballFrames[1]+=1
                fireballFrameCounts[1]=0
            else:
                fireballFrameCounts[1]+=1
            if fireballFrames[1]==3:
                fireballFrames[1]=0
                if fireballCounts[1]<=3:
                    fireballCounts[1]+=1
                else:
                    rightTurret=False
                    rightExplosion=True
                    fireballCounts[1]=0
                    fireballPositions[1]=[787,315]
                    bossHealth-=4

        if leftExplosion or rightExplosion or turretExplosion:#if an explosion is active
            if leftExplosion:#display the explosion at the right spot
                screen.blit(explosionPics[explosionFrame],(380,250))
            elif rightExplosion:
                screen.blit(explosionPics[explosionFrame],(525,250))
            else:
                screen.blit(explosionPics[explosionFrame],(845,355))
            if explosionFrameCount>=9:#do the frame timers for the explosion
                explosionFrame+=1
                explosionFrameCount=0
            else:
                explosionFrameCount+=1
            if explosionFrame==4:#get rid of the explosion after the animation
                explosionFrame=0
                if leftExplosion:
                    leftExplosion=False
                elif rightExplosion:
                    rightExplosion=False
                else:
                    turretExplosion=False
                    explodedTurret=True

        if bossHealth<=50 and explodedTurret==False:#explode the turret if the boss is at half health
            doubleFireBall=True#activate double fireball
            if explodedTurretDelay>=60:
                turretExplosion=True
            else:
                explodedTurretDelay+=1
            
        if activeThunder==True:#if a lightning is active
            if thunderFrameCount>=5:
                thunderFrame+=1
                thunderFrameCount=0
            else:
                thunderFrameCount+=1
            if thunderFrame>=16:
                thunderFrame=0
                activeThunder=False
                thunderPositions=[]

        if thunderSecondCount>=250 and bossAlive:#only spawn a lightning if the boss is alive
            thunderSecondCount=0
            xPosition=randint(40,910)
            thunderPositions.append(xPosition)
            activeThunder=True
        else:
            thunderSecondCount+=1

        for thunderPos in thunderPositions:
            screen.blit(thunderPics[thunderFrame],(thunderPos,-65))

        dist=sqrt(((X-640)**2)+((Y-415)**2))#calculate speed/direction of energy ball
        if energyTimer>=110 and bossAlive:
            energyTimer=0
            if dist>250:#dont let it shoot if you are too close cuz its impossible to dodge
                #so its not really fair
                energyPositions.append([640,415])
                energyFrames.append(0)
                energyFrameCounts.append(0)
                ang = atan2(Y-415,X-640)
                vx = cos(ang)*6#horiz. component
                vy = sin(ang)*6#vertical component
                energySpeeds.append([vx,vy])#add the new speeds to the list
            
        else:
            energyTimer+=1

        #moving energy balls
        for i in range(len(energyPositions)):
            if energyFrameCounts[i]>=3:
                energyFrameCounts[i]=0
                energyFrames[i]+=1
            else:
                energyFrameCounts[i]+=1
            if energyFrames[i]>=7:
                energyFrames[i]=0
            energyPositions[i][0]+=energySpeeds[i][0]
            energyPositions[i][1]+=energySpeeds[i][1]
            screen.blit(energyPics[energyFrames[i]],(energyPositions[i]))

        ####BOSS DEAD
        if bossHealth<=0:
            bossAlive=False

        if bossAlive==False:#disable mechanics and show the key
            if (3) in gameKeys:
                if direction=="down":
                    keyY+=0.5
                    if keyY>=405:
                        direction="up"
                elif direction=="up":
                    keyY-=0.5
                    if keyY<=375:
                        direction="down"
                screen.blit(keyPic,(450,keyY))
                if playerRect.colliderect(keyRect):#if you get the key
                    gameKeys.remove(3)
                    return("lobby")
        #########
        
        display.flip()  
        myClock.tick(60)

def door4():
    global X, Y, VY, ONGROUND, XCONST, RAPID, lives, hitFrames, offset, enemycounter, dragonDirection, tracker
    offset = 0  # just to get rid of some annoying errors
    X = 550
    Y = 400
    VY = 0
    lives = 5
    bullets = []
    newDragon = [] #list to hold active dragons
    count = 0 #timer
    speed = 10  # bullet speed
    timecounter = 150 #timer
    fire = [] #fire balls list
    dragonDirection = "left" #dragon direction
    magmaTimer = 0 #timer to add new magma
    volcanoEruptTimer = 0 #timer to errupt volcano
    usedMagma = [] #active magma list

    if tracker == 0: #checking the wave
        plats = [[Rect(0, 660, 1300, 2)], [Rect(105, 560, 280, 2)], [Rect(490, 445, 280, 2)], [Rect(885, 545, 280, 2)]] #plats
        level4Background = image.load("images/level4BG.png").convert() #loading bg
        WAVE = 1 #setting wave
        magmaNum = 200 #number of magma
        enemycounter=16 #number of enemies
        dragonNum=8 #num of dragons
        fireMenNum=8 #num of fire men
        minHealth=2 #min and max dragon health
        maxHealth=4
        minHeight=0 #min and max dragon y coordinatre
        maxHeight=200
        maxSpawn = 3000 #max dragon x coordinate
    elif tracker == 1:
        plats = [[Rect(410, 466, 375, 2)], [Rect(818, 380, 375, 2)]]
        level4Background = image.load("images/level4BG2.png").convert()
        WAVE = 2
        X = 500
        Y=350
        magmaNum = 100
        enemycounter=12
        dragonNum=12
        fireMenNum=0
        minHealth=3
        maxHealth=5
        minHeight=0
        maxHeight=150
        maxSpawn = 4000
    tracker += 1 #increasing tracker

    heartPic = image.load("images/heart.png").convert_alpha() #loading images
    playerPic = [addPics("all characters", 13, 15),
                 addPics("all characters", 25, 27)]
    firemenPic = [addPics("all characters", 70, 72),
                  addPics("all characters", 82, 84)]
    dragonPic = [addPics("dragon", 10, 12),
                 addPics("dragon", 4, 6)]
    fireballPic = image.load("images/fireball.png")
    fireballPic = transform.scale(fireballPic, (50, 50))
    magmaPic = image.load("images/magma30x30.png")
    platformPic = image.load("images/firerock.png")
    platformPic = transform.scale(platformPic, (100, 10))
    streakUp = image.load("images/streakup.png").convert_alpha()
    streakDown = image.load("images/streakdown.png").convert_alpha()

    magma = [[randint(0, 1400), randint(-200, 0), randint(-6, -3)] for j in range(magmaNum)]  # [X,Y,SPEED]
    dragon = [[randint(1500,maxSpawn), randint(minHeight, maxHeight), randint(minHealth, maxHealth), randint(3, 5), -1, -1, -1, randint(1, 2), 0, 0,
                   randint(20, 100), 0, randint(70, 140), False, 150] for j in range(dragonNum)]  # [X,Y,HEALTH,SPEED,NEWMOVE,MOVE,FRAME,dragondirection,lavaplacementx,""y,speed of lava ... .... ..., onScreen](40)(1500-7400)
    firemen = [[randint(0, 1250), 660 - 61, randint(2, 3), randint(2, 5), -1, -1, -1, randint(1, 2),None,None,None,None,None,True,30] for j in range(fireMenNum)]  # [X,Y,HEALTH,SPEED,NEWMOVE,MOVE,FRAME](40)(1500-7400)
    volcanoMagma = [[263,170,randint(-9,-5),randint(8,12), "up"] for j in range(10)]

    for d in dragon: #itterating through dragons
        d[8] = d[0] #getting cuurent dragon x and y pos
        d[9] = d[1] 
        if d[7] == 1: #setting dragon direction
            d[7] = "left"
        if d[7] == 2:
            d[7] = "right"
    for f in firemen: #itterating through fire men
        if f[7] == 1: #setting men direction
            f[7] = "left"
        if f[7] == 2:
            f[7] = "right"

    running = True
    myClock = time.Clock()
    while running:
        for evt in event.get():
            if evt.type == QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            tracker = 0
            WAVE = 1
            return ("ESCMenu")
        #PLAYER DIED
        if lives <= 0:
            tracker=0
            WAVE=1
            return("deadScreen4")
        #PLAYER FELL
        if Y>=720:
            if developerMode == False:
                lives-=1
            X = randint(350, 650)
            Y = 320

        playerRect = Rect(X, Y + 8, 30, 58) #calling functions
        movePlayer(playerPic)
        checkCollision(plats)
        moveEnemies(dragon, dragonPic)
        moveEnemies(firemen, firemenPic)
        checkMobCollision(dragon, bullets, 154, 123, False, 0, [])
        checkMobCollision(firemen, bullets, 33, 61, False, 0, [])
        #DRAW SCENE
        screen.blit(level4Background, (0, 0)) #adding bg
        screen.blit(playerPic[move][int(frame)], (X, Y)) #adding player pic
        shoot(speed, bullets, plats) 
        displayLives(heartPic)

        for m in dragon: #itterating through dragons
            m[8] += 2.5
            m[9] += 2.5
            screen.blit(dragonPic[m[5]][int(m[6])], (m[0], m[1])) #adding dragon pic
            if m[0]<=1250: 
                m[11] += 1
                if m[11] == m[12]:
                    m[11] = 0
                    fire.append([m[0], m[1], m[7], randint(3,8), randint(2,4)])
        
        for x in fire: #itterating through fire balls
            if x[2] == "left": #checking direction
                x[0] -= x[3] #moving fire balls
                x[1] += x[4]
                screen.blit(fireballPic, (x[0] , x[1] + 50)) #adding fire ball pics
                fireballRect = Rect(x[0] , x[1] + 50, 50, 50) #hit box
            elif x[2] == "right":
                x[0] += x[3]
                x[1] += x[4]
                screen.blit(fireballPic, (x[0] + 120, x[1] + 70))
                fireballRect = Rect(x[0] + 120, x[1] + 70, 50, 50)

            if fireballRect.colliderect(playerRect): #checking collison
                fire.remove(x) #removing fire ball
                if developerMode == False: 
                    lives -= 1 #reducing lives
                    
        for m in firemen: #adding fire men pics
            screen.blit(firemenPic[m[5]][int(m[6])], (m[0], m[1]))

        if WAVE == 2: #checking if wave 2
            volcanoEruptTimer += 1 #increasing timer
            if volcanoEruptTimer >= 400: #checking timer
                for i in volcanoMagma: #itterating through magma
                    if i[4] == "up": #checking if direction is up 
                        screen.blit(streakUp,(i[0],i[1])) #adding magma pic
                        i[1]+=i[2] #moving magma up (i[2] is negative)
                        if i[1]<-300: #checking if magma is high up
                            i[4] = "down" #changing direction
                            i[0]+=randint(-263,937) #changing x coordinate
                    if i[4] == "down": #checking if magma is moving down
                        screen.blit(streakDown,(i[0],i[1])) #adding pics
                        i[1]+=i[3] #moving down
                        if i[1]>=1250: #checking if its at the ground
                            volcanoMagma.remove(i) #removing magma
                        if len(volcanoMagma)==0: #checking if all the magma have hit the ground
                            volcanoMagma = [[263,170,randint(-9,-5),randint(8,12), "up"] for j in range(10)] #adding new magma
                            volcanoEruptTimer=0 #resetting timer

                    streakRect = Rect(i[0], i[1], 50, 70) #magma hit box
                    if playerRect.colliderect(streakRect): #checking collision
                        if developerMode == False: 
                            lives-=1 #reducing lives
                        volcanoMagma.remove(i) #removing magma      
                    
    #MOVING MAGMA AND CHECKING MAGMA COLLISION
        magmaTimer += 1
        if magmaTimer >= 50:
            if len(magma)>0:
                usedMagma.append(magma.pop())
            magmaTimer = 0
        for m in usedMagma:
            m[0] += m[2]
            m[1] += abs(m[2])
            screen.blit(magmaPic, (m[0], m[1]))
            magmaRect = Rect(m[0], m[1], 30, 30)
            if playerRect.colliderect(magmaRect):
                if developerMode == False:
                    lives -= 1
                try:
                    usedMagma.remove(m)
                except:
                    pass
            if m[1] > 720:
                try:
                    usedMagma.remove(m)
                except:
                    pass
            for b in bullets:
                bulletRect = Rect(int(b[0]), int(b[1]), 7, 7)
                if magmaRect.colliderect(bulletRect):
                    bullets.remove(b)
                    try:
                        usedMagma.remove(m)
                    except:
                        pass

    #CHANGING PHASE/ ENDING LEVEL
        if enemycounter <= 0 and WAVE == 1:
            WAVE = 2
            fade = Surface((1250, 720))
            fade.fill((255, 0, 0))
            for alpha in range(100, 300):
                fade.set_alpha(alpha)
                screen.blit(level4Background, (0, 0))
                screen.blit(playerPic[move][int(frame)], (X, Y))
                screen.blit(fade, (0, 0))
                display.update()
                time.delay(1)
            return ("door4")
        if enemycounter <= 0 and WAVE == 2:
            fade = Surface((1250, 720))
            fade.fill((255, 0, 0))
            for alpha in range(100, 300):
                fade.set_alpha(alpha)
                screen.blit(level4Background, (0, 0))
                screen.blit(playerPic[move][int(frame)], (X, Y))
                screen.blit(fade, (0, 0))
                display.update()
                time.delay(1)
            tracker = 0
            return ("level4Complete")  # will be master door in future

        display.flip()
        myClock.tick(60)

def level4Complete():
    global gameKeys, X, Y, VY, ONGROUND, XCONST, RAPID
    X = 150
    Y = 600
    VY = 0
    keyY = 300
    direction = "down"
    
    level4Background = image.load("images/level4BG.png").convert() #loading images
    keyPic = image.load("images/key.png")
    playerPic = [addPics("all characters", 13, 15),
                 addPics("all characters", 25, 27)]
    
    plats = [[Rect(0, 660, 1300, 2)], [Rect(105, 560, 280, 2)], [Rect(490, 445, 280, 2)], [Rect(885, 545, 280, 2)]] #plats
    
    running = True
    myClock = time.Clock()
    while running:
        for evt in event.get():
            if evt.type == QUIT:
                pass
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            return ("ESCMenu")
 
        keyRect = Rect(590, keyY, 75, 75) #key hit box
        playerRect = Rect(X, Y + 8, 30, 58) #player hit box

        movePlayer(playerPic)
        checkCollision(plats)
        screen.blit(level4Background, (0, 0)) #adding bg
        
        if (4) in gameKeys: #moving key
            if direction == "down":
                keyY += 0.5
                if keyY >= 330:
                    direction = "up"
            elif direction == "up":
                keyY -= 0.5
                if keyY <= 300:
                    direction = "down"
            screen.blit(keyPic, (590, keyY))
            if playerRect.colliderect(keyRect):
                gameKeys.remove(4)
                return ("lobby")

        screen.blit(playerPic[move][0], (X, Y)) #adding player pic

        display.flip()
        myClock.tick(60)

#==============================================================================================================================================================================================================
def movePlayer(playerPic): #Moves player up, down, left, right and jumping and manages sprites
    global move, frame, player, X, Y, VY, ONGROUND, XCONST
    
    keys=key.get_pressed()
    newMove=-1
    if page=="lobby": #checking what level the function is being called in and setting the maximum the player can move, the jumping power and gravity power
        maxX=1215
        minX=0
        jumpingPower=13
        gravityPower=0.7
    elif page=="door1":
        minX=400
        maxX=4900
        jumpingPower=13
        gravityPower=0.7
    elif page=="level1Complete":
        minX=0
        maxX=1200
        jumpingPower=13
        gravityPower=0.7
    elif page=="door2":
        maxX=14500
    elif page=="level2Complete":
        minX=-3
        maxX=1185
    elif page=="door3":
        minX=400
        maxX=5336
        jumpingPower=16
        gravityPower=0.7
    elif page=="level3complete":
        minX=0
        maxX=950
        jumpingPower=16
        gravityPower=0.7
    elif page=="door4" or page=="level4Complete":
        minX=0
        maxX=1240
        jumpingPower=13
        gravityPower=0.7
    else:
        minX=0
        maxX=10000
        jumpingPower=16
        gravityPower=0.7
    
#MOVEMENT
    if page!="door2" and page!="level2Complete": #not sopace level
        if (keys[K_a] or keys[K_LEFT]) and (X>minX):#checking if player can move left
            X-=7 #moving left
            newMove=0 #setting animation
        elif (keys[K_d] or keys[K_RIGHT]) and (X<maxX):#checking if player can move right
            X+=7
            newMove=1
        if (keys[K_SPACE] or keys[K_UP]) and ONGROUND and VY==0:#checking if player can jump
            VY=-jumpingPower #moving up
            ONGROUND=False #not on ground
        Y+=VY
        VY+=gravityPower#gravity power
        
        if move==newMove: #changing animation
            frame=frame+0.2
            if frame>=len(playerPic[move]): #slowing down animation
                frame=1 #1 is the first frame for the animation (0 is idle)
        elif newMove!=-1:
            move=newMove
            frame=1

    else: #space lvl
        move=0 #setting default animation
        if page=="door2" and X<maxX: #checking if player can move
            X+=5 #constantly moving the player right
        elif page=="level2Complete": #checking if the levl is lvl2 complete
            if (keys[K_a] or keys[K_LEFT]) and (X>minX): #checking playe presses and moving player
                X-=7
            if (keys[K_d] or keys[K_RIGHT]) and (X<maxX):
                X+=7
        if (keys[K_w] or keys[K_UP]) and Y>0:
            Y-=7
            move=1 #bobbing up
        if (keys[K_s] or keys[K_DOWN]) and Y+43<720:
            Y+=7
            move=2 #bobbing down
            
def moveEnemies(mobs,mobPic): #Moves enemies (either towards player or just forward)
    global player, X, Y, VY, batCounter
    global dragonDirection
    
    if page=="door2":               
        for m in mobs: #itterating through mobs
            if m[0]+offset>=-300 and m[0]+offset<=1250: #checking if mobs can move
                m[0]-=m[3] #moving mobs left
                m[4]=1
    elif page=="level1Complete": 
        for m in mobs:
            batCounter+=0.1
            m[0]-=m[3]
            m[4]=1
            if batCounter>=30 or m[0]<=0 or m[0]>=1250:
                m[3]=m[3]*-1
                batCounter=0

    elif page == "door4":
        for m in mobs:
            if m[13]==False:
                m[0]-=1
                m[4]=0
                if m[0]<1250:
                    m[13]=True
            if m[13]==True:
                if m[0]>=1250- m[14] and m[0]<=1250:
                    m[7]="left"
                if m[7] == "left":
                    m[0] -= m[3]
                    m[4] = 0
                elif m[7] == "right":
                    m[0] += m[3]
                    m[4] = 1
                if m[0] < 0 or m[0] > 1250- m[14]:
                    if m[7] == "left":
                        m[7] = "right"
                    elif m[7] == "right":
                        m[7] = "left"
                
            if m[5] == m[4]:
                m[6] = m[6] + 0.2
                if m[6] >= len(mobPic[m[5]]):  # slowing down animation
                    m[6] = 1  # 1 is the first frame for the animation (0 is iidle)
            elif m[4] != -1:
                m[5] = m[4]
                m[6] = 1

    else:
        for m in mobs:            
            if X>m[0] and m[0]<X+750: #and mobRect.colliderect(p[0]) and playerRect.colliderect(p[0]):     
                m[0]+=m[3]
                m[4]=1     
            if X<m[0] and m[0]<X+1500: #and mobRect.colliderect(p[0]) and playerRect.colliderect(p[0]):
                m[0]-=m[3]
                m[4]=0  

            if m[5]==m[4]:
                m[6]=m[6]+0.2
                if m[6]>=len(mobPic[m[5]]): #slowing down animation
                    m[6]=1 #1 is the first frame for the animation (0 is iidle)
            elif m[4]!=-1:
                m[5]=m[4]
                m[6]=1
    
def checkCollision(plats): #Makes sure player cannot go through the ground and plats
    global player, X, Y, VY, ONGROUND, XCONST, RAPID
    if page=="lobby" or page=="level1Complete" or page=="door4" or page=="level3Complete" or page=="level4Complete":#not scrolling
        playerRect=Rect(X+10,Y+34,10,32)
    elif page=="door1" or page=="door3":#scrolling
        playerRect=Rect(XCONST+10,Y+34,10,32)#THIS HIT BOX IS DIFFERENT THAN THE HITBOX USED TO CHECK COLLISION BETWEEN MOBS AND THE PLAYER
    if page=="door3" or page=="level3Complete":
        if page=="door3":
            playerHeadRect=Rect(XCONST+10,Y,10,15)
            falseHead=Rect(XCONST+10,Y-VY,10,16)#the false rectangles are rectangles outside of the typical hitbox
            #of the player. they are used to see if the player is about to hit something
            playerBodyRect=Rect(XCONST+10,Y+15,10,35)
            falseBodyLeft=Rect(XCONST+3,Y+15,7,35)
            falseBodyRight=Rect(XCONST+20,Y+15,7,35)
        else:
            playerHeadRect=Rect(X+10,Y,10,15)
            falseHead=Rect(X+10,Y-VY,10,16)
            playerBodyRect=Rect(X+10,Y+15,10,35)
            falseBodyLeft=Rect(X+3,Y+15,7,35)
            falseBodyRight=Rect(X+20,Y+15,7,35)
        for p in plats:
            if playerRect.colliderect(p[0]): #if the feet hit a platform
                ONGROUND=True
                VY=0
                Y=p[0].y-57#put you on top of the plat
            if falseHead.colliderect(p[0]):#if you bump your head
                VY=0.6#make you slowly fall down
                Y+=4
            if falseBodyLeft.colliderect(p[0]):#if you run into a wall to the left or right
                X+=7
            elif falseBodyRight.colliderect(p[0]):
                X-=7

    else:#not checking for walls and ceilings / you can jump through platforms
        for p in plats:
            if playerRect.colliderect(p[0]):
                if VY>0:
                    ONGROUND=True
                    VY=0
                    Y=p[0].y-57

def checkMobCollision(mobs,bullets,mobHitBoxWidth,mobHitBoxHeight,canDrop,chanceOfDrop,boost): #checks collision between mobs and bullets, mobs and the player and also checks if a mob should drop a boost
    global player, X, Y, VY, ONGROUND, XCONST, RAPID, lives
    global enemycounter
    for m in mobs:
        if page=="door1":
            mobRect=Rect(m[0]+offset,m[1],mobHitBoxWidth,mobHitBoxHeight)
            playerRect=Rect(XCONST,Y+8,30,58)#THIS HIT BOX IS DIFFERENT THAN THE HITBOX USED TO CHECK COLLISION BETWEEN PLATFORMS AND THE PLAYER
        elif page=="level1Complete":
            mobRect=Rect(m[0],m[1],mobHitBoxWidth,mobHitBoxHeight)
            playerRect=Rect(X,Y+8,30,58)#THIS HIT BOX IS DIFFERENT THAN THE HITBOX USED TO CHECK COLLISION BETWEEN PLATFORMS AND THE PLAYER
        elif page=="door2":
            mobRect=Rect(m[0]+offset,m[1],mobHitBoxWidth,mobHitBoxHeight)
            if move==0:
                playerRect=Rect(XCONST,Y,73,33)
            elif move==1 or move==2:
                playerRect=Rect(XCONST,Y,63,44)
        elif page=="door4":
            mobRect=Rect(m[0],m[1],mobHitBoxWidth,mobHitBoxHeight)
            playerRect=Rect(X,Y+8,30,58)

        if page=="level1Complete" or (m[0]+offset>=0 and m[0]+offset<=1250):
            for b in bullets[:]:#checking collision between mobs and bullets
                bulletRect=Rect(int(b[0]),int(b[1]),7,7)
                if mobRect.colliderect(bulletRect):
                    bullets.remove(b)
                    m[2]-=1
                    if m[2]<=0:
                        if canDrop==True:
                            dropped=chanceOfDrop
                            if dropped==1:
                                boost.append([m[0],m[1],"speed"])
                            if dropped==2:
                                boost.append([m[0],m[1],"extraLife"])
                        try:
                            mobs.remove(m)
                            if page=="door4":
                                enemycounter-=1

                        except:
                            pass

            if playerRect.colliderect(mobRect):#checking collision between mobs and player
                if developerMode==False:
                    lives-=1
                try:
                    mobs.remove(m)
                    if page=="door4":
                        enemycounter-=1

                except:
                    pass

def checkObjectCollision(sawPositions,laserPositions,laserTimer,leverFlipped, thunderFrame):
    global lives, hitFrames, offset, thunderPositions
    global player, X, Y, VY
    playerRect=Rect(XCONST,Y+10,10,42)
    for pos in sawPositions:#check every saw
        sawRect=Rect(pos+offset,550,120,55)
        if playerRect.colliderect(sawRect) and hitFrames==50:#if you havent been hit in the last 5/6 of a second
            hitFrames=0#reset the cooldown of you being hit
            if developerMode==False:
                lives-=1

    for pos in laserPositions:#check every laser
        if laserPositions.index(pos)==0:
            laserRect=Rect(pos[0]+offset+10,pos[1],20,210)
            if leverFlipped==False and playerRect.colliderect(laserRect):#only check this laser
                #if it hasnt been disabled yet
                if developerMode==False:
                    lives-=1
                X=(laserPositions[0][0])-300#move you back a bit
                Y=150
        else:
            laserRect=Rect(pos[0]+offset+10,pos[1],20,275)
            if laserTimer<60 and (0<laserPositions.index(pos)<3 or 4<laserPositions.index(pos)<7):#check the first set of timed lasers
                if playerRect.colliderect(laserRect):
                    if developerMode==False:
                        lives-=1
                    X=3800
                    Y=280
            elif laserTimer>60 and 2<laserPositions.index(pos)<5:#check the second set of timed lasers
                if playerRect.colliderect(laserRect):
                    if developerMode==False:
                        lives-=1
                    X=3800
                    Y=280

    for pos in thunderPositions:#check every lightning bolt
        thunderRect=Rect(offset+pos+10,-20,100,640)
        if 10<thunderFrame<16 and playerRect.colliderect(thunderRect):#if the lightning is hitting the ground and hitting you
            if developerMode==False:
                lives-=1
                del thunderPositions[thunderPositions.index(pos)]

def checkBoss3Collision(energyPositions, thunderFrame, thunderPositions, hitFrames):
    global lives, energySpeeds, energyFrameCounts, energyFrames
    global player, X, Y, VY
    playerRect=Rect(X+5,Y+10,20,42)
    for pos in thunderPositions:#check lightning again like the above function
        thunderRect=Rect(pos+10,-20,100,640)
        if 10<thunderFrame<16 and playerRect.colliderect(thunderRect) and hitFrames==50:
            hitFrames=0
            if developerMode==False:
                lives-=1
                del thunderPositions[thunderPositions.index(pos)]

    for pos in energyPositions:#check every energy ball
        energyRect=Rect(pos[0],pos[1],50,55)
        if energyRect.colliderect(playerRect):#if you get hit
            ind=energyPositions.index(pos)
            if developerMode==False:
                lives-=1
                del energyPositions[ind]#get rid of the energy ball
                del energySpeeds[ind]
                del energyFrameCounts[ind]
                del energyFrames[ind]
    
def shoot(speed,bullets,plats): #creates player bullets
    global player, X, Y, VY, ONGROUND, XCONST, RAPID
    mx, my = mouse.get_pos() #getting mouse pos
    mb = mouse.get_pressed() #getting mouse clicks
    keys=key.get_pressed() #getting key clicks
    if page=="level1Complete" or page=="door4" or page=="lobby":#not scrolling
        XCONST=X
                    
    if RAPID>0: #decreasing rapid
        RAPID-=1
    if mb[0]==1 and RAPID==0: #checking for player shooting
        if page=="door1" or page=="level1Complete" or page=="door3" or page=="door4" or page=="lobby": #resetting rapid based on level
            RAPID = 20 #(20)
        elif page=="door2":
            RAPID = 10
        #*******************************
        ang = atan2(my-Y-30,mx-XCONST-20)
        vx = cos(ang)*speed#horiz. component
        vy = sin(ang)*speed#vertical component
        #*******************************
        bullets.append([XCONST+20,Y+30,vx,vy])#adding bullets to list


    for b in bullets[:]: #itterating through bullets
        '''
        if isMovingBack and page=="door1": #FIXES BULLETS GETTING REALLY SLOW WHEN MOVING BACK
            b[0]+=b[2]+7
            b[1]+=b[3]
        else:
            b[0]+=b[2]
            b[1]+=b[3]
        '''
        b[0]+=b[2] #moving bullets
        b[1]+=b[3]
            
        if b[0]>1250 or b[0]<0 or b[1]>720 or b[1]<0: #checking if bullets is off screen and deleting it
            bullets.remove(b)
        bulletRect=Rect(int(b[0]),int(b[1]),7,7) #drawing bullet
        for p in plats: #itterating through bullets
            if bulletRect.colliderect(p[0]):
                try:
                    bullets.remove(b)
                except:
                    pass
        draw.rect(screen,(255,215,0),bulletRect)

def enemyShoot(enemyBulletSpeed,enemyBullets,mob,isBoss): #creates enemy bullets
    global lives, player, X, Y, VY, ONGROUND, XCONST

    if isBoss==False: #checking if its not a boss thats shooting
        for m in mob: #itterating through mobs
            if (m[0]>X and m[0]<X+1000 and page!="level1Complete") or (page=="level1Complete" and m[1]>0): #checkin g if the mob is within a specicifc range around the player
                if m[7]>0: #decreasing rapid
                    m[7]-=1
                if m[7]==0: #checking if rapid is 0
                    if page=="level1Complete": #resetting rapid based on lvl
                        m[7]=randint(60,240)
                    else:
                        m[7]=60
                    #*******************************
                    ang = atan2(Y-m[1],X-m[0])
                    vx = cos(ang)*enemyBulletSpeed#horiz. component
                    vy = sin(ang)*enemyBulletSpeed#vertical component
                    #******************************
                    enemyBullets.append([m[0],m[1],vx,vy]) #adding bullet

        for l in enemyBullets: #drawing bullets and checking collision
            if page=="level1Complete":
                playerRect=Rect(X,Y,30,58)
                enemyBulletRect=Rect(int(l[0]),int(l[1]),16,15)
            elif page=="door2":
                if move==0:
                    playerRect=Rect(XCONST,Y,73,33)
                elif move==1 or move==2:
                    playerRect=Rect(XCONST,Y,63,44)
                enemyBulletRect=Rect(int(l[0])+offset,int(l[1]),7,7)  
                draw.rect(screen,(255,255,255),enemyBulletRect)
            else:
                playerRect=Rect(XCONST,Y,16,15)
                enemyBulletRect=Rect(int(l[0])+offset,int(l[1]),7,7)                
                draw.rect(screen,(255,255,255),enemyBulletRect)
            l[0]+=l[2]
            l[1]+=l[3]
            if enemyBulletRect.colliderect(playerRect):
                if developerMode==False:
                    lives-=1
                try:
                    enemyBullets.remove(l)
                except:
                    pass 
            if l[0]+offset<=0 or ((l[0]>=1250 or l[1]>=720 or l[1]<=0) and page!="door2"):
                try:
                    enemyBullets.remove(l)
                except:
                    pass
                        
    else: #it is a boss
        global bossRapid, bossAction, bossX, bossY
        if bossRapid>0: #decreasing rapid
            bossRapid-=1
        if bossRapid==0:
            bossRapid=60
            #*******************************
            ang = atan2(Y-bossY,X-bossX)
            vx = cos(ang)*enemyBulletSpeed#horiz. component
            vy = sin(ang)*enemyBulletSpeed#vertical component
            #******************************
            enemyBullets.append([bossX,bossY+50,vx,vy]) #adding bullets
        
        for l in enemyBullets: #itterating through bullets, drawing them and checking for collision
            playerRect=Rect(X,Y+8,30,58)
            l[0]+=l[2]
            l[1]+=l[3]              
            enemyBulletRect=Rect(int(l[0]),int(l[1]),33,33)
            if enemyBulletRect.colliderect(playerRect):
                if developerMode==False:
                    lives-=1
                try:
                    enemyBullets.remove(l)
                except:
                    pass
            if l[0]<=0 or l[0]>1250 or l[1]>720:
                try:
                    enemyBullets.remove(l)
                except:
                    pass

def finalBoss(bullets, dadPics):
    global FX, FY, finalBossMove, finalBossFrame, finalBossDirection, finalBossJumpTimer, finalBossDirectionChangeTimer, finalBossTempDirection, isFinalBossJumping, finalBossJumpDirection, isFinalBossMoving, finalBossLives, finalBossSpeed, isFinalBossMovingAway, finalBossJumpTimer2
    dadNewMove = -1
    finalBossAIRight=Rect(FX-150, FY+8, 300, 70) #hit box that checks for bullet collision and determines if the boss should jump
    dadRect=Rect(FX,FY+8,30,50) #boss hit box
    for b in bullets:  #itterating through bullets
        bulletRect = Rect(int(b[0]), int(b[1]), 7, 7) #drawing bullet
        if bulletRect.colliderect(dadRect): #checking if the bullet hit the boss
            finalBossLives-=1 #decreasing boss lives
            bullets.remove(b) #removing bullet

    for b in bullets[:]:  #checking collision between bullets and dad's jumping hit box
        bulletRect = Rect(int(b[0]), int(b[1]), 7, 7) 
        if bulletRect.colliderect(finalBossAIRight) and FY==355 and (abs(int(b[2]))==9):
            finalBossTempDirection = finalBossDirection #temporairly storing direction 
            bossRandJump=randint(0,3) #determining if boss can jump (to prvenet the boss from being over powered)
            if bossRandJump<=1: #checking num
                isFinalBossJumping = True #jump is true

    if finalBossDirection == "right": #changing sprite animation based on direction
        dadNewMove = 1
    elif finalBossDirection == "left":
        dadNewMove = 0

    if isFinalBossMovingAway == False and isFinalBossMoving == False: 
        dadNewMove = -1
        if finalBossDirection == "right":
            finalBossMove = 1
        elif finalBossDirection == "left":
            finalBossMove = 0

    if isFinalBossMoving: #moving final boss
        if finalBossDirection == "right" and FX+120<=X:
            FX+= finalBossSpeed
        elif finalBossDirection == "left" and FX-120>=X:
            FX-= finalBossSpeed
        else:
            dadNewMove = -1

    if isFinalBossMovingAway:
        if finalBossDirection == "right":
            FX+= finalBossSpeed
        elif finalBossDirection == "left":
            FX-= finalBossSpeed

    if finalBossMove == dadNewMove: #moving boss animation
        finalBossFrame = finalBossFrame + 0.2
        if finalBossFrame >= len(dadPics[finalBossMove]):  # slowing down animation
            finalBossFrame = 1  # 1 is the first frame for the animation (0 is idle)
    elif dadNewMove != -1:
        finalBossMove = dadNewMove
        finalBossFrame = 1

    screen.blit(dadPics[finalBossMove][int(finalBossFrame)], (FX, FY)) #adding player pic

    if isFinalBossJumping: #boss jumping mechanics
        if finalBossJumpDirection == "up":
            finalBossJumpTimer+=0.5
            finalBossJumpTimer2= 10 - finalBossJumpTimer
            FY -= finalBossJumpTimer2
            if FY >= 355:
                FY = 355
                isFinalBossJumping = False
                finalBossJumpDirection = "up"
                finalBossJumpTimer = 0
                finalBossJumpTimer2 = 0

    finalBossDirectionChangeTimer += 1 #increasing timer
    if finalBossDirectionChangeTimer >= 100: #checking timer
        directionRand=randint(0,10) #gneerating random number --> random action
        if directionRand <=4: #checking number and changing movement accordingly
            isFinalBossMoving = True
            finalBossSpeed = randint (2, 4)
            isFinalBossMovingAway = False
        elif directionRand>4 and directionRand<=7:
            isFinalBossMovingAway=True
            isFinalBossMoving = False
            finalBossSpeed = randint(2, 4)
        else:
            isFinalBossMoving = False
            isFinalBossMovingAway = False
        jumpRand=randint(0,3)
        if jumpRand == 1:
            isFinalBossJumping = True
        finalBossDirectionChangeTimer = 0

    if isFinalBossMovingAway == False: #checking if the player passes the boss and moving the boss towards the player
        if finalBossDirection == "left" and X < FX:
            pass
        elif finalBossDirection == "right" and X >FX:
            pass
        else:
            if finalBossDirection == "right":
                finalBossDirection = "left"
            elif finalBossDirection == "left":
                finalBossDirection = "right"

    elif isFinalBossMovingAway == True:
        if finalBossDirection == "left" and X < FX:
            if finalBossDirection == "right":
                finalBossDirection = "left"
            elif finalBossDirection == "left":
                finalBossDirection = "right"
        elif finalBossDirection == "right" and X >FX:
            if finalBossDirection == "right":
                finalBossDirection = "left"
            elif finalBossDirection == "left":
                finalBossDirection = "right"
        else:
            pass

    if FX <= 50: #checking if boss reaches screen edges and stopping movement
        isFinalBossMovingAway = False
        directionRand = randint(0, 2)
        if directionRand == 0:
            finalBossDirection = "none"
        elif directionRand == 1:
            finalBossDirection = "right"

    if FX >= 1210:
        isFinalBossMovingAway = False
        directionRand = randint(0,2)
        if directionRand == 0:
            finalBossDirection = "none"
        elif directionRand == 1:
            finalBossDirection = "left"

def finalBossShoot(speed, bullets): #same function as shoot() and enemyshoot()
    global lives, player, X, Y, VY, ONGROUND, XCONST, finalBossRapid, FX, FY, finalBossDirection, gameLives
    playerRect = Rect(X, Y + 8, 30, 58)

    if finalBossDirection == "left" and X < FX:
        shooting = True
    elif finalBossDirection == "right" and X >FX:
        shooting = True
    else:
        shooting = False

    if finalBossRapid > 0:
        finalBossRapid -= 1
    if shooting and finalBossRapid == 0:
        finalBossRapid = randint(30,75)
        # ******************************
        ang = atan2(Y - FY , X - FX )
        vx = cos(ang) * speed  # horiz. component
        vy = sin(ang) * speed  # vertical component
        # *******************************
        bullets.append([FX + 20, FY + 30, vx, vy])

    for b in bullets[:]:
        b[0] += b[2]
        b[1] += b[3]

        if b[0] > 1250 or b[0] < 0 or b[1] > 720 or b[1] < 0:
            bullets.remove(b)
        bulletRect = Rect(int(b[0]), int(b[1]), 7, 7)

        if bulletRect.colliderect(playerRect):
            if developerMode == False:
                gameLives -= 1
            bullets.remove(b)

        draw.rect(screen, (255, 215, 0), bulletRect)

def displayLives(heartPic): #display lives
    global lives
    for h in range(lives):#draw as many hearts as you have lives
        if page!="level3Complete":
            screen.blit(heartPic,(1190+h*-50,10))
        else:
            screen.blit(heartPic,(940+h*-50,10))

def displayGameLives(gameHeartPic):
    global gameLives
    for h in range (gameLives):
        screen.blit(gameHeartPic,(1190+h*-50,10))

def displayGameKeys(keyPic):
    global gameKeys
    for h in range(4-len(gameKeys)):#draw how many keys you have collected
        #(or removed from the list)
        screen.blit(keyPic,(0+h*50,10))
    
def addPics(name,start,end):
    mypics=[]#pics will go in a list
    for i in range(start,end+1):
        mypics.append(image.load("%s/%s%03d.png"%(name,name,i)))
    return mypics

#=================================================================================================================================================================================================================

page="lobby"
while page!="exit": 
    if page=="lobby": #checking what page should be displayed --> calling that function and setting display size
        screen=display.set_mode((1250,720))
        page=lobby()
    if page=="door1":
        screen=display.set_mode((1250,666))
        page=door1()
    if page=="door2":
        screen=display.set_mode((1250,720))
        page=door2()
    if page=="door3":
        screen=display.set_mode((1250,720))
        page=door3()
    if page=="door4":
        screen=display.set_mode((1250,720))
        page=door4()
        
    if page=="level1Complete":
        screen=display.set_mode((1250,666))
        page=level1Complete()
    if page=="level2Complete":
        screen=display.set_mode((1250,720))
        page=level2Complete()
    if page=="level3Complete":
        screen=display.set_mode((999,720))
        page=level3Complete()
    if page=="level4Complete":
        screen=display.set_mode((1250,720))
        page=level4Complete()

    if page == "deadScreenLobby":
        screen = display.set_mode((1250, 720))
        page = deadScreen("lobbyDead")
    if page=="deadScreen1":
        screen=display.set_mode((1250,720))
        page=deadScreen(1)
    if page == "deadScreen1Complete":
        screen=display.set_mode((1250,666))
        page=deadScreen("1Complete")
    if page=="deadScreen2":
        screen=display.set_mode((1250,720))
        page=deadScreen(2)
    if page=="deadScreen3":
        screen=display.set_mode((1250,720))
        page=deadScreen(3)
    if page=="deadScreen3Complete":
        screen=display.set_mode((1250,666))
        page=deadScreen("3Complete")
    if page=="deadScreen4":
        screen=display.set_mode((1250,720))
        page=deadScreen(4)

    if page == "easterEgg":
        screen = display.set_mode((1250, 720))
        page = easterEgg()
    if page == "gameComplete":
        screen = display.set_mode((1250, 720))
        page = gameComplete()
    if page=="ESCMenu":
        screen = display.set_mode((1250, 720))
        page = ESCMenu()

quit()
