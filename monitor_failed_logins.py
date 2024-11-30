import re

def monitor_logs(log_file):
    failed_logins = {}
    with open(log_file, 'r') as file:
        for line in file:
            if 'Failed login' in line:
                ip_address = extract_ip(line)
                if ip_address in failed_logins:
                    failed_logins[ip_address] += 1
                else:
                    failed_logins[ip_address] = 1
    return failed_logins

def extract_ip(log_entry):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    match = re.search(ip_pattern, log_entry)
    return match.group(0) if match else None


log_file = 'server_logs.txt'
failed_logins = monitor_logs(log_file)
print(failed_logins)
