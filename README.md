# Tarea
Últimos dos programas del semestre

# ARP Spoofing y Detección de Modificación en la Tabla ARP

Este repositorio contiene dos scripts en Python:

1. **ARP Spoofing**: Ataca a una máquina víctima modificando su dirección MAC registrada para el router en su tabla ARP.
2. **Detección de Modificación en la Tabla ARP**: Verifica si la tabla ARP de la máquina ha sido manipulada.

## Requisitos

- Python 3.x
- Biblioteca `scapy`

Puedes instalar `scapy` utilizando `pip`:

```sh
pip install scapy
```

## ARP Spoofing

El script `arp_spoof.py` envía paquetes ARP falsos para engañar a la máquina víctima y hacerle creer que la dirección MAC del atacante es la del router.

### Uso

1. Abre el archivo `arp_spoof.py` y reemplaza las siguientes variables con las direcciones adecuadas para tu red:

- `attacker_mac`: La dirección MAC de la máquina atacante.
- `target_ip`: La dirección IP de la máquina víctima.
- `spoof_ip`: La dirección IP del router.

2. Ejecuta el script con permisos de superusuario:

```sh
sudo python arp_spoof.py
```

3. Para detener el ataque, presiona `Ctrl + C`.

## Detección de Modificación en la Tabla ARP

El script `check_arp.py` verifica si la tabla ARP de la máquina ha sido manipulada al comparar la dirección MAC actual del router con una dirección MAC conocida y esperada.

### Uso

1. Abre el archivo `check_arp.py` y reemplaza las siguientes variables con las direcciones adecuadas para tu red:

- `router_ip`: La dirección IP del router.
- `expected_mac`: La dirección MAC esperada del router.

2. Ejecuta el script:

```sh
python check_arp.py
```

## Notas

- **Permisos de superusuario:** Ejecutar scripts de manipulación de red generalmente requiere permisos de superusuario, por lo que deberás ejecutarlos con `sudo` en sistemas Unix/Linux.
- **Dirección MAC y dirección IP:** Asegúrate de reemplazar las direcciones IP y MAC con las correctas para tu red y dispositivos.
- **Consideraciones legales y éticas:** Realizar ataques de ARP spoofing sin autorización es ilegal y antiético. Solo realiza pruebas en entornos controlados y con permiso explícito de los dueños de la red.

