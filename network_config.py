import json
import re
import random
import sys

# Predefined subnets
IPv4_SUBNET = "192.168.1.0/24"
IPv6_SUBNET = "2001:db8::/64"

# Lease database (simulating with a Python dictionary)
lease_db = {}

def validate_mac(mac):
    """Validate MAC address format."""
    pattern = re.compile(r'([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}')
    return bool(pattern.match(mac))

def generate_ipv4():
    """Generate a random IPv4 address in the predefined subnet."""
    return f"192.168.1.{random.randint(10, 254)}"

def generate_ipv6(mac):
    """Generate an IPv6 address using EUI-64 format based on MAC."""
    mac_parts = mac.split(':')
    ipv6_address = f"2001:db8::{mac_parts[0]}{mac_parts[1]}:{mac_parts[2]}{mac_parts[3]}:{mac_parts[4]}{mac_parts[5]}"
    return ipv6_address

def assign_ip(mac, dhcp_version):
    """Assign an IP address based on DHCP version."""
    if not validate_mac(mac):
        return json.dumps({"error": "Invalid MAC address format"})
    
    if mac in lease_db:
        return json.dumps({
            "mac_address": mac,
            "assigned_ip": lease_db[mac]['ip'],
            "lease_time": lease_db[mac]['lease_time']
        })
    
    # Ensure DHCP version is valid before proceeding
    if dhcp_version == "DHCPv4":
        ip = generate_ipv4()  # Assign an IPv4 address
    elif dhcp_version == "DHCPv6":
        ip = generate_ipv6(mac)  # Assign an IPv6 address
    else:
        return json.dumps({"error": "Invalid DHCP version"})
    
    lease_time = 3600  # Lease time in seconds
    lease_db[mac] = {"ip": ip, "lease_time": lease_time}
    
    return json.dumps({
        "mac_address": mac,
        "assigned_ip": ip,
        "lease_time": lease_time
    })

# Collect input from the command line arguments (passed from process.php)
if len(sys.argv) < 3:
    print(json.dumps({"error": "Insufficient arguments provided"}))
    sys.exit(1)

mac_address = sys.argv[1]  # MAC address from the form input
dhcp_version = sys.argv[2]  # DHCP version from the form input

# Call the function and print the result
result = assign_ip(mac_address, dhcp_version)
print(result)

