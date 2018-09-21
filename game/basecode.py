## CS - 1110 INTRODUCTION TO PROGRAMMING
## LABORATORY SECTION 105 (3:30 PM)
## JEC2GW and CJP7ZG
## DECEMBER 2ND 2016

## ----------------------------------------- FINAL GAME PROJECT -----------------------------------------------

## GOT GUIDANCE FROM LECTURE CODE, LECTURE MATERIALS, AND GAMEBOX API PDF

## ------------------------------------------ VARIABLES ---------------------------------------

## IMPORTING PYGAME, GAMEBOX, and RANDOM
import pygame
import gamebox
import random

## DEFINING CAMERA
camera = gamebox.Camera(800,600)

## CREATING TRON LOGO AND BACKGROUND

logo = gamebox.from_image(625,50,"tronlogo.png")
logo.scale_by(0.5)

gamebackdrop = gamebox.from_image(400,300, 'background.jpg')
playingfield = gamebox.from_color(400, 400, 'black', 600, 600)

## DEFINING BOOLEAN VARIABLE TO START GAME
start = False
restart = True

## DEFINING COUNTUP TIMER AND HIGHLIGHT
countup = 0

## DEFINING SCORE VARIABLE AND HIGHLIGHT
scoreplayer1 = 0
scoreplayer2 = 0

scorehighlight = gamebox.from_color(400, 400, 'black', 600, 600)

## DEFINING CHARACTERS AND SPRITESHEETS
player1x = random.randint(150,300)
player1y = 400

player1 = gamebox.from_color(player1x, player1y, 'red', 10, 10)
player1trail = [gamebox.from_color(player1x, player1y, 'red', 10, 10)]

player2x = random.randint(500,650)
player2y = 400

player2 = gamebox.from_color(player2x, player2y, 'blue', 10, 10)
player2trail = [gamebox.from_color(player2x, player2y, 'blue', 10, 10)]

## DEFINING EXPLOSIONS
explosionsprite = gamebox.load_sprite_sheet("explosionsprite.png",4,4)

p1boom = gamebox.from_image(player1x,player1y,explosionsprite[9])

explosions = []

## BOOLEAN MOVEMENT VARIABLES FOR PLAYERS 1 AND 2

p1north = True
p1south = False
p1east = False
p1west = False

p2north = True
p2south = False
p2east = False
p2west = False

## CREATING WALLS/BOUNDARIES FOR GAME

walls = [gamebox.from_color(100,400,"green",5, 600), gamebox.from_color(700,400,"green",5, 600),
         gamebox.from_color(400,100,"green",605, 5), gamebox.from_color(400,599,"green",600, 5)]

## DEFINING SOUND VARAIBLES FOR GAME
backgroundsound = gamebox.load_sound('Tron.wav')
explosionsound = gamebox.load_sound('Explosion 1.wav')
coinsound = gamebox.load_sound('Coin.wav')
restartsound = gamebox.load_sound('Restart.wav')


## DEFINING COINS LIST AND VARAIBLES
coinsprite = gamebox.load_sprite_sheet("Coin.png", 1, 1)
coins = [gamebox.from_image(400, random.randint(120,580), coinsprite[0])]
coins[0].scale_by(0.5)

## ------------------------------------------ CODE --------------------------------------------

