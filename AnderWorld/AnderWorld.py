import pygame
pygame.init()
back = (35, 20, 30)
mw = pygame.display.set_mode((1555, 802))
mw.fill(back)
clock = pygame.time.Clock()
dx = 3
dy = 3
fire=0
move_right = False
move_left = False
game_over = False
click_x=0
click_y=0
attack=0
step_knight=0
step_archer=0
step_assasin=0
step_tank=0
start=0

knight_attack=0
archer_attack=0
assasin_attack=0
tank_attack=0
mag_attack=0

step_mag=0
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        font = pygame.font.SysFont('verdana', fsize)
        lines = text.split('\n')  # Разделяем текст на строки
        self.images = []  # Список изображений для каждой строки
        self.text_height = 0  # Высота текста
        for line in lines:
            image = font.render(line, True, text_color)
            self.images.append(image)
            self.text_height += image.get_height()  # Увеличиваем высоту текста
    def draw(self, shift_x=0, shift_y=0):
        y_offset = 0
        for image in self.images:
            mw.blit(image, (self.rect.x + shift_x, self.rect.y + shift_y + y_offset))
            y_offset += image.get_height()
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image , (self.rect.x, self.rect.y))


class Hero(Picture):
    def __init__(self,filename,x=0,y=0,width=10,height=10, name=0, health=0, armor=0, power=0, weapon=0, name_weapon=0):
        Picture.__init__(self,filename, x=x, y=y, width=width, height=height)
        self.x=x
        self.y=y
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.name_weapon = name_weapon
        self.image = pygame.image.load(filename)
    def draw_health_bar(self, screen):
        health_bar_width = self.rect.width * (self.health / 100)
        pygame.draw.rect(screen, (0, 255, 0),(self.rect.x, self.rect.y - 10, health_bar_width, 5))
        health_bar_width = self.rect.width * (self.armor / 100)
        pygame.draw.rect(screen, (100, 100, 100), (self.rect.x, self.rect.y - 5, health_bar_width, 5))
        font = pygame.font.SysFont('arial', 12)
        text_surface = font.render(str(self.health), True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x, self.rect.y - 25))

    def draw_health_bar_drakon(self, screen):
        health_bar_width_drakon = self.rect.width * (self.health / 1500)
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x+100, self.rect.y +700, health_bar_width_drakon, 50))
        font = pygame.font.SysFont('arial', 40)
        text_surface = font.render(f'Health: {self.health}', True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x+100, self.rect.y + 700))
    def draw_helth_bar_dragon_hp(self, screen):
        health_bar_width_drakon = self.rect.width * (self.health / 1000)
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x+100, self.rect.y +700, health_bar_width_drakon, 50))
        font = pygame.font.SysFont('arial', 40)
        text_surface = font.render(f'Health: {self.health}', True, (220, 0, 0))
        screen.blit(text_surface, (self.rect.x+100, self.rect.y + 700))


knight = Hero("knight.png",10,30,100,50,'Річард', 60, 40, 25, "Меч", '"Винищувач драконів"')
archer = Hero("archer.png",10,180,100,50,'Бард', 40, 10, 40, "Лук", '"Тінь пращурів"')
assasin = Hero("assasin.png",10,330,100,50,"Тінь", 35, 5, 15, "Кинжал", '"Срібний клик"')
tank = Hero("gnom.png",10,480,100,50,"Брут", 80, 80, 5, "Сокира", '"Сокира вікінга"')
mag = Hero("mag.png",10,630,100,50,"Мерлін", 50, 5, 35, "Магічний посох", '')
drakon = Hero("drakon.png",650,-110,500,500,'Смогг',1500,0,40,'','')

