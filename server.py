from socketserver import *

host = 'localhost'
port = 9092
addr = (host, port)

# обработчик запросов UDP подкласс DatagramRequestHandler
# Этот класс работает аналогично классу TCP, за исключением того,
# self.request состоит из пары данных и сокета клиента,
# так как нет никакой связи адрес, клиент должен быть явно указан при отправке данных обратно через SendTo()
class MyUDPHandler(DatagramRequestHandler):

    # функция handle делает всю работу, необходимую для обслуживания запроса.
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        print('client send: ', data)

        # sendto - отправка сообщения UDP
        socket.sendto(b'Приветик от UDP сервера', self.client_address)


if __name__ == "__main__":
    # Создаем экземпляр класса
    server = UDPServer(addr, MyUDPHandler)

    print('Сервер запущен, приветик')
    # serve_forever - запускаем сервер
    server.serve_forever()