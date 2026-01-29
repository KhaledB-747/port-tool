 Port Tool 🛠️

Simple Python tool to lookup services by port number or scan port ranges.

 Features
- Get service name by port number
- Get port number by service name
- Scan port ranges
- Clean table output using pandas
- CLI interface with argparse

 Usage

```bash
python port_tool.py -m 80
python port_tool.py -n http
python port_tool.py -s 20 -e 100
