from notificador import Notificador

class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str):
        print(f"E-mail enviado: {mensagem}")