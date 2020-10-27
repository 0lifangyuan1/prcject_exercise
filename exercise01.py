"""
编写一个程序完成，如果浏览器访问127.0.0.1：8888/python
的时候可以访问到Python.html网页，否则则访问不到任何内容
提示404信息
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(5)

c, addr = s.accept()
print("Connect from", addr)

data = c.recv(1024 * 10).decode()
tmp = data.split(" ")
if tmp[1]=="/python":
    with open("Python.html") as f:
    # file = open("Python.html","rb")
    # while True:
        content = f.read(1024)
        # if not data:
        #     break
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:text/html\r\n"
    response += "\r\n"
    response += content

else:
    response = "HTTP/1.1 404 NOT FOUND\r\n"
    response += "Content-Type:text/html\r\n"
    response += "\r\n"
    response += "Sorry this page is not exist"

c.send(response.encode())
# file.close()
c.close()
s.close()
