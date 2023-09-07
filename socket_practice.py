import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

headers = b''  # Initialize an empty bytes variable to store headers
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    headers += data
    print(data.decode(), end='')

mysock.close()

# Extract and print the headers
header_text = headers.decode()
header_lines = header_text.split('\r\n\r\n', 1)
if len(header_lines) > 1:
    headers = header_lines[0]
    print("\n\nHeaders:\n")
    for header in headers.split('\r\n'):
        print(header)

# The remaining part of the received data is the content
content = header_lines[1]
print("\n\nContent:\n")
print(content)
