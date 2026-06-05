# Network Factors Affecting File Download Performance

## Project Description

This project investigates how Round-Trip Time (RTT), geographic location, and transfer protocols affect file download performance under real-world Internet conditions.

The experiment evaluates the relationship between network latency and download performance using FTP, HTTP, and HTTPS across geographically distributed servers located in Europe, Asia, and North America.

---

## Research Question

**How do RTT, geographic location, and transfer protocols affect file download performance under real-world Internet conditions?**

---

## Experimental Setup

Measurements were collected using an HP 340S G7 notebook connected through a fiber-optic Internet connection.

### Measurement Environment

- Operating System: Windows 11 Pro
- Python Version: Python 3.12.5
- Processor: Intel Core i5-1035G1
- Memory: 16 GB RAM
- Connection Type: Wi-Fi over fiber-optic network
- Measurement Location: Hebron, Palestine

Measurements were collected between:

- Start: May 29, 2026 (18:43:02)
- End: June 1, 2026 (19:14:35)

The measurement campaign resulted in **3239 measurement rounds**.

---

## Protocols

- FTP
- HTTP
- HTTPS

---

## Collected Data

Each measurement record includes:

- Timestamp
- Geographic region
- Host name
- Protocol type
- RTT (milliseconds)
- Download time (seconds)
- Measurement status

---

## Server Regions

The experiment uses mirror servers located in:

- Europe (Germany)
- Asia (Azerbaijan)
- North America (USA)

All servers provide access to the same file:

```text
ls-lR.gz (~35.6 MB)
