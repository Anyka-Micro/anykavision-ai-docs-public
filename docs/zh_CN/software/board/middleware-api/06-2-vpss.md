# 视频处理子系统

## 概述

&emsp;&emsp;视频处理子系统模块（VPSS模块）主要提供两方面的功能：

&emsp;&emsp;1、与VI模块进行绑定提供isp相关基础操作。（流程部分）

&emsp;&emsp;2、提供一些图像效果处理功能。（效果部分）

本节介绍流程部分的数据结构和接口。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示：

| **库接口**                     | **描述**                 |
| --------------------------- | ---------------------- |
| VPSS_CHN_MODE_E             | VPSS 视频帧输出模式           |
| VPSS_WORK_MODE_E            | VPSS 工作模式              |
| VPSS_GRP_ATTR_S             | VPSS GROUP属性           |
| VPSS_CHN_ATTR_S             | VPSS 通道属性              |
| VPSS_FRAME_INFO_S           | VPSS 视频帧结构             |
| AK_MPI_VPSS_GetVersion      | 获取VPSS库版本号             |
| AK_MPI_VPSS_GetConfVersion  | 获取ISPCONF文件的版本号        |
| AK_MPI_VPSS_CreateGrp       | 创建VPSS Group           |
| AK_MPI_VPSS_DestroyGrp      | 销毁VPSS Group           |
| AK_MPI_VPSS_StartGrp        | 开启VPSS Group           |
| AK_MPI_VPSS_StopGrp         | 关闭VPSS Group           |
| AK_MPI_VPSS_SetGrpAttr      | 设置VPSS Group属性         |
| AK_MPI_VPSS_GetGrpAttr      | 获取VPSS Group属性         |
| AK_MPI_VPSS_SetChnAttr      | 设置VPSS通道的属性            |
| AK_MPI_VPSS_GetChnAttr      | 获取VPSS通道的属性            |
| AK_MPI_VPSS_EnableChn       | 使能VPSS通道               |
| AK_MPI_VPSS_DisableChn      | 禁用VPSS通道               |
| AK_MPI_VPSS_BindChn         | 绑定输入的VI通道              |
| AK_MPI_VPSS_GetFrame        | 从VPSS通道中获取一帧处理完成的图像    |
| AK_MPI_VPSS_ReleaseFrame    | 释放一帧VPSS通道的图像          |
| AK_MPI_VPSS_GetGrpFrame     | 从VPSS GROUP获取一帧原始raw图像 |
| AK_MPI_VPSS_ReleaseGrpFrame | 释放一帧VPSS GROUP raw图像   |

<br/>

## 数据结构

### **VPSS_CHN_MODE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;视频帧输出模式

&emsp;&emsp;【定义】

```c
typedef enum akVPSS_CHN_MODE_E
{
     VPSS_CHN_FRAME_MODE,  //frame mode is normal mode.
    VPSS_CHN_SLICE_MODE,  //slice mode for saving dma memory, just user in venc kernel-kernel mode.
    VPSS_CHN_MODE_TOTAL
}VPSS_CHN_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**            | **描述**     |
| ------------------- | ---------- |
| VPSS_CHN_FRAME_MODE | FRAME模式输出。 |
| VPSS_CHN_SLICE_MODE | SLICE模式输出。 |
| VPSS_CHN_MODE_TOTAL | 模式总数       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32VpssChn, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

<br/>

### **VPSS_WORK_MODE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;VPSS工作模式。

&emsp;&emsp;【定义】

```c
typedef enum akVPSS_WORK_MODE_E
{
    VPSS_WORK_USER,                    //Receive memory input, i.e., user space data input through AK_MPI_VPSS_SendFrame
    VPSS_WORK_AUTO,                    //Normal mode, data input from sensor.
    VPSS_WORK_TOTAL
}VPSS_WORK_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**        |
| --------------- | ------------- |
| VPSS_WORK_USER  | USER模式支持内存输入  |
| VPSS_WORK_AUTO  | Auto模式即绑定的流模式 |
| VPSS_WORK_TOTAL | 模式总数          |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

