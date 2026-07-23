# FOP-monitor-linux
A Terminal-based Linux system monitor built with Python and Textual. Features CPU usage, memory usage, disk, processes, network, and per-port traffic monitoring in a full-screen TUI with live graphs, alerts, and customizable dashboards.

Inspired by tools like `btop`, `htop`, and `iftop`, built using Python and the Textual framework.

## Features

- Real-time CPU monitoring
- Memory and swap usage
- Disk usage and I/O statistics
- Live network bandwidth
- Per-interface traffic
- TCP/UDP connection statistics
- Top running processes
- Historical usage graphs
- Alert system for high resource usage
- Modern terminal user interface (TUI)
- Keyboard shortcuts
- Theme support

## Planned Features

- Per-port bandwidth monitoring
- Packet rate (PPS)
- Latency monitor
- Docker container monitoring
- Game server statistics
- Log viewer
- Remote monitoring
- Export metrics (JSON/CSV)
- Plugin system

## Tech Stack

- Python 3.13
- Textual
- Rich
- psutil
- asyncio
- Scapy (optional)
- Linux

## Installation

```bash
git clone https://github.com/raxerzsupreme/FOP-monitor-linux.git
cd FOP-monitor-linux

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Project Structure

```
FOP-monitor-linux/
├── app.py
├── collectors/
├── widgets/
├── utils/
├── assets/
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] Basic TUI Layout
- [ ] CPU & Memory Widget
- [ ] Disk Monitor
- [ ] Network Interface Monitor
- [ ] Process Viewer
- [ ] Historical Graphs
- [ ] Alert System
- [ ] Per-Port Statistics
- [ ] Configuration Support
- [ ] Release v1.0

## License

MIT
