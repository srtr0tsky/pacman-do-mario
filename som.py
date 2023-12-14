from PPlay.sound import Sound

class config_som():
    def __init__(self) -> None:
        pass

    def trilha_sonora(tocar):
        som = Sound("sons/26.-Giga-Bite-_Axial-Disc-1_.ogg")
        if tocar == True:
            return som.play()
        else:
            return som.pause()

    def game_over(tocar):
        som = Sound("sons/Game-Over.ogg")
        if tocar == True:
            return som.play()
        else:
            return som.pause()
    def hit(tocar):
        som = Sound("sons/Retro-Event-Wrong-Simple-03.ogg")
        if tocar == True:
            return som.play()
        else:
            return som.pause()
    

