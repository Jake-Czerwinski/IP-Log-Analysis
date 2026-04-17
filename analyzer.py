import re

def main():
    log_file = input("Enter the log file name: ").strip()
    failed_count = 0
    ip_counts = {}

    try:
        with open(log_file, "r") as file:
            for line in file:
                if "failed" in line.lower():
                    failed_count += 1
                    ip_match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)

                    if ip_match:
                        ip_address = ip_match.group()
                    else:
                        continue

                    if ip_address in ip_counts:
                        ip_counts[ip_address] += 1
                    else:
                        ip_counts[ip_address] = 1
    except FileNotFoundError:
        print("Error: File not found.")
        return

    print(f"\nTotal failed login attempts: {failed_count}")

    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

    print("\nFailed login attempts by IP:")
    for ip, count in sorted_ips:
        print(f"{ip}: {count}")

    print("\nSuspicious IPs:")
    for ip, count in sorted_ips:
        if count >= 3:
            print(f"{ip} flagged as suspicious with {count} failed attempts")

    with open("report.txt", "w") as report:
        report.write("Log Analysis Report\n")
        report.write("=" * 40 + "\n")

        report.write(f"\nTotal failed login attempts: {failed_count}\n")

        report.write("\nFailed login attempts by IP:\n")
        for ip, count in sorted_ips:
            report.write(f"{ip}: {count}\n")

        report.write("\nSuspicious IPs:\n")
        for ip, count in sorted_ips:
            if count >= 3:
                report.write(f"{ip} flagged as suspicious with {count} failed attempts\n")

    print("\nReport saved to report.txt")


if __name__ == "__main__":
    main()