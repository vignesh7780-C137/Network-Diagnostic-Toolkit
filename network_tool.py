import socket
import subprocess
import platform
import ssl
from datetime import datetime

import dns.resolver


def print_header():
    print()
    print("╔══════════════════════════════════════════╗")
    print("║       NETWORK DIAGNOSTIC TOOL            ║")
    print("╚══════════════════════════════════════════╝")
    print()


def print_section(title):
    print()
    print(f"--- {title} ---")


def resolve_hostname(hostname):
    """Resolve a hostname to an IP address."""

    print_section("DNS RESOLUTION")

    try:
        ip_address = socket.gethostbyname(hostname)

        print("[✓] DNS Resolution Successful")
        print(f"    Hostname  : {hostname}")
        print(f"    IP Address: {ip_address}")

        return ip_address

    except socket.gaierror:
        print("[X] DNS Resolution Failed")
        print("    Could not resolve the hostname.")

        return None


def ping_host(hostname):
    """Test reachability and calculate ping statistics."""

    print_section("CONNECTIVITY & LATENCY")

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", hostname]
    else:
        command = ["ping", "-c", "4", hostname]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[X] Host is not reachable.")
        return

    print("[✓] Host is reachable")

    latencies = []

    for line in result.stdout.splitlines():
        if "time=" in line:
            try:
                time_part = line.split("time=")[1]
                latency = float(time_part.split("ms")[0])
                latencies.append(latency)
            except (ValueError, IndexError):
                pass

    if latencies:
        packets_sent = 4
        packets_received = len(latencies)
        packet_loss = (
            (packets_sent - packets_received)
            / packets_sent
        ) * 100

        print()
        print("    Ping Statistics")
        print(f"    Packets sent     : {packets_sent}")
        print(f"    Packets received : {packets_received}")
        print(f"    Packet loss      : {packet_loss:.0f}%")
        print(f"    Minimum latency  : {min(latencies):.2f} ms")
        print(f"    Average latency  : {sum(latencies) / len(latencies):.2f} ms")
        print(f"    Maximum latency  : {max(latencies):.2f} ms")

    else:
        print("[X] Could not calculate latency statistics.")


def scan_ports(ip_address):
    """Check common TCP ports."""

    print_section("TCP PORT SCAN")

    ports = [21, 22, 25, 80, 443]

    for port in ports:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(2)

        result = sock.connect_ex(
            (ip_address, port)
        )

        if result == 0:
            print(f"[✓] Port {port:<3} OPEN")
        else:
            print(f"[X] Port {port:<3} CLOSED or FILTERED")

        sock.close()


def check_ssl(hostname):
    """Check HTTPS connection and certificate."""

    print_section("SSL / TLS")

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_socket:

                certificate = secure_socket.getpeercert()
                tls_version = secure_socket.version()

                print("[✓] SSL Connection Successful")
                print(f"    TLS Version: {tls_version}")

                if certificate:
                    expiry_date = certificate["notAfter"]

                    expiry_datetime = datetime.strptime(
                        expiry_date,
                        "%b %d %H:%M:%S %Y %Z"
                    )

                    print(
                        f"    Certificate expires: "
                        f"{expiry_datetime}"
                    )

    except Exception as error:
        print("[X] SSL Check Failed")
        print(f"    Reason: {error}")


def dns_records(hostname):
    """Look up common DNS record types."""

    print_section("DNS RECORDS")

    record_types = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "CNAME"
    ]

    for record_type in record_types:

        print(f"\n    {record_type} Records:")

        try:
            answers = dns.resolver.resolve(
                hostname,
                record_type
            )

            for answer in answers:
                print(f"        {answer}")

        except (
            dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers,
            dns.resolver.LifetimeTimeout
        ):
            print("        No record found")


def main():
    """Run the Network Diagnostic Toolkit."""

    print_header()

    hostname = input("Enter hostname: ").strip()

    if not hostname:
        print("\n[X] Hostname cannot be empty.")
        return

    ip_address = resolve_hostname(hostname)

    if ip_address is None:
        return

    ping_host(hostname)
    scan_ports(ip_address)
    check_ssl(hostname)
    dns_records(hostname)

    print()
    print("==========================================")
    print("        DIAGNOSTIC COMPLETE")
    print("==========================================")


if __name__ == "__main__":
    main()