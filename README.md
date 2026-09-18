# DNS Tunneling Simulation

This project demonstrates the basic idea behind transferring data through DNS query names.

It does not send any real DNS traffic.

## Sender

The sender:

1. Reads a message.
2. Checks that it contains no more than 20 characters.
3. Converts the message to hexadecimal.
4. Splits the hex string into 4-character chunks.
5. Prints each chunk as a simulated DNS query.

Example:

```text
4865.example.com
6c6c.example.com
6f.example.com