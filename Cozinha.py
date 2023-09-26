import time
from datetime import datetime


def preparo(pedido, tempo, tipo):
    print(f"Pedido {pedido} está {tipo} - TEMPO: {str(tempo)} SEGUNDOS")
    time.sleep(tempo)
    return pedido


def cancelar_pedido_na_cozinha(pedido, mesa):
    print(f"Pedido {pedido} da mesa {mesa} cancelado")


class Cozinha:
    def __init__(self):
        self.tipo_pedido = {
            "carbonara": "cozimento",
            "lasanha": "forno",
            "espaguete à bolonhesa": "cozimento",
            "sushi": "preparo a frio",
            "hambúrguer": "chapa",
            "pizza": "forno",
            "salada Caesar": "montagem",
            "frango grelhado": "churrasqueira",
            "tacos": "montagem",
            "risoto de cogumelos": "cozimento",
        }
        self.pedido_ser_preparado = " "

    def cozimento(self):
        return preparo(self.pedido_ser_preparado, 10, "cozinhando")

    def forno(self):
        return preparo(self.pedido_ser_preparado, 20, "assando")

    def preparo_a_frio(self):
        return preparo(self.pedido_ser_preparado, 10, "sendo preparado")

    def chapa(self):
        return preparo(self.pedido_ser_preparado, 15, "na chapa")

    def montagem(self):
        return preparo(self.pedido_ser_preparado, 5, "sendo montado")

    def churrasqueira(self):
        return preparo(self.pedido_ser_preparado, 25, "na churrasqueira")

    def cozinhar(self, pedido, hora_inicio):
        for key, value in self.tipo_pedido.items():
            if pedido.lower() == key:
                self.pedido_ser_preparado = pedido
                tipo = value.strip().replace(" ", "_")
                pedido_ready = eval(f"self.{tipo}()")
                horario_fim = datetime.now().strftime("%H:%M:%S")
                tempo_de_preparo = datetime.strptime(
                    horario_fim, "%H:%M:%S"
                ) - datetime.strptime(hora_inicio, "%H:%M:%S")
                return pedido_ready, tempo_de_preparo
            else:
                pass

        return None, None
