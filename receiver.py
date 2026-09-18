import sys

hex_message = ""

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    chunk = line.split(".")[0]
    hex_message += chunk

message_bytes = bytes.fromhex(hex_message)
message = message_bytes.decode("utf-8")

print("Recovered message:", message)