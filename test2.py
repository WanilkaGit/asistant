from pygame import * # Імпортуємо бібліотеку pygame для того щоб наша гра працювала

level1 = [
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "rr    °  °      l                             r    °  °  °     l     .",
    "r  ------------                                ---------------       .",
    "rr / l                                       r / l         r / l     .",
    "rr   l                                       r   l         r   l     .",
    "rr     °  l                       r     °  °     l   r         l     .",
    "r  ------                           ------------       -------       .",
    "r     r / l                                          r / l           .",
    "r     r   l                                          r   l           .",
    "r     r       °  °   l                       r   °  °    l           .",
    "r       ------------                           ---------             .",
    "r                r / l                       r / l                   .",
    "r                r   l                       r   l                   .",
    "r                                                                    .",
    "----------------------------------------------------------------------"]

level1_width = len(level1[0]) * 40 # Задаємо ширину нашій грі у вигляді пікселів.
level1_height = len(level1) * 40 # Задаємо висоту нашій грі у вигляді пікселів.

W = 1280 # Змінна з значенням ширини екрану
H = 720 # Змінна з значенням висоти екрану

window = display.set_mode((W, H)) # Встановлюємо розміри екрану (вікну)
back = transform.scale(image.load('images/bg_sc.jpg'), (W, H)) # Встановлюємо фон грі
display.set_caption('Blockada') # Встановлюємо навзву екрану (вікну)
display.set_icon(image.load("images/portal.png")) # Встановлюємо іконку грі (вікну)

hero_r = "images/image_sr.png" # Лівий вид песронажа (його картинка)
hero_l = "images/image_sl_l.png" # Правий вид песронажа (його картинка)

enemy_l = "images/cyborg.png" # Лівий вид ворога (його картинка)
enemy_r = "images/cyborg_r.png" # Правий вид ворога (його картинка)

coin_img = "images/pngegg.png" # Змінна з картинкою монети
door_img = "images/door.png" # Змінна з картинкою двері
key_img = "images/key.png" # Змінна з картинкою ключа
chest_open = "images/cst_open.png" # Змінна з картинкою відкритого сундука
chest_close = "images/chest_1.png" # Змінна з картинкою закритого сундука
stairs = "images/stair.png" # Змінна з картинкою лісницьою
portal_img = "images/portal.png" # Змінна з картинкою портала
platform = "images/platform_1.png" # Змінна з картинкою платформи
power = "images/mana.png" # Змінна з картинкою сили
nothing = "images/nothing.png" # Змінна з картинкою "нічого"

font.init()
font2 = font.SysFont(('font/calibrib.ttf'), 60)
e_tap = font2.render('press (e)', True, (255, 0, 255))
k_need = font2.render('You need a key to open!', True, (255, 0, 255))
space = font2.render('press (space) to kill the enemy', True, (255, 0, 255))

