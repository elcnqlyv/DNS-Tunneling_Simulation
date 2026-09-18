# DNS Tunneling Simulation

A small Python project that demonstrates the basic concept of encoding data inside DNS subdomains.

This program only simulates DNS queries by printing them to the console. It does not send any network traffic.

## How it works

### Sender

The sender:

1. Accepts a message up to 20 characters.
2. Converts the message into UTF-8 bytes.
3. Applies XOR using a single-byte key.
4. Converts the encrypted bytes to hexadecimal.
5. Splits the hexadecimal string into 4-character chunks.
6. Appends each chunk to `example.com`.

Example format:

```text
624f.example.com
4646.example.com
45.example.com