drakon_start = Hero("drakon_start.png", 650, -110, 500, 500, 'Смогг', 1000, 0, 50, '', '')
knight_start = Hero("knight_start.png", 0, 200, 100, 50, 'Річард', 70, 30, 25, "Меч", '"Винищувач драконів"')
mag_start = Hero("mag_start.png", 0, 200, 100, 50, "Мерлін", 50, 25, 35, "Магічний посох", '')
tank_start = Hero("gnom_start.png", 20, 200, 100, 50, "Брут", 100, 70, 5, "Сокира", '"Сокира вікінга"')
fon_start = Hero("fon.png",0,0,1555,802,'',0,0,0,'','')
fon_defeat = Hero("fon_defeat.png",0,0,155,802,'',0,0,0,'','')
knight_phrase = Label(320,100,1000,1000,back)
knight_phrase.set_text("Смогг зруйнував багато сіл та міст\nі продовжує бути\nзагрозою для\nсусідніх поселень!\nМи повинні його здолати!",50,((250,220,10)))
mag_phrase = Label(320,100,1000,1000,back)
mag_phrase.set_text("Для початку потрібно\nпознайомитись та розібрати\nтактику бою.",50,((200,100,0)))
tank_phrase = Label(420,100,1000,1000,back)
tank_phrase.set_text("Немає часу, дракон\nвже наближається!\nПознайомимось в битві.\nМене звати Брут, я\n буду вас захищати!",50,((100,100,0)))
spase = Label(600,750,10,100,back)
spase.set_text("Натисніть пробіл для продовження",20,((200,200,200)))
spase_start = Label(600,750,10,100,back)
spase_start.set_text("Натисніть пробіл для початку",20,((200,200,200)))
game_name = Label(600,100,10,100,back)
game_name.set_text("AnderWorld",50,((200,0,0)))
loading = Label(700,400,50,100,back)
loading.set_text("loading...",30,((10,10,10)))
system =Hero("system.png",50,250,100,100,'',0,0,0,'','')
system_phrase = Label(420,100,1000,1000,back)
system_phrase.set_text("Ви - відважна команда героїв.\nВаша мета - здолати дракона\nта принести мир в цей світ!",50,((100,0,0)))
knight_info = Label(15,30,100,50,back)
knight_info.set_text("Ім'я: "+knight.name+"\nСила атаки: "+str(knight.power)+"\n"+knight.weapon+":\n"+knight.name_weapon+"\nОсобливість:\nКоли Річард втрачає\nздоров'я всі союзники\nотримують додаткові 5 броні!\nБез броні Річард сильніший!",10,((250,220,10)))
archer_info = Label(15,180,100,50,back)
archer_info.set_text("Ім'я: "+archer.name+"\nСила атаки: "+str(archer.power)+"\n"+archer.weapon+":\n"+archer.name_weapon+"\nОсобливість:\nПовністю блокує\nпершу отриману\nатаку!\nТакож лучник\nотримує менше пошкоджень.",10,((10,110,10)))
assasin_info = Label(15,330,100,50,back)
assasin_info.set_text("Ім'я: "+assasin.name+"\nСила атаки: "+str(assasin.power)+"\n"+assasin.weapon+":\n"+assasin.name_weapon+"\nОсобливість:\nЯкщо у ворога 100\nі менше здоров'я\nТінь закінчує бій\nоднією атакою!",10,((0,0,0)))
tank_info = Label(15,480,100,50,back)
tank_info.set_text("Ім'я: "+tank.name+"\nСила атаки: "+str(tank.power)+"\n"+tank.weapon+":\n"+tank.name_weapon+"\nОсобливість:\nЯкщо атака ворога вб'є\nсоюзника Брут захистить\nйого та візьме удар на себе!\nТаким чином врятувати Брут може\nлише тричі!",10,((100,100,0)))
mag_info = Label(15,600,100,50,back)
mag_info.set_text("Ім'я: "+mag.name+"\nСила атаки: "+str(mag.power)+"\n"+mag.weapon+"\nОсобливість:\nОдин раз Мерлін\nможе воскресити\nполеглого союзника!",10,((200,100,0)))

game_defeat = Label(700,500,100,100,back)
game_defeat.set_text("game over\n  DEFEAT",50,((200,0,0)))
game_victory = Label(660,400,100,100,back)
game_victory.set_text("VICTORY",50,((250,220,10)))

drakon_fire = Hero("dragon_fire.png",390,340,500,500,'',0,0,0,'','')
fire_ball = Hero ("fire_ball_2.png",500,430,200,200,'',0,0,0,'',',')
arrow = Hero("arrow.png",500,430,200,200,'',0,0,0,'',',')

knight_K = Label(15,70,10,10,back)
knight_K.set_text("K",20,((200,200,200)))
archer_A = Label(15,200,10,10,back)
archer_A.set_text("A",20,((200,200,200)))
assasin_S = Label(15,330,10,10,back)
assasin_S.set_text("S",20,((200,200,200)))
tank_T = Label(15,550,10,10,back)
tank_T.set_text("T",20,((200,200,200)))
mag_M = Label(15,630,10,10,back)
mag_M.set_text("M",20,((200,200,200)))

knight_super=0
archer_super=0
mag_super=0
tank_super=0

