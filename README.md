# ArpSpoof
Herramienta para realizar pruebas de envenenamiento de tablas arp, también este tipo de pruebas es conocido como ARPSpoof o ARPPoisoning.
# Requisitos
- Python 3.7.8.
- setuptools.
# Dependencias
- colorama==0.4.4.
- scapy==2.4.5.

# Configuración
Antes de utilizar el script se debe establecer el redirecionamiento de IP (IP Forwarding). aquí se explicará tanto para sistemas windows como para linux. Cabe mencionar que el script fue probado en Kali Linux y Windows 10.

## Configuración en windows.
- Abra una commamd promp (cmd) con permiso de administración.

- Ejecute el siguiente comando: netsh. Se cagara la consola de la utilidad netsh.exe en la ventana de comandos.
 
![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto1.PNG)

- Ingrese el siguiente comando: interface ipv4. en la venta de comando se estableceran la interfaces de IPv4.

- ![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto2.PNG)

- Luego, ingrese el comando: show interface. Se mostrara un listado de las interfaces de red.
 
![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto3.PNG)

- Verificar si la opción IP forward la interface activa en su ordenador, esta habilitada o deshabilitada. En este caso se verificará la interface número 9 con el siguiente comando: show interface 9. Donde el número 9 hace referencia al ID de la interface que se muestra en la columna "Ind".
 
![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto4.PNG)

En este caso la interface se muestra deshabilitada (Disabled), en la foto se muestra resaltada con amarillo. Si su sistema operativo esta configurado en español la opción se denomina "reenvío", por el contrario si esta configurado en inglés la opción se denomina "Forwarding".

- Por último, debemos cambiar el parámetro de "reenvío" o "Forwarding" a enabled. Con el siguiente comando: set interface 9 forwarding="enabled".
 
![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto5.PNG) 

- Finalmente, puede ejecutar el comando: show interface 9, para ver si los cambios se realizaron exitosamente.
 
![alt text](https://github.com/LW-Homeless/ArpSpoof/blob/main/img/foto6.PNG)

## Configuración en Linux.
- Abra una terminal y ejecute el siguiente comando: echo 1 > /proc/sys/net/ipv4/ip_forward .

- Luego, verifique que los cambios se han realizado con exito. Con el siguiente comando: cat  /proc/sys/net/ipv4/ip_forward . Al ejecutar el comando se deberia imprimir en la terminal el número 1, lo que significa que el cambio se realizo con exito.

# Instrucciones de uso
- Descarga o clona el repositorio.
- Instala las dependencia con el siguiente comando.
```
pip install -r requirements.txt
```
- Luego, ejecuta el archivo Main.py con el siguiente comando.
```
python main.py -t [IP_Obejetivo]  -h [IP Host]
```
Ejemplo de ejecución:
```
python main.py -t 10.10.10.1 -h 10.10.10.23
```
El comando anterior comenzará a realizar el envenamiento de las tablas arp del objetivo y host.

------------

Para detener la ejecución del script precione la combinación de teclas Ctrl+C.
