import datetime
import io
from unittest import TestCase
from unittest.mock import patch

from Cozinha import Cozinha, cancelar_pedido_na_cozinha


class MyTestCase(TestCase):
    def test_cozinhar_sucesso(self):
        cozinha = Cozinha()

        pedido_ready, tempo_preparo = cozinha.cozinhar(
            "salada Caesar", datetime.datetime.now().strftime("%H:%M:%S")
        )

        assert pedido_ready == "salada Caesar"
        assert tempo_preparo == 5

    def test_cozinhar_falha(self):
        cozinha = Cozinha()

        pedido_ready, tempo_preparo = cozinha.cozinhar(
            "cerveja", datetime.datetime.now().strftime("%H:%M:%S")
        )

        assert pedido_ready is None
        assert tempo_preparo is None

    def test_output_cancelar_pedido(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            cancelar_pedido_na_cozinha("sushi", 1)
            output = mock_stdout.getvalue()

        assert output == "Pedido sushi da mesa 1 cancelado\n"

    def test_de_cozimento_retorno(self):
        cozinha = Cozinha()

        cozinha.pedido_ser_preparado = "espaguete a bolonhesa"

        output = cozinha.cozimento()

        assert output == "espaguete a bolonhesa"

    def test_de_cozimento_output(self):
        cozinha = Cozinha()

        cozinha.pedido_ser_preparado = "espaguete a bolonhesa"

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            cozinha.cozimento()
            output = mock_stdout.getvalue()

        assert (
            output
            == "Pedido espaguete a bolonhesa está cozinhando - TEMPO: 10 SEGUNDOS\n"
        )