class Setting(sprite.Sprite): # Класс з оновними значеннями гри (налаштування)
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Setting): # Класс з створенням гравця
    def r_l(self):
        global mana
        key_pressed = key.get_pressed()
        if key_pressed[K_a]:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))
            mana.side = "left"
        if key_pressed[K_d]:
            self.rect.x += self.speed
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
            mana.side = 'right'

    def u_d(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed

class Enemy(Setting): # Класс з створенням ворога
    def __init__(self, x, y, width, height, speed, img, side):
        Setting.__init__(self, x, y, width, height, speed, img)
        self.side = side

    def update(self):
        global side
        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed
            

class Mana(Enemy):
    pass

mana = Mana(0, -100, 25, 25, 15, power, 'left')

class Camera(object): # Класс для створенная функцій камері, яка наблюдає за гравцем
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2
    
    l = min(0, l)  # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t)  # Не виходимо за нижню межу
    t = min(0, t)  # Не виходимо за верхню межу
    
    return Rect(l, t, w, h)

def collides():
    global open_ch, open_d, coins_score, coin_img
    key_pressed = key.get_pressed()
    for s in stairs_lst:
        if sprite.collide_rect(hero, s):
            hero.u_d()
            if hero.rect.y < s.rect.y - 40:
                hero.rect.y = s.rect.y - 40
            if hero.rect.y > s.rect.y + 130:
                hero.rect.y = s.rect.y + 130
    for l in block_l:
        if sprite.spritecollide(l, manas, True):
            items.remove(mana)
            manas.remove()
        if sprite.collide_rect(hero, l):
            hero.rect.x = hero.rect.x - hero.width
        if sprite.collide_rect(en1, l):
            en1.side = 'left'
            en1.image = transform.scale(image.load(enemy_r), (en1.width, en1.height))
        if sprite.collide_rect(en2, l):
            en2.side = 'left'
            en2.image = transform.scale(image.load(enemy_r), (en2.width, en2.height))
        if sprite.collide_rect(en3, l):
            en3.side = 'left'
            en3.image = transform.scale(image.load(enemy_r), (en3.width, en3.height))
        if sprite.collide_rect(en4, l):
            en4.side = 'left'
            en4.image = transform.scale(image.load(enemy_r), (en4.width, en4.height))
        if sprite.collide_rect(en5, l):
            en5.side = 'left'
            en5.image = transform.scale(image.load(enemy_r), (en5.width, en5.height))
        if sprite.collide_rect(en6, l):
            en6.side = 'left'
            en6.image = transform.scale(image.load(enemy_r), (en6.width, en6.height))
        if sprite.collide_rect(en7, l):
            en7.side = 'left'
            en7.image = transform.scale(image.load(enemy_r), (en7.width, en7.height))
        if sprite.collide_rect(en8, l):
            en8.side = 'left'
            en8.image = transform.scale(image.load(enemy_r), (en8.width, en8.height))
        if sprite.collide_rect(en9, l):
            en9.side = 'left'
            en9.image = transform.scale(image.load(enemy_r), (en9.width, en9.height))
        if sprite.collide_rect(en10, l):
            en10.side = 'left'
            en10.image = transform.scale(image.load(enemy_r), (en10.width, en10.height))

    for r in block_r:
        if sprite.spritecollide(r, manas, True):
            items.remove(mana)
            manas.remove()
        if sprite.collide_rect(hero, r):
            hero.rect.x = hero.rect.x + hero.width
        if sprite.collide_rect(en1, r):
            en1.side = 'right'
            en1.image = transform.scale(image.load(enemy_l), (en1.width, en1.height))
        if sprite.collide_rect(en2, r):
            en2.side = 'right'
            en2.image = transform.scale(image.load(enemy_l), (en2.width, en2.height))
        if sprite.collide_rect(en3, r):
            en3.side = 'right'
            en3.image = transform.scale(image.load(enemy_l), (en3.width, en3.height))
        if sprite.collide_rect(en4, r):
            en4.side = 'right'
            en4.image = transform.scale(image.load(enemy_l), (en4.width, en4.height))
        if sprite.collide_rect(en5, r):
            en5.side = 'right'
            en5.image = transform.scale(image.load(enemy_l), (en5.width, en5.height))
        if sprite.collide_rect(en6, r):
            en6.side = 'right'
            en6.image = transform.scale(image.load(enemy_l), (en6.width, en6.height))
        if sprite.collide_rect(en7, r):
            en7.side = 'right'
            en7.image = transform.scale(image.load(enemy_l), (en7.width, en7.height))
        if sprite.collide_rect(en8, r):
            en8.side = 'right'
            en8.image = transform.scale(image.load(enemy_l), (en8.width, en8.height))
        if sprite.collide_rect(en9, r):
            en9.side = 'right'
            en9.image = transform.scale(image.load(enemy_l), (en9.width, en9.height))
        if sprite.collide_rect(en10, r):
            en10.side = 'right'
            en10.image = transform.scale(image.load(enemy_l), (en10.width, en10.height))
    if sprite.collide_rect(hero, key1):
        window.blit(e_tap, (500, 50))
        if key_pressed[K_e]:
            items.remove(key1)
            key1.rect.y = -100
            open_ch = True


    if sprite.collide_rect(hero, chest) and open_ch == False:
        window.blit(k_need, (450, 50))
        
    if sprite.collide_rect(hero, chest) and open_ch == True:
        window.blit(e_tap, (500, 50))
        if key_pressed[K_e]:
            chest.image = transform.scale(image.load(chest_open), (chest.width, chest.height))
            open_d = True

    if sprite.collide_rect(hero, door) and open_d == False:
        hero.rect.x = door.rect.x - hero.width
        window.blit(k_need, (450, 50))
        
    if sprite.collide_rect(hero, door) and open_d == True:
        hero.rect.x = door.rect.x - hero.width
        window.blit(e_tap, (450, 50))
        if key_pressed[K_e]:
            door.rect.x = -200

    for coin in coins:
        if sprite.collide_rect(hero, coin):
            coins_score += 1
            coins.remove(coin)
            items.remove(coin)

    if sprite.collide_rect(hero, en1):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en2):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en3):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en4):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en5):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en6):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en7):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en8):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en9):
        hero.rect.x = 300
        hero.rect.y = 650
    
    if sprite.collide_rect(hero, en10):
        hero.rect.x = 300
        hero.rect.y = 650

    if sprite.collide_rect(hero, portal):
        quit()

coins_score = 0
font1 = font.SysFont('bold', 55)

def menu():
    pass

def rules():
    pass

def pause():
    pass

def restart(self):
    window.blit(self.image, (self.rect.x, self.rect.y))

