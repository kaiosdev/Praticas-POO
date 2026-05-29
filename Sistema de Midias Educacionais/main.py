from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado
from plataforma import Plataforma

if __name__ == "__main__":
    plataforma = Plataforma("ICET Play")

    video_poo = Video("Aula de Polimorfismo", 45, "1080p")
    podcast_tech = Podcast("FirewallTalks #42", 60, "Alternei Brito")
    texto_artigo = TextoNarrado("O Futuro do Python", 10, "Português")

    print("")
    plataforma.adicionar_midia(video_poo)
    plataforma.adicionar_midia(podcast_tech)
    plataforma.adicionar_midia(texto_artigo)

    plataforma.listar_midias()

    plataforma.reproduzir_todas()