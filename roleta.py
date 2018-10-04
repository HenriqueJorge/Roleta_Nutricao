import pygame
from pygame.locals import *
from sys import exit
from acoes import *

pygame.init()
pygame.font.init()

class roleta() :

    def __init__(self, screen ,items , bg_color=(0,0,0), font=None, font_size=60, font_color= (0,0,0)):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height

            #Posição da da palavra de menu
            posx = (self.scr_width / 2) - (width / 2)
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
        
        
    def run(self) :
        mainloop = True
        fundo = pygame.image.load("imagens/fundo.jpg").convert()
        comecar = numero()
        pygame.mixer.music.load("som/theme.mp3")
        pygame.mixer.music.play(-1)
       
        

        while mainloop :
            self.clock.tick(50)
            for event in pygame.event.get() :
                if event.type == QUIT:
                    pygame.mixer.stop()
                    pygame.quit()
                    exit()
                    
                keys = pygame.key.get_pressed()
                
                if comecar.start == False :
                    if comecar.contLines < 9 :
                        if keys[K_SPACE] :
                            comecar.iniciar()
                            comecar.escoAleato()
                    
         
                
            #print(comecar.start)
            #print(comecar.imagen)
            #print(comecar.numFora)
            #print(comecar.fonte)
                    

            self.clock.tick(50)


            self.screen.blit(fundo, (0, 0))
            self.screen.blit(comecar.animacao() ,(comecar.position["x"], comecar.position["y"]))
            
            for name, label, (width, height), (posx, posy) in self.items:
                font = pygame.font.SysFont(None, 60)
                texto = font.render(comecar.fonte[0], 1, (0,0,0))
                self.screen.blit(texto, (687, 87))
                
                texto1 = font.render(comecar.fonte[1], 1, (0,0,0))
                self.screen.blit(texto1, (687, 133))

                texto2 = font.render(comecar.fonte[2], 1, (0,0,0))
                self.screen.blit(texto2, (687, 179))

                texto3 = font.render(comecar.fonte[3], 1, (0,0,0))
                self.screen.blit(texto3, (687, 225))

                texto4 = font.render(comecar.fonte[4], 1, (0,0,0))
                self.screen.blit(texto4, (687, 271))

                texto5 = font.render(comecar.fonte[5], 1, (0,0,0))
                self.screen.blit(texto5, (687, 317))

                texto6 = font.render(comecar.fonte[6], 1, (0,0,0))
                self.screen.blit(texto6, (687, 363))

                texto7 = font.render(comecar.fonte[7], 1, (0,0,0))
                self.screen.blit(texto7, (687, 409))

                texto8 = font.render(comecar.fonte[8], 1, (0,0,0))
                self.screen.blit(texto8, (687, 455))
                
            pygame.display.flip()
            pygame.display.update()

if __name__ == "__main__" :

    screen = pygame.display.set_mode((1200, 632), 0, 32)
    pygame.display.set_caption('Roleta v0.1')
    
    menu_items = ("1")

    gm = roleta(screen, menu_items)
    gm.run()
            
        
