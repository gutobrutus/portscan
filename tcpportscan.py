import socket
import sys
from datetime import datetime
from time import strftime

print("""
 ____            _     ____                    _____ ____ ____  
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __   |_   _/ ___|  _ \ 
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \    | || |   | |_) |
|  __/ (_) | |  | |_   ___) | (_| (_| | | | |   | || |___|  __/ 
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|   |_| \____|_|    
                                                            
""")
try:
    host = input("Digite o host ou ip a ser verificado: ")
    min_port = int(input("Informe a primeira porta do intervalo: "))
    max_port = int(input("Informe a última porta do intervalo: "))
    try:
        if min_port >= 0 and max_port >= 0 and max_port >= min_port:
            pass
        else:
            print("\n Intervalo de portas inválido")
            print("Saindo...")
            sys.exit(1)
    except Exception:
        print("\n Intervalo de portas inválido ou outro erro no intervalo")
        print("Saindo...")
        sys.exit(1)
except KeyboardInterrupt:
    print("\n Usuário solicitou interrupção...")
    print("Saindo...")
    sys.exit(1)

ports = range(min_port, max_port + 1)
start_time = datetime.now()

print("Iniciando o scan de portas no host {} em {} \n".format(host, strftime("%H:%M:%S")))
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((host, port))
    if code == 0:
        print("A porta {} está aberta".format(str(port)))

stop_time = datetime.now()
total_time = stop_time - start_time
print("Scan finalizado - Tempo total: {}".format(str(total_time)))