import pygame 
import time
import math
from utils import scale_img, blit_rotate_center, blit_text_center
pygame.font.init()

# variable of the track
GRASS = scale_img(pygame.image.load('img/grass.jpg'), 2.5)
TRACK = scale_img(pygame.image.load('img/track.png'), 0.9)
HEDGE = scale_img(pygame.image.load('img/track-border.png'), 0.9)
HEDGE_MASK = pygame.mask.from_surface(HEDGE)
FINISH = pygame.image.load('img/finish.png')
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POS = (130, 250)

# variable of the car
BARR = scale_img(pygame.image.load('pilots/barr.png'), 0.5)
FITT = scale_img(pygame.image.load('pilots/fitt.png'), 0.5)
MASS = scale_img(pygame.image.load('pilots/mass.png'), 0.5)
PIQ = scale_img(pygame.image.load('pilots/piq.png'), 0.5)
SEN = scale_img(pygame.image.load('pilots/sen.png'), 0.5)

# variable of the window
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brasil Racing')
MAIN_FONT = pygame.font.SysFont("comicsans", 44)
FPS = 60
# out from 2: (110, 70), old 6: (404, 680), old 12: (734, 399), 
PATH = [(175, 119), (56, 133), (70, 481), (318, 731), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]
# laps = 2

# level class
class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)

# draw the pilots
class AbstractCar: # not to be initiate directly
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acc = 0.5
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acc, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acc, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal
    
    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

# player class
class Player(AbstractCar):
    IMG = SEN
    START_POS = (180, 200)

    def reduce_speed(self):
        # self.acc = 0
        self.vel = max(self.vel - self.acc/2, 0)
        self.move()
    
    def bounce(self):
        self.vel = -self.vel/2
        self.move()

# computer class
class Computer(AbstractCar):
    IMG = PIQ
    START_POS = (150, 200)

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel
    
    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi/2
        else:
            desired_radian_angle = math.atan(x_diff/y_diff)
        
        if target_y > self.y:
            desired_radian_angle += math.pi
        
        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))
    
    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

        if rect.collidepoint(*target):
           self.current_point += 1
            # if self.current_point == len(self.path):
              #  self.current_point = 0
    def move(self):
        if self.current_point >= len(self.path):
            return
        
        self.calculate_angle()
        self.update_path_point()
        super().move()
    
    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0

# draw the objects
def draw(win, images, player, computer, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(
        f"Vel: {round(player.vel, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

    player.draw(win)
    computer.draw(win)
    pygame.display.update()

# move player
def move_player(player):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player.rotate(left=True)
    if keys[pygame.K_d]:
        player.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player.move_backward()
    
    if not moved:
        player.reduce_speed()

# collision detection
def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(HEDGE_MASK) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POS)
    if computer_finish_poi_collide != None:
        blit_text_center(WIN, MAIN_FONT, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POS)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)

# define race loop
race = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0)), (HEDGE, (0,0)), (FINISH, FINISH_POS), (HEDGE, (0,0))]
player = Player(5, 5)
computer = Computer(5, 5, PATH)
game_info = GameInfo()

while race:
    clock.tick(FPS) # the loop can't run faster than 60 frame per second

    # blit to show the objects on screen / putting on order of later appear
    draw(WIN, images, player, computer, game_info)
    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                game_info.start_level()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player)
    computer.move()
    handle_collision(player, computer, game_info)

    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        game_info.reset()
        player.reset()
        computer.reset()
pygame.quit()