# MQTT Lab

Python-based MQTT lab using the paho-mqtt client library.

This repository contains small publisher/subscriber scripts and packet captures for experimenting with:
- Topic hierarchies
- QoS levels (0 and 1)
- Keepalive behavior
- Last Will and Testament (LWT)
- Persistent sessions (clean session disabled)

## Repository Structure

- src/: MQTT publisher and subscriber scripts
- captures/: Wireshark packet capture files (.pcapng)
- notes/: Extra notes (currently empty)
- requirements.txt: Python dependency list

## Requirements

- Python 3.9+
- An MQTT broker running on localhost:1883 (or update the broker host in the scripts)

Dependency:
- paho-mqtt==2.1.0

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Scripts Overview

- src/subscriber.py: General subscriber for topics under spain/+/+, france/+/+, and status/#
- src/publisher.py: Publisher for spain/madrid/temp with keepalive=30 and LWT configured
- src/publisher2.py: Second publisher for france/paris/* topics with keepalive=120 and LWT configured
- src/subscriber_exercise8.py: Subscriber for Exercise 8 using clean_session=False and client_id=subscriber_exercise8
- src/publisher_qos0.py: Exercise 8 publisher for QoS 0 message
- src/publisher_qos1.py: Exercise 8 publisher for QoS 1 message

## Running the Main Scenario

Open separate terminals in the project root.

1. Start subscriber:

```bash
python src/subscriber.py
```

2. Start first publisher:

```bash
python src/publisher.py
```

3. Start second publisher:

```bash
python src/publisher2.py
```

Notes:
- The subscriber in src/subscriber.py disconnects gracefully after 5 minutes.
- To test LWT behavior, terminate a publisher abruptly (for example with kill -9).

## Packet Captures

The captures/ directory contains .pcapng files for different lab steps and QoS scenarios, including:
- mqtt1.pcapng ... mqtt8_qos1.pcapng
- secondPart.pcapng

These files can be opened with Wireshark for protocol analysis.

## Configuration Notes

All scripts currently connect to:
- host: localhost
- port: 1883

If your broker is remote, update the connect(...) host value in the scripts under src/.
