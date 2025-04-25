# arp_spoof_local

This repository contains a Python script (`arp_spoofing.py`) designed to perform ARP (Address Resolution Protocol) spoofing attacks on a local network. ARP spoofing, also known as ARP poisoning, is a technique used to associate the attacker's MAC address with the IP address of another host (like the gateway or a specific target) on the network. This can allow the attacker to intercept network traffic intended for the spoofed IP address.

**Warning:** This script is intended for **educational and ethical security testing purposes only** on networks you have explicit permission to test. **Unauthorized use of this script on networks you do not own or have permission to test is illegal and unethical.** The author(s) assume no responsibility for any misuse or damage caused by this script.

## Functionality

The `arp_spoofing.py` script operates as follows:

1.  **ARP Response Packets:** It continuously crafts and sends ARP response packets.
2.  **Target Deception:** These packets are forged to make the target machine believe that the attacker's machine (running this script) has the MAC address associated with the `spoof_ip` (typically the network gateway).
3.  **Traffic Redirection (Potential):** If successful, this can lead to the target machine sending its network traffic to the attacker's machine instead of the intended destination.

**Important Considerations:**

* **Dependencies:** This script requires the `scapy` library to be installed. You can install it using pip:
    ```bash
    pip install scapy
    ```
    You might need to run this command with administrator privileges (`sudo pip install scapy` on Linux/macOS).
* **Root/Administrator Privileges:** Running this script typically requires root or administrator privileges as it involves sending raw network packets.
* **Target Information:** You need to know the IP address (`target_ip`) and MAC address (`target_mac`) of the target device you wish to spoof. You also need the IP address of the machine you want the target to associate with your MAC address (`spoof_ip`), which is often the network gateway.
* **Continuous Attack:** The script, as currently written, runs indefinitely, continuously sending ARP response packets. You will need to manually interrupt it (e.g., using `Ctrl+C`).
* **Network Impact:** ARP spoofing can disrupt network communication and may be easily detectable on a monitored network.
* **Ethical Use:** Use this script only on networks you have explicit permission to test.

## Usage

1.  **Install Scapy:** If you haven't already, install the `scapy` library:
    ```bash
    pip install scapy
    ```
2.  **Modify Parameters:** Open the `arp_spoofer.py` file and carefully modify the following variables in the "**Attack Parameters**" section:
    * `target_ip`: Replace `"192.168.1.112"` with the actual IP address of the target device on your local network.
    * `target_mac`: Replace `"14:87:6a:07:72:c4"` with the actual MAC address of the target device. You can usually find this information using tools like `arp -a` (Windows) or `arp -n` (Linux/macOS) on your local network.
    * `spoof_ip`: Replace `"192.168.1.1"` with the IP address you want the target to associate with your MAC address. This is often the IP address of the network gateway (router).
3.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved `arp_spoofer.py`, and run it with the necessary privileges (root or administrator):
    ```bash
    sudo python arp_spoofer.py  # Linux/macOS
    python arp_spoofer.py       # Windows (run as administrator)
    ```
4.  **Interrupt the Attack:** To stop the script, press `Ctrl+C` in the terminal.

**Disclaimer:**

This script is provided for educational and ethical security testing purposes only. The author(s) assume no responsibility for any misuse or damage caused by its use. By using this script, you acknowledge that you are responsible for ensuring your actions comply with all applicable laws and regulations.
