from scapy.all import ARP, sr1

def check_arp_table(router_ip, expected_mac):
    # Crear un paquete ARP para solicitar la dirección MAC del router
    arp_request = ARP(pdst=router_ip)
    arp_response = sr1(arp_request, timeout=2, verbose=False)

    if arp_response:
        actual_mac = arp_response.hwsrc
        if actual_mac == expected_mac:
            print(f"Tabla ARP intacta. La dirección MAC del router es: {actual_mac}")
        else:
            print(f"ALERTA: La tabla ARP ha sido modificada. La dirección MAC esperada era: {expected_mac} pero se encontró: {actual_mac}")
    else:
        print("No se recibió respuesta del router.")

if __name__ == "__main__":
    router_ip = "192.168.0.1"  # IP del router
    expected_mac = "f8:8b:37:e8:0b:2d"  # Dirección MAC esperada del router
    check_arp_table(router_ip, expected_mac)