def tick(keys):
    ## GLOBAL VARIABLES
    global scoreplayer1, scoreplayer2, agreed, countup, p1north, p1west, p1east, p1south, \
        p2north, p2south, p2west, p2east, \
        player1x, player1y, player2x, player2y, \
        restart, frame, counter, boomx, boomy

    ## CREATING RESTART MESSAGE AND HIGHLIGHT TO INFORM PLAYER
    restartmessage = gamebox.from_text(625, 50, "PRESS SPACE TO CONTINUE", "TIMES", 20, "white")
    restartmessagehighlight = gamebox.from_color(625, 50, "red", 325, 50)

    ## RESTART CONDITION - IF SPACE IS PRESSED AND RESTART BOOLEAN IS FALSE
    if pygame.K_SPACE in keys and restart == False:
        ## SET RESTART BOOLEAN TO TRUE
        restart = True
        ## REDEFINING PLAYER 1 POSITIONING
        player1x = random.randint(150,300)
        player1y = 400
        ## REDEFINING PLAYER 2 POSITIONING
        player2x = random.randint(500,650)
        player2y = 400

        ## RE-CREATING PLAYER 1 LISTS
        player1trail[:] = []
        player1trail.append(gamebox.from_color(player1x, player1y, 'red', 10, 10))

        player2trail[:] = []
        player2trail.append(gamebox.from_color(player2x, player2y, 'blue', 10, 10))

        ## RE-CREATING COINS

        coins.append(gamebox.from_image(400, random.randint(120,580), coinsprite[0]))
        coins[0].scale_by(0.5)

        ## PLAYING RESTART SOUND

        restartsound.play()

        ## CLEARING EXPLOSIONS LIST
        explosions[:] = []

        ## RESETTING BOOLEAN VARIABLES FOR GAME RESTART
        p1north = True
        p1south = False
        p1east = False
        p1west = False

        p2north = True
        p2south = False
        p2east = False
        p2west = False

    ## DEFINING GAME RESTART CONDITION
    if restart == True:

    ## CLEARING CAMERA FOR GAME
        camera.draw(gamebackdrop)
        camera.draw(playingfield)

        ## DRAWING TRON LOGO
        camera.draw(logo)
        ## CREATING COUNT-UP TIMER
        countup += 1

        ## DEFINING MATH BEHIND TIMER
        seconds = str(int((countup / ticks_per_second) % 60)).zfill(2)
        minutes = str(int((countup / ticks_per_second) / 60))

        ## DEEFINING COINS SCORE
        for coin in coins:
            ## CREATING CONDITION FOR PLAYER 1 COIN COLLECTION
            if player1trail[len(player1trail)-1].touches(coin):
                scoreplayer1 += 1
                coinsound.play()
                coins.remove(coin)
            ## CREATING CONDITION FOR PLAYER 2 COIN COLLECTION
            if player2trail[len(player2trail) - 1].touches(coin):
                scoreplayer2 += 1
                coinsound.play()
                coins.remove(coin)
            camera.draw(coin)

    ## CREATING RANDOM SPAWN OF COIN
        if int(countup) % 150 == 0:
            coins.append(gamebox.from_image(random.randint(150,300), random.randint(120, 580), coinsprite[0]))
            coins[len(coins)-1].scale_by(0.5)

    ## DEFINING PLAYER 1 CHARACTER MOVEMENTS

        if pygame.K_w in keys:
            if p1south == False:
                p1north = True
                p1south = False
                p1east = False
                p1west = False

        if pygame.K_s in keys:
            if p1north == False:
                p1north = False
                p1south = True
                p1east = False
                p1west = False


        if pygame.K_d in keys:
            if p1west == False:
                p1north = False
                p1south = False
                p1east = True
                p1west = False

        if pygame.K_a in keys:
            if p1east == False:
                p1north = False
                p1south = False
                p1east = False
                p1west = True



    ## DEFINING PLAYER 2 CHARACTER MOVEMENTS

        if pygame.K_UP in keys:
            if p2south == False:
                p2north = True
                p2south = False
                p2east = False
                p2west = False


        if pygame.K_DOWN in keys:
            if p2north == False:
                p2north = False
                p2south = True
                p2east = False
                p2west = False


        if pygame.K_RIGHT in keys:
            if p2west == False:
                p2north = False
                p2south = False
                p2east = True
                p2west = False

        if pygame.K_LEFT in keys:
            if p2east == False:
                p2north = False
                p2south = False
                p2east = False
                p2west = True

    ## CONDITION FOR P1 NORTH MOVEMENT
        if p1north == True and p1south == False and p1east == False and p1west == False:
            ## DECREASING PLAYER 1 Y POSITION
            player1y -= 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player1trail.append(gamebox.from_color(player1x, player1y, 'red', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player1trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player1trail[len(player1trail)-1].top_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player1x, player1y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1north = False
                    p2north = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer2 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

    ## CONDITION FOR P2 NORTH MOVEMENT
        if p2north == True and p2south == False and p2east == False and p2west == False:
            ## DECREASING PLAYER 1 Y POSITION
            player2y -= 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player2trail.append(gamebox.from_color(player2x, player2y, 'blue', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player2trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player2trail[len(player2trail) - 1].top_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1north = False
                    p2north = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer1 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

    ## CONDITION FOR P1 SOUTH MOVEMENT
        if p1north == False and p1south == True and p1east == False and p1west == False:
            ## INCREASING PLAYER 1 Y POSITION
            player1y += 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player1trail.append(gamebox.from_color(player1x, player1y, 'red', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player1trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player1trail[len(player1trail) - 1].bottom_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player1x, player1y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1south = False
                    p2south = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer2 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

    ## CONDITION for P2 SOUTH MOVEMENT
        if p2north == False and p2south == True and p2east == False and p2west == False:
            ## DECREASING PLAYER 1 Y POSITION
            player2y += 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player2trail.append(gamebox.from_color(player2x, player2y, 'blue', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player2trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player2trail[len(player2trail)-1].bottom_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1south = False
                    p2south = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    print("This ran")
                    ## INCREASING PLAYER SCORE
                    scoreplayer1 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False
    ## CONDITION FOR P1 EAST MOVEMENT
        if p1north == False and p1south == False and p1east == True and p1west == False:
            ## INCREASING PLAYER 1 X POSITION
            player1x += 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player1trail.append(gamebox.from_color(player1x, player1y, 'red', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player1trail:
                camera.draw(trail)
                ## CODE HERE IS DIFFERENT BECAUSE OF ISSUES WITH THE .right_touches() METHOD
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player1trail[len(player1trail)-1].x < trail.x and player1trail[len(player1trail)-1].right_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player1x, player1y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1east = False
                    p2east = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    if player2trail[len(player2trail)-1].x < trail.x and player2trail[len(player2trail)-1].right_touches(trail):
                        scoreplayer1 += 1
                    elif player1trail[len(player1trail)-1].x < trail.x and player1trail[len(player1trail)-1].right_touches(trail):
                        scoreplayer2 += 1
                    ## CLEARING PLAYER1TRAIL LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False


        ## CONDITION for P2 EAST MOVEMENT
        if p2north == False and p2south == False and p2east == True and p2west == False:
            ## DECREASING PLAYER 1 Y POSITION
            player2x += 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player2trail.append(gamebox.from_color(player2x, player2y, 'blue', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player2trail:
                camera.draw(trail)
                ## CODE HERE IS DIFFERENT BECAUSE OF ISSUES WITH THE .right_touches() METHOD
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player2trail[len(player2trail) - 1].x < trail.x and player2trail[len(player2trail) - 1].right_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1east = False
                    p2east = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer1 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

    ## CONDITION FOR P1 WEST MOVEMENT
        if p1north == False and p1south == False and p1east == False and p1west == True:
            ## DECREASING PLAYER 1 X POSITION
            player1x -= 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player1trail.append(gamebox.from_color(player1x, player1y, 'red', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player1trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player1trail[len(player1trail)-1].left_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player1x, player1y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1west = False
                    p2west = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer2 += 1
                    ## CLEARING PLAYER1TRAIL LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

        ## CONDITION for P2 WEST MOVEMENT
        if p2north == False and p2south == False and p2east == False and p2west == True:
            ## DECREASING PLAYER 1 Y POSITION
            player2x -= 5
            ## CREATING PLAYER 1 TRAIL IN RELEVANT DIRECTION
            player2trail.append(gamebox.from_color(player2x, player2y, 'blue', 10, 10))
            ## DRAWING PLAYER 1 TRAIL
            for trail in player2trail:
                camera.draw(trail)
                ## DEFINING PLAYER 1 COLLISION CONDITION(S)
                if player2trail[len(player2trail)-1].left_touches(trail):
                    ## CREATING EXPLOSION AT RELEVANT REGION
                    explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))
                    ## PLAYING EXPLOSION SOUND
                    explosionsound.play()
                    ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                    p1west = False
                    p2west = False
                    ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                    coins[:] = []
                    ## INCREASING PLAYER SCORE
                    scoreplayer1 += 1
                    ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                    player1trail[:] = []
                    player2trail[:] = []
                    camera.draw(explosions[len(explosions) - 1])
                    ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                    camera.draw(restartmessagehighlight)
                    camera.draw(restartmessage)
                    ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                    restart = False

        ## DRAWING SCORE(s) ON SCREEN
        player1score = gamebox.from_text(150, 35, "PLAYER 1 SCORE: " + str(scoreplayer1), "TIMES", 20, "White")
        player2score = gamebox.from_text(150, 65, "PLAYER 2 SCORE: " + str(scoreplayer2), "TIMES", 20, "White")

        countuphighlight = gamebox.from_color(150, 50, 'black', 250, 75)
        camera.draw(countuphighlight)
        camera.draw(player1score)
        camera.draw(player2score)

        ## DRAWING TIMER ON SCREEN
        countuptimer = gamebox.from_text(400, 50, minutes + ":" + seconds, "TIMES", 25, "White")

        timerhighlight = gamebox.from_color(400, 50, 'black', 75, 50)
        camera.draw(timerhighlight)
        camera.draw(countuptimer)

        ## DRAWING WALLS/ARENA BOUNDARIES
        for wall in walls:
            camera.draw(wall)


    ## DEFINING PLAYER TRAIL CONDITION TO PREVENT ERRORS
    if len(player1trail) != 0 and len(player2trail) != 0:
    ## DEFINING CONDITIONS FOR PLAYER 1 COLLISION WITH PLAYER 2
        for trail in player2trail:
            if player1trail[len(player1trail)-1].touches(trail):
                ## CREATING EXPLOSION AT RELEVANT REGION
                explosions.append(gamebox.from_image(player1x, player1y, explosionsprite[9]))
                ## PLAYING EXPLOSION SOUND
                explosionsound.play()
                ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                p1west = False
                p2west = False
                p1east = False
                p2east = False
                p1north = False
                p2north = False
                p1south = False
                p2south = False
                ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                coins[:] = []
                ## INCREASING PLAYER SCORE
                scoreplayer2 += 5
                ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                player1trail[:] = []
                player2trail[:] = []
                camera.draw(explosions[len(explosions) - 1])
                ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                camera.draw(restartmessagehighlight)
                camera.draw(restartmessage)
                ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                restart = False

    ## DEFINING PLAYER TRAIL CONDITION TO PREVENT ERRORS
    if len(player1trail) != 0 and len(player2trail) != 0:
    ## DEFINING CONDITIONS FOR PLAYER 2 COLLISION WITH PLAYER 1

        for trail in player1trail:
            if player2trail[len(player2trail)-1].touches(trail):
                ## CREATING EXPLOSION AT RELEVANT REGION
                explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))
                ## PLAYING EXPLOSION SOUND
                explosionsound.play()
                ## SETTING NORTH BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
                p1west = False
                p2west = False
                p1east = False
                p2east = False
                p1north = False
                p2north = False
                p1south = False
                p2south = False
                ## CLEARING COINS LIST IN PREPARATION FOR RESTART
                coins[:] = []
                ## INCREASING PLAYER SCORE
                scoreplayer1 += 5
                ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
                player1trail[:] = []
                player2trail[:] = []
                camera.draw(explosions[len(explosions) - 1])
                ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
                camera.draw(restartmessagehighlight)
                camera.draw(restartmessage)
                ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
                restart = False

    ## DEFINING PLAYER TRAIL CONDITION TO PREVENT ERRORS
    if len(player1trail)!= 0 and len(player2trail)!= 0:
        ## DEFINING PLAYER COLLISION CONDITION WITH WEST WALL
        if player1trail[len(player1trail) - 1].touches(walls[0]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player1x,player1y,explosionsprite[9]))
            ## PLAYING EXPLOSION SOUND
            explosionsound.play()
            ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1west = False
            p2west = False
            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer2 += 1
            camera.draw(explosions[len(explosions)-1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

        ## DEFINING PLAYER COLLISION CONDITION WITH WEST WALL
        elif player2trail[len(player2trail)-1].touches(walls[0]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1west = False
            p2west = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer1 += 1
            camera.draw(explosions[len(explosions) - 1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

        ## DEFINING PLAYER COLLISION CONDITION WITH EAST WALL
        elif player1trail[len(player1trail) - 1].touches(walls[1]):

            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player1x,player1y,explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1east BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1east = False
            p2east = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []


            ## INCREASING PLAYER 2 SCORE
            scoreplayer2 += 1

            camera.draw(explosions[len(explosions)-1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)

            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

        ## DEFINING PLAYER COLLISION CONDITION WITH EAST WALL
        elif player2trail[len(player2trail) - 1].touches(walls[1]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1east = False
            p2east = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer1 += 1
            camera.draw(explosions[len(explosions) - 1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

        ## DEFINING PLAYER COLLISION CONDITION WITH NORTH WALL
        elif player1trail[len(player1trail) - 1].touches(walls[2]):

            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player1x,player1y,explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1north BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1north = False
            p2north = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []


            ## INCREASING PLAYER 2 SCORE
            scoreplayer2 += 1
            camera.draw(explosions[len(explosions)-1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)

            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

            ## DEFINING PLAYER COLLISION CONDITION WITH NORTH WALL
        elif player2trail[len(player2trail) - 1].touches(walls[2]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1north = False
            p2north = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer1 += 1
            camera.draw(explosions[len(explosions) - 1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

        ## DEFINING PLAYER COLLISION CONDITION WITH SOUTH WALL
        elif player1trail[len(player1trail) - 1].touches(walls[3]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player1x,player1y,explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1south BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1south = False
            p2south = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer2 += 1

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)

            camera.draw(explosions[len(explosions)-1])
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

            ## DEFINING PLAYER COLLISION CONDITION WITH SOUTH WALL
        elif player2trail[len(player2trail) - 1].touches(walls[3]):
            ## CREATING EXPLOSION AT RELEVANT REGION
            explosions.append(gamebox.from_image(player2x, player2y, explosionsprite[9]))

            ## PLAYING EXPLOSION SOUND

            explosionsound.play()

            ## SETTING p1west BOOLEAN VARIABLE TO FALSE TO PREVENT FURTHER MOVEMENT
            p1south = False
            p2south = False

            ## CLEARING PLAYER1TRAIL and PLAYER1OUTLINE LISTS IN PREPARATION FOR RESTART
            player1trail[:] = []
            player2trail[:] = []

            ## CLEARING COINS LIST IN PREPARATION FOR RESTART
            coins[:] = []

            ## INCREASING PLAYER 2 SCORE
            scoreplayer1 += 1
            camera.draw(explosions[len(explosions) - 1])

            ## DRAWING RESTART MESSAGE TO INFORM PLAYER(S)
            camera.draw(restartmessagehighlight)
            camera.draw(restartmessage)
            ## SETTING RESTART BOOLEAN TO FALSE TO PREPARE FOR GAME RESTART
            restart = False

## DEFINING CONDITION FOR PLAYER 1 GAME WIN
    if scoreplayer1 > scoreplayer2 and scoreplayer1 >= 20:
        ## CREATING PLAYER 1 AND PLAYER 2 FINAL SCORE VARIABLES
        winner = gamebox.from_text(400, 350, "PLAYER 1 WINS! ", "TIMES", 50, "Red")
        p1score = gamebox.from_text(400, 425, "PLAYER 1 SCORE: " + str(scoreplayer1), "TIMES", 50, "Black")
        p2score = gamebox.from_text(400, 500, "PLAYER 2 SCORE: " + str(scoreplayer2), "TIMES", 50, "Black")

        ## CLEARING WHITE BACKGROUND
        camera.clear("white")

        ## DRAWING GAMEOVER IMAGE
        camera.draw(gamebox.from_image(400, 200,"gameover.png"))

        ## PLAYING BACKGROUND SOUND TO FINISH
        backgroundsound.play()

        ## DRAWING SCORES
        camera.draw(winner)
        camera.draw(p1score)
        camera.draw(p2score)

        ## PAUSING GAMEBOX
        gamebox.pause()

## DEFINING CONDITION FOR PLAYER 2 GAME WIN
    if scoreplayer2 > scoreplayer1 and scoreplayer2 >= 20:
        ## CREATING PLAYER 1 AND PLAYER 2 FINAL SCORE VARIABLES
        winner = gamebox.from_text(400, 350, "PLAYER 2 WINS! ", "TIMES", 50, "Red")
        p1score = gamebox.from_text(400, 425, "PLAYER 1 SCORE: " + str(scoreplayer1), "TIMES", 50, "Black")
        p2score = gamebox.from_text(400, 500, "PLAYER 2 SCORE: " + str(scoreplayer2), "TIMES", 50, "Black")

        ## CLEARING WHITE BACKGROUND
        camera.clear("white")

        ## DRAWING GAMEOVER IMAGE
        camera.draw(gamebox.from_image(400, 200,"gameover.png"))

        ## PLAYING BACKGROUND SOUND TO FINISH
        backgroundsound.play()

        ## DRAWING SCORES
        camera.draw(winner)
        camera.draw(p1score)
        camera.draw(p2score)
        ## PAUSING GAMEBOX
        gamebox.pause()
    ## DISPLAYING CAMERA
    camera.display()
## DEFINING FUNCTION TO START GAME
def intro(keys):
    global start
    if start == True:
        gamebox.timer_loop(ticks_per_second,tick)
    else:
        ## DEFINING BACKGROUND OF GAME START
        background = gamebox.from_image(400, 300, "startingbackground.jpg")
        ## SCALING BACKGROUND FOR BETTER FIT
        background.scale_by(0.65)
        ## CREATING INSTRUCTIONS TO INFORM PLAYER(S)
        instructions = gamebox.from_text(400, 125, "PRESS SPACE TO START", "TIMES", 24, "white")
        howtoplay = gamebox.from_text(400,410, "HOW TO PLAY", 'TIMES', 18, 'white')
        player1instructions = gamebox.from_text(400,430, "PLAYER 1 - UP, DOWN, LEFT, RIGHT", 'TIMES', 12, 'white')
        player2instructions = gamebox.from_text(400, 450, "PLAYER 2 - W, A, S, D", 'TIMES', 12, 'white')
        generalinstructions = gamebox.from_text(400, 470, "TRAP YOUR OPPONENT IN YOUR PATH", 'TIMES', 12, 'white')
        generalinstructions1 = gamebox.from_text(400, 490, "AND GATHER COINS TO GET POINTS", 'TIMES', 12, 'white')
        generalinstructions2 = gamebox.from_text(400, 510, "FIRST TO 10 POINTS WINS!", 'TIMES', 12, 'white')
        names = gamebox.from_text(600, 590, "Connor Park (CJP7ZG) & John Cragun (JEC2GW)", 'TIMES', 15, 'white')
        instructionshighlight = gamebox.from_color(400,125, "red", 350, 50)
        howtoplayhighlight = gamebox.from_color(400, 460, "red", 350, 125)
        nameshighlight = gamebox.from_color(600, 590, "red", 385, 20)
        ## DRAWING INSTRUCTIONS FOR GAME
        camera.draw(background)
        camera.draw(instructionshighlight)
        camera.draw(howtoplayhighlight)
        camera.draw(nameshighlight)
        camera.draw(instructions)
        camera.draw(howtoplay)
        camera.draw(player1instructions)
        camera.draw(player2instructions)
        camera.draw(generalinstructions)
        camera.draw(generalinstructions1)
        camera.draw(generalinstructions2)
        camera.draw(names)
        ## DEFINING USER INPUT TO START GAME
        if pygame.K_SPACE in keys:
            start = True
            backgroundsound.stop()
        camera.display()
## DEFINING TICKS PER SECOND
ticks_per_second = 30
## PLAYING BACKGROUND MUSIC
backgroundsound.play(-1)
## DEFINING TICK FUNCTION LOOP
gamebox.timer_loop(ticks_per_second, intro)