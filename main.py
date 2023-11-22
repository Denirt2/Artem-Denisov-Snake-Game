import random
import pygame_menu
from src.config import *
from src.fruit import BadApple, Fruit, GoldenApple
from src.GUI import DeadBlock, SquareImage
from src.snake_body import SnakeBody
from src.snake_head import SnakeHead, SnakeHeadEasy


# Запуск самой игры
def start_game(nickname, difficulty):
    # Создание экрана
    width = 20 * 30
    height = 20 * 30
    margin = 4 * 30
    plain = [margin, width - margin, margin, height - margin]
    FPS = 30
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Змейка")
    font = pygame.font.SysFont('courier', 36)

    # Группы спрайтов
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    bad_apples = pygame.sprite.Group()
    bodies = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    # Клетки поля
    board_squres = list()
    for i in range(20):
        board_squres.append(list())
        for j in range(20):
            board_squres[i].append(0)

    # Задний фон
    display.fill(screen_color)

    # Создание объектов
    board = SquareImage(board_image, width, height)
    if difficulty.get_value()[1] == 0:
        head = SnakeHeadEasy(head_color, plain)
    else:
        head = SnakeHead(head_color, plain)
    last_body = head
    all_sprites.add(board)
    all_sprites.add(head)

    # Сложность 4+ - обалвяем так же стены
    if difficulty.get_value()[1] >= 3:
        dead_block_1 = DeadBlock(block_color, (30, 180), (margin + 30, margin + 90))
        dead_block_2 = DeadBlock(block_color, (30, 180), (width - margin - 60, margin + 90))
        dead_block_3 = DeadBlock(block_color, (180, 30), (margin + 90, margin + 30))
        dead_block_4 = DeadBlock(block_color, (180, 30), (margin + 90, height - margin - 60))
        for i in range(margin // 30 + 3, (width - margin) // 30 - 3):
            board_squres[margin // 30 + 1][i] = 1
            board_squres[(height - margin) // 30 - 2][i] = 1
            board_squres[i][margin // 30 + 1] = 1
            board_squres[i][(width - margin) // 30 - 2] = 1
        blocks.add(dead_block_1)
        blocks.add(dead_block_2)
        blocks.add(dead_block_3)
        blocks.add(dead_block_4)
        all_sprites.add(blocks)

    # Сложность 5 - Змейка изначально с максимальной скоростью
    if difficulty.get_value()[1] == 4:
        head.max_wait = head.max_wait_limit

    # Игровой цикл
    running = True
    score_point = 0
    while running:
        # Обработка всех событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    head.turn_down()
                if event.key == pygame.K_UP:
                    head.turn_up()
                if event.key == pygame.K_RIGHT:
                    head.turn_right()
                if event.key == pygame.K_LEFT:
                    head.turn_left()

        # Генерация фруктов (Сложность 3+ Генерация "Испорченных яблок")
        def create_fruit():
            coords = (random.randint(4, 15), random.randint(4, 15))
            while board_squres[coords[0]][coords[1]] == 1:
                coords = (random.randint(4, 15), random.randint(4, 15))
            new_fruit = Fruit(fruit_color, plain, coords)
            fruits.add(new_fruit)
            all_sprites.add(new_fruit)

        def create_bad_apple():
            coords = (random.randint(4, 15), random.randint(4, 15))
            while board_squres[coords[0]][coords[1]] == 1:
                coords = (random.randint(4, 15), random.randint(4, 15))
            new_bad_apple = BadApple(bad_apple_color, plain, coords)
            bad_apples.add(new_bad_apple)
            all_sprites.add(new_bad_apple)

        def create_golden_apple():
            coords = (random.randint(4, 15), random.randint(4, 15))
            while board_squres[coords[0]][coords[1]] == 1:
                coords = (random.randint(4, 15), random.randint(4, 15))
            new_golden_apple = GoldenApple(golden_apple_color, plain, coords)
            fruits.add(new_golden_apple)
            all_sprites.add(new_golden_apple)

        # Проверка на создание фрукта
        if (random.randint(0, 670) <= 2 and len(fruits) < 4) or len(fruits) == 0:
            if random.randint(0, 100) < 15:
                create_golden_apple()
            else:
                create_fruit()

        # Проверка на создание плохого фрукта
        if difficulty.get_value()[1] == 2 and random.randint(0, 670) <= 2:
            if len(bad_apples) == 0:
                create_bad_apple()
        elif difficulty.get_value()[1] == 3 and random.randint(0, 670) <= 2:
            if len(bad_apples) <= 1:
                create_bad_apple()
        elif difficulty.get_value()[1] == 4 and random.randint(0, 670) <= 2:
            if len(bad_apples) <= 2:
                create_bad_apple()

        # Съедание фрукта
        for i in fruits:
            if i.in_hitbox(head.rect.center):
                score_point += i.GetScore()
                i.kill()
                if len(bodies) % 2 == 1:
                    new_body = SnakeBody(body_color_second, last_body, head)
                else:
                    new_body = SnakeBody(body_color_first, last_body, head)
                last_body = new_body
                bodies.add(new_body)
                all_sprites.add(new_body)

        # Съедание плохого фрукта
        for i in bad_apples:
            if i.in_hitbox(head.rect.center):
                score_point += i.GetScore()
                i.kill()
                if len(bodies) % 2 == 1:
                    new_body = SnakeBody(body_color_second, last_body, head)
                else:
                    new_body = SnakeBody(body_color_first, last_body, head)
                last_body = new_body
                bodies.add(new_body)
                all_sprites.add(new_body)

        # Проверка врезалась ли змейка в себя же
        for body in bodies:
            if body.head_in_hitbox:
                head.is_live = False

        # Проверка, врезалась ли змейка в стену (Сложность 4+)
        if difficulty.get_value()[1] >= 3:
            for block in blocks:
                if block.in_hitbox(head):
                    head.is_live = False

        if not head.is_live:
            break

        # Текст
        display.fill(screen_color)
        score = font.render(f'Score: {score_point}', False, text_color)
        display.blit(score, (30, 30))

        # Рендер
        all_sprites.update()
        all_sprites.draw(display)
        pygame.display.flip()

        clock.tick(FPS)
    # Завершение игры
    write_score(nickname, score_point)
    return


# Таблица лидеров
def top_players():
    display_scores = pygame.display.set_mode((600, 600))
    scores_menu = pygame_menu.Menu("Таблица лидеров", 600, 600, theme=pygame_menu.themes.THEME_SOLARIZED)
    scores_menu.add.button("Назад", main_menu)
    with open("src/scores.txt", 'r') as file:
        lines = file.readlines()
        results = list()
        for i in range(0, len(lines) // 2):
            results.append([0, ''])
        for i in range(0, len(lines) - 1, 2):
            results[i // 2][0] = int(lines[i + 1][:len(lines[i + 1]) - 1])
            results[i // 2][1] = lines[i][:len(lines[i]) - 1]
        results.sort(reverse=True)
        for i in range(0, min(5, len(results))):
            scores_menu.add.label(str(i + 1) + '. ' + results[i][1] + ": " + str(results[i][0]))
    scores_menu.mainloop(display_scores)


# Запись счёта в файл
def write_score(nickname, score_point):
    # Запись счёта
    with open('src/scores.txt', 'r') as file:
        already_in = False
        for line in file:
            if already_in:
                old_score = str(line)
                break
            if nickname.get_value() + '\n' == line:
                already_in = True
    with open('src/scores.txt', 'r') as file:
        old_data = file.read()
    if already_in:
        score_point = max(score_point, int(old_score))
        new_data = old_data.replace(nickname.get_value() + "\n" + old_score,
                                    nickname.get_value() + "\n" + str(score_point) + "\n", 1)
        with open('src/scores.txt', 'w') as file:
            file.write(new_data)
    else:
        new_data = nickname.get_value() + "\n" + str(score_point) + "\n"
        with open('src/scores.txt', 'a') as file:
            file.write(new_data)


def main_menu():
    # Начинаем игру
    def start():
        start_game(nickname, difficulty)
    # Создаём меню
    menu_display = pygame.display.set_mode((600, 600))
    menu = pygame_menu.Menu('Змейка by Denirt', 600, 600, theme=pygame_menu.themes.THEME_SOLARIZED)

    # Создаём интерфейс меню
    nickname = menu.add.text_input('Ник: ', default="Player")
    difficulty = menu.add.selector("Уровень сложности: ", [("Очень просто", 1), ("Классика", 2), ("Усложнённая 1", 3),
                                                           ("Усложнённая 2", 4), ("Хард", 5)])
    menu.add.button('Играть', start)
    menu.add.button('Таблица рекордов', top_players)
    menu.add.button('Выход', pygame_menu.events.EXIT)

    menu.mainloop(menu_display)


pygame.init()
pygame.font.init()
main_menu()
