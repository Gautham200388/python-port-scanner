
# Python Network Port Scanner

A Python-based TCP port scanner that checks selected ports on a target IP address and saves scan results to a JSON report.

## Features

- Validates target IP addresses
- Offers common-port and full-range scan modes
- Scans TCP ports and identifies successful connections
- Removes duplicate ports from selected lists
- Maps common port numbers to service names
- Displays scan progress
- Counts open, closed, and timed-out or unreachable ports
- Exports results to JSON with a timestamp

## Technologies

- Python 3
- Socket programming
- JSON
- IP address validation

## Requirements

- Python 3.12 or compatible Python 3 version
- No third-party packages required

## How to Run

Open a terminal in the project directory and run:

    py port_scanner.py

Enter the target IP address, then choose a scan mode:

1. Common ports
2. All TCP ports

The scan results are saved to `scan_report.json`.

## Scan Statuses

- **OPEN:** A TCP connection was established.
- **CLOSED:** The connection was explicitly refused.
- **FILTERED_OR_UNREACHABLE:** The connection timed out or another socket error prevented a successful connection. This status does not prove that a firewall is filtering the port.

## Limitations

This is a learning project that performs basic TCP connection checks. Service names are inferred from common port mappings; they do not confirm which service is actually running.

Localhost testing on Windows may produce unexpected timeouts for some ports. Results should be verified when accuracy matters.

## Responsible Use

Scan only computers and networks you own or have explicit permission to test. This tool is not a full vulnerability scanner and does not exploit services.
