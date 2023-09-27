import io
import unittest
from unittest import TestCase
from unittest.mock import Mock, patch

from restaurant.Cliente import Cliente


class MyTestCase(TestCase):
    def test_fezer_um_pedido(self):
        mock_cozinha = Mock()

        cliente = Cliente(mesa=1)
        cliente.cozinha_object = mock_cozinha
        cliente.cozinha_object.cozinhar.return_value = ("pizza", 20)

        pedido_ready, tempo_de_preparo = cliente.fazer_um_pedido(
            "pizza", "12:00:00"
        )

        assert pedido_ready == "pizza"

    def test_verificar_gorjeta(self):
        cliente = Cliente(mesa=1)
        cliente.valor_da_conta = 100.0
        ten4cent = True
        assert cliente.pagar(ten4cent) == 110.0  # 10% de gorjeta

    def test_cancelar_um_pedido(self):
        cliente = Cliente(mesa=1)
        cliente.descricao_produtos = [{"pizza": 11.99}, {"lasanha": 10.49}]

        cliente.cancelar_pedido("pizza")

        assert cliente.descricao_produtos == [{"lasanha": 10.49}]

    def test_verififcar_se_refeicao_existe(self):
        mock_cozinha = Mock()

        cliente = Cliente(mesa=1)
        cliente.cozinha_object = mock_cozinha

        cliente.cozinha_object.cozinhar.return_value = (None, None)

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            pedido_ready, tempo_preparo = cliente.fazer_um_pedido(
                "cerveja", "12:00:00"
            )
            output = mock_stdout.getvalue()

        assert output == "Pedido não foi possível ser realizado\n"

    def test_calculo_mesa_subtrai_preco_corretamente(self):
        cliente = Cliente(mesa=1)
        cliente.valor_da_conta = 50.0
        cliente.__calculo_mesa__(10.0, "sub")
        assert cliente.valor_da_conta == 40.0


if __name__ == "__main__":
    unittest.main()
