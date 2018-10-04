import pygame
from pygame.locals import *
from random import randint 

pygame.font.init()

class numero :

    def __init__(self):
        self.position = {"x" : 109 , "y" : 170}
        self.imagen = 1
        self.numFora = []
        self.start = False
        self.cont = 0
        self.conti = -1 
        self.fonte = ["","","","","","","","",""]
        self.cont2 = 0
        self.contTerm = 0
        self.contLines = 0
        self.f = True


    def escoAleato(self) :
        num = int(randint(0,71))
        i = 0
        while i < len(self.numFora) :
            if num == self.numFora[i]:
                num = int(randint(0,71))
                i = 0
            i += 1
        self.numFora.append(num)
        self.imagen = num


    def iniciar(self) :
        self.start = True


  #  def texto(self) :
   #     font_padrao = pygame.font.get_default_font()
    #    font_num = pygame.font.SysFont(font_padrao, 45)
     #   self.fonte += "" + str(self.numFora[self.cont2]) + " "
      #  self.cont2 += 1
    

    def animacao(self) :
        if self.start and self.f :
            if self.cont < 1 and self.conti < 71:
                self.conti += 1
                return pygame.image.load("imagens/" + str(self.conti) + ".jpg").convert()
            elif self.cont == 1 :
                self.cont = 0
                self.conti = 0
                self.start = False
                font_padrao = pygame.font.get_default_font()
                font_num = pygame.font.SysFont(font_padrao, 45)

                if self.contTerm == 8 :
                    self.contLines += 1
                    self.contTerm = 0
                
                if self.numFora[self.cont2] > -1 and self.numFora[self.cont2] < 9 :
                    self.fonte[self.contLines] += "" + "0" + str(self.numFora[self.cont2] + 1) + " "
                    self.contTerm += 1
                
                else :
                    self.fonte[self.contLines] += "" + str(self.numFora[self.cont2] + 1) + " "
                    self.contTerm += 1
                    
                self.cont2 += 1
                return pygame.image.load("imagens/" + str(self.imagen) + ".jpg").convert()
            else :
                self.cont += 1
                self.conti = 0
                return pygame.image.load("imagens/" + str(self.conti) + ".jpg").convert()
        elif len(self.numFora) == 72 :
            self.f = False
            self.start = True
            return pygame.image.load("imagens/game_over.jpg").convert()

        elif self.f :
            self.start = False
            return pygame.image.load("imagens/" + str(self.imagen) + ".jpg").convert()
        
