import pygame
import sys
 
from collections import defaultdict
 
 
class Game:
    def __init__(self, 
                 caption, 
                 width, 
                 height, 
                 back_image_filename, 
                 frame_rate):
        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        for o in self.objects:
            o.update()
 
    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, 
                                pygame.MOUSEBUTTONUP, 
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
 
            self.handle_events()
            self.update()
            self.draw()
 
            pygame.display.update()
            self.clock.tick(self.frame_rate)

class TextObject:
    def __init__(self, 
                 x, 
                 y, 
                 text_func, 
                 color, 
                 font_name, 
                 font_size):
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_surface(text_func())
 
    def draw(self, surface, centralized=False):
        text_surface, self.bounds = \
            self.get_surface(self.text_func())
        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2,
                   self.pos[1])
        else:
            pos = self.pos
        surface.blit(text_surface, pos)
 
    def get_surface(self, text):
        text_surface = self.font.render(text, 
                                        False, 
                                        self.color)
        return text_surface, text_surface.get_rect()
 
    def update(self):
        pass


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('background.jpg')
 
while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)


from game_object import GameObject
 
 
class Brick(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

class Ball(GameObject):
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, 
                            x - r, 
                            y - r, 
                            r * 2, 
                            r * 2, 
                            speed)
        self.radius = r
        self.diameter = r * 2
        self.color = color
 
    def draw(self, surface):
        pygame.draw.circle(surface, 
                           self.color, 
                           self.center, 
                           self.radius)

import config as c
from game_object import GameObject
 
 
class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)
 
    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
               self.state = 'hover'
        else:
            self.state = 'normal'
 
    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'
 
    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

class Breakout(Game):
    def show_message(self, 
                     text, 
                     color=colors.WHITE, 
                     font_name='Arial', 
                     font_size=20, 
                     centralized=False):
        message = TextObject(c.screen_width // 2, 
                             c.screen_height // 2, 
                             lambda: text, color, 
                             font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)

        
import config as c
from game_object import GameObject
 
 
class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
 
    ...
 
    def update(self):
        if self.moving_left:
            dx = -(min(self.offset, self.left))
        elif self.moving_right:
            dx = min(self.offset, c.screen_width - self.right)
        else:
            return
 
        self.move(dx, 0)

    def create_ball(self):
        speed = (random.randint(-2, 2), c.ball_speed)
        self.ball = Ball(c.screen_width // 2,
                         c.screen_height // 2,
                         c.ball_radius,
                         c.ball_color,
                         speed)
        self.objects.append(self.ball)

    def handle_ball_collisions(self):
        def intersect(obj, ball):
            edges = dict(
                left=Rect(obj.left, obj.top, 1, obj.height),
                right=Rect(obj.right, obj.top, 1, obj.height),
                top=Rect(obj.left, obj.top, obj.width, 1),
                bottom=Rect(obj.left, obj.bottom, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if
                             ball.bounds.colliderect(rect))
            if not collisions:
                return None
 
            if len(collisions) == 1:
                return list(collisions)[0]
 
            if 'top' in collisions:
                if ball.centery >= obj.top:
                    return 'top'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'
 
            if 'bottom' in collisions:
                if ball.centery >= obj.bottom:
                    return 'bottom'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'



# Hit paddle
s = self.ball.speed
edge = intersect(self.paddle, self.ball)
if edge is not None:
    self.sound_effects['paddle_hit'].play()
if edge == 'top':
    speed_x = s[0]
    speed_y = -s[1]
    if self.paddle.moving_left:
        speed_x -= 1
    elif self.paddle.moving_left:
        speed_x += 1
    self.ball.speed = speed_x, speed_y
elif edge in ('left', 'right'):
    self.ball.speed = (-s[0], s[1])


# Hit floor
if self.ball.top > c.screen_height:
    self.lives -= 1
    if self.lives == 0:
        self.game_over = True
    else:
        self.create_ball()


# Hit ceiling
if self.ball.top < 0:
    self.ball.speed = (s[0], -s[1])
 
# Hit wall
if self.ball.left < 0 or self.ball.right > c.screen_width:
    self.ball.speed = (-s[0], s[1])

# Hit brick
for brick in self.bricks:
    edge = intersect(brick, self.ball)
    if not edge:
        continue
 
    self.bricks.remove(brick)
    self.objects.remove(brick)
    self.score += self.points_per_brick
 
    if edge in ('top', 'bottom'):
        self.ball.speed = (s[0], -s[1])
    else:
        self.ball.speed = (-s[0], s[1])

from game_object import GameObject
from text_object import TextObject
import config as c
 
 
class Button(GameObject):
    def __init__(self, 
                 x, 
                 y, 
                 w, 
                 h, 
                 text, 
                 on_click=lambda x: None, 
                 padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click
 
        self.text = TextObject(x + padding, 
                               y + padding, lambda: text, 
                               c.button_text_color, 
                               c.font_name, 
                               c.font_size)
 
    def draw(self, surface):
        pygame.draw.rect(surface, 
                         self.back_color, 
                         self.bounds)
        self.text.draw(surface)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)
 
    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'
 
    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'
 
    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    def back_color(self):
        return dict(normal=c.button_normal_back_color,
                    hover=c.button_hover_back_color,
                    pressed=c.button_pressed_back_color)[self.state]
    def create_menu(self):
        for i, (text, handler) in enumerate((('PLAY', on_play), 
                                             ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def on_play(button):
        for b in self.menu_buttons:
            self.objects.remove(b)
 
        self.is_game_running = True
        self.start_level = True
 
    def on_quit(button):
        self.game_over = True
        self.is_game_running = False
