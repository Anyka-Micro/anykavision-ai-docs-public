# 公共服务

## 概述

&emsp;&emsp;公共服务模块（common模块）主要用于实现平台的基础功能，例如获取当前系统时间、时间格式转换等。

&emsp;&emsp;这些功能互相独立，无密切联系，由公共服务模块统一管理。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示:

| **函数接口**             | **描述**                           |
| ------------------------ | ---------------------------------- |
| AK_BASE_CommonGetVersion | 获取common模块的版本信息           |
| AK_BASE_SleepMs          | 休眠指定的毫秒数                   |
| AK_BASE_GetOstime        | 获取系统时间                       |
| AK_BASE_GetOsTimeStamp   | 获取系统时间戳                     |
| AK_BASE_GetLocalDate     | 获取当前日期                       |
| AK_BASE_SetLocalDate     | 设置当前日期                       |
| AK_BASE_DiffMsTime       | 获取时间差                         |
| AK_BASE_SecondsToString  | 将时间戳转化为字符串               |
| AK_BASE_SecondsToDate    | 将时间戳转换为日期                 |
| AK_BASE_DateToSeconds    | 将时间信息转换成时间戳             |
| AK_BASE_DateToString     | 将时间信息转化为字符串             |
| AK_BASE_StringToDate     | 将字符串格式的时间信息转换成结构体 |
| AK_BASE_SdkInit          | Anyka SDK初始化函数                |
| AK_BASE_SdkExit          | Anyka SDK退出函数                  |

<br/>

##  版本信息获取

### **AK_BASE_CommonGetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取common模块的版本信息。

&emsp;&emsp;【语法】

```C
    const AK_CHAR* AK_BASE_CommonGetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**     | **描述**                 |
| -------------- | ------------------------ |
| const AK_CHAR* | 返回common模块的版本信息 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

## 时间相关操作

### **AK_BASE_SleepMs**

&emsp;&emsp;【描述】

&emsp;&emsp;休眠指定的毫秒数。

&emsp;&emsp;【语法】

```C
    AK_VOID AK_BASE_SleepMs(const AK_S32 s32Ms);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| s32Ms        | 毫秒数   | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| AK_VOID    | -        |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_GetOstime**

&emsp;&emsp;【描述】

&emsp;&emsp;获取系统时间。

&emsp;&emsp;【语法】

