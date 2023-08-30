import pygame
import os
import random

# Criando a tela
pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Carrega as animações
RUNNING = [pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Dino', 'DinoRun1.png')),
           pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Dino', 'DinoRun2.png'))]

DUCKING = [pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Dino', 'DinoDuck1.png'))]

JUMPING = pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Dino', 'DinoJump.png'))

SMALL_CACTUS = [pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'SmallCactus1.png')),
                pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'SmallCactus2.png')),
                pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'SmallCactus3.png'))]

LARGE_CACTUS = [pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'LargeCactus1.png')),
                pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'LargeCactus2.png')),
                pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Cactus', 'LargeCactus3.png'))]

BRID = [pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Bird', 'Bird1.png')),
        pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Bird', 'Bird2.png'))]

CLOUD = pygame.image.load(os.path.join('C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Other', 'Cloud.png'))

BG = pygame.image.load(os.path.join("C:\\Users\\Yamac\\OneDrive\\Documentos\\Programação\\FEA.dev\\Github\\Dinossauro\\Images\\Other", "Track.png"))

class Dinosaur:
    X_POS = 80  # Coordenada x do dinossauro
    Y_POS = 310  # Coordenada y do dinossauro
    # Lembrando que nesse jogo, o dinossauro não se move na tela
    Y_POS_DUCK = 340  # Coordenada y do dinossauro agachado. Por algum motivo, o dinossauro agachado é um pouco mais alto que o normal ???
    JUMP_VEL = 8.5  # Velocidade do pulo do dinossauro

    def __init__(self):
        self.run_img = RUNNING
        self.duck_img = DUCKING
        self.jump_img = JUMPING
        
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]  # Imagem inicial do dinossauro
        self.dino_rect = self.image.get_rect()  # Pega a hitbox do dinossauro
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, userInput):
        """
        Função que atualiza o dinossauro baseado no input do usuário
        """
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:  # Para ficar mais fácil de animar o dinossauro
            self.step_index = 0        

        if userInput[pygame.K_UP] and not self.jump:  # Se o usuário aperta para a cima e o dino não está pulando, pula
            self.jump = True
            self.run = False
            self.duck = False
        elif userInput[pygame.K_DOWN] and not self.duck:  # Se o usuário aperta para baixo e o dino não está agachado, agacha
            self.jump = False
            self.run = False
            self.duck = True
        elif not(self.jump or userInput[pygame.K_DOWN]):  # Se o usuário não está apertando nada, o dino corre
            self.jump = False
            self.run = True
            self.duck = False

    def run(self):
        """
        Atualiza a imagem do dinossauro de modo a parecer que ele está se movendo
        """
        self.init_img = self.run_img[self.step_index //5]
        self.dino_rect = self.init_img.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    

    def duck(self):
        self.image = self.duck_img[self.setp_index // 5]    
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4  # Diminui a coordenada y do dino (o que significa que aumenta a posição dele na tela)    
            self.jump_vel -= 0.8

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)  # A nuvem aparece em algum lugar entre 800 e 1000 pixels da direita da tela
        self.y = random.randint(50, 100)  # A nuvem aparece em algum lugar entre 50 e 100 pixels do topo da tela
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed  # A nuvem se move para a esquerda
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed =14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 20)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1  # Aumenta a velocidade do jogo a cada 100 pontos

        text = font.render('Points:', str(points), True, (0, 0, 0))
        textRect = text.get_rect()  # Tudo nessa porra precisa de coordenadas
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:                                # A ideia é que o background vá se movendo, e quando a imagem acabar, põe outr imagem
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Loop para permitir sair do jogo no X
    while run:  # As paradas no pygame são sempre em while loop
        for event in pygame.event.get(): # event é qualquer ação realizada pelo usuário
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255)) # Preenche a tela com a cor branca
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)  # Atualiza o dinossauro baseado no input do usuário

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()
        
        clock.tick(30)
        pygame.display.update() 