def start_pos(): # Функція стартової позиції
    global items, camera, hero, stairs_lst, block_r, block_l, coins, plat, en1, en2, en3, en4, en5, en6, en7, en8, en9, en10
    global key1, key2, door, chest, open_ch, open_d, coins_score, manas, portal
    hero = Player(300, 650, 70, 70, 10, hero_l)
    camera = Camera(camera_config, level1_width, level1_height)
    items = sprite.Group()
    manas = sprite.Group()

    key1 = Setting(190, 350, 80, 30, 5, key_img)
    chest = Setting(500, 150, 100, 100, 5, chest_close)
    door = Setting(1100, 590, 70, 120, 5, door_img)
    portal = Setting(2700, 600, 100, 100, 0, portal_img)

    en1 = Enemy(135, 335, 55, 55, 5, enemy_l, 'right')

    en2 = Enemy(350, 490, 55, 55, 5, enemy_l, 'right')
    en3 = Enemy(700, 490, 55, 55, 5, enemy_r, 'left')

    en4 = Enemy(2120, 490, 55, 55, 5, enemy_r, 'left')
    en5 = Enemy(1900, 490, 55, 55, 5, enemy_l, 'right')

    en6 = Enemy(2400, 340, 55, 55, 5, enemy_r, 'left')

    en7 = Enemy(2400, 180, 55, 55, 5, enemy_r, 'left')
    en8 = Enemy(1900, 170, 55, 55, 5, enemy_l, 'right')

    en9 = Enemy(1830, 330, 55, 55, 5, enemy_r, 'left')
    en10 = Enemy(1450, 330, 55, 55, 5, enemy_l, 'right')

    open_d = False
    open_ch = False

    block_r = []
    block_l = []
    plat = []
    coins = []
    stairs_lst = []

    x = 0
    y = 0
    for r in level1:
        for c in r:
            if c == "-":
                p1 = Setting(x, y - 30, 120, 120, 0, platform)
                plat.append(p1)
                items.add(p1)
            if c == 'l':
                p2 = Setting(x, y, 40, 40, 0, nothing)
                block_l.append(p2)
                items.add(p2)
            if c == 'r':
                p3 = Setting(x, y, 40, 40, 0, nothing)
                block_r.append(p3)
                items.add(p3)
            if c == '°':
                p4 = Setting(x, y, 40, 40, 0, coin_img)
                coins.append(p4)
                items.add(p4)
            if c == '/':
                p5 = Setting(x + 20, y - 50, 40, 180, 0, stairs)
                stairs_lst.append(p5)
                items.add(p5)
            x += 40
        y += 40
        x = 0
    items.add(hero)
    items.add(door)
    items.add(key1)
    items.add(chest)
    items.add(portal)
    
    items.add(en1)
    items.add(en2)
    items.add(en3)
    items.add(en4)
    items.add(en5)
    items.add(en6)
    items.add(en7)
    items.add(en8)
    items.add(en9)
    items.add(en10)

def lvl1():
    game = True # Зміння зі значенням True (правдиве значення яке робить так, щоб гра працювала).
    while game:
        time.delay(50)
        window.blit(back, (0, 0))
        for e in event.get():
            if e.type == QUIT:
                game = False
        hero.r_l()

        en1.update()
        en2.update()
        en3.update()
        en4.update()
        en5.update()
        en6.update()
        en7.update()
        en8.update()
        en9.update()
        en10.update()

        mana.update()

        camera.update(hero)
        collides()
        for i in items:
            window.blit(i.image, camera.apply(i))

        score = font1.render('Зібрано монет: ' + str(coins_score), 1, (255, 255, 0)) # Створюємо текст для пропущенних ворогів
        window.blit(score, (10, 20)) # Відмальовуємо текст з пропущенними ворогами, який ми вже створили раніше.

        key_pressed = key.get_pressed()

        if key_pressed[K_SPACE]:
            mana.rect.x = hero.rect.centerx
            mana.rect.y = hero.rect.top
            items.add(mana)
            manas.add(mana)

        if sprite.spritecollide(en1, manas, True):
            items.remove(mana)
            en1.rect.y = -200
            items.remove(en1)

        if sprite.spritecollide(en2, manas, True):
            items.remove(mana)
            en2.rect.y = -200
            items.remove(en2)

        if sprite.spritecollide(en3, manas, True):
            items.remove(mana)
            en3.rect.y = -200
            items.remove(en3)

        if sprite.spritecollide(en4, manas, True):
            items.remove(mana)
            en4.rect.y = -200
            items.remove(en4)

        if sprite.spritecollide(en5, manas, True):
            items.remyove(mana)
            en5.rect.y = -200
            items.remove(en5)

        if sprite.spritecollide(en6, manas, True):
            items.remove(mana)
            en6.rect.y = -200
            items.remove(en6)
    
        if sprite.spritecollide(en7, manas, True):
            items.remove(mana)
            en7.rect.y = -200
            items.remove(en7)
        
        if sprite.spritecollide(en8, manas, True):
            items.remove(mana)
            en8.rect.y = -200
            items.remove(en8)

        if sprite.spritecollide(en9, manas, True):
            items.remove(mana)
            en9.rect.y = -200
            items.remove(en9)

        if sprite.spritecollide(en10, manas, True):
            items.remove(mana)
            en10.rect.y = -200
            items.remove(en10)

        display.update() # Оновлюємо екран.

def lvl1_end():
    pass

start_pos() # Викликаємо функцію
lvl1() # Викликаємо функцію для працювання гри.