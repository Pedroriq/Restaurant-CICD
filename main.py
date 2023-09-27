from datetime import datetime

from Cliente import Cliente

if __name__ == "__main__":

    counter = 0
    add_cliente = True
    lista_client = []
    while add_cliente:

        init_option = int(input('1. Adicionar Cliente\n'
                            '2. Cliente Existente\n'
                            '3. Sair\n'))
        print('\n-----------------------------------------------\n')
        if init_option == 1 or init_option == 2:

            if init_option == 1:
                cliente = Cliente(counter)
                lista_client.append(cliente)
                counter += 1

            elif init_option == 2:
                mesa = int(input('Selecionar mesa: '))
                print('\n-----------------------------------------------\n')
                cliente = lista_client[mesa]

            add_pedido = True
            while add_pedido:
                pedido_option = int(input('1. Adicionar Pedido\n'
                                      '2. Cancelar Pedido\n'
                                      '3. Fechar Conta\n'
                                      '4. Sair da area de pedidos\n'))
                print('\n-----------------------------------------------\n')
                if pedido_option == 1:
                    new_pedido = input('Pedido: ')
                    print('\n-----------------------------------------------\n')
                    pedido_ready, tempo_de_preparo = cliente.fazer_um_pedido(new_pedido, datetime.now().strftime("%H:%M:%S"))
                    print('\n-----------------------------------------------\n')
                elif pedido_option == 2:
                    canceled_pedido = input('Pedido: ')
                    print('\n-----------------------------------------------\n')
                    cliente.cancelar_pedido(canceled_pedido)
                elif pedido_option == 3:
                    gorjeta = input('Gorjeta (Y/N): ')
                    print('\n-----------------------------------------------\n')
                    if gorjeta == 'Y':
                        ten4cent = True
                    else:
                        ten4cent = False
                    cliente.pagar(ten4cent)
                else:
                    break

        else:
            break

