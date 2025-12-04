import requests

def lookup_ip(ip):
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] != "success":
            return None

        return {
            "IP": ip,
            "Country": data["country"],
            "Region": data["regionName"],
            "City": data["city"],
            "ISP": data["isp"],
            "Latitude": data["lat"],
            "Longitude": data["lon"]
        }

    except requests.RequestException:
        return None
