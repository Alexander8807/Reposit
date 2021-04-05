import pygame

WIDTH, HEIGHT = 900, 500  #высота и ширина окна

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #создание окна
pygame.display.set_caption("Let's learn Python") #заголовок окна
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
FPS = 60  #фпс
VEL = 5   #движение 5 пикселей
CAT_IMAGE_WIDTH = 128
CAT_IMAGE_HEIGHT = 128   #размеры кота
CAT_IMAGE = pygame.image.load("cat.png")  #обозначить картинку
CAT = pygame.transform.scale(CAT_IMAGE, (128, 128)) #изменить картинку
#CAT = pygame.transform.rotate(CAT, 90) #повернуть на 90 градусов

def cat_move(keys_pressed, hit_box):
    if keys_pressed[pygame.K_LEFT] and hit_box.x - VEL > 0:  #нажать кнопку лево
        hit_box.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and hit_box.x + VEL < WIDTH - CAT_IMAGE_WIDTH:  #нажать кнопку право
        hit_box.x += VEL
    if keys_pressed[pygame.K_UP] and hit_box.y - VEL > 0:  #нажать кнопку верх
        hit_box.y -= VEL
    if keys_pressed[pygame.K_DOWN] and hit_box.y + VEL < HEIGHT - CAT_IMAGE_HEIGHT:  #нажать кнопку вниз
        hit_box.y += VEL

def draw_windows(hit_box): #функция для отрисовки, последовательно
    WIN.fill((125, 125, 125)) #заполнить цветом
    WIN.blit(CAT, (hit_box.x, hit_box.y))  #загрузить картинку
    #pygame.draw.rect(WIN, (125, 0, 0), (0, 0, 100, 100))  #нарисовать квадрат
                    #окно, цвет, координаты x и y, ширина высота
    #pygame.draw.rect(WIN, (0, 0, 0), BORDER) #квадрат границы
    pygame.display.update()  #обновить окно

def main():
    hit_box = pygame.Rect(0, 0, CAT_IMAGE_WIDTH, CAT_IMAGE_HEIGHT)
    clock = pygame.time.Clock() #для работы фпс
    condition = True
    while condition:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #тип
                condition = False
        keys_pressed = pygame.key.get_pressed() #кнопки, нажатые одновременно
        cat_move(keys_pressed, hit_box)
        draw_windows(hit_box) #рисуем
    pygame.quit()        #цикл обновления окна, обязательно


if __name__ == "__main__": #для импортирования
    main()