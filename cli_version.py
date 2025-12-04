from validator import validate_ip
from geolocate import lookup_ip

def main():
    ip = input("Enter an IP address: ").strip()

    if not validate_ip(ip):
        print("Invalid IP address")
        return

    result = lookup_ip(ip)
    if not result:
        print("Could not retrieve geolocation data")
        return

    print("\nIP Geolocation Results")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
