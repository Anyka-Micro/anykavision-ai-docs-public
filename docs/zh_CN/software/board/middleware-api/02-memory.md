# 内存管理

## 概述

&emsp;&emsp;内存管理模块（MEM模块）属于平台软件中的基础设施，具有底层操作系统无关性.

&emsp;&emsp;主要负责软件运行过程中内存管理、内存跟踪以及相关功能配置。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示。

| **库接口**                          | **描述**                                             |
| ----------------------------------- | ---------------------------------------------------- |
| AK_BASE_MemAlloc                    | 内存分配函数，同时完成内存块申请记录                 |
| AK_BASE_MemFree                     | 内存释放函数                                         |
| AK_BASE_MemPoolInit                 | 初始化一个内存池                                     |
| AK_BASE_MemPoolDestroy              | 销毁一个内存池，释放其中的所有内存块                 |
| AK_BASE_MemPoolAlloc                | 从指定内存池中获取一块内存，内存池不足时自动进行扩展 |
| AK_BASE_MemPoolFree                 | 归还从内存池中获取到的内存                           |
| AK_BASE_MemRbInit                   | 初始化一个循环buffer                                 |
| AK_BASE_MemRbDestroy                | 释放一个循环buffer                                   |
| AK_BASE_MemRbReset                  | 重置一个循环buffer                                   |
| AK_BASE_MemRbWrite                  | 向循环buffer写入一段数据                             |
| AK_BASE_MemRbReadRequest            | 从循环buffer中获取读指针                             |
| AK_BASE_MemRbReadCancel             | 设置读指针为“未使用”状态                             |
| AK_BASE_MemRbRead                   | 从循环buffer中读取数据                               |
| AK_BASE_MemRbGetDataSize            | 从循环buffer中读取数据                               |
| AK_BASE_MemDmaAlloc                 | 申请一段DMA内存                                      |
| AK_BASE_MemDmaFree                  | 释放DMA内存                                          |
| AK_BASE_MemDmaVaddr2Paddr           | 虚拟地址转换为物理地址                               |
| AK_BASE_MemDmaPoolCreate            | 创建DMA内存池                                        |
| AK_BASE_MemDmaPoolActivate          | 初始化DMA内存池                                      |
| AK_BASE_MemDmaPoolExit              | 退出DMA内存池                                        |
| AK_BASE_MemDmaPoolGetUsedMem        | 获取DMA内存池已使用大小                              |
| AK_BASE_MemDmaPoolGetFreeMem        | 获取DMA内存池空余大小                                |
| AK_BASE_MemDmaPoolSetThreshold      | 设置DMA内存池申请阈值                                |
| AK_BASE_MemDmaPoolCreateReservedObj | 创建DMA内存池中的特定保留内存                        |
| AK_BASE_MemGetVersion               | 获取内存管理模块的版本信息                           |
| AK_BASE_MemGetUsedDetail            | 查询已申请的内存块信息详情                           |
| AK_BASE_MemReleaseUsedDetail        | 释放用于记录内存块使用详细信息的链表                 |
| AK_BASE_MemGetUsedTotal             | 查询模块已申请的内存总数，单位：Byte                 |
| AK_BASE_MemDmaGetUsed               | 查询模块已申请的DMA内存总数，单位：Byte              |
| AK_BASE_MemDmaGetReservedSize       | 查询系统保留内存大小，单位：Byte                     |
| AK_BASE_MemGetTotalSize             | 查询系统总内存大小，单位：Byte                       |

<br/>

##  数据结构

### **USED_MEM_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;已申请的内存块信息详情。

&emsp;&emsp;【定义】