<br/>

### **VPSS_GRP_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;VPSS GROUP属性。

&emsp;&emsp;【定义】

```c
typedef struct akVPSS_GRP_ATTR_S
{
    AK_U32                 u32Width;
    AK_U32                 u32Height;
    AK_U8                 pu8IspCfgPath[MAX_CFG_PATH_LEN];
    AK_S32               s32AttachSensorId;
    PIXEL_FORMAT_E          enInputPixFmt;
    VPSS_WORK_MODE_E     enWorkMode;
    ISP_DAY_NIGHT_MODE_E enLoadMode;
    AK_BOOL                 bEnGrpBypass;
    AK_BOOL                 bMirror;
    AK_BOOL                 bFlip;
}VPSS_GRP_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**                                                        |
| ----------------- | ------------------------------------------------------------- |
| u32Width          | 输入的宽度                                                         |
| u32Height         | 输入的高度                                                         |
| pu8IspCfgPath     | ISP配置文件路径                                                     |
| s32AttachSensorId | CIS的ID，通过AK_MPI_VI_GetSensorId接口获取。                           |
| enInputPixFmt     | 输入的数据像素格式                                                     |
| enWorkMode        | VPSS GROUP工作模式。USER模式或者Auto模式。                                |
| enLoadMode        | 初始化时加载ispconf里的哪个子文件                                          |
| bEnGrpBypass      | 使能Bypass VPSS的isp处理过程。打开后能通过AK_MPI_VPSS_GetGrpFrame接口获取raw数据。 |
| bMirror           | 是否水平翻转                                                        |
| bFlip             | 是否垂直翻转                                                        |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

<br/>

### **VPSS_CHN_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;VPSS 通道属性。SLICE模式仅适用于AUTO模式。

&emsp;&emsp;【定义】

```c
typedef struct akVPSS_CHN_ATTR_S
{
    AK_U32                u32Width;
    AK_U32                u32Height;
    AK_U32                u32MaxBufSize;
    CROP_INFO_S            stCropInfo;
    PIXEL_FORMAT_E         enOutputPixFmt;
    VPSS_CHN_MODE_E        enChnMode;
    AK_U32                u32FrameDepth;
    AK_S32                s32Fps;
}VPSS_CHN_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**                   |
| -------------- | ------------------------ |
| u32Width       | 输出的宽度                    |
| u32Height      | 输出的高度                    |
| u32MaxBufSize  | 最大的分辨率的buf大小             |
| stCropInfo     | 通道裁剪信息                   |
| enOutputPixFmt | 输出的像素格式                  |
| enChnMode      | 通道输出模式，FRAME模式或者SLICE模式。 |
| u32FrameDepth  | 内部缓存帧数                   |
| s32Fps         | 通道帧率控制                   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32VpssChn, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

<br/>

### **VPSS_FRAME_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;VPSS 视频帧结构。

【定义】

```c
typedef struct akVPSS_FRAME_INFO_S
{
    FRAME_S                stFrame;
    AK_U64                u64PhyAddr;
    PIXEL_FORMAT_E         enOutputPixFmt;
    AK_VOID                *pvMdInfo;
}VPSS_FRAME_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**   |
| -------------- | -------- |
| stFrame        | 帧信息数据结构体 |
| u64PhyAddr     | 帧存放的物理地址 |
| enOutputPixFmt | 输出的像素格式  |
| pvMdInfo       | 移动侦测数据   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_GetFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

<br/>

### VPSS_STITCH_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;拼接模式枚举

​        【定义】

```c
typedef enum akVPSS_STITCH_MODE_E
{
    VPSS_STITCH_VERTICAL_MODE,        //stitch dual sensor can use slice mode.
    VPSS_STITCH_HORIZONTAL_MODE,    //stitch dual sensor can not use slice mode.
    VPSS_STITCH_MODE_TOTAL
}VPSS_STITCH_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                    | **描述** |
| --------------------------- | ------ |
| VPSS_STITCH_VERTICAL_MODE   | 垂直拼接   |
| VPSS_STITCH_HORIZONTAL_MODE | 横向拼接   |
| VPSS_STITCH_MODE_TOTAL      | 拼接总数   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