```C
    AK_VOID AK_BASE_GetOstime(TIME_VAL_S *pstTv);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**       | **取值范围** | **输入/输出** |
| ------------ | -------------- | ------------ | ------------- |
| pstTv        | 输出的系统时间 | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| AK_VOID    | -        |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

【相关结构体定义】

```C
typedef struct akTIME_VAL_S {
    AK_U64 u64Sec;     /* seconds */
    AK_U64 u64Usec;    /* microseconds */
}TIME_VAL_S;
```

【成员】

| **成员名称** | **描述** |
| ------------ | -------- |
| u64Sec       | 秒       |
| u64Usec      | 微秒     |

<br/>

### **AK_BASE_GetOsTimeStamp**

&emsp;&emsp;【描述】

&emsp;&emsp;获取系统时间戳。

&emsp;&emsp;【语法】

```C
    time_t AK_BASE_GetOsTimeStamp(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| AK_VOID      | -        | -            | -             |

&emsp;&emsp;【返回值】

| **返回值** | **描述**                                      |
| ---------- | --------------------------------------------- |
| time_t     | 时间戳。相当于返回Linux 的 time_t time(NULL); |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_GetLocalDate**

&emsp;&emsp;【描述】

&emsp;&emsp;获取当前日期。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_GetLocalDate(DATE_S *pstDate);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| pstDate      | 输出本地的当前日期 | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0        | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 参数为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_SetLocalDate**

&emsp;&emsp;【描述】

&emsp;&emsp;设置当前日期。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_SetLocalDate(const DATE_S *pstDate);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| pstDate      | 当前日期 | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0        | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 参数为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_DiffMsTime**

&emsp;&emsp;【描述】

&emsp;&emsp;获取时间差。

&emsp;&emsp;【语法】

```C
    long AK_BASE_DiffMsTime(const TIME_VAL_S *pstCurTime,
                    const TIME_VAL_S *pstPreTime);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围** | **输入/输出** |
| ------------ | ---------- | ------------ | ------------- |
| pstCurTime   | 待比较时间 | -            | 输入          |
| pstPreTime   | 基准时间   | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**           |
| ---------- | ------------------ |
| long       | 返回时间差，单位ms |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_SecondsToString**

&emsp;&emsp;【描述】

&emsp;&emsp;将时间戳转化为字符串。

&emsp;&emsp;【语法】

```C
    AK_CHAR* AK_BASE_SecondsToString(time_t secs);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围**             | **输入/输出** |
| ------------ | -------- | ------------------------ | ------------- |
| secs         | 时间戳   | [-2147483648,2147483647] | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**                                                     |
| ---------- | ------------------------------------------------------------ |
| AK_CHAR* | 存放输出字符串的指针，格式：yyyy-MM-dd HH:mm:ss。<br/>例如: 2016-04-06 10:06:06 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_SecondsToDate**

&emsp;&emsp;【描述】

&emsp;&emsp;将时间戳转换为日期。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_SecondsToDate(time_t seconds, DATE_S *pstDate);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围**             | **输入/输出** |
| ------------ | -------- | ------------------------ | ------------- |
| seconds      | 时间戳   | [-2147483648,2147483647] | 输入          |
| pstDate      | 时间信息 | -                        | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0        | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码**             | **描述** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | 参数错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_DateToSeconds**

&emsp;&emsp;【描述】

&emsp;&emsp;将时间信息转换成时间戳。

&emsp;&emsp;【语法】

```C
    time_t AK_BASE_DateToSeconds(const DATE_S *pstDate);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------ | -------- | ------------ | ------------- |
| pstDate      | 时间信息 | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**      |
| ---------- | ------------- |
| time_t     | 时间戳，单位s |
| -1         | 失败          |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_DateToString**

&emsp;&emsp;【描述】

&emsp;&emsp;将时间信息转换成字符串。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_DateToString(const DATE_S *pstDate, AK_CHAR *pcStr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                          | **取值范围** | **输入/输出** |
| ------------ | --------------------------------- | ------------ | ------------- |
| pstDate      | 时间信息                          | -            | 输入          |
| pcStr        | 时间字符串，格式：yyyyMMdd-HHmmss | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0        | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 参数为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

### **AK_BASE_StringToDate**

&emsp;&emsp;【描述】

&emsp;&emsp;将字符串格式的时间信息转换成结构体。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_StringToDate(const AK_CHAR *pcTimeStr, DATE_S *pstDate);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                    | **取值范围** | **输入/输出** |
| ------------ | ------------------------------------------- | ------------ | ------------- |
| pcTimeStr    | 字符串格式的时间信息，格式：yyyyMMdd-HHmmss | -            | 输入          |
| pstDate      | 结构体格式的时间信息                        | -            | 输出          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0        | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | 参数为空 |
| ERROR_TYPE_INVALID_ARG  | 参数有误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

<br/>

## SDK初始化/退出

### **AK_BASE_SdkInit**

&emsp;&emsp;【描述】

&emsp;&emsp;Anyka SDK初始化函数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_SdkInit(SDK_RUN_CONFIG_S *pstConfig);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**          | **取值范围** | **输入/输出** |
| ------------ | ----------------- | ------------ | ------------- |
| pstConfig    | SDK初始化配置参数 | -            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |
| 非0          | 失败     |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG          | 参数错误        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

> **注意：** 使用Anyka的SDK必须先调用该函数。

&emsp;&emsp;【相关结构体定义】

```C
typedef struct akSDK_RUN_CONFIG_S {
    AK_S32 s32MemTraceFlag;
    AK_S32 s32DmaMemTraceFlag;
    // isp tool server flag, 0 : disable, 1 : enable
    AK_S32 s32IspToolServerFlag;
} SDK_RUN_CONFIG_S;
```

【成员】

| **成员名称**         | **描述**                                                     |
| -------------------- | ------------------------------------------------------------ |
| s32MemTraceFlag      | 开启普通内存的跟踪功能，若要支持ak_mem_get_used_total，需要打开此标记 |
| s32DmaMemTraceFlag   | 开启DMA内存的跟踪功能，若要支持ak_mem_dma_get_used，需要打开此标记 |
| s32IspToolServerFlag | 开启isp调试工具服务。0 不开启；1 开启，端口默认8765；除了0和1，其余取值范围（1024，65536） 表示开启，端口按照此数值。此标记开启，等同于调用AK_EXT_ITS_Start接口。 |

> **安全提示：** ISP 工具服务仅用于调试。非调试环境请将 `s32IspToolServerFlag` 保持为 `0`；调试时仅在隔离的开发网络中启用，并用主机和网络防火墙限制可连接设备。修改端口号不能代替访问控制。

### **AK_BASE_SdkExit**

&emsp;&emsp;【描述】

&emsp;&emsp;Anyka SDK退出函数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_SdkExit(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 0          | 成功     |

&emsp;&emsp;【错误码列表】

| **错误码**          | **描述**      |
| ------------------- | ------------- |
| ERROR_TYPE_NOT_INIT | 没有初始化sdk |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_common.a

&emsp;&emsp;头文件：ak_common.h

> **注意：** 要跟AK_BASE_SdkInit接口配对使用。
<br/>

### /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

#### stat

| 参数    | 说明           |
| ------- | -------------- |
| Version | COMMON库版本号 |

<br/>

## 错误码说明

| 错误代码 | 宏定义                          | 描述             |
| -------- | ------------------------------- | ---------------- |
| 0        | ERROR_TYPE_NO_ERROR             | 无错误           |
| 0x100    | ERROR_TYPE_POINTER_NULL         | 指针为空         |
| 0x101    | ERROR_TYPE_INVALID_ARG          | 参数错误         |
| 0x102    | ERROR_TYPE_MALLOC_FAILED        | malloc失败       |
| 0x103    | ERROR_TYPE_PMEM_MALLOC_FAILED   | pmem malloc失败  |
| 0x104    | ERROR_TYPE_FUNC_NOT_SUPPORT     | 函数不支持       |
| 0x105    | ERROR_TYPE_NOT_INIT             | 没有初始化       |
| 0x106    | ERROR_TYPE_CALL_ORDER_WRONG     | 调用顺序错误     |
| 0x107    | ERROR_TYPE_DEV_OPEN_FAILED      | 设备打开失败     |
| 0x108    | ERROR_TYPE_DEV_INIT_FAILED      | 设备初始化失败   |
| 0x109    | ERROR_TYPE_DEV_CTRL_FAILED      | 设备操作失败     |
| 0x10a    | ERROR_TYPE_DEV_READ_FAILED      | 设备读失败       |
| 0x10b    | ERROR_TYPE_DEV_WRITE_FAILED     | 设备写失败       |
| 0x10c    | ERROR_TYPE_DEV_CLOSE_FAILED     | 设备关闭失败     |
| 0x10d    | ERROR_TYPE_FILE_OPEN_FAILED     | 文件打开失败     |
| 0x10e    | ERROR_TYPE_FCNTL_FAILED         | 文件操作失败     |
| 0x10f    | ERROR_TYPE_FILE_READ_FAILED     | 文件读失败       |
| 0x110    | ERROR_TYPE_FILE_WRITE_FAILED    | 文件写失败       |
| 0x111    | ERROR_TYPE_IOCTL_FAILED         | IOCTL失败        |
| 0x112    | ERROR_TYPE_CLOSE_FAILED         | 关闭失败         |
| 0x113    | ERROR_TYPE_GET_V4L2_PTR_FAILED  | 获取V4L2指针失败 |
| 0x114    | ERROR_TYPE_INVALID_USER         | 用户无效         |
| 0x115    | ERROR_TYPE_THREAD_CREATE_FAILED | 线程创建失败     |
| 0x116    | ERROR_TYPE_POPEN_FAILED         | POPEN失败        |
| 0x117    | ERROR_TYPE_MEDIA_LIB_FAILED     | 媒体库失败       |
| 0x118    | ERROR_TYPE_NO_DATA              | 没有数据         |
| 0x119    | ERROR_TYPE_EBUSY                | 设备忙           |
| 0x11a    | ERROR_TYPE_NO_ENOUGH_RESOURCE   | 没有足够资源     |
| 0x11b    | ERROR_TYPE_NO_LEFT_SPACE        | 没有足够空间     |

<br/>
