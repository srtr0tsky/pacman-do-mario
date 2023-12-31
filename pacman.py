
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import* 
from viloes import viloes_andando, verifica_colisao_parede
from som import *
from variaveis import *


menu = GameImage("assets/menu.png")
victory = GameImage("assets/victory.png")
gameover = GameImage("assets/gameover.png")

pontos = 0
def monedas(pontos):
    global moedas_coletadas
    num1 = ((750) // 32)
    num2 = (750 // 30)
    for i in range(len(matriz_moedas)):
        for j in range(len(matriz_moedas[i])):
            x = j * num2 + (0.5 * num2)
            y = i * num1 + (0.5 * num1)
            if matriz_moedas[i][j] == 1 and (x, y) not in moedas_coletadas:
                moeda = Sprite("assets/moeda.png")
                moeda.set_position(x - moeda.width // 2, y - moeda.height // 2)
                moeda.draw()
                if mario.collided(moeda):
                    moedas_coletadas.append((x, y))  
                    pontos +=1
    return pontos

config_som.trilha_sonora(True)

status = 0
def tela_menu(): 
    menu.draw()
    janela.update()
def tela_gameover():
    gameover.draw()
    janela.update()
def tela_victory():
    victory.draw()
    janela.update()
    time.sleep(1)

while True:
    
    if status ==0:
        tela_menu()
        if janela.get_keyboard().key_pressed("ENTER"):
            status = 1
    
    while status == 1:     
        # Mário colidindo com as paredes
        if verifica_colisao_parede(mario):
            mario.x = mario.anterior_x
            mario.y = mario.anterior_y
        mario.anterior_x = mario.x
        mario.anterior_y = mario.y
        #movendo o mário
        if (janela.get_keyboard().key_pressed("left")):
            mario.direcao = "left"
        elif (janela.get_keyboard().key_pressed("right")):
            mario.direcao = "right"
        elif (janela.get_keyboard().key_pressed("up")):
            mario.direcao = "up"
        elif (janela.get_keyboard().key_pressed("down")):
            mario.direcao = "down"
        if mario.direcao == "left":
            mario.x -= mario.vel * janela.delta_time()
        elif mario.direcao == "right":
            mario.x += mario.vel * janela.delta_time()
        elif mario.direcao == "up":
            mario.y -= mario.vel * janela.delta_time()
        elif mario.direcao == "down":
            mario.y += mario.vel * janela.delta_time()
        
        #passando pelos tubos
        if (tudo_dir.collided(mario)):
            mario.set_position(150,360)   
        if (tubo_esq.collided(mario)):
            mario.set_position(600,360) 
        #peerdendo as vidas ao encostar nos viloes
        if (v1.collided(mario)):
            if vidas != 1:
                config_som.trilha_sonora(False)
                config_som.hit(True)
            v1.set_position(330,339)  
            vidas -=1
            mario.set_position(350,550)
        if (v2.collided(mario)):
            if vidas != 1:
                config_som.trilha_sonora(False)
                config_som.hit(True)
                
            v2.set_position(330,339)  
            vidas -=1
            mario.set_position(350,550)
            
        if (v3.collided(mario)):
            if vidas != 1:
                config_som.trilha_sonora(False)
                config_som.hit(True)
            v3.set_position(330,339)  
            vidas -=1
            mario.set_position(350,550)
            
        if (v4.collided(mario)):
            if vidas != 1:
                config_som.trilha_sonora(False)
                config_som.hit(True)
            v4.set_position(330,339)  
            vidas -=1
            mario.set_position(350,550)
            
        #colidindo viloes nas paredes
        if verifica_colisao_parede(v1):
            v1.x = v1.anterior_x
            v1.y = v1.anterior_y
        v1.anterior_x = v1.x
        v1.anterior_y = v1.y
        if verifica_colisao_parede(v2):
            v2.x = v2.anterior_x
            v2.y = v2.anterior_y
        v2.anterior_x = v2.x
        v2.anterior_y = v2.y
        if verifica_colisao_parede(v3):
            v3.x = v3.anterior_x
            v3.y = v3.anterior_y
        v3.anterior_x = v3.x
        v3.anterior_y = v3.y
        if verifica_colisao_parede(v4):
            v4.x = v4.anterior_x
            v4.y = v4.anterior_y
        v4.anterior_x = v4.x
        v4.anterior_y = v4.y   

        
            
            
        if pontos == 245:
            config_som.trilha_sonora(False)
            config_som.game_over(True)
            time.sleep(2)
            tela_victory()
            time.sleep(1)
            status = 0
            pontos = 0
            moedas_coletadas = []
            vel=150 
            vidas=3
            mario = GameImage("assets/mario.png")
            mario.set_position(350,550)
            mario.vel = vel
            mario.direcao = "down"
            break
                
        viloes_andando(v1, vel, mario)
        viloes_andando(v2, vel, mario)
        viloes_andando(v3, vel, mario)
        viloes_andando(v4, vel, mario)
        #game over se perder as 3 vidas
        
    
        if vidas == 0:
            config_som.trilha_sonora(False)
            config_som.game_over(True)
            time.sleep(2)
            tela_gameover()
            time.sleep(1)
            tela_menu()
            status = 0
            pontos = 0
            moedas_coletadas = []
            vel=150 
            vidas=3
            mario = GameImage("assets/mario.png")
            mario.set_position(350,550)
            mario.vel = vel
            mario.direcao = "down"
            break
        
        janela.set_background_color([0,0,50])
        pontos =monedas(pontos)
        for parede in paredes:
            parede.draw()
        mario.draw()
        v3.draw()
        v4.draw()
        v1.draw()
        v2.draw()
        tubo_esq.draw()
        tudo_dir.draw()
        janela.draw_text(("Vidas:"), 0, 0, size=18, font_name="Arial", bold=True, italic = True, color=[255, 255, 255])
        janela.draw_text (str(vidas), 60, 0, size=18, font_name="Arial", bold=True, italic = True, color=[255, 255, 255])  
        janela.draw_text(("Pontos:"), 80, 0, size=18, font_name="Arial", bold=True, italic = True, color=[255, 255, 255])
        janela.draw_text (str(pontos), 160, 0, size=18, font_name="Arial", bold=True, italic = True, color=[255, 255, 255])  
        janela.update()
        
        
 
