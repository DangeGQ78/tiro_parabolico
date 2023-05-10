import pygame
import math
import sys
import pygame_gui

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Movimiento Parabólico')





class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Dibuja el suelo
pygame.draw.rect(screen, (255, 0, 0), (0, 550, 800, 50))

# Dibuja la bola en la posición inicial
x = 100
y = 540
pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 10)

# Dibuja el botón de inicio de la simulación
start_button = Button(700, 500, 100, 50, (0, 255, 0), "Start")

def start_simulation():
    x0 = 100
    y0 = 539
    v0 = 50
    theta = math.pi / 6 # 45 grados en radianes
    g = 9.81 # aceleración gravitatoria en m/s^2
    t = 0
    floor = 550 # Altura del suelo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calcular la posición actual del objeto
        x = x0 + v0 * math.cos(theta) * t
        y = y0 - v0 * math.sin(theta) * t + 0.5 * g * t**2
        
        # Comprobar si el objeto ha chocado contra el suelo
        if y >= floor - 10:
            y = floor - 10

        # Dibujar el suelo y la bola en la pantalla
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (0, 550, 800, 50))
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 10)
      
        # Comprobar si el objeto ha chocado contra el suelo
        if y >= floor - 10:
            break

        # Actualizar la pantalla
        pygame.display.update()

        # Actualizar el tiempo
        t += 0.005

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(event.pos):
                start_simulation()

    # Dibujar el botón en la pantalla
    start_button.draw(screen)

    # Actualizar la pantalla
    pygame.display.update()
