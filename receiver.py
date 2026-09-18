import sys

KEY = 0x2A

hex_message = ""

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    chunk = line.split(".")[0]
    hex_message += chunk

encrypted_bytes = bytes.fromhex(hex_message)

decrypted_bytes = bytes(byte ^ KEY for byte in encrypted_bytes)

message = decrypted_bytes.decode("utf-8")

print("Recovered message:", message)