```c
typedef struct akUSED_MEM_INFO_S {
    AK_S32 s32ModuleId;
    AK_CHAR acFunc[20];
    AK_S64 s64Time;
    AK_U32 u32Size;
    AK_VOID* pvAddr;
    struct akUSED_MEM_INFO_S *pstNext;
}USED_MEM_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                           |
| ------------ | ---------------------------------- |
| s32ModuleId  | 已申请的内存块的模块id             |
| acFunc[20]   | 已申请的内存块的调用函数名         |
| s64Time      | 已申请的内存块的申请时间           |
| u32Size      | 已申请的内存块的申请size，单位byte |
| pvAddr       | 已申请的内存块的内存地址           |
| pstNext      | 下一个内存块信息的指针             |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

<br/>

## 基础接口

### **AK_BASE_MemAlloc**

&emsp;&emsp;【描述】

&emsp;&emsp;内存分配函数，同时完成内存块申请记录。

&emsp;&emsp;【语法】

```C
    AK_VOID* AK_BASE_MemAlloc(AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId  | 申请内存块的模块ID | -            | 输入          |
| u32Size      | 每个内存块的大小   | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**                                         |
| ---------- | ------------------------------------------------ |
| AK_VOID\* | 成功时返回申请到的内存块的首地址，失败时返回NULL |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

&emsp;&emsp;经过宏定义封装的接口如下：

```c
    #define AK_BASE_MemAlloc(s32ModuleId, u32Size) \
    AK_BASE_MemAlloc_(s32ModuleId, u32Size, __FUNCTION__, AK_BASE_GetOsTimeStamp())
```
> **注意：**此接口申请内存成功后，若需要清零，请用户调用memset来清零。

<br/>

### **AK_BASE_MemFree**

&emsp;&emsp;【描述】

&emsp;&emsp;内存释放函数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemFree(AK_VOID *pvPtr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| pvPtr        | 待释放的内存首地址 | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**               |
| ---------- | ---------------------- |
| 0          | 成功                   |
| 非0        | 失败，返回值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

## 内存池管理

### **AK_BASE_MemPoolInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化一个内存池。此接口是通过宏定义封装的。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemPoolInit(AK_S32 *ps32PoolId, AK_S32 s32ModuleId, \
    AK_U32 u32Nmemb, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                       | **取值范围** | **输入/输出** |
| ------------ | ------------------------------ | ------------ | ------------- |
| ps32PoolId   | 申请到的内存池ID               | -            | 输出          |
| s32ModuleId  | 申请内存池的模块ID             | -            | 输入          |
| u32Nmemb     | 申请的内存池中包含的内存块个数 | -            | 输入          |
| u32Size      | 每个内存块的大小，单位：Byte   | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| ----------------------------- | -------- |
| ERROR_TYPE_POINTER_NULL       | 空指针   |
| ERROR_TYPE_INVALID_ARG        | 参数无效 |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | 资源不足 |
| ERROR_TYPE_MALLOC_FAILED      | 分配失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemPoolDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁内存池，释放其中所有的内存块。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemPoolDestroy(AK_S32 s32MemPoolId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**         | **取值范围** | **输入/输出** |
| ------------ | ---------------- | ------------ | ------------- |
| s32MemPoolId | 待销毁的内存池ID | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemPoolAlloc**

&emsp;&emsp;【描述】

&emsp;&emsp;从指定内存池中获取一块内存，以备内存池不足时自动扩展。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemPoolAlloc(AK_VOID **ppMemBlk, AK_S32 s32MemPoolId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                       | **取值范围** | **输入/输出** |
| ------------ | ------------------------------ | ------------ | ------------- |
| ppMemBlk     | 从内存池中申请到的内存块首地址 | -            | 输出          |
| s32MemPoolId | 内存池ID                       | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| ----------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG        | 参数无效 |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | 资源不足 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemPoolFree**

&emsp;&emsp;【描述】

&emsp;&emsp;归还从内存池中获取到的内存。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemPoolFree(AK_VOID *pvPtr, AK_S32 s32MemPoolId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**             | **取值范围** | **输入/输出** |
| ------------ | -------------------- | ------------ | ------------- |
| pvPtr     | 待归还的内存块首地址 | 非NULL           | 输入          |
| s32MemPoolId	| 内存池ID			| [0-8]				| 输入		|

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 空指针   |
| ERROR_TYPE_INVALID_ARG  | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

## 循环buffer管理

### **AK_BASE_MemRbInit**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化一个循环buffer。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbInit(AK_S32 *ps32RbId, AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**               | **取值范围** | **输入/输出** |
| ------------ | ---------------------- | ------------ | ------------- |
| ps32RbId     | 申请到的循环buffer的ID | -            | 输出          |
| s32ModuleId  | 申请循环buffer的模块ID | -            | 输入          |
| u32Size      | 申请的循环buffer大小   | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**             |
| ---------- | -------------------- |
| 0          | 成功                 |
| 非0        | 失败，返回为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| ----------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG        | 参数无效 |
| ERROR_TYPE_NO_ENOUTH_RESOURCE | 资源不足 |
| ERROR_TYPE_MALLOC_FAILED      | 分配失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbDestroy**

&emsp;&emsp;【描述】

&emsp;&emsp;释放一个循环buffer。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbDestroy(AK_S32 s32RbId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待释放的循环buffer ID | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbReset**

&emsp;&emsp;【描述】

&emsp;&emsp;重置一个循环buffer。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbReset(AK_S32 s32RbId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待重置的循环buffer ID | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbWrite**

&emsp;&emsp;【描述】

&emsp;&emsp;向循环buffer写入一段数据。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbWrite(AK_S32 s32RbId, AK_U8 *pu8From, AK_S32 s32WriteLen);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待写入的循环buffer id | -            | 输入          |
| pu8From      | 数据源缓存首地址      | -            | 输入          |
| s32WriteLen  | 待写入的数据长度      | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**               | **描述** |
| ------------------------ | -------- |
| ERROR_TYPE_NO_LEFT_SPACE | 空间不足 |
| ERROR_TYPE_INVALID_ARG   | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbReadRequest**

&emsp;&emsp;【描述】

&emsp;&emsp;从循环buffer中获取读指针。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbReadRequest(AK_S32 s32RbId, AK_S32 *ps32ReadptrId);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                   | **取值范围** | **输入/输出** |
| ------------- | -------------------------- | ------------ | ------------- |
| s32RbId       | 待处理的循环buffer ID      | -            | 输入          |
| ps32ReadptrId | 申请到的循环buffer读指针ID | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| ----------------------------- | -------- |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | 资源不足 |
| ERROR_TYPE_INVALID_ARG        | 参数无效 |
| ERROR_TYPE_POINTER_NULL       | 空指针   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbReadCancel**

&emsp;&emsp;【描述】

&emsp;&emsp;设置读指针为“未使用”状态。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbReadCancel(AK_S32 s32RbId, AK_S32 s32ReadptrId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待处理的循环buffer id | -            | 输入          |
| s32ReadptrId | 读指针的索引          | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbRead**

&emsp;&emsp;【描述】

&emsp;&emsp;从循环buffer中读取数据。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbRead(AK_S32 s32RbId, AK_S32 s32ReadptrId, AK_U8 *pu8To, \
    AK_S32 s32ReadLen, AK_S32 *ps32Result);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待读取的循环buffer ID | -            | 输入          |
| s32ReadptrId | 读指针的索引          | -            | 输入          |
| pu8To        | 数据输出缓存首地址    | -            | 输出          |
| s32ReadLen   | 待读取的数据长度      | -            | 输入          |
| ps32Result   | 成功读取出的数据长度  | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemRbGetDataSize**

&emsp;&emsp;【描述】

&emsp;&emsp;获取循环buffer中的数据大小。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemRbGetDataSize(AK_S32 s32RbId, AK_S32 *ps32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId      | 待查询的循环buffer ID | -            | 输入          |
| ps32Size     | 循环buffer中的数据量  | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**         |
| ---------- | ---------------- |
| 0          | 成功             |
| 非0        | 失败，返回错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

## DMA内存操作

### **AK_BASE_MemDmaAlloc**

&emsp;&emsp;【描述】

&emsp;&emsp;申请一段DMA内存。

&emsp;&emsp;【语法】

```C
    AK_VOID * AK_BASE_MemDmaAlloc(AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围** | **输入/输出** |
| ------------ | ------------------- | ------------ | ------------- |
| s32ModuleId  | 申请DMA内存的模块ID | -            | 输入          |
| u32Size      | 待申请内存块的大小  | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**                                           |
| ---------- | -------------------------------------------------- |
| AK_VOID    | 成功时返回申请到的内存块的首地址，失败时返回NULL。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaFree**

&emsp;&emsp;【描述】

&emsp;&emsp;释放DMA内存。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaFree(AK_VOID *pvPtr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| pvPtr        | 待释放的DMA内存首地址 | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaVaddr2Paddr**

&emsp;&emsp;【描述】

&emsp;&emsp;虚拟地址转换为物理地址。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaVaddr2Paddr(AK_VOID *pvPtr, AK_U64 *pu64Paddr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| pvPtr        | 待转换的虚拟地址   | -            | 输入          |
| pu64Paddr    | 输出的物理内存地址 | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 空指针   |
| ERROR_TYPE_INVALID_ARG  | 参数无效 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolCreate**

&emsp;&emsp;【描述】

&emsp;&emsp;创建DMA内存池。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolCreate(MODULE_ID_E enMid, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid        | 申请DMA内存池的模块ID | -            | 输入          |
| u32Size      | DMA内存池大小         | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolActivate**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化DMA内存池。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolActivate(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| -            | -        | -            | -             |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolExit**

&emsp;&emsp;【描述】

&emsp;&emsp;退出DMA内存池。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolExit(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| -            | -        | -            | -             |

&emsp;&emsp;【返回值】

| **返回值** | **描述**         |
| ---------- | ---------------- |
| int        | 0 成功，总是成功 |
&emsp;&emsp;【错误码列表】

| **错误码** | **描述**        |
| ------------ | -------- |
| -                        | -               |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolGetUsedMem**

&emsp;&emsp;【描述】

&emsp;&emsp;获取DMA内存池已使用大小情况信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolGetUsedMem(MODULE_ID_E enMid, AK_U64 *pu64Total);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid        | 申请DMA内存池的模块ID | -            | 输入          |
| pu64Total    | DMA内存池已使用总量   | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolGetFreeMem**

&emsp;&emsp;【描述】

&emsp;&emsp;获取DMA内存池空余大小情况信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolGetFreeMem(MODULE_ID_E enMid, AK_U64 *pu64Total);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid        | 申请DMA内存池的模块ID | -            | 输入          |
| pu64Total    | DMA内存池空余总量     | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolSetThreshold**

&emsp;&emsp;【描述】

&emsp;&emsp;设置DMA内存池申请阈值。

&emsp;&emsp;当ak_mem_dma_alloc\_大于阈值时，从该模块的DMA内存池中分配，否则在DMA剩余内存中分配。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolSetThreshold(MODULE_ID_E enMid, AK_U64 u64Threshold);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**              | **取值范围** | **输入/输出** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid        | 申请DMA内存池的模块ID | -            | 输入          |
| u64Threshold | DMA内存池申请阈值     | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolCreateReservedObj**

&emsp;&emsp;【描述】

&emsp;&emsp;在DMA内存池中创建特定保留内存。

&emsp;&emsp;当ak_mem_dma_alloc\_大于阈值时，从该DMA内存池中的特定保留内存中分配，否则在该模块的DMA内存池中普通内存分配。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaPoolCreateReservedObj(MODULE_ID_E enMid, \
    AK_U64 u64Size, AK_U64 u64AllocThreshold);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**              | **取值范围** | **输入/输出** |
| ----------------- | --------------------- | ------------ | ------------- |
| enMid             | 申请DMA内存池的模块ID | -            | 输入          |
| u64Size           | 保留内存大小          | -            | 输入          |
| u64AllocThreshold | 保留内存申请阈值      |              | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**        |
| ---------- | --------------- |
| AK_S32     | 0 成功，-1 失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

## 版本信息获取

### **AK_BASE_MemGetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取内存管理模块的版本信息。

&emsp;&emsp;【语法】

```C
    const AK_CHAR* AK_BASE_MemGetVersion(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| AK_VOID      | -        | -            | -             |

&emsp;&emsp;【返回值】

| **返回值**      | **描述**                     |
| --------------- | ---------------------------- |
| const AK_CHAR * | 返回内存管理模块的版本库信息 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

## 内存使用状态查询

### **AK_BASE_MemGetUsedDetail**

&emsp;&emsp;【描述】

&emsp;&emsp;查询已申请的内存块信息详情。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                   | **取值范围**                  | **输入/输出** |
| ------------ | -------------------------- | ----------------------------- | ------------- |
| s32ModuleId  | 待查询内存占用情况的模块ID | 参考enum module_id            | 输入          |
| ppstMemUsed  | 输出内存申请信息的结构体   | 参考s_used_mem_info，取值为空 | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**         |
| ---------- | ---------------- |
| 0          | 成功             |
| 非0        | 失败，返回错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**                             |
| --------------------------- | ------------------------------------ |
| ERROR_TYPE_FUNC_NOT_SUPPORT | 该功能不支持（没有打开内存跟踪功能） |
| ERROR_TYPE_INVALID_ARG      | 参数错误                             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_BASE_MemGetUsedDetail(s32ModuleId, &pstMemUsed);
    AK_BASE_MemReleaseUsedDetail(pstMemUsed);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_BASE_MemReleaseUsedDetail(USED_MEM_INFO_S *pstMemUsed);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_MemReleaseUsedDetail**

&emsp;&emsp;【描述】

&emsp;&emsp;释放用于记录内存块使用详细信息的链表。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemReleaseUsedDetail(USED_MEM_INFO_S *pstMemUsed);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                 | **取值范围** | **输入/输出** |
| ------------ | ------------------------ | ------------ | ------------- |
| pstMemUsed   | 待释放的内存详细信息链表 | 非空         | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功。             |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 参数为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_BASE_MemGetUsedDetail(s32ModuleId, &pstMemUsed);
    AK_BASE_MemReleaseUsedDetail(pstMemUsed);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**当使用ak_mem_get_used_detai接口查询内存块使用详情之后，必须调用该接口（ak_mem_release_used_detail）释放用于记录内存块使用详情的链表，否则将有可能产生内存泄漏。

<br/>

### **AK_BASE_MemGetUsedTotal**

&emsp;&emsp;【描述】

&emsp;&emsp;查询模块已申请的内存总数，单位：BYTE。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemGetUsedTotal(AK_S32 s32ModuleId, AK_U64 *pu64TotalUsed);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                         | **取值范围** | **输入/输出** |
| ------------- | -------------------------------- | ------------ | ------------- |
| s32ModuleId   | 待查询内存占用情况的模块ID       | -            | 输入          |
| pu64TotalUsed | 查询结果，内存使用总量，单位BYTE | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**                             |
| --------------------------- | ------------------------------------ |
| ERROR_TYPE_FUNC_NOT_SUPPORT | 该功能不支持（内存跟踪功能没有打开） |
| ERROR_TYPE_INVALID_ARG      | 参数错误                             |
| ERROR_TYPE_POINTER_NULL     | 参数为空                             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaGetUsed**

&emsp;&emsp;【描述】

&emsp;&emsp;查询模块已申请的DMA内存总数，单位：BYTE。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaGetUsed(AK_S32 s32ModuleId, AK_U64 *pu64TotalUsed);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                            | **取值范围** | **输入/输出** |
| ------------- | ----------------------------------- | ------------ | ------------- |
| s32ModuleId   | 待查询DMA内存占用情况的模块ID       | -            | 输入          |
| pu64TotalUsed | 查询结果，DMA内存使用总量，单位BYTE | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| 0          | 成功               |
| 非0        | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**                           |
| --------------------------- | ---------------------------------- |
| ERROR_TYPE_FUNC_NOT_SUPPORT | 该功能不支持（内存跟踪功能未开启） |
| ERROR_TYPE_INVALID_ARG      | 参数错误                           |
| ERROR_TYPE_POINTER_NULL     | 参数为空                           |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemDmaGetReservedSize**

&emsp;&emsp;【描述】

&emsp;&emsp;查询系统保留内存大小，单位：BYTE。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemDmaGetReservedSize(AK_U64 *pu64Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                         | **取值范围** | **输入/输出** |
| ------------ | -------------------------------- | ------------ | ------------- |
| pu64Size     | 查询结果，保留内存总量，单位BYTE | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### **AK_BASE_MemGetTotalSize**

&emsp;&emsp;【描述】

&emsp;&emsp;查询系统内存总大小，单位：BYTE。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_MemGetTotalSize(AK_U64 *pu64Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                           | **取值范围** | **输入/输出** |
| ------------ | ---------------------------------- | ------------ | ------------- |
| pu64Size     | 查询结果，系统内存总大小，单位BYTE | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_mem.a或者libplat_mem.so

&emsp;&emsp;头文件：ak_mem.h

<br/>

### /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

#### stat

| 参数    | 说明        |
| ------- | ----------- |
| Version | MEM库版本号 |
