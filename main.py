from datetime import datetime

from Cliente import Cliente

if __name__ == "__main__":
    cliente_1 = Cliente(1)

    pedido_ready_1, tempo_de_preparo_1 = cliente_1.fazer_um_pedido(
        "sushi", datetime.now().strftime("%H:%M:%S")
    )
    pedido_ready_2, tempo_de_preparo_2 = cliente_1.fazer_um_pedido(
        "carbonara", datetime.now().strftime("%H:%M:%S")
    )

    cliente_1.cancelar_pedido(pedido_ready_1)

    cliente_1.pagar(ten4cent=True)
