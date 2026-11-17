# 多线程操作

##  概述

&emsp;&emsp;多线程操作模块（Thread模块）主要负责完成底层相关线程操作函数的封装及线程通信机制的封装，为上层提供统一的接口，便于后期上层软件移植。

<br/>

## API 参考

&emsp;&emsp;本模块提供API参考，如下表所示：

| **库接口**               | **描述**                                              |
| ------------------------------- | ------------------------------------------------------------ |
| AK_BASE_ThreadGetVersion | 获取线程模块版本信息                                         |
| AK_BASE_ThreadCreate | 创建一个新线程                                               |
| AK_BASE_ThreadJoin | 等待线程执行结束                                             |
| AK_BASE_ThreadDetach | 分离线程                                                     |
| AK_BASE_ThreadDetach | 取消线程的执行                                               |
| AK_BASE_ThreadExit | 终止线程执行                                                 |
| AK_BASE_ThreadGetTid | 获取线程tid                                          |
| AK_BASE_ThreadSetName | 设置线程名称                                                 |
| AK_BASE_ThreadMutexInit | 初始化互斥锁                                                 |
| AK_BASE_ThreadMutexLock | 获得互斥锁                                                   |
| AK_BASE_ThreadMutexUnlock | 释放互斥锁                                                   |
| AK_BASE_ThreadMutexDestroy | 销毁互斥锁                                                   |
| AK_BASE_ThreadMutexattrInit | 初始化一个互斥锁属性变量                                     |
| AK_BASE_ThreadMutexattrDestroy | 销毁一个互斥锁属性变量                                       |
| AK_BASE_ThreadMutexattrSettype | 设置互斥锁属性变量的值                                       |
| AK_BASE_ThreadMutexattrGettype | 获取互斥锁属性变量的值                                  |
| AK_BASE_ThreadSemInit | 初始化信号量                                                 |
| AK_BASE_ThreadSemPost | 信号量加1                                                    |
| AK_BASE_ThreadSemWait | 当信号量大于0时，信号量减1；当信号量为0时，该函数阻塞。      |
| AK_BASE_ThreadSemDestroy | 销毁信号量                                                   |
| AK_BASE_ThreadSemTrywait | 尝试获取信号量（当信号量大于0时，信号量减1，返回0；当信号量为0时， 返回-1） |
| AK_BASE_ThreadSemTimeWait | 获取信号量，获取不到时则阻塞，直到超时后返回                 |
| AK_BASE_ThreadCondInit | 初始化条件变量                                               |
| AK_BASE_ThreadCondDestroy | 销毁一个条件变量                                             |
| AK_BASE_ThreadCondWait | 等待条件变量的条件获得满足，不满足则一直阻塞                 |
| AK_Base_ThreadCondTimewait | 等待条件变量的条件获得满足，不满足则等待到超时后返回         |
| AK_BASE_ThreadCondSignal | 条件变量所需的条件得到满足，发出一个信号                     |
| AK_BASE_ThreadCondBroadcast | 条件变量所需的条件得到满足，以广播的形式发出信号             |
| AK_BASE_ThreadRWlockInit | 初始化读写锁                                                 |
| AK_BASE_ThreadRWlockDestroy | 销毁读写锁                                                   |
| AK_BASE_ThreadRWlockRDlock | 获取读锁                                                     |
| AK_BASE_ThreadRWlockWRlock | 获取写锁                                                     |
| AK_BASE_ThreadRWlockTryRDlock | 尝试获取读锁                                                 |
| AK_BASE_ThreadRWlockTryWRlock | 尝试获取写锁                                                 |
| AK_BASE_ThreadRWlockUnlock | 释放读写锁                                                   |
| AK_BASE_ThreadRWlockattrInit | 初始化读写锁属性                                             |
| AK_BASE_ThreadRWlockattrDestroy | 销毁读写锁属性                                               |
| AK_BASE_ThreadRWlockattrGetPshared | 获取共享属性                                                 |
| AK_BASE_ThreadRWlockattrSetPshared | 设置共享属性                                                 |

<br/>

## 版本信息获取

### **AK_BASE_ThreadGetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取线程模块版本信息。

&emsp;&emsp;【语法】

