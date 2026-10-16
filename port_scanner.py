
import socket
import json
import ipaddress
from datetime import datetime


# Ask for the target IP address
target_ip = input("Enter target IP address: ").strip()

# Validate the IP address
try:
    ipaddress.ip_address(target_ip)
except ValueError:
    print("Invalid IP address. Please enter a valid IPv4 or IPv6 address.")
    raise SystemExit


# Check the status of a TCP port
def scan_port(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)

    try:
        client.connect((target_ip, port))
        return "open"

    except ConnectionRefusedError:
        return "closed"

    except socket.timeout:
        return "filtered_or_unreachable"

    except OSError:
        return "filtered_or_unreachable"

    finally:
        client.close()


# Choose scan mode
print("\nChoose scan mode:")
print("1. Common ports")
print("2. All TCP ports (1-65535)")

while True:
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        ports = [
    21, 22, 23, 25, 53, 80, 110, 143,
    443, 445, 3306, 3389, 5432, 8080, 8443
]
        break

    elif choice == "2":
        ports = list(range(1, 65536))
        break

    else:
        print("Invalid choice. Enter 1 or 2.")


# Common port-to-service mappings
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT"
}

open_ports = []
scan_results = []


# Run the scan
print("\nPython Network Port Scanner")
print("Target:", target_ip)
print("-" * 45)


for index, port in enumerate(ports, start=1):
    service = services.get(port, "Unknown service")
    status = scan_port(port)

    print("Port", port, "-", service, "-", status.upper())

    if status == "open":
        open_ports.append(port)

    scan_results.append({
        "port": port,
        "service": service,
        "status": status
    })

    if index % 500 == 0 or index == len(ports):
        print(f"Progress: {index}/{len(ports)} ports scanned")



open_count = sum(1 for result in scan_results if result["status"] == "open")
closed_count = sum(1 for result in scan_results if result["status"] == "closed")
timeout_count = sum(
    1 for result in scan_results
    if result["status"] == "filtered_or_unreachable"
)

# Display the summary
print("-" * 45)
print("Scan complete")
print("Open ports:", open_count)
print("Closed ports:", closed_count)
print("Timed-out or unreachable ports:", timeout_count)
print("Open ports found:", len(open_ports))
print("Open ports:", open_ports)


# Build the JSON report


report = {
    "target_ip": target_ip,
    "scan_time": datetime.now().isoformat(timespec="seconds"),
    "total_ports_scanned": len(ports),
    "open_ports": open_ports,
    "summary": {
        "open": open_count,
        "closed": closed_count,
        "filtered_or_unreachable": timeout_count
    },
    "results": scan_results
}



# Save the report
with open("scan_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Scan report saved to scan_report.json")
