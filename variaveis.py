from PPlay.window import *
from PPlay.gameimage import *
#configuração da janela
janela = Window(750, 750)
janela.set_title("Mário")
# configuração do mario
vel=150 
vidas=3
mario = GameImage("assets/mario.png")
mario.set_position(350,550)
mario.vel = vel
mario.direcao = "down"


# configuração dos vilões 

v1 = GameImage("assets/v1.png")
v1.set_position(375,339)
v2 = GameImage("assets/v2.png")
v2.set_position(375,339)
v3 = GameImage("assets/v3.png")
v3.set_position(375,339)
v4 = GameImage("assets/v4.png")
v4.set_position(375,339)



#objetos 

tubo_esq = GameImage("assets/tubo_e.png")
tubo_esq.set_position(-20,318)
tudo_dir = GameImage("assets/tubo_d.png")
tudo_dir.set_position(650,318)

# configuração das paredes
p1 = GameImage("assets/p1.png")
p1.set_position(0,0)
p2 = GameImage("assets/p1.png")
p2.set_position(725,0)
p3 = GameImage("assets/p2.png")
p3.set_position(0,0)
p4 = GameImage("assets/p2.png")
p4.set_position(0,725)
p5 = GameImage("assets/p3.png")
p5.set_position(78,72)
p6 = GameImage("assets/p3.png")
p6.set_position(580,72)
v3 = GameImage("assets/v3.png")
v3.set_position(375,339)
p7 = GameImage("assets/p4.png")
p7.set_position(217-15,82-5)
p8 = GameImage("assets/p4.png")
p8.set_position(442-15,82-5)
p9 = GameImage("assets/p5.png")
p9.set_position(75,165)
p10 = GameImage("assets/p5.png")
p10.set_position(582,165)
p21 = GameImage("assets/p5.png")
p21.set_position(83-10,510)
p22 = GameImage("assets/p5.png")
p22.set_position(592-12,510)
p23 = GameImage("assets/p5.png")
p23.set_position(5,578)
p24 = GameImage("assets/p5.png")
p24.set_position(665-10,590-10)
p25 = GameImage("assets/p5.png")
p25.set_position(245-10,235)
p26 = GameImage("assets/p5.png")
p26.set_position(442-20,235)
p11 = GameImage("assets/p6.png")
p11.set_position(295-10,170)
p12 = GameImage("assets/p6.png")
p12.set_position(295,450)
p13 = GameImage("assets/p6.png")
p13.set_position(295-10,585-5)
p36 = GameImage("assets/p6.png")
p36.set_position(-19,330)
p37 = GameImage("assets/p6.png")
p37.set_position(-19,400)
p38 = GameImage("assets/p6.png")
p38.set_position(590,330)
p39 = GameImage("assets/p6.png")
p39.set_position(590,400)
p40 = GameImage("assets/p6.png")
p40.set_position(0,235)
p41 = GameImage("assets/p6.png")
p41.set_position(590,235)
p44 = GameImage("assets/p6.png")
p44.set_position(-19,450-10)
p45 = GameImage("assets/p6.png")
p45.set_position(590,450-10)
p48 = GameImage("assets/p6.png")
p48.set_position(295,385)
p14 = GameImage("assets/p7.png")
p14.set_position(365-10,195)
p15 = GameImage("assets/p7.png")
p15.set_position(365,470)
p16 = GameImage("assets/p7.png")
p16.set_position(365,605)
p17 = GameImage("assets/p7.png")
p17.set_position(217,590)
p18 = GameImage("assets/p7.png")
p18.set_position(515,590)
p19 = GameImage("assets/p7.png")
p19.set_position(133,540)
p20 = GameImage("assets/p7.png")
p20.set_position(592,540)
p49 = GameImage("assets/p7.png")
p49.set_position(295,325)
p50 = GameImage("assets/p7.png")
p50.set_position(435,325)
p27 = GameImage("assets/p8.png")
p27.set_position(217,385)
p28 = GameImage("assets/p8.png")
p28.set_position(515,385)
p29 = GameImage("assets/p8.png")
p29.set_position(365,25)
p42 = GameImage("assets/p8.png")
p42.set_position(140,245)
p43 = GameImage("assets/p8.png")
p43.set_position(590,245)
p30 = GameImage("assets/p9.png")
p30.set_position(225,175)
p31 = GameImage("assets/p9.png")
p31.set_position(502,175)
p32 = GameImage("assets/p10.png")
p32.set_position(93,645)
p33 = GameImage("assets/p10.png")
p33.set_position(442,645)
p34 = GameImage("assets/p11.png")
p34.set_position(212,520)
p35 = GameImage("assets/p11.png")
p35.set_position(442,520)
p46 = GameImage("assets/p13.png")
p46.set_position(140,420)
p47 = GameImage("assets/p13.png")
p47.set_position(590,420)


paredes=  [p1,  p2,  p3,  p4,  p5,  p6,  p7,  p8,  p9,  p10,
           p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,
           p21, p22, p23, p24, p25, p26, p27, p28, p29, p30,
           p31, p32, p33, p34, p35, p36, p37, p38, p39, p40,
           p41, p42, p43, p44, p45, p46, p47, p48, p49, p50]

# configuração das moedas 

#criando a matriz para as moedas
matriz_moedas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#criando uma matriz de moedas e fazendo as sumir quando encostadas pelo mario
moedas_coletadas = []