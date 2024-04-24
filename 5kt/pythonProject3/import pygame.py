import sqlite3
import shelve
import pygame
import pickle

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')


#users
connection.row_factory = sqlite3.Row


connection.commit()

connection.close()

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((760,428))
pygame.display.set_caption("5kt")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("images/bg.png")
player = pygame.image.load("images/player_right/1.png")

walk_right = [
pygame.image.load("images/player_right/1.png"),
pygame.image.load("images/player_right/2.png"),
pygame.image.load("images/player_right/3.png"),
pygame.image.load("images/player_right/4.png")
]
walk_left = [
pygame.image.load("images/player_right/1_1.png"),
pygame.image.load("images/player_right/1_2.png"),
pygame.image.load("images/player_right/1_3.png"),
pygame.image.load("images/player_right/1_4.png")
]

enemy = pygame.image.load("images/pudge.png")
enemy_x = 770
enemy_list_in_game = []


player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 318

is_jump = False
jump_count = 8


enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 3500)

label = pygame.font.SysFont("arial", 40)
pause_label = label.render("PAUSE", False, (255, 255, 255))


gameplay = True



bg_sound = pygame.mixer.Sound("sounds/Shaman_-_YA_RUSSKIJJ_74749727.mp3")
bg_sound.play()
bg_sound.set_volume(0)

def print_text(message, x, y, font_color = (69, 22, 28), font_size =100):
    font_type = pygame.font.Font(None, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()




        print_text("PAUSE", 160,300, (69,22,28), 100)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            paused = False
            pygame.display.update()

scores = 0
#record = 0
above_enemy = False

# ХЗ КАК ДОПИЛИТЬ ФУНКЦИЮ  SCORE
def count_scores():
     global scores, above_enemy



# ХЗ КАК ДОПИЛИТЬ ФУНКЦИЮ  GAME OVER
# def game_over():
    # stopped = True
    # while stopped:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #
    #     print_text("game over", 160, 300, (69, 22, 28), 100)
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_0]:
    #         paused = False
    #         return True
    #     if keys[pygame.K_0]:
    #         return False
    #         pygame.display.update()
    #
    #
    #     return game_over()
    #
    # while running():
    #     pass
    # pygame.quit()
    # quit()










running = True
while running:


    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 760, 0))
    print_text("Scores: " + str(scores), 650,400, (66,66,66),30)

    # d = shelve.open("score")
    # d["score"] = scores
    # d.close()


    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    if enemy_list_in_game:
        for (i, el ) in  enumerate(enemy_list_in_game):
            screen.blit(enemy, el)
            el.x -= 10

            if el.x < -10:
                enemy_list_in_game.pop(i)

                scores += 1




            if player_rect.colliderect(el):
                gameplay = False
                #сохранить очки
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))


    if keys [pygame.K_RIGHT]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    elif keys [pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed
    if keys[pygame.K_ESCAPE]:
        pause()

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -760:
        bg_x = 0



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft=(760, 315)))


    clock.tick(35)




