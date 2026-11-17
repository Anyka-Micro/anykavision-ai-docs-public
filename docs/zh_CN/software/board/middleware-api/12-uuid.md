# UUID

## 概述

&emsp;&emsp;获取芯片唯一ID模块（UUID模块）。

<br/>

##  API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **函数接口 **                 | **描述 **                       |
| ----------------------------- | ------------------------------- |
| AK_BASE_UuidGetVersion        | 获取uuid版本号                  |
| AK_BASE_UuidOpen              | 打开uuid设备                    |
| AK_BASE_UuidClose             | 关闭uuid设备                    |
| AK_BASE_UuidGetGlobalId       | 获取global_ID区数据             |
| AK_BASE_UuidGetGlobalIdLength | 获取global_ID的长度，单位为字节 |
<br/>

## 版本信息获取

###  **AK_BASE_UuidGetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取uuid库的版本号

&emsp;&emsp;【语法】

```C
    const AK_CHAR* AK_BASE_UuidGetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值 **    | **描述 ** |
| -------------- | --------- |
| uuid模块版本号 | 成功      |
| NULL           | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libpalt_uuid.a、libplat_osal.a

&emsp;&emsp;头文件：ak_uuid.h

<br/>

## 打开/关闭模块

###  **AK_BASE_UuidOpen**

&emsp;&emsp;【描述】

&emsp;&emsp;打开uuid模块

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_UuidOpen(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **    |
| ----------- | ------------ |
| 0           | 成功         |
| 其他        | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_uuid.a、libplat_osal.a

&emsp;&emsp;头文件：ak_uuid.h

> **注意：**接口只允许open一次，多次open接口会返回错误。

<br/>

### **AK_BASE_UuidClose**

&emsp;&emsp;【描述】

&emsp;&emsp;关闭uuid模块

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_UuidClose(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **    |
| ----------- | ------------ |
| 0           | 成功         |
| 其他        | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_uuid.a、libplat_osal.a

&emsp;&emsp;头文件：ak_uuid.h

> **注意：**接口只允许close一次，多次close接口会返回错误。

<br/>

## global_ID分区相关操作

###  **AK_BASE_UuidGetGlobalId**

&emsp;&emsp;【描述】

&emsp;&emsp;获取global ID区域的数据。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_UuidGetGlobalId(AK_U8** ppu8Buf);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **                       | **取值范围 ** | **输入/输出 ** |
| ------------- | ------------------------------- | ------------- | -------------- |
| ppu8Buf       | 保存传出global id数据的地址指针 | 二重指针      | 输出           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **    |
| ----------- | ------------ |
| 0           | 成功         |
| 其他        | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_uuid.a、libplat_osal.a

&emsp;&emsp;头文件：ak_uuid.h

> **注意：**该接口在调用AK_BASE_UuidOpen接口之后调用。返回的二重指针需要在AK_BASE_UuidClose之前获取数据。

<br/>

### **AK_BASE_UuidGetGlobalIdLength**

&emsp;&emsp;【描述】

&emsp;&emsp;获取global ID区域的长度，单位为字节。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_UuidGetGlobalIdLength(AK_S32* ps32Length);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **                         | **取值范围 ** | **输入/输出 ** |
| ------------- | --------------------------------- | ------------- | -------------- |
| ps32Length    | 获取global ID区的长度，单位为字节 | 非负数        | 输出           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **    |
| ----------- | ------------ |
| 0           | 成功         |
| 其他        | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_uuid.a、libplat_osal.a

&emsp;&emsp;头文件：ak_uuid.h

> **注意：**该接口在调用AK_BASE_UuidOpen接口之后调用。

<br/>

&emsp;&emsp;示例代码：

```c
    #include "ak_uuid.h"
    #include <stdio.h>
    ....

    AK_BASE_PrintNormal(MODULE_ID_APP, "** uuid demo version: %s **\n",       AK_BASE_UuidGetVersion());
    int ret =-1;
    int length = -1;
    ret = AK_BASE_UuidOpen();					//if use uuid ,first must open uuid
    unsigned char* global_ptr;
    ret = AK_BASE_UuidGetGlobalId(&global_ptr);
    ret = AK_BASE_UuidGetGlobalIdLength(&length);
    for(int i =0;i< length;i++){
	  AK_BASE_PrintNoticeEx(MODULE_ID_APP," global_id=%x\n",global_ptr[i]);
    }
    AK_BASE_UuidClose();	  //close uuid ,will free the mempry which malloced in inner
```

<br/>

## 错误码说明

| 错误代码   | 宏定义                        | 描述                      |
| ---------- | ----------------------------- | ------------------------- |
| 0x20000000 | ERROR_UUID_INVALID_ARG        | 参数检查错误              |
| 0x20000001 | ERROR_UUID_GLOBAL_ID_ZERO     | global 区为空，不可读取   |
| 0x20000002 | ERROR_UUID_UNWRITABLE         | custom 区非空，不可以写入 |
| 0x20000003 | ERROR_UUID_OTHERS             | 其他错误，数据比对错误等  |
| 0x20000004 | ERROR_UUID_DEV_NOT_OPENED     | uuid设备没有打开          |
| 0x20000005 | ERROR_UUID_DEV_NOT_EXISTED    | uuid设备不存在            |
| 0x20000006 | ERROR_UUID_DEV_ALREADY_OPENED | uuid设备已经打开          |
| 0x20000007 | ERROR_UUID_UNKNOW             | 未知的错误                |

<br/>