### VPSS_STITCH_CHN_S

&emsp;&emsp;【说明】

&emsp;&emsp;需要拼接的通道

​        【定义】

```c
typedef struct akVPSS_STITCH_CHN_S
{
    AK_S32                    s32VpssGrp;
    AK_S32                    s32VpssChn;
}VPSS_STITCH_CHN_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**                                                    |
| ---------- | --------------------------------------------------------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            |
| s32VpssChn | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

### VPSS_STITCH_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;拼接通道属性

​        【定义】

```c
typedef struct akVPSS_STITCH_ATTR_S
{
    VPSS_STITCH_MODE_E    enStitchmode;
    AK_U32                    u32StitchChnNum;
    VPSS_STITCH_CHN_S        astStitchChn[MAX_STITCH_CHN_NUM];
}VPSS_STITCH_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**                                                        |
| --------------- | ------------------------------------------------------------- |
| enStitchmode    | 拼接模式                                                          |
| u32StitchChnNum | 需要拼接的通道个数。例如：双目拼接，u32StitchChnNum = 1；三目拼接，u32StitchChnNum =2 |
| astStitchChn    | 拼接通道属性                                                        |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

## 版本信息获取

### **AK_MPI_VPSS_GetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取VPSS库的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR *AK_MPI_VPSS_GetVersion(void);
```

&emsp;&emsp;【返回值】

| **返回值**   | **描述** |
| --------- | ------ |
| VPSS模块版本号 | 成功     |
| NULL      | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetConfVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取ISPCONF文件的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR *AK_MPI_VPSS_GetConfVersion(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值**       | **描述** |
| ------------- | ------ |
| ISPCONF文件的版本号 | 成功     |
| NULL          | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_CreateGrp**

&emsp;&emsp;【描述】

&emsp;&emsp;创建VPSS Group，创建多个通道则内部分时复用ISP硬件。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                         | **输入/输出** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstVpssGrpAttr | VPSS的group属性                                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                     | **描述**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG      | 参数错误          |
| ERROR_VPSS_GRP_CREATED_YET  | Group已经创建     |
| ERROR_VPSS_GRP_CREATE_FAIL  | Group创建失败     |
| ERROR_VPSS_ISP_DEV_OPEN     | ISP设备打开失败     |
| ERROR_VPSS_GET_PAD_ID       | 获取PAD ID失败    |
| ERROR_VPSS_GRPID_NO_FOUND   | Group id找不到   |
| ERROR_TYPE_MALLOC_FAILED    | 内存申请失败        |
| ERROR_TYPE_FILE_READ_FAILED | ISP conf文件读失败 |
| ERROR_TYPE_DEV_INIT_FAILED  | ISP设备初始化失败    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_DestroyGrp**

&emsp;&emsp;【描述】

&emsp;&emsp;销毁VPSS的GROUP。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_DestroyGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_StartGrp**

&emsp;&emsp;【描述】

&emsp;&emsp;开启VPSS的GROUP。

&emsp;&emsp;startGrp后如果要创建新的通道，需要stopGrp才可以。因为startGrp时会对此前加入该组的通道进行相关初始化工作，所以需要stopGrp后才能添加新的通道。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_StartGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                        | **描述**      |
| ------------------------------ | ----------- |
| ERROR_VPSS_NO_WORK             | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG         | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND      | Group id找不到 |
| ERROR_VPSS_GRP_ENABLE_YET      | Group已经开启   |
| ERROR_VPSS_CHN_SET_BUF_FAIL    | 通道设置buf失败   |
| ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | 通道申请buf失败   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_StopGrp**

&emsp;&emsp;【描述】

&emsp;&emsp;关闭VPSS的GROUP。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_StopGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_SetGrpAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置VPSS group的属性。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_SetGrpAttr(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                         | **输入/输出** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstVpssGrpAttr | VPSS的group属性                                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetGrpAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取VPSS group的属性。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_GetGrpAttr(AK_S32 s32VpssGrp, VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                         | **输入/输出** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstVpssGrpAttr | VPSS的group属性                                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_SetChnAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置VPSS通道的属性。

&emsp;&emsp;设置通道属性加上startGrp相当于创建通道。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                                    | **输入/输出** |
| -------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId       | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |
| pstVpssChnAttr | VPSS的通道属性                                                 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                      | **描述**      |
| ---------------------------- | ----------- |
| ERROR_VPSS_NO_WORK           | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG       | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND    | Group id找不到 |
| ERROR_VPSS_CHN_REGISTER_FAIL | 通道注册失败      |
| ERROR_VPSS_CHN_OPEN          | 通道打开失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetChnAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取VPSS通道的属性。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                                    | **输入/输出** |
| -------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId       | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |
| pstVpssChnAttr | VPSS的通道属性                                                 | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |
| ERROR_VPSS_CHNID_NO_FOUND | 通道id找不到     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_EnableChn**

&emsp;&emsp;【描述】

&emsp;&emsp;使能VPSS通道。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_EnableChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                                    | **输入/输出** |
| ---------- | --------------------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId   | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                        | **描述**      |
| ------------------------------ | ----------- |
| ERROR_VPSS_NO_WORK             | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG         | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND      | Group id找不到 |
| ERROR_VPSS_CHNID_NO_FOUND      | 通道id找不到     |
| ERROR_VPSS_GRP_NOT_ENABLE      | Group没有使能   |
| ERROR_VPSS_CHN_ENABLE_YET      | 通道已经使能      |
| ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | 通道申请buf失败   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_DisableChn**

&emsp;&emsp;【描述】

&emsp;&emsp;禁用VPSS通道。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_DisableChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                                    | **输入/输出** |
| ---------- | --------------------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId   | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |
| ERROR_VPSS_CHNID_NO_FOUND | 通道id找不到     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_BindChn**

&emsp;&emsp;【描述】

&emsp;&emsp;绑定输入的VI通道。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_BindChn( AK_S32 s32VpssGrp, AK_S32 s32LinkChnId);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32LinkChnId | VI的通道id                                        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetFrame**

&emsp;&emsp;【描述】

&emsp;&emsp;从VPSS通道中获取一帧处理完成的图像。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_GetFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                                    | **输入/输出** |
| ------------ | --------------------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId     | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |
| pstFrameInfo | 视频帧结构                                                     | 输出        |
| s32MilliSec  | 超时，-1阻塞；0非阻塞；大于0，等待时间，单位ms                                | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_VPSS_CHN_NO_OPEN    | 通道没有打开      |
| ERROR_TYPE_INVALID_ARG    | Dev参数错误     |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |
| ERROR_VPSS_CHNID_NO_FOUND | 通道id找不到     |
| ERROR_VPSS_GRP_NOT_ENABLE | Group没有使能   |
| ERROR_VPSS_CHN_NOT_ENABLE | 通道没有使能      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_ReleaseFrame**

&emsp;&emsp;【描述】

&emsp;&emsp;释放一帧VPSS通道的图像。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_ReleaseFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                                    | **输入/输出** |
| ------------ | --------------------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId     | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |
| pstFrameInfo | 视频帧结构                                                     | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |
| ERROR_VPSS_CHNID_NO_FOUND | 通道id找不到     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetGrpFrame**

&emsp;&emsp;【描述】

&emsp;&emsp;从VPSS GROUP获取一帧原始raw图像。

&emsp;&emsp;可以开启VPSS的bypass工作模式获取原始输入数据，但这会占用3DNR的内存，因此要先禁用3DNR，并且此时PP通道无法输出YUV数据。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_GetGrpFrame(AK_S32 s32VpssGrp, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstFrameInfo | 视频帧结构                                          | 输出        |
| s32MilliSec  | 超时，-1阻塞；0非阻塞；大于0，等待时间，单位ms                     | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**      |
| -------------------------- | ----------- |
| ERROR_VPSS_NO_WORK         | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG     | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND  | Group id找不到 |
| ERROR_TYPE_MALLOC_FAILED   | 申请内存失败      |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### **AK_MPI_VPSS_ReleaseGrpFrame**

&emsp;&emsp;【描述】

&emsp;&emsp;释放一帧VPSS GROUP raw图像。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_ReleaseGrpFrame(AK_S32 s32VpssGrp, VPSS_FRAME_INFO_S *pstFrameInfo);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstFrameInfo | 视频帧结构                                          | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                | **描述** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | 参数错误   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

<br/>

### AK_MPI_VPSS_SetStitchChn

&emsp;&emsp;【描述】

&emsp;&emsp;设置拼接通道

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

&emsp;&emsp;【参数】

| **参数名称**          | **描述**                                                    | **输入/输出** |
| ----------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp        | VPSS GROUP id, [0,4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| s32ChnId          | VPSS的通道id, [0, 2]。默认主通道的ChnId为0，次通道的ChnId为1，第三通道的ChnId为2。 | 输入        |
| pstVpssStitchAttr | 拼接通道结构体指针                                                 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS未初始化    |
| ERROR_TYPE_INVALID_ARG    | 参数错误        |
| ERROR_VPSS_GRPID_NO_FOUND | Group id找不到 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a

&emsp;&emsp;头文件：ak_vpss.h

## 调用流程

```c
    /* 初始化vi */
    AK_MPI_VI_CreateDev(s32ViDev,&stViDevAttr);
    AK_MPI_VI_SetChnAttr(s32ViDev, 0, &stViChnAttr);

    /* 初始化vpss */
    AK_MPI_VPSS_CreateGrp(s32GrpId, &stGrpAttr);
    AK_MPI_VPSS_SetChnAttr(s32GrpId, 0, &stVpssChnAttr);

    /* 绑定vi和vpss */
    AK_MPI_VI_BindVpssGrp(s32DevId, 0, s32DevId);
    AK_MPI_VPSS_BindChn(s32DevId, s32LinkChnId);

    /* 使能vi */
    AK_MPI_VI_EnableDev(s32ViDev);
    AK_MPI_VI_EnableChn(s32ViDev, 0);

    /* 使能vpss */
    AK_MPI_VPSS_StartGrp(s32GrpId);
    AK_MPI_VPSS_EnableChn(s32GrpId, 0);

    /* 取帧和释放帧 */
    AK_MPI_VPSS_GetFrame(j, 0, &stFrame, 2000);
    AK_MPI_VPSS_ReleaseFrame(j, 0, &stFrame);

    /* 关闭vpss */
    AK_MPI_VPSS_DisableChn(s32GrpId, 0);
    AK_MPI_VPSS_StopGrp(s32GrpId);
    AK_MPI_VPSS_DestroyGrp(s32GrpId);

    /* 关闭vi */
    AK_MPI_VI_DisableChn(s32ViDev, 0);
    AK_MPI_VI_DisableDev(s32ViDev);
    AK_MPI_VI_DestroyDev(s32ViDev);
