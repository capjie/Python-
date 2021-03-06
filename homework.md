{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 作业1\n",
    "要求: \n",
    "    1. 尽量自己独立完成，如不懂可以问同学和老师，但是所有的代码都要自己输入，看懂，亲自运行\n",
    "    2. 注意作业的截止时间，要在截止时间前提交\n",
    "    3. 作业提交需要将完成后的notebook,导出为markdown格式的文件,(选择File->Download as->Markdown(.md)文件)。\n",
    "题目："
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 编写一个程序，输出你的姓名和学号，例如：  张三 201633424。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "L 17271223\n"
     ]
    }
   ],
   "source": [
    "id,name =  17271223,'L'\n",
    "print(name,id)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  用程序计算下列表达式的计算结果：  \n",
    "1. 10除3的商\n",
    "1. 10除3的余数  \n",
    "1. 二进制11110000的值  \n",
    "1. sin(30) #30度  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.3\n",
      "2.1\n",
      "3.11110000\n",
      "4.0.49999999999999994\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "i0 = 10//3\n",
    "i1 = 10%3\n",
    "i2 = 0b11110000\n",
    "i3 = math.sin(math.pi/6)\n",
    "print('1.{}\\n2.{}\\n3.{}\\n4.{}'.format(i0,i1,i2,i3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 计算1~100的和及平均数。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "sum = 0\n",
    "for i in range(101):#range（100），只循环到99\n",
    "    sum +=i\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 随机获取10个100以内的整数，求其中的最大值以及其第一次出现的位置。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "#for i in range(10):\n",
    "    #print(random.randint(0,100),end=' ')以空格的形式结尾输出\n",
    "value = [random.randint(0,100) for x in range(10)]#将数据存储在列表中\n",
    "print(value)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 编写程序，用户输入一个4位整数，输出其每一位上的数之和。例如：用户输入 1234，计算1+2+3+4，程序输出 10。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "脚本文本代码的理解：  \n",
    "读取下面一段代码，假设该代码存储在名为MyTCPSocket.py的文本中。当运行该文本时，解释主函数中走的每一步的含义（也就是if __name__ == '__main__': 内的所有步骤命令，两个函数def server() 和 def client() 内部详细功能可以忽略）。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Foundations of Python Network Programming, Third Edition\n",
    "# TCP client and server that leave too much data waiting\n",
    "\n",
    "import argparse, socket, sys\n",
    "\n",
    "def server(host, port, bytecount):\n",
    "    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)\n",
    "    sock.bind((host, port))\n",
    "    sock.listen(1)\n",
    "    print('Listening at', sock.getsockname())\n",
    "    while True:\n",
    "        sc, sockname = sock.accept()\n",
    "        print('Processing up to 1024 bytes at a time from', sockname)\n",
    "        n = 0\n",
    "        while True:\n",
    "            data = sc.recv(1024)\n",
    "            if not data:\n",
    "                break\n",
    "            output = data.decode('ascii').upper().encode('ascii')\n",
    "            sc.sendall(output)  # send it back uppercase\n",
    "            n += len(data)\n",
    "            print('\\r  %d bytes processed so far' % (n,), end=' ')\n",
    "            sys.stdout.flush()\n",
    "        print()\n",
    "        sc.close()\n",
    "        print('  Socket closed')\n",
    "\n",
    "def client(host, port, bytecount):\n",
    "    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "    bytecount = (bytecount + 15) // 16 * 16  # round up to a multiple of 16\n",
    "    message = b'capitalize this!'  # 16-byte message to repeat over and over\n",
    "\n",
    "    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')\n",
    "    sock.connect((host, port))\n",
    "\n",
    "    sent = 0\n",
    "    while sent < bytecount:\n",
    "        sock.sendall(message)\n",
    "        sent += len(message)\n",
    "        print('\\r  %d bytes sent' % (sent,), end=' ')\n",
    "        sys.stdout.flush()\n",
    "\n",
    "    print()\n",
    "    sock.shutdown(socket.SHUT_WR)\n",
    "\n",
    "    print('Receiving all the data the server sends back')\n",
    "\n",
    "    received = 0\n",
    "    while True:\n",
    "        data = sock.recv(42)\n",
    "        if not received:\n",
    "            print('  The first data received says', repr(data))\n",
    "        if not data:\n",
    "            break\n",
    "        received += len(data)\n",
    "        print('\\r  %d bytes received' % (received,), end=' ')\n",
    "\n",
    "    print()\n",
    "    sock.close()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    choices = {'client': client, 'server': server}\n",
    "    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')\n",
    "    parser.add_argument('role', choices=choices, help='which role to play')\n",
    "    parser.add_argument('host', help='interface the server listens at;'\n",
    "                        ' host the client sends to')\n",
    "    parser.add_argument('bytecount', type=int, nargs='?', default=16,\n",
    "                        help='number of bytes for client to send (default 16)')\n",
    "    parser.add_argument('-p', metavar='PORT', type=int, default=1060,\n",
    "                        help='TCP port (default 1060)')\n",
    "    args = parser.parse_args()\n",
    "    function = choices[args.role]\n",
    "    function(args.host, args.p, args.bytecount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 编写功能函数num=function_name(input)  \n",
    "统计下面这句话The Zen of Python中，单词'is'出现的次数  \n",
    "提示，help(str.split)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "zen = \"\"\"The Zen of Python, by Tim Peters\n",
    "\n",
    "Beautiful is better than ugly.\n",
    "Explicit is better than implicit.\n",
    "Simple is better than complex.\n",
    "Complex is better than complicated.\n",
    "Flat is better than nested.\n",
    "Sparse is better than dense.\n",
    "Readability counts.\n",
    "Special cases aren't special enough to break the rules.\n",
    "Although practicality beats purity.\n",
    "Errors should never pass silently.\n",
    "Unless explicitly silenced.\n",
    "In the face of ambiguity, refuse the temptation to guess.\n",
    "There should be one-- and preferably only one --obvious way to do it.\n",
    "Although that way may not be obvious at first unless you're Dutch.\n",
    "Now is better than never.\n",
    "Although never is often better than *right* now.\n",
    "If the implementation is hard to explain, it's a bad idea.\n",
    "If the implementation is easy to explain, it may be a good idea.\n",
    "Namespaces are one honking great idea -- let's do more of those!\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
