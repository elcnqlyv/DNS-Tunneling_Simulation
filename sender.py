message = input("Enter message: ")

if len(message) > 20:
    print("Message must be 20 characters or less.")
    exit()

hex_message = message.encode("utf-8").hex()

for i in range(0, len(hex_message), 4):
    chunk = hex_message[i:i + 4]
    print(f"{chunk}.example.com")