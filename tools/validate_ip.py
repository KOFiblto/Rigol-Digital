import sys
import re

def validate_ip(ip):
    # Regular expression to match a valid IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    
    match = re.match(pattern, ip)
    if not match:
        return False

    # Check if each segment is in the range 0-255
    for part in match.groups():
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True

def replace_ip_in_file(ip, filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Replace the IP address in line 14
    new_content = re.sub(r'TCPIP0::.*::INSTR', f'TCPIP0::{ip}::INSTR', content)

    with open(filename, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    ip = sys.argv[1] if len(sys.argv) > 1 else ""
    
    if validate_ip(ip):
        replace_ip_in_file(ip, "Rigol1000z/run.py")
        input("IP has been replaced. Press any key to close...")
        sys.exit(0)  # Exit with status code 0 (success)
    else:
        sys.exit(1)  # Exit with status code 1 (failure)
