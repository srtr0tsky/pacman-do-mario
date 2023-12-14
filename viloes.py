from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.window import *
from variaveis import *
import random

v1.direcao = "right"
v2.direcao = "down"
v3.direcao = "left"
v4.direcao = "up"

def viloes_andando(game_image, vel, mario):
    direcao = ["up", "down", "left", "right"]
    
    
    if random.randint(1, 45) < 2:
        game_image.direcao = random.choice(direcao)

    # calcula a distanci entre o vilão e o mario
    distancia_x = mario.x - game_image.x
    distancia_y = mario.y - game_image.y
    distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5

    
    distancia_perseguir = 100

    if distancia < distancia_perseguir:
        direcao_x = distancia_x / distancia
        direcao_y = distancia_y / distancia

        # atualiza a posição do vilão 
        game_image.x += direcao_x * (vel - 80) * janela.delta_time()
        game_image.y += direcao_y * (vel - 80) * janela.delta_time()
        
        # checa a colisão 
        for parede in paredes:
            if game_image.collided(parede):
                if direcao_x > 0:
                    game_image.x -= vel * janela.delta_time()
                else:
                    game_image.x += vel * janela.delta_time()
                if direcao_y > 0:
                    game_image.y -= vel * janela.delta_time()
                else:
                    game_image.y += vel * janela.delta_time()
    else:
        # se o mario estiver fora do raio, o vilão continua se movendo aleatoriamente
        if game_image.direcao == "up":
            game_image.y -= vel  * janela.delta_time()
        elif game_image.direcao == "down":
            game_image.y += vel * janela.delta_time()
        elif game_image.direcao == "left":
            game_image.x -= vel * janela.delta_time()
        elif game_image.direcao == "right":
            game_image.x += vel * janela.delta_time()




#função batendo na parede
def verifica_colisao_parede(sprite):
    for parede in paredes:
        if sprite.collided(parede):
            return True
    return False

'''
class config_viloes():
    def __init__(self) -> None:
        pass

        
    def viloes_andando(self, janela, game_image, vel, mario):
        
        self.paredes = cenario.paredes(self)
        self.direcao = ["up", "down", "left", "right"]
       
        if random.randint(1, 45) < 2:
            game_image.direcao = random.choice(self.direcao)

        # calcula a distanci entre o vilão e o mario
        self.distancia_x = mario.x - game_image.x
        self.distancia_y = mario.y - game_image.y
        self.distancia = (self.distancia_x ** 2 + self.distancia_y ** 2) ** 0.5

        
        self.distancia_perseguir = 100

        if self.distancia < self.distancia_perseguir:
            self.direcao_x = self.distancia_x / self.distancia
            self.direcao_y = self.distancia_y / self.distancia

            # atualiza a posição do vilão 
            game_image.x += self.direcao_x * (self.vel - 80) * self.janela.delta_time()
            game_image.y += self.direcao_y * (self.vel - 80) * self.janela.delta_time()
            
            # checa a colisão 
            
            for self.parede in self.paredes:
                if game_image.collided(self.parede):
                    if self.direcao_x > 0:
                        game_image.x -= vel * janela.delta_time()
                    else:
                        game_image.x += vel * janela.delta_time()
                    if self.direcao_y > 0:
                        game_image.y -= vel * janela.delta_time()
                    else:
                        game_image.y += vel * janela.delta_time()
        else:
            # se o mario estiver fora do raio, o vilão continua se movendo aleatoriamente
            if game_image.direcao == "up":
                game_image.y -= vel  * janela.delta_time()
            elif game_image.direcao == "down":
                game_image.y += vel * janela.delta_time()
            elif game_image.direcao == "left":
                game_image.x -= vel * janela.delta_time()
            elif game_image.direcao == "right":
                game_image.x += vel * janela.delta_time()

    #função batendo na parede
    def verifica_colisao_parede(self, sprite):
        for self.parede in cenario.paredes(self):
            if sprite.collided(self.parede):
                return True
        return False

'''