import pygame
import random

from game_logic import adjust_grid



pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)


WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#towrzymy liste, ktora zawiera randomowe pozycie w touple, set zeby sie nie powtarzaly
def gen(num):
    return set([(random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)) for _ in range(num)])


def draw_grid(positions):
    #rozmieszczenie czerwonych kwadratow
    for position in positions:
        col,row = position
        top_left=(col*TILE_SIZE, row*TILE_SIZE)
        pygame.draw.rect(screen, RED, (*top_left,TILE_SIZE, TILE_SIZE))

    #tworzenie grida
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row*TILE_SIZE), (WIDTH, row*TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col*TILE_SIZE, 0), (col*TILE_SIZE, HEIGHT))




def main():
    positions = set()
    running = True
    playing = False
    count = 0
    update_freq = 120
    generation = 0



    while running:
        clock.tick(FPS)

        if playing:
            count +=1

        if playing and count >= update_freq:
            count = 0
            positions = adjust_grid(positions, GRID_WIDTH, GRID_HEIGHT)
            generation+=1


        speed = FPS / update_freq

        status = "playing" if playing else "on pause"

        pygame.display.set_caption(
            f"Conway's Game of Life is {status} | Generation: {generation} | Speed: {speed:.1f} gen/s")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos=(col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                    generation = 0

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4,10)*GRID_WIDTH)
                    generation = 0
                    count = 0

                if event.key == pygame.K_UP and update_freq>10:
                    update_freq -= 10
                    print(update_freq)

                if event.key == pygame.K_DOWN and update_freq < 120:
                    update_freq+=10
                    print(update_freq)

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()