import sys


KEY = 0x2A


print("Enter message: ", end="", file=sys.stderr)
message = input()

if len(message) > 20:
    print("Message must be 20 characters or less.")
    exit()

message_bytes = message.encode("utf-8")

encrypted_bytes = bytes(byte ^ KEY for byte in message_bytes)

hex_message = encrypted_bytes.hex()

for i in range(0, len(hex_message), 4):
    chunk = hex_message[i:i + 4]
    print(f"{chunk}.example.com")