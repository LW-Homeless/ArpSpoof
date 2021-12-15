# ArpSpoof
Herramienta para realizar pruebas de envenenamiento de tablas arp, también este tipo de pruebas es conocido como ARPSpoof o ARPPoisoning.
# Requisitos
- Python 3.7.8.
- setuptools.
# Dependencias
- colorama==0.4.4.
- scapy==2.4.5.

# Configuración
Antes de utilizar el script se debe establecer el redirecionamiento de IP (IP Forwarding). aquí se explicará para sistema operativo linux. Cabe mencionar que el script fue probado en Kali Linux.


## Configuración en Linux.
- Abra una terminal y ejecute el siguiente comando: echo 1 > /proc/sys/net/ipv4/ip_forward .

![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto_kali_1.PNG)

- Luego, verifique que los cambios se han realizado con exito. Con el siguiente comando: cat  /proc/sys/net/ipv4/ip_forward . Al ejecutar el comando se deberia imprimir en la terminal el número 1, lo que significa que el cambio se realizo con exito.

![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto_kali_2.PNG)

# Instrucciones de uso
- Descarga o clona el repositorio.
- Instala las dependencia con el siguiente comando.
```
pip install -r requirements.txt
```
- Luego, ejecuta el archivo main.py con el siguiente comando.
```
python main.py -t [IP_Obejetivo]  -g [IP_Gateway]
```
Ejemplo de ejecución:
```
python main.py -t 10.10.10.23 -g 10.10.10.1
```
El comando anterior comenzará a realizar el envenamiento de las tablas arp del objetivo y Gateway.

------------

Para detener la ejecución del script precione la combinación de teclas Ctrl+C.
