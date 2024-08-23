import requests

def mac_vendor(mac):
    '''Trace MAC Address Vendor'''
    URL = f"https://api.macvendors.com/{mac}"
    vendor = requests.get(URL).text
    return vendor


if __name__ == "__main__":

    your_mac = input("Input your MAC Address : ")
    result = mac_vendor(your_mac)
    print(f"Your MAC Vendor = {result}")
