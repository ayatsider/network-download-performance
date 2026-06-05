import csv
import time
import subprocess
from datetime import datetime
from pathlib import Path

INTERVAL_SECONDS = 600
OUTPUT_FILE = "protocol_measurements.csv"

SITES = [
    {
        "region": "Germany",
        "host": "mirror.netcologne.de",
        "paths": {
            "FTP": "ftp://mirror.netcologne.de/ubuntu/ls-lR.gz",
            "HTTP": "http://mirror.netcologne.de/ubuntu/ls-lR.gz",
            "HTTPS": "https://mirror.netcologne.de/ubuntu/ls-lR.gz"
        }
    },
    {
        "region": "Asia",
        "host": "aze.archive.ubuntu.com",
        "paths": {
            "FTP": "ftp://aze.archive.ubuntu.com/ubuntu/ls-lR.gz",
            "HTTP": "http://aze.archive.ubuntu.com/ubuntu/ls-lR.gz",
            "HTTPS": "https://aze.archive.ubuntu.com/ubuntu/ls-lR.gz"
        }
    },
    {
        "region": "USA",
        "host": "ftp.osuosl.org",
        "paths": {
            "FTP": "ftp://ftp.osuosl.org/pub/ubuntu/ls-lR.gz",
            "HTTP": "http://ftp.osuosl.org/pub/ubuntu/ls-lR.gz",
            "HTTPS": "https://ftp.osuosl.org/pub/ubuntu/ls-lR.gz"
        }
    }
]


def run_command(command, timeout=300):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), -1


def measure_rtt(host):
    command = ["ping", "-n", "4", host]

    stdout, stderr, code = run_command(command, timeout=30)

    for line in stdout.splitlines():
        if "Average" in line:
            return line.split("Average =")[-1].replace("ms", "").strip()

    return None


def measure_download_time(url):
    command = [
        "curl",
        "-L",
        "-o",
        "NUL",
        "-s",
        "-w",
        "%{time_total}",
        url
    ]

    stdout, stderr, code = run_command(command)

    if code == 0:
        return stdout, "success"
    else:
        return None, f"failed: {stderr}"


def create_csv_if_needed():
    if not Path(OUTPUT_FILE).exists():
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "region",
                "host",
                "protocol",
                "url",
                "rtt_ms",
                "download_time_sec",
                "status"
            ])


def run_measurement_round():
    for site in SITES:

        print(f"\n========== {site['region']} ==========")

        rtt = measure_rtt(site["host"])

        for protocol, url in site["paths"].items():

            print(f"\nTesting {protocol}")
            print(url)

            download_time, status = measure_download_time(url)

            row = [
                datetime.now().isoformat(timespec="seconds"),
                site["region"],
                site["host"],
                protocol,
                url,
                rtt,
                download_time,
                status
            ]

            with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(row)

            print(row)


if __name__ == "__main__":

    create_csv_if_needed()

    # أول تجربة مباشرة
    print("\nStarting initial test round...")
    run_measurement_round()

    # ثم كل 10 دقائق
    while True:
        print("\nSleeping for 10 minutes...")
        time.sleep(INTERVAL_SECONDS)

        print("\nStarting scheduled round...")
        run_measurement_round()