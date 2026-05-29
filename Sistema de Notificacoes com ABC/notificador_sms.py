from notificador import Notificador

class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str):
        print(f"SMS enviado: {mensagem}")