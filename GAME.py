import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("ДРАКОНДЮК")

walkRight = [pygame.image.load('Walk1.png'),pygame.image.load('Walk2.png'),
            pygame.image.load('Walk3.png'), pygame.image.load('Walk4.png'),
             pygame.image.load('Walk5.png'), pygame.image.load('Walk6.png')]
walkLeft = [pygame.image.load('Walk1M.png'),pygame.image.load('Walk2M.png'),
            pygame.image.load('Walk3M.png'), pygame.image.load('Walk4M.png'),
             pygame.image.load('Walk5M.png'), pygame.image.load('Walk6M.png')]
bg = pygame.image.load ('bg.jpg')
playerStand = pygame.image.load ('Stop.png')
#anJump = pygame.image.load('Jump.png')

fire = [pygame.image.load('f1.png'),pygame.image.load('f2.png'),
            pygame.image.load('f3.png'), pygame.image.load('f4.png')]

clock = pygame.time.Clock()

x = 210
y = 411
width = 76
height = 84
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"
class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self, win):
         pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (round(x), round(y)))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount // 5], (round(x), round(y)))
        animCount += 1
    else:
        win.blit(playerStand, (round(x), round(y)))
        #animCount += 1
        for bullet in bullets:
            bullet.draw(win)
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 1.5), round(y+ height // 3.7), 3, (255,0,0), facing))
           # bullets.append(snaryad(win.blit(walkLeft[animCount // 5], (round(x), round(y)))))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - width -5:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
       # if keys[pygame.K_UP] and y > 5:
          #  y -= speed
        #if keys[pygame.K_DOWN] and y < 500 - height -5:
            #y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount <0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()
pygame.quit()