import os
print('Process %s start...' % os.getpid())

pid = os.fork()    # 该方法在windows上无法使用
if pid == 0:
    print(r'I am child process %s and myparent is %s' %(os.getpid, os.getppid(0)))
else:
    print("I %s just created a child process %s" %(os.getpid, pid))