star_1 = Hero("star_1.png",750,200,60,60,'',0,0,0,'','')
star_2 = Hero("star.png",700,250,50,50,'',0,0,0,'','')
star_3 = Hero("star.png",800,250,50,50,'',0,0,0,'','')
star_4 = Hero("star.png",650,250,50,50,'',0,0,0,'','')
star_5 = Hero("star.png",850,250,50,50,'',0,0,0,'','')



knight_death=0
archer_death=0
assasin_death=0
tank_death=0
mag_death=0

while not game_over:
    mw.fill(back)
    death=knight_death+archer_death+assasin_death+tank_death+mag_death
    if start==0:
        fon_start.draw()
        game_name.draw()
        spase_start.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mw.fill((150,150,150))
                    loading.draw()
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    start=1
    elif start==1:
        knight_start.draw()
        knight_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=2
    elif start==2:
        mag_start.draw()
        mag_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=3
    elif start==3:
        tank_start.draw()
        tank_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=4
    elif start==4:
        system.draw()
        system_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=5
    elif start==5:
        system.draw()
        system_phrase.set_text("Натиснувши на клавішу героя\nВи отримаєте змогу ознайомитись\nз його характеристиками.\nЦе допоможе в складанні плану битви!",50,((100,0,0)))
        system_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=6
    elif start==6:
        system.draw()
        system_phrase.set_text("Поки дракон накопичує сил для атаки,\nВи встигнете нанести йому три удари.\nПісля цього дракон атакує воїнa,\nякий стоїть найближче.\nБудьте обережні!",50,((100,0,0)))
        system_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=7
    elif start==7:
        system.draw()
        system_phrase.set_text("І останнє.\nНе дайте дракону вбити союзників.\nКраще покинути бій,\nпридумати кращий план\nта повернутись знову,\nаніж просто загинути!\nУдачі Вам!",50,((100,0,0)))
        system_phrase.draw()
        spase.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start=8
    elif start==8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:# кінець гри на "p"
                    game_over= True
                if attack < 3:
                    if knight.health>0:
                        if event.key == pygame.K_k:# вибір лицаря
                            if step_knight==1:
                                if knight_attack == 0 or death>=3:
                                    knight.rect.x=700
                                    knight.rect.y=430
                                    drakon.health-=knight.power
                                    attack+=1
                                    step_knight=2
                                    knight_attack=1
                            if step_knight==0:
                                knight.rect.x+=100
                                knight.rect.y=30
                                assasin.rect.x=10
                                assasin.rect.y = 330
                                archer.rect.x=10
                                archer.rect.y = 180
                                mag.rect.x=10
                                mag.rect.y = 630
                                tank.rect.x=10
                                tank.rect.y = 480
                                step_knight+=1
                                step_archer=0
                                step_tank=0
                                step_assasin=0
                                step_mag=0
                    elif knight.health<=0:
                        if mag_super==0:
                            knight.health=55
                            mag_super=1
                        elif mag_super==1:
                            knight.health=0
                            knight_death=1
                    if archer.health>0:
                        if event.key == pygame.K_a:# вибір лучника
                            if step_archer==1:
                                if archer_attack==0 or death>=3:
                                    archer.rect.x=200
                                    archer.rect.y=430
                                    arrow.rect.x = 300
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    arrow.rect.x += 100
                                    mw.fill(back)
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    arrow.rect.x += 100
                                    mw.fill(back)
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    arrow.rect.x += 100
                                    mw.fill(back)
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    arrow.rect.x += 100
                                    mw.fill(back)
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    arrow.rect.x += 100
                                    mw.fill(back)
                                    arrow.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    drakon.health-=archer.power
                                    attack+=1
                                    step_archer=2
                                    archer_attack=1
                            if step_archer==0:
                                archer.rect.x+=100
                                knight.rect.y = 30
                                assasin.rect.x = 10
                                assasin.rect.y = 330
                                knight.rect.x = 10
                                archer.rect.y = 180
                                mag.rect.x = 10
                                mag.rect.y = 630
                                tank.rect.x = 10
                                tank.rect.y = 480
                                step_archer+=1
                                step_knight = 0
                                step_tank = 0
                                step_assasin = 0
                                step_mag = 0
                    elif archer.health<=0:
                        if mag_super==0:
                            archer.health=55
                            mag_super=1
                        elif mag_super==1:
                            archer.health=0
                            archer_death=1
                    if assasin.health>0:
                        if event.key == pygame.K_s:# вибір вбивці
                            if step_assasin==1:
                                if drakon.health<=100:
                                    if assasin_attack == 0 or death >= 3:
                                        assasin.rect.x = 700
                                        assasin.rect.y = 430
                                        drakon.health=0
                                elif drakon.health>100:
                                    if assasin_attack==0 or death>=3:
                                        assasin.rect.x=700
                                        assasin.rect.y=430
                                        drakon.health-=assasin.power
                                        attack+=1
                                        step_assasin=2
                                        assasin_attack=1
                            if step_assasin==0:
                                assasin.rect.x+=100
                                knight.rect.y = 30
                                knight.rect.x = 10
                                assasin.rect.y = 330
                                archer.rect.x = 10
                                archer.rect.y = 180
                                mag.rect.x = 10
                                mag.rect.y = 630
                                tank.rect.x = 10
                                tank.rect.y = 480
                                step_assasin+=1
                                step_knight = 0
                                step_archer = 0
                                step_tank = 0
                                step_mag = 0
                    elif assasin.health<=0:
                        if mag_super==0:
                            assasin.health=55
                            mag_super=1
                        elif mag_super==1:
                            assasin.health=0
                            assasin_death=1
                    if tank.health>0:
                        if event.key == pygame.K_t:# вибір танка
                            if step_tank==1:
                                if tank_attack==0 or death>=3:
                                    tank.rect.x=700
                                    tank.rect.y=430
                                    drakon.health-=tank.power
                                    attack+=1
                                    step_tank=2
                                    tank_attack=1
                            if step_tank==0:
                                tank.rect.x+=100
                                knight.rect.y = 30
                                assasin.rect.x = 10
                                assasin.rect.y = 330
                                archer.rect.x = 10
                                archer.rect.y = 180
                                mag.rect.x = 10
                                mag.rect.y = 630
                                knight.rect.x = 10
                                tank.rect.y = 480
                                step_tank+=1
                                step_knight = 0
                                step_archer = 0
                                step_assasin = 0
                                step_mag = 0
                    elif tank.health<=0:
                        if mag_super==0:
                            tank.health=55
                            mag_super=1
                        elif mag_super==1:
                            tank.health=0
                            tank_super=3
                            tank_death=1
                    if mag.health>0:
                        if event.key == pygame.K_m:# вибір мага
                            if step_mag==1:
                                if mag_attack==0 or death:
                                    mag.rect.x=500
                                    mag.rect.y=430
                                    fire_ball.rect.x=500
                                    fire_ball.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    fire_ball.rect.x+=100
                                    mw.fill(back)
                                    fire_ball.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    fire_ball.rect.x += 100
                                    mw.fill(back)
                                    fire_ball.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    fire_ball.rect.x += 100
                                    mw.fill(back)
                                    fire_ball.draw()
                                    if knight.health > 0:
                                        knight.draw()
                                        knight.draw_health_bar(mw)
                                        if step_knight == 0:
                                            knight_K.draw()
                                    if archer.health > 0:
                                        archer.draw()
                                        archer.draw_health_bar(mw)
                                        if step_archer == 0:
                                            archer_A.draw()
                                    if assasin.health > 0:
                                        assasin.draw()
                                        assasin.draw_health_bar(mw)
                                        if step_assasin == 0:
                                            assasin_S.draw()
                                    if tank.health > 0:
                                        tank.draw()
                                        tank.draw_health_bar(mw)
                                        if step_tank == 0:
                                            tank_T.draw()
                                    if mag.health > 0:
                                        mag.draw()
                                        mag.draw_health_bar(mw)
                                        if step_mag == 0:
                                            mag_M.draw()
                                    drakon.draw()
                                    if step_knight == 1:
                                        knight_info.draw()
                                    if step_archer == 1:
                                        archer_info.draw()
                                    if step_assasin == 1:
                                        assasin_info.draw()
                                    if step_tank == 1:
                                        tank_info.draw()
                                    if step_mag == 1:
                                        mag_info.draw()
                                    if drakon.health >= 150:
                                        drakon.draw_health_bar_drakon(mw)
                                    else:
                                        drakon.draw_helth_bar_dragon_hp(mw)
                                    pygame.display.flip()
                                    pygame.time.delay(100)
                                    drakon.health-=mag.power
                                    attack+=1
                                    step_mag=2
                                mag_attack=1
                            if step_mag==0:
                                mag.rect.x+=100
                                knight.rect.x=10
                                knight.rect.y = 30
                                assasin.rect.x = 10
                                assasin.rect.y = 330
                                archer.rect.x = 10
                                archer.rect.y = 180
                                mag.rect.y = 630
                                tank.rect.x = 10
                                tank.rect.y = 480
                                step_mag+=1
                                step_knight = 0
                                step_archer = 0
                                step_tank = 0
                                step_assasin = 0
                    elif mag.health<=0:
                        mag.health=0
                        mag_super=1
                        mag_death=1
                    if event.key == pygame.K_SPACE:
                        knight.rect.x = 10
                        knight.rect.y = 30
                        assasin.rect.x = 10
                        assasin.rect.y = 330
                        archer.rect.x = 10
                        archer.rect.y = 180
                        mag.rect.x = 10
                        mag.rect.y = 630
                        tank.rect.x = 10
                        tank.rect.y = 480
                        step_mag = 0
                        step_knight = 0
                        step_archer = 0
                        step_tank = 0
                        step_assasin = 0
                    if attack==3:
                        knight_attack=0
                        archer_attack=0
                        assasin_attack=0
                        tank_attack=0
                        mag_attack=0
                        if step_knight==2:
                            if knight.armor + knight.health < drakon.power and tank_super < 3:
                                step_knight = 0
                                knight.rect.x = 10
                                knight.rect.y = 30
                                step_tank = 2
                                tank.rect.x = 700
                                tank.rect.y = 430
                                tank_super+=1
                                if tank.armor == 0:
                                    tank.health -= drakon.power
                                    attack = 0
                                elif tank.armor > 0:
                                    tank.armor -= drakon.power
                                    attack = 0
                                    if tank.armor < 0:
                                        tank.health += tank.armor
                                        tank.armor = 0
                            elif knight.armor>0:
                                knight.armor-=drakon.power
                                attack=0
                                archer.armor += 5
                                assasin.armor += 5
                                tank.armor += 5
                                mag.armor += 5
                                if knight.armor<=0:
                                    knight.health+=knight.armor
                                    knight.armor=0
                                    if knight_super==0:
                                        knight.power+=10
                                        knight_super=1
                            elif knight.armor==0:
                                knight.health-=drakon.power
                                archer.armor += 5
                                assasin.armor += 5
                                tank.armor += 5
                                mag.armor += 5
                                attack=0
                        elif step_archer==2:
                            if archer.armor + archer.health < drakon.power and tank_super < 3:
                                step_archer = 0
                                archer.rect.x = 10
                                archer.rect.y = 180
                                step_tank = 2
                                tank.rect.x = 700
                                tank.rect.y = 430
                                tank_super+=1
                                if tank.armor == 0:
                                    tank.health -= drakon.power
                                    attack = 0
                                elif tank.armor > 0:
                                    tank.armor -= drakon.power
                                    attack = 0
                                    if tank.armor < 0:
                                        tank.health += tank.armor
                                        tank.armor = 0
                            elif archer_super==0:
                                archer_super=1
                                attack=0
                            elif archer_super==1:
                                if archer.armor==0:
                                    archer.health-=drakon.power
                                    archer.health+=20
                                    attack=0
                                elif archer.armor>0:
                                    archer.armor-=drakon.power
                                    archer.armor+=20
                                    attack=0
                                    if archer.armor<0:
                                        archer.health+=archer.armor
                                        archer.armor=0
                        elif step_assasin==2:
                            if assasin.armor + assasin.health < drakon.power and tank_super < 3:
                                step_assasin = 0
                                assasin.rect.x = 10
                                assasin.rect.y = 330
                                step_tank = 2
                                tank.rect.x = 700
                                tank.rect.y = 430
                                tank_super+=1
                                if tank.armor == 0:
                                    tank.health -= drakon.power
                                    attack = 0
                                elif tank.armor > 0:
                                    tank.armor -= drakon.power
                                    attack = 0
                                    if tank.armor < 0:
                                        tank.health += tank.armor
                                        tank.armor = 0
                            elif assasin.armor==0:
                                assasin.health-=drakon.power
                                attack=0
                            elif assasin.armor>0:
                                assasin.armor-=drakon.power
                                attack=0
                                if assasin.armor<0:
                                    assasin.health+=assasin.armor
                                    assasin.armor=0
                        elif step_tank==2:
                            if tank.armor==0:
                                tank.health-=drakon.power
                                attack=0
                            elif tank.armor>0:
                                tank.armor-=drakon.power
                                attack=0
                                if tank.armor<0:
                                    tank.health+=tank.armor
                                    tank.armor=0
                        elif step_mag==2:
                            if mag.armor + mag.health < drakon.power and tank_super < 3:
                                step_mag = 0
                                mag.rect.x = 10
                                mag.rect.y = 630
                                step_tank = 2
                                tank.rect.x = 700
                                tank.rect.y = 430
                                tank_super+=1
                                if tank.armor == 0:
                                    tank.health -= drakon.power
                                    attack = 0
                                elif tank.armor > 0:
                                    tank.armor -= drakon.power
                                    attack = 0
                                    if tank.armor < 0:
                                        tank.health += tank.armor
                                        tank.armor = 0
                            elif mag.armor==0:
                                mag.health-=drakon.power
                                attack=0
                            elif mag.armor>0:
                                mag.armor-=drakon.power
                                attack=0
                                if mag.armor<0:
                                    mag.health+=mag.armor
                                    mag.armor=0
                        mw.fill(back)
                        drakon_fire.draw()
                        if knight.health > 0:
                            knight.draw()
                            knight.draw_health_bar(mw)
                            if step_knight == 0:
                                knight_K.draw()
                        if archer.health > 0:
                            archer.draw()
                            archer.draw_health_bar(mw)
                            if step_archer == 0:
                                archer_A.draw()
                        if assasin.health > 0:
                            assasin.draw()
                            assasin.draw_health_bar(mw)
                            if step_assasin == 0:
                                assasin_S.draw()
                        if tank.health > 0:
                            tank.draw()
                            tank.draw_health_bar(mw)
                            if step_tank == 0:
                                tank_T.draw()
                        if mag.health > 0:
                            mag.draw()
                            mag.draw_health_bar(mw)
                            if step_mag == 0:
                                mag_M.draw()
                        drakon.draw()
                        if step_knight == 1:
                            knight_info.draw()
                        if step_archer == 1:
                            archer_info.draw()
                        if step_assasin == 1:
                            assasin_info.draw()
                        if step_tank == 1:
                            tank_info.draw()
                        if step_mag == 1:
                            mag_info.draw()
                        if drakon.health >= 150:
                            drakon.draw_health_bar_drakon(mw)
                        else:
                            drakon.draw_helth_bar_dragon_hp(mw)
                        pygame.display.flip()
                        pygame.time.delay(1000)
        if knight.health>0:
            knight.draw()
            knight.draw_health_bar(mw)
            if step_knight==0:
                knight_K.draw()
        if archer.health>0:
            archer.draw()
            archer.draw_health_bar(mw)
            if step_archer==0:
                archer_A.draw()
        if assasin.health>0:
            assasin.draw()
            assasin.draw_health_bar(mw)
            if step_assasin==0:
                assasin_S.draw()
        if tank.health>0:
            tank.draw()
            tank.draw_health_bar(mw)
            if step_tank==0:
                tank_T.draw()
        if mag.health>0:
            mag.draw()
            mag.draw_health_bar(mw)
            if step_mag==0:
                mag_M.draw()
        if drakon.health>0:
            drakon.draw()
        elif drakon.health<=0:
            back=(0,0,50)
            mw.fill(back)
            game_victory.draw()
            if death==4:
                star_1.draw()
            elif death==3:
                star_1.draw()
                star_2.draw()
            elif death==2:
                star_1.draw()
                star_2.draw()
                star_3.draw()
            elif death==1:
                star_1.draw()
                star_2.draw()
                star_3.draw()
                star_4.draw()
            elif death==0:
                star_1.draw()
                star_2.draw()
                star_3.draw()
                star_4.draw()
                star_5.draw()
            pygame.display.flip()
            pygame.time.delay(5000)
            game_over=True
        if step_knight==1:
            knight_info.draw()
        if step_archer==1:
            archer_info.draw()
        if step_assasin==1:
            assasin_info.draw()
        if step_tank==1:
            tank_info.draw()
        if step_mag==1:
            mag_info.draw()
        if drakon.health>=150:
            drakon.draw_health_bar_drakon(mw)
        elif drakon.health<150 and drakon.health>0:
            drakon.draw_helth_bar_dragon_hp(mw)
        if knight.health<=0 and archer.health<=0 and assasin.health<=0 and tank.health<=0 and mag.health<=0:
            fon_defeat.draw()
            game_defeat.draw()
            pygame.display.flip()
            pygame.time.delay(3000)
            game_over=True
    pygame.display.update()
    clock.tick(40)
