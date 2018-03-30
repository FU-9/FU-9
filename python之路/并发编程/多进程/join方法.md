#### Process对象的join方法
在主进程运行过程中如果想并发地执行其他的任务，我们可以开启子进程，此时主进程的任务与子进程的任务分为两种情况

+ 情况一：在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务限制性完毕后，主进程还需要等待子进程执行完毕，然后同一回收资源
+ 情况二：如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，就需要有一种机制能够让主进程检测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用

```
from multiprocessing import Process
import time
import random
import os
def task():
  print('%s runing' %os.getpid())
  time.sleep(random.randint(1,5))
  print('%s run end' %os.getpid())

if __name__ == '__main__':
  p1 = Process(target=task)
  p1.start()
  p1.join()#等待p1停止，才执行下一行代码
  print("主")
```
#### Process对象的其他属性或方法
进程对象的其他方法：terminate与is_alive
```
from multiprocessing import Process
import time
import random

def task(name):
  print("%s is runing"%name)
  time.sleep(random.randint(1,5))
  print('%s is end'%name)

if __name__ == '__main__':
  p1.Process(target=task,args=('p1',))
  p1.start()

  p1.terminate()#关闭进程，不会立即关闭，所以is_alive立即查看的结果可能还是存活
  print(p1.is_alive)#结果为True
  print('主')
  print(p1.is_alive())#结果为False
```
进程对象的其他属性：name与pid
```
from multiprocessing import Process
import time
import random

def task(name):
  print("%s is runing"%name)
  time.sleep(random.randint(1,5))
  print('%s is end'%name)

if __name__ == '__main__':
  p1=Process(target=task,args=('p1',),name="子进程1")
  p1.start()
  print(p1.name,p1.pid)
```