```

<br/>

## vpss流程示例

### **ak_vpss_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**        | **输入参数说明**                      |
| --------------- | ------------------------------- |
| chn_index       | 通道id                            |
| frame_cnt       | 保存yuv帧数                         |
| chn_res_index   | 通道分辨率id                         |
| chn_framerate   | 通道采集帧率                          |
| isp_config_path | ISP config file 保存路径，默认为空，需要填写。 |
| frame_save_path | 保存yuv图像数据的路径                    |
| dev_cnt         | 设备数量[1, 2]，默认1，双目版本用2           |

<br/>

&emsp;&emsp;输出结果：输出采集的YUV数据，保存在指定的path目录下。

<br/>

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### param

| 参数                     | 说明               |
| ---------------------- | ---------------- |
| sensor_fps             | sensor帧率         |
| grp0_width             | group宽度          |
| grp0_height            | group高度          |
| grp0_ispCfgPath        | isp conf 路径      |
| grp0_sensorId          | sensor id        |
| grp0_inputPixFmt       | group的输入格式       |
| grp0_workMode          | group工作模式        |
| grp0_bEnGrpBypass      | 使能bypass         |
| grp0_bMirror           | 镜像               |
| grp0_bFlip             | 翻转               |
| grp0_chn0_width        | 输出通道宽度           |
| grp0_chn0_height       | 输出通道高度           |
| grp0_chn0_maxBufSize   | 最大buf大小          |
| grp0_chn0_outputPixFmt | 通道输出格式           |
| grp0_chn0_chnMode      | 通道工作模式           |
| grp0_chn0_frameDepth   | 采集Buf个数          |
| grp0_chn0_fps          | 通道帧率             |
| grp0_chn0_crop_x       | 通道裁剪分辨率[x,y,w,h] |
| grp0_chn0_crop_y       | 通道裁剪分辨率[x,y,w,h] |
| grp0_chn0_crop_w       | 通道裁剪分辨率[x,y,w,h] |
| grp0_chn0_crop_h       | 通道裁剪分辨率[x,y,w,h] |

### stat

| 参数               | 说明          |
| ---------------- | ----------- |
| version          | vpss库版本号    |
| ispsdk_version   | isp sdk库版本号 |
| mode             | 当前模式        |
| grp0_status      | group状态     |
| grp0_chn0_status | 通道状态        |

<br/>

## 错误码说明

| 错误代码       | 宏定义                            | 含义          |
| ---------- | ------------------------------ | ----------- |
| 0x0a000000 | ERROR_VPSS_INVALID_GRPID       | grp id无效    |
| 0x0a000001 | ERROR_VPSS_GRPID_NO_FOUND      | grp id没有找到  |
| 0x0a000002 | ERROR_VPSS_GRP_CREATE_FAIL     | grp创建失败     |
| 0x0a000003 | ERROR_VPSS_GRP_CREATED_YET     | grp已经创建     |
| 0x0a000004 | ERROR_VPSS_NO_WORK             | 模块没有工作      |
| 0x0a000005 | ERROR_VPSS_GRP_NOT_DISABLE     | grp没有禁用     |
| 0x0a000006 | ERROR_VPSS_GRP_NOT_ENABLE      | grp没有使能     |
| 0x0a000007 | ERROR_VPSS_GRP_ENABLE_YET      | grp已经使能     |
| 0x0a000008 | ERROR_VPSS_CHN_NOT_ENABLE      | 通道注册失败      |
| 0x0a000009 | ERROR_VPSS_CHN_ENABLE_YET      | 通道已经使能      |
| 0x0a00000a | ERROR_VPSS_CHN_REGISTER_FAIL   | 通道注册失败      |
| 0x0a00000b | ERROR_VPSS_CHNID_NO_FOUND      | 通道id没有找到    |
| 0x0a00000c | ERROR_VPSS_CHN_SET_BUF_FAIL    | 通道设置buf失败   |
| 0x0a00000d | ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | 通道申请buf失败   |
| 0x0a00000e | ERROR_VPSS_CHN_SET_QBUF_FAIL   | 通道设置qbuf失败  |
| 0x0a00000f | ERROR_VPSS_BIND_CHN            | 绑定通道错误      |
| 0x0a000010 | ERROR_VPSS_GET_PAD_ID          | 获取pad id错误  |
| 0x0a000011 | ERROR_VPSS_ISP_DEV_OPEN        | isp设备打开错误   |
| 0x0a000012 | ERROR_VPSS_CHN_OPEN            | 通道打开失败      |
| 0x0a000013 | ERROR_VPSS_CHN_NO_OPEN         | 通道没有打开      |
| 0x0a000014 | ERROR_VPSS_SENSOR_ID           | sensor id错误 |
| 0x0a000015 | ERROR_VPSS_EXP_NOT_STABLE      | 曝光没有稳定      |

<br/>
