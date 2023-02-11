import pygame
import random
import os
pygame.font.init()

WIDTH, HEIGHT = 1300, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 60
coin_IMAGE = pygame.image.load(os.path.join("coin.png"))
box = pygame.image.load(os.path.join("box.png"))
coin = pygame.transform.scale(coin_IMAGE, (70, 70))
blue = (50, 130, 200)
score = 0
score_FONT = pygame.font.SysFont("comicsans", 40)
game_over_font = pygame.font.SysFont("comicsans", 100)
black = (0,0,0)
coin_vel = 5
game_over = False
index = 15
sprite_list = [coin, box]

def draw_window(r_coin, r_box, game_over):
    score_txt = score_FONT.render("Score: "+str(score), 1, black)
    index_txt = score_FONT.render("Tries left: "+str(index), 1, black)
    WIN.blit(score_txt, (0,0))
    WIN.blit(index_txt, (WIDTH-index_txt.get_width(), 0))
    
    pygame.display.update()
    if game_over==False:
        WIN.fill(blue)
        WIN.blit(coin, (r_coin.x, r_coin.y))
        WIN.blit(box, (r_box.x, r_box.y))

    pygame.display.update()
    
def place_coin(r_coin, game_over):
    if game_over==False:
        r = random.randrange(0,WIDTH-r_coin.width)
        r_coin.x = r 

def box_mov(keys_pressed, r_box, game_over):
    if game_over==False:
        if keys_pressed[pygame.K_LEFT] and r_box.x>0:
            r_box.x -= 5
        elif keys_pressed[pygame.K_RIGHT] and r_box.x<WIDTH-r_box.width:
            r_box.x += 5

def main():
    global score, coin_vel, game_over, index
    r_coin = pygame.Rect(0,-coin.get_height(), coin.get_width(), coin.get_height())
    r_box = pygame.Rect(WIDTH/2-box.get_width()/2, HEIGHT-box.get_height(), box.get_width(), box.get_height())
    clock = pygame.time.Clock()
    run = True
    place_coin(r_coin, game_over)

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        box_mov(keys_pressed, r_box, game_over)
        draw_window(r_coin, r_box, game_over)
        r_coin.y += coin_vel

        if r_coin.y==HEIGHT-r_coin.height:
            index -= 1
            if game_over==False:
                r_coin.y = -coin.get_height()
                place_coin(r_coin, game_over)
                r_coin.y += coin_vel
        elif r_coin.colliderect(r_box) and r_coin.y<r_box.y:
            index -= 1
            score += 1
            if game_over==False:
                r_coin.y = -coin.get_height()
                place_coin(r_coin, game_over)
                r_coin.y += coin_vel
        
        if index==0:
            game_over = True
            game_over_txt = game_over_font.render("Game over", 1, black)
            WIN.blit(game_over_txt, (WIDTH/2-game_over_txt.get_width()/2, 200))
            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()