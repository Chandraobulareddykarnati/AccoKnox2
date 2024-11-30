import re
from collections import Counter

LOG_FILE = 'access.log'

def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    ip_addresses = []
    requested_pages = []
    error_404_count = 0

    for log in logs:
        parts = re.split(r'\s+', log)
        if len(parts) < 9:
            continue
        ip_addresses.append(parts[0])
        requested_pages.append(parts[6])  # Assuming the request path is the 7th field
        if parts[8] == "404":  # Assuming the status code is the 9th field
            error_404_count += 1

    return ip_addresses, requested_pages, error_404_count

def generate_report(ip_addresses, requested_pages, error_404_count):
    ip_count = Counter(ip_addresses)
    page_count = Counter(requested_pages)

    print("Top 5 IPs:")
    for ip, count in ip_count.most_common(5):
        print(f"{ip}: {count} requests")

    print("\nTop 5 Requested Pages:")
    for page, count in page_count.most_common(5):
        print(f"{page}: {count} requests")

    print(f"\nTotal 404 Errors: {error_404_count}")

if __name__ == "__main__":
    try:
        ips, pages, errors = parse_log(LOG_FILE)
        generate_report(ips, pages, errors)
    except FileNotFoundError:
        print(f"Log file '{LOG_FILE}' not found.")
