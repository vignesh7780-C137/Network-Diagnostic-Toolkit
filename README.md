# Network Diagnostic Toolkit

A Python-based command-line network diagnostic tool that performs basic DNS, connectivity, TCP port, and SSL/TLS checks for a specified hostname.

## Features

* DNS hostname resolution
* DNS record lookup

  * A
  * AAAA
  * MX
  * NS
  * CNAME
* Host reachability testing
* Ping latency statistics
* Packet loss calculation
* TCP port checking
* SSL/TLS connection testing
* TLS version detection
* SSL certificate expiration information
* Input validation
* Structured command-line output

## Technologies Used

* Python
* Python `socket` module
* Python `subprocess` module
* Python `ssl` module
* `dnspython`
* TCP/IP networking concepts
* DNS
* ICMP/ping
* TLS/SSL

## Project Structure

```text
Network-Diagnostic-Toolkit/
│
├── network_tool.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.x
* Internet connection
* `dnspython`

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd Network-Diagnostic-Toolkit
```

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the tool with:

```bash
python network_tool.py
```

Enter a hostname when prompted:

```text
Enter hostname: google.com
```

The tool then performs the configured network diagnostics and displays the results in the terminal.

## Example

```text
--- DNS RESOLUTION ---
[✓] DNS Resolution Successful
    Hostname  : google.com
    IP Address: xxx.xxx.xxx.xxx

--- CONNECTIVITY & LATENCY ---
[✓] Host is reachable

    Ping Statistics
    Packets sent     : 4
    Packets received : 4
    Packet loss      : 0%
    Average latency  : xx.xx ms

--- TCP PORT SCAN ---
[✓] Port 80  OPEN
[✓] Port 443 OPEN

--- SSL / TLS ---
[✓] SSL Connection Successful
    TLS Version: TLSv1.3

--- DNS RECORDS ---
    A Records:
        xxx.xxx.xxx.xxx

==========================================
        DIAGNOSTIC COMPLETE
==========================================
```

## Networking Concepts Demonstrated

### DNS

The tool resolves hostnames into IP addresses and retrieves common DNS record types.

### Connectivity and Latency

The tool uses ping to determine whether a host is reachable and calculates basic latency and packet-loss statistics.

### TCP Ports

The tool attempts TCP connections to selected common ports and reports whether they are open or closed/filtered.

### SSL/TLS

The tool establishes a secure connection to port 443 and retrieves information about the server's TLS connection and certificate.

## Security Considerations

This tool is intended for basic network diagnostics and educational purposes.

Only scan systems and hosts that you own or have permission to test. Port scanning and network diagnostics against systems without authorization may violate organizational policies or applicable laws.

User input is stripped and validated before processing.

## Limitations

* Port results can vary depending on firewalls and network filtering.
* Ping may be blocked by some hosts.
* DNS results can vary depending on the resolver being used.
* SSL certificate information depends on the availability of an HTTPS service.
* The current version is a command-line application.

## Future Improvements

Possible future versions could include:

* Flask REST API
* HTML/CSS/JavaScript dashboard
* JSON output
* Configurable port ranges
* More detailed SSL certificate information
* Response-time history
* Exportable diagnostic reports

## Learning Outcomes

This project provided practical experience with:

* Python networking
* DNS resolution
* TCP sockets
* Ping and latency measurement
* SSL/TLS connections
* Python package management
* Virtual environments
* Error handling
* Command-line application design
* GitHub project documentation

## License

This project is intended for educational and portfolio purposes.
