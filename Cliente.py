from Cozinha import Cozinha, cancelar_pedido


class Cliente:
    def __init__(self, mesa):
        self.mesa = mesa
        self.preco_pedido = {
            "carbonara": 12.99,
            "lasanha": 10.49,
            "espaguete à bolonhesa": 9.99,
            "sushi": 18.99,
            "hambúrguer": 7.99,
            "pizza": 11.99,
            "salada Caesar": 6.49,
            "frango grelhado": 13.99,
            "tacos": 8.99,
            "risoto de cogumelos": 15.99,
        }
        self.valor_da_conta = 0
        self.descricao_produtos = []

    def pedido_pronto(self, pedido_ready, tempo_de_preparo):
        if pedido_ready:
            print(
                f"Pedido {pedido_ready} da mesa {self.mesa} está pronto \n>>> Tempo de preparo: {tempo_de_preparo} <<<"
            )
        else:
            print("Pedido não foi possível ser realizado")

    def __calculo_mesa__(self, preco, tipo):
        if tipo == "add":
            self.valor_da_conta += preco
        elif tipo == "sub":
            self.valor_da_conta -= preco

    def fazer_um_pedido(self, pedido, horario):
        cozinha_object = Cozinha()
        pedido_ready, tempo_de_preparo = cozinha_object.cozinhar(
            pedido=pedido, hora_inicio=horario
        )
        if pedido_ready is not None:
            preco = self.preco_pedido.get(pedido_ready)
            self.__calculo_mesa__(preco, "add")
            self.descricao_produtos.append({pedido_ready: preco})
            self.pedido_pronto(pedido_ready, tempo_de_preparo)
            return pedido_ready, tempo_de_preparo
        else:
            self.pedido_pronto(None, None)
            return None, None

    def cancelar_pedido(self, pedido):
        cancelar_pedido(pedido, self.mesa)
        preco = self.preco_pedido.get(pedido)
        self.descricao_produtos.remove({pedido: preco})
        self.__calculo_mesa__(preco, "sub")

    def pagar(self, ten4cent):
        for produto in self.descricao_produtos:
            print(produto)
        if ten4cent:
            tip = round((self.valor_da_conta * 0.1), 2)
        else:
            tip = 0

        print(f"Pedidos: {round(self.valor_da_conta, 2)}")
        print(f"Gorjeta: {tip}")
        print(f"O total da conta foi: {round(self.valor_da_conta, 2) + tip}")
        return round(self.valor_da_conta, 2) + tip
