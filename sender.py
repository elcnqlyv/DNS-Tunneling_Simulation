message = input("Enter message: ")

hex_message = message.encode("utf-8").hex()

for i in range(0, len(hex_message), 4):
    chunk = hex_message[i:i + 4]
    print(f"{chunk}.example.com")