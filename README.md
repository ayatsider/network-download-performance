# Network Factors Affecting File Download Performance

## Project Description

This project investigates how Round-Trip Time (RTT) and protocol type affect file download performance under different network conditions.

The experiment evaluates the relationship between network latency and download performance using three transfer protocols (FTP, HTTP, and HTTPS) across multiple server regions and different network environments.

---

## Research Question

How do RTT and protocol type affect file download performance across FTP, HTTP, and HTTPS under different network conditions?

---

## Experiment Setup

Measurements were collected using two client devices connected through different network environments.

Client A:

* Operating System: [ADD]
* Connection Type: [ADD]
* Network Type / ISP: [ADD]
* Device Specifications: [ADD]

Client B:

* Operating System: [ADD]
* Connection Type: [ADD]
* Network Type / ISP: [ADD]
* Device Specifications: [ADD]

Measurements were collected between 7:00 PM on May 28 and 7:00 PM on June 1.

For fair comparison between measurement environments, 1488 raw measurements were selected from each client dataset.

---

## Protocols

* FTP
* HTTP
* HTTPS

---

## Metrics

The experiment collects the following metrics:

* Timestamp
* Server region
* Host name
* Protocol type
* RTT (milliseconds)
* Download time (seconds)
* Measurement status

---

## Project Structure

```text
network-download-performance/

├── README.md
├── requirements.txt
├── measure.py
├── config/
│   └── servers.txt
├── raw_data/
│   ├── clientA_raw.csv
│   └── clientB_raw.csv
├── cleaned_data/
│   ├── clientA_cleaned.csv
│   └── clientB_cleaned.csv
├── analysis/
│   └── analysis.py
├── figures/
│   └── setup_diagram.png
└── docs/
    └── paper.pdf
```

---

## Requirements

Python 3.x

Required packages:

```text
pandas
matplotlib
numpy
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## How To Run The Measurement Script

Run:

```bash
python measure.py
```

The script:

* Measures RTT using Windows ping
* Downloads files using curl
* Tests three regions
* Tests FTP, HTTP, and HTTPS
* Repeats measurements every 600 seconds

---

## Data

Raw datasets are stored in:

```text
raw_data/
```

Processed / cleaned datasets are stored in:

```text
cleaned_data/
```

---

## Server List

Server URLs are stored inside:

```text
config/servers.txt
```

The experiment uses servers from:

* Germany
* Asia
* USA

Each server supports:

* FTP
* HTTP
* HTTPS

---

## Dataset Format

Each CSV record contains:

* timestamp
* region
* host
* protocol
* url
* rtt_ms
* download_time_sec
* status

---

## Reproducibility

To reproduce the experiment:

* Use Python 3.x
* Use Windows environment
* Ensure curl is installed and accessible from command line
* Use the same server list provided in config/servers.txt
* Use the same file size and file URLs
* Use the same measurement interval (600 seconds)
* Use FTP, HTTP, and HTTPS protocols
* Run:

```bash
python measure.py
```

The experiment should be performed using similar measurement duration and network conditions.

---

## Limitations

Measurements were collected under real-world network conditions.

Therefore, several factors may influence measurements:

* Network instability
* Timeout events
* Server unavailability
* Measurement interruptions
* Environmental variability

Failed measurements were retained within raw datasets but excluded from statistical analysis.

---

## License

This repository is provided for academic and research purposes.
