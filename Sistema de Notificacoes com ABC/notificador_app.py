from notificador import Notificador

class NotificadorApp(Notificador):
    def notificar(self, mensagem: str):
        print(f"Notificação no App: {mensagem}")