```C
    const AK_CHAR* AK_BASE_ThreadGetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述**         |
| ---------------- | ---------------------- |
| const AK_CHAR* | 返回线程模块的版本信息 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

## 线程控制

### **AK_BASE_ThreadCreate**

&emsp;&emsp;【描述】

&emsp;&emsp;创建一个新线程。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCreate(AK_PTHREAD_T *ptId, pfnBASE_ThreadFunc func, AK_VOID *pvArg, AK_S32 s32StackSize, AK_S32 s32Priority);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptId           | 线程ID         | -                  | 输出                                    |
| func           | 线程入口地址   | -                  | 输入                                    |
| pvArg           | 线程传入参数   | -                  | 输入                                    |
| s32StackSize | 线程栈大小     | -                  | 输入                                    |
| s32Priority    | 线程优先级     | s32Priority设置为-1时，调度策略为SCHED_OTHER，非实时线程；s32Priority设置在[1, 99]，调度策略为SCHED_RR，轮询式调度，实时线程，s32Priority值越大优先级越高。 | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadJoin**

&emsp;&emsp;【描述】

&emsp;&emsp;等待线程执行结束。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadJoin(AK_PTHREAD_T tId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId            | 线程ID         | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadDetach**

&emsp;&emsp;【描述】

&emsp;&emsp;分离线程。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadDetach(AK_PTHREAD_T tId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId             | 线程ID         | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadCancel**

&emsp;&emsp;【描述】

&emsp;&emsp;取消线程的执行。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCancel(AK_PTHREAD_T tId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId             | 线程ID         | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadExit**

&emsp;&emsp;【描述】

&emsp;&emsp;终止线程执行。

&emsp;&emsp;【语法】

```C
    AK_VOID AK_BASE_ThreadExit(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| -                | -         | -                  | -                                    |

&emsp;&emsp;【返回值】

无

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadGetTid**

&emsp;&emsp;【描述】

&emsp;&emsp;获得线程ID。

&emsp;&emsp;【语法】

```C
    AK_S64 AK_BASE_ThreadGetTid(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| AK_VOID        | -              | -                  | -                                       |

&emsp;&emsp;【返回值】

| **返回值** | **描述**       |
| ---------------- | -------------------- |
| AK_S64   | 调用函数所属的线程ID |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSetName**

&emsp;&emsp;【描述】

&emsp;&emsp;设置线程名称。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSetName(const AK_CHAR *pcName);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| pcName         | 线程名称       | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

##  互斥锁

### **AK_BASE_ThreadMutexInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化互斥锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexInit(AK_MUTEX_T *ptMutex, AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex       | 待初化的互斥锁 | -                  | 输出                                    |
| ptAttr         | 互斥锁属性     | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexLock**

&emsp;&emsp;【描述】

&emsp;&emsp;获得互斥锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexLock(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex       | 待操作的互斥锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexUnlock**

&emsp;&emsp;【描述】

&emsp;&emsp;释放互斥锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexUnlock(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex       | 待操作的互斥锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁互斥锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexDestroy(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex       | 待操作的互斥锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化一个互斥锁属性变量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexattrInit(AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptAttr         | 互斥锁属性变量指针 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁一个互斥锁属性变量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexattrDestroy(AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptAttr         | 互斥锁属性变量指针 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrSettype**

&emsp;&emsp;【描述】

&emsp;&emsp;设置互斥锁属性变量的值。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexattrSettype(AK_MUTEXATTR_T *ptAttr, AK_S32 s32Kind);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**         | **取值范围** | **输入/输出** |
| ------------------ | ---------------------- | ------------------ | --------------------------------------- |
| ptAttr         | 待操作的互斥锁变量指针 | -                  | 输入                                    |
| s32Kind        | 互斥锁的种类           | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrGettype**

&emsp;&emsp;【描述】

&emsp;&emsp;获取互斥锁属性变量的值。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadMutexattrGettype(const AK_MUTEXATTR_T *ptAttr, AK_S32 *ps32Kind);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**         | **取值范围** | **输入/输出** |
| ------------------ | ---------------------- | ------------------ | --------------------------------------- |
| ptAttr         | 待操作的互斥锁变量指针 | -                  | 输入                                    |
| ps32Kind       | 获取到互斥锁变量的值   | -                  | 输出                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

## 信号量

### **AK_BASE_ThreadSemInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化信号量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemInit(AK_SEM_T *ptSem, AK_U32 u32Value);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待操作的信号量 | -                  | 输出                                    |
| u32Value      | 信号量初始值   | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSemPost**

&emsp;&emsp;【描述】

&emsp;&emsp;信号量加1。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemPost(AK_SEM_T *ptSem);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待操作的信号量 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSemWait**

&emsp;&emsp;【描述】

&emsp;&emsp;当信号量大于0时，信号量减1；当信号量为0时，此函数阻塞。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemWait(AK_SEM_T *ptSem);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待操作的信号量 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSemDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁信号量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemDestroy(AK_SEM_T *ptSem);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待销毁的信号量 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSemTrywait**

&emsp;&emsp;【描述】

&emsp;&emsp;尝试获取信号量（当信号量大于0时，信号量减1，返回0；当信号量为0时，     返回-1）。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemTrywait(AK_SEM_T *ptSem);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待操作的信号量 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadSemTimeWait**

&emsp;&emsp;【描述】

&emsp;&emsp;获取信号量，获取不到时则阻塞，直到超时后返回。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadSemTimeWait(AK_SEM_T *ptSem, const struct timespec *abs_timeout);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem           | 待操作的信号量 | -                  | 输入                                    |
| abs_timeout | 超时时间       | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| -1               | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

## 条件变量

### **AK_BASE_ThreadCondInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化条件变量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCondInit(AK_COND_T *ptCond);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针   | -                  | 输出                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadCondDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁一个条件变量。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCondDestroy(AK_COND_T *ptCond);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针   | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadCondWait**

&emsp;&emsp;【描述】

&emsp;&emsp;等待条件变量的条件获得满足，不满足则一直阻塞。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCondWait(AK_COND_T *ptCond, AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**             | **取值范围** | **输入/输出** |
| ------------------ | -------------------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针               | -                  | 输入                                    |
| ptMutex       | 条件变量配套的互斥锁的指针 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_Base_ThreadCondTimewait**

&emsp;&emsp;【描述】

&emsp;&emsp;等待条件变量的条件获得满足，不满足则等待到超时后返回。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_Base_ThreadCondTimewait(AK_COND_T *ptCond,
        AK_MUTEX_T *ptMutex, const struct timespec *abstime);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**             | **取值范围** | **输入/输出** |
| ------------------ | -------------------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针               | -                  | 输入                                    |
| ptMutex       | 条件变量配套的互斥锁的指针 | -                  | 输入                                    |
| abstime     | 超时时间                   | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadCondSignal**

&emsp;&emsp;【描述】

&emsp;&emsp;条件变量所需的条件得到满足，发出一个信号。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCondSignal(AK_COND_T *ptCond);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针   | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadCondBroadcast**

&emsp;&emsp;【描述】

&emsp;&emsp;条件变量所需的条件得到满足，以广播的形式发出信号。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadCondBroadcast(AK_COND_T *ptCond);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond         | 条件变量指针   | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

## 读写锁

### **AK_BASE_ThreadRWlockInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化读写锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockInit(AK_RWLOCK_T *ptRWlock, AK_RWLOCKATTR_T *ptRWlockattr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围** | **输入/输出** |
| ------------------ | ---------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待初始化的读写锁 | -                  | 输入                                    |
| ptRWlockattr | 读写锁属性       | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁读写锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockDestroy(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockRDlock**

&emsp;&emsp;【描述】

&emsp;&emsp;获取读锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockRDlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockWRlock**

&emsp;&emsp;【描述】

&emsp;&emsp;获取写锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockWRlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockTryRDlock**

&emsp;&emsp;【描述】

&emsp;&emsp;尝试获取读锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockTryRDlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockTryWRlock**

&emsp;&emsp;【描述】

&emsp;&emsp;尝试获取写锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockTryWRlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockUnlock**

&emsp;&emsp;【描述】

&emsp;&emsp;释放读写锁。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockUnlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock     | 待操作的读写锁 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化读写锁属性。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockattrInit(AK_RWLOCKATTR_T * ptRWlockattr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | 待操作的读写锁属性 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁读写锁属性。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockattrDestroy(AK_RWLOCKATTR_T * ptRWlockattr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | 待操作的读写锁属性 | -                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrGetPshared**

&emsp;&emsp;【描述】

&emsp;&emsp;获取共享属性。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockattrGetPshared(AK_RWLOCKATTR_T * ptRWlockattr, AK_S32 *ps32Value);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | 待操作的读写锁属性 | -                  | 输入                                    |
| ps32Value     | 共享属性值         | - | 输出                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrSetPshared**

&emsp;&emsp;【描述】

&emsp;&emsp;设置共享属性。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_ThreadRWlockattrSetPshared(AK_RWLOCKATTR_T * ptRWlockattr, AK_S32 s32Value);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | 待操作的读写锁属性 | -                  | 输入                                    |
| s32Value      | 共享属性值         | - | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 非0              | 失败           |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_thread.a

&emsp;&emsp;头文件：ak_thread.h

<br/>

### /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

#### stat

| 参数    | 说明           |
| ------- | -------------- |
| Version | THREAD库版本号 |
