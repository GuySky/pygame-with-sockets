import pygame
import data.engine as e
from data.network import Network as net
from random import *
from pygame.locals import *

class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Test game')

        self.WINDOW_SIZE = (900,600)
        self.DISPLAY_SIZE = (300, 200)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.display = pygame.Surface(self.DISPLAY_SIZE)

        self.clock = pygame.time.Clock()

        self.player = e.PhysicsEntity('player', (50, 50), (20, 20))
        self.player_network = net()
        self.players_dict = {}

        self.movement = {'up': False, 'left': False, 'down': False, 'right': False}


    def run(self):

        self.run = True
        while self.run:
            self.display.fill('black')

            self.player.update(self.movement)
            self.player.render(self.display, 'red')
            self.player_network.sending_thread(self.player.getObjData())

            for player in self.player_network.get_data():
                self.players_dict[player] = self.player_network.get_data()[player]
            
            for player in self.players_dict:
                another_one = pygame.Rect(self.players_dict[player]['x'], 
                                          self.players_dict[player]['y'], 
                                          self.players_dict[player]['width'], 
                                          self.players_dict[player]['height'])
                pygame.draw.rect(self.display, 'green', another_one)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False

                if event.type == KEYDOWN:
                    if event.key == K_w:
                        self.movement['up'] = True
                    if event.key == K_a:
                        self.movement['left'] = True
                    if event.key == K_s:
                        self.movement['down'] = True
                    if event.key == K_d:
                        self.movement['right'] = True
                
                if event.type == KEYUP:
                    if event.key == K_w:
                        self.movement['up'] = False
                    if event.key == K_a:
                        self.movement['left'] = False
                    if event.key == K_s:
                        self.movement['down'] = False
                    if event.key == K_d:
                        self.movement['right'] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(120)

        self.player_network.sending_thread({'x': 0, 'y': 0, 'width': 0, 'height': 0, 'type': 0})
        self.player_network.close_connection()
        pygame.quit()


Game().run()