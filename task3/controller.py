import os
import signal


def readLine(fd):
        b = os.read(fd, 1)
        if b == None:
                return None

        ch = b.decode('utf-8')
        # print('P_0: char = ' + ch + ' read from = ' + str(fd))
        s = ''
        while ch != '\n':
                s = s + ch
                ch = os.read(fd, 1).decode('utf-8')
        return s


p10r, p10w = os.pipe()


cid = os.fork()

if cid != 0:
        os.close(p10r)

        os.dup2(1, p10r)
        os.dup2(p10w, 1)

        argv = ['./producer']
        os.execve(argv[0], argv, os.environ)

p02r, p02w = os.pipe()
p20r, p20w = os.pipe()

cid = os.fork()

if cid != 0:
        os.close(p02w)
        os.close(p20r)

        os.dup2(0, p02w)
        os.dup2(1, p20r)
        os.dup2(p02r, 0)
        os.dup2(p20w, 1)

        argv = ['/usr/bin/bc']
        os.execve(argv[0], argv, os.environ)

computed = 0

def handle_SIGUSR1(sig, frame):
        mess = 'Produced: ' + str(computed) + '\n'
        os.write(2, mess.encode())

signal.signal(signal.SIGUSR1, handle_SIGUSR1)


# print('Inisializationn complete')
s = readLine(p10r)
while s:
        # print('P_0: line read = ' + s)
        os.write(p02w, (s+'\n').encode())
        res = readLine(p20r)
        print(s + ' = ' + res, flush=True)
        computed = computed + 1
        s = readLine(p10r)