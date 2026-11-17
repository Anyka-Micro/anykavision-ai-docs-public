# 视频流模式

## 概述

&emsp;&emsp;视频流模式模块主要负责视频方面的常用封装，vpss和venc绑定使用。

&emsp;&emsp;一个源channel可以绑定多个目的channel，但是一个目的channel只能与一个源channel绑定。

<br/>

## API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **数据结构**         | **描述**       |
| ---------------- | ------------ |
| EXT_CHN_S        | channel信息结构体 |
| BIND_MODE_E      | 绑定参数结构体      |
| EXT_BIND_PARAM_S | 绑定参数结构体      |

<br/>

| **函数接口**                     | **描述**               |
| ---------------------------- | -------------------- |
| AK_EXT_VIDEO_GetVersion      | 获取视频流模式库的版本号         |
| AK_EXT_VIDEO_SetDstChnActive | 使能/不使能已被绑定的目的channel |
| AK_EXT_VIDEO_VencGetStream   | 获取视频流数据              |
| AK_EXT_VIDEO_BindChn         | 绑定channel            |
| AK_EXT_VIDEO_UnbindChn       | 解绑channel            |
| AK_EXT_VIDEO_SetCb           | 设置回调函数               |
| AK_EXT_VIDEO_UnsetCb         | 取消回调函数               |
| AK_EXT_VIDEO_SetChnAttr      | 设置channel参数          |
| <br/>                        |                      |

## 数据结构

### EXT_CHN_S

&emsp;&emsp;【说明】

&emsp;&emsp;channel信息结构体

&emsp;&emsp;【定义】

```c
typedef struct akEXT_CHN_S
{
    MODULE_ID_E         enModId;            /* module id  */
    AK_S32              s32DevId;
    /* object id, chn id for vpss, encoder id for venc, decoder id for vdec*/
    AK_S32              s32ChnId;
}EXT_CHN_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                                                                        |
| -------- | ----------------------------------------------------------------------------- |
| enModId  | 模块id                                                                          |
| s32DevId | 设备id                                                                          |
| s32ChnId | 通道id。若enModId 是vpss，则u32ChnId为vpss chn id，若enModId是venc，则u32ChnId为venc chn id |
| <br/>    |                                                                               |

### BIND_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;编码模式枚举

&emsp;&emsp;【定义】

```c
typedef enum akBIND_MODE_E
{
    USER_MODE = 0x0,
    AUTO_MODE,
}BIND_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**  |
| --------- | ------- |
| USER_MODE | 用户态编码模式 |
| AUTO_MODE | 内核态编码模式 |

<br/>

### EXT_BIND_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;绑定参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct akEXT_BIND_PARAM_S
{
    AK_S32                      s32BPFrameRate;             /* frame rate control */
    AK_S32                      s32BPFrameDepth;            /* frame list max length*/
    BIND_MODE_E                 s32BPMode;                   /* bind mode */
}EXT_BIND_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**            |
| --------------- | ----------------- |
| s32BPFrameRate  | 帧率                |
| s32BPFrameDepth | 编码后的数据缓存列表最大长度    |
| s32BPMode       | 编码模式（0 用户态、1 内核态） |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;AK_EXT_VIDEO_BindChn

<br/>

## 接口

### AK_EXT_VIDEO_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取视频流模式库的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR* AK_EXT_VIDEO_GetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**   | **描述** |
| --------- | ------ |
| 视频流模式库版本号 | 成功     |
| NULL      | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_BindChn

&emsp;&emsp;【描述】

&emsp;&emsp;绑定源channel和目的channel。

​        一路源通道绑定多路编码时，只支持绑定都是用户态编码或者都是内核态编码，不能同时绑定用户态编码和内核态编码。

&emsp;&emsp;【语法】

```c
AK_S32 AK_EXT_VIDEO_BindChn(const EXT_CHN_S *pstSrcChn,const EXT_CHN_S *pstDstChn,
                                            const EXT_BIND_PARAM_S *pstBparam);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**    | **取值范围**            | **输入/输出** |
| --------- | --------- | ------------------- | --------- |
| pstSrcChn | 源channel  | 参考APP_CHN_S结构体      | 输入        |
| pstDstChn | 目的channel | 参考APP_CHN_S结构体      | 输入        |
| pstBparam | 绑定参数      | 参考APP_BIND_PARAM结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                                     | **描述**                    |
| ------------------------------------------- | ------------------------- |
| ERROR_TYPE_INVALID_ARG                      | 参数错误                      |
| ERROR_EXT_VIDEO_WRONG_SRC_MODULE            | 源channel模块不支持             |
| ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION     | 错误的绑定关系                   |
| ERROR_EXT_VIDEO_DST_CHN_MUTLEPLE_BINDED     | 目的channel多次绑定             |
| ERROR_EXT_VIDEO_SRC_CHN_OUTOF_RANGE         | 源channel绑定的目的channel超过最大量 |
| ERROR_VI_INVALID_CHNID                      | 错误的vi chn id              |
| ERROR_VI_INVALID_DEVID                      | 错误的vi dev id              |
| ERROR_VI_DEVID_NOT_OPEN                     | vi 设备没有打开                 |
| ERROR_VI_CHANNEL_NOT_EXIST                  | vi channel不存在             |
| ERROR_VENC_USER_NULL                        | venc用户不存在                 |
| ERROR_EXT_VIDEO_SRC_DST_CHN_PARAM_NOT_MATCH | 源channel和目的channel分辨率不匹配  |
| ERROR_EXT_VIDEO_GENERATE_GOBJ_FAILED        | 构建视频绑定结构失败                |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_UnbindChn

&emsp;&emsp;【描述】

&emsp;&emsp;解绑源channel和目的channel。

&emsp;&emsp;【语法】

```C
AK_S32 AK_EXT_VIDEO_UnbindChn(const EXT_CHN_S *pstSrcChn,const EXT_CHN_S *pstDstChn);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**    | **取值范围**       | **输入/输出** |
| --------- | --------- | -------------- | --------- |
| pstSrcChn | 源channel  | 参考APP_CHN_S结构体 | 输入        |
| pstDstChn | 目的channel | 参考APP_CHN_S结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                                 | **描述**             |
| --------------------------------------- | ------------------ |
| ERROR_TYPE_INVALID_ARG                  | 参数错误               |
| ERROR_EXT_VIDEO_WRONG_SRC_MODULE        | 源channel模块不支持      |
| ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION | 错误的绑定关系            |
| ERROR_EXT_VIDEO_SRC_HHN_NOT_BINDED      | 源channel没有绑定       |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED      | 目的channel没有绑定      |
| ERROR_EXT_VIDEO_DST_CHN_NOT_DISABLED    | 目的channel没有disable |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_SetDstChnActive

&emsp;&emsp;【描述】

&emsp;&emsp;使能/不使能已被绑定的目的channel。

&emsp;&emsp;目的channel需要在被bind之后，才可以调用该接口函数使能/不使能目的channel。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_EXT_VIDEO_SetDstChnActive(const EXT_CHN_S *pstChn, AK_S32 s32Enable);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**    | **取值范围**       | **输入/输出** |
| --------- | --------- | -------------- | --------- |
| pstChn    | 目的channel | 参考APP_CHN_S结构体 | 输入        |
| s32Enable | 使能标记      | 0 不使能，1 使能     | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                            | **描述**        |
| ---------------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG             | 参数错误          |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED | 目的channel没有绑定 |
| ERROR_VENC_USER_NULL               | venc用户不存在     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_VencGetStream

&emsp;&emsp;【描述】

&emsp;&emsp;获取视频流数据。

&emsp;&emsp;【语法】

```C
AK_S32 AK_EXT_VIDEO_VencGetStream(const EXT_CHN_S *pstChn, VIDEO_STREAM_S *pstVideoStream);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**    | **取值范围**       | **输入/输出** |
| -------------- | --------- | -------------- | --------- |
| pstChn         | 目的channel | 参考APP_CHN_S结构体 | 输入        |
| pstVideoStream | stream数据  | -              | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                             | **描述**        |
| ----------------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG              | 参数错误          |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED  | 目的channel没有绑定 |
| ERROR_EXT_VIDEO_ENCODRE_HAS_NO_DATA | 没有编码数据        |
| ERROR_VENC_USER_NULL                | 编码用户不存在       |
| ERROR_VENC_GET_STREAM_FAILED        | 获取编码帧失败       |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_SetCb

&emsp;&emsp;【描述】

&emsp;&emsp;设置bind chn的回调函数。这个回调函数会在数据从源chn出来之后，在到达其被bind的各个目的chn之前被调用，属于各个目的chn共有的前处理函数性质。

&emsp;&emsp;对于AK_EXT_VIDEO_SetCb函数，funcVideoDataCb和pvOutput这两个参数都是AK_EXT_VIDEO_SetCb函数的输入参数。AK_EXT_VIDEO_SetCb函数是把funcVideoDataCb和pvOutput这两个参数配置给内部使用，pvOutput这个指针的输出数据，在funcVideoDataCb被回调调用的时候才有数据输出。

&emsp;&emsp;【语法】

```C
AK_S32 AK_EXT_VIDEO_SetCb(const EXT_CHN_S *pstChn, EXT_VIDEO_DATA_CB_S funcVideoDataCb, AK_VOID *pvOutput);
```

&emsp;&emsp;【参数】

| **参数名称**        | **描述**                                                                         | **取值范围**       | **输入/输出** |
| --------------- | ------------------------------------------------------------------------------ | -------------- | --------- |
| pstChn          | 源channel                                                                       | 参考APP_CHN_S结构体 | 输入        |
| funcVideoDataCb | 回调函数                                                                           | 非空             | 输入        |
| pvOutput        | pvOutput为配置funcVideoDataCb的pvOutput参数，具体pvOutput参数的意义请参考funcVideoDataCb回调函数声明。 | 非空             | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**   | **描述**      |
| --------- | ----------- |
| AK_FAILED | 找不到源channel |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

> **注意：**funcVideoDataCb回调函数的声明。

<br/>

```c
typedef AK_VOID (*EXT_VIDEO_DATA_CB_S)(EXT_CHN_S *pstChn, AK_VOID *pvInput, AK_VOID *pvOutput);
```

<br/>

### AK_EXT_VIDEO_UnsetCb

&emsp;&emsp;【描述】

&emsp;&emsp;取消回调函数。

&emsp;&emsp;【语法】

```C
AK_S32 AK_EXT_VIDEO_UnsetCb(const EXT_CHN_S *pstChn);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**       | **输入/输出** |
| -------- | -------- | -------------- | --------- |
| pstChn   | 源channel | 参考APP_CHN_S结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**   | **描述**      |
| --------- | ----------- |
| AK_FAILED | 找不到源channel |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

### AK_EXT_VIDEO_SetChnAttr

&emsp;&emsp;【描述】

&emsp;&emsp;设置channel参数。

&emsp;&emsp;【语法】

```C
AK_S32 AK_EXT_VIDEO_SetChnAttr(const EXT_CHN_S *pstDstChn,
                               const EXT_BIND_PARAM_S *pstBparam);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**    | **取值范围**            | **输入/输出** |
| --------- | --------- | ------------------- | --------- |
| pstDstChn | 目的channel | 参考APP_CHN_S结构体      | 输入        |
| pstBparam | channel参数 | 参考APP_BIND_PARAM结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                | **描述**       |
| ---------------------- | ------------ |
| ERROR_TYPE_INVALID_ARG | 参数错误         |
| AK_FAILED              | 找不到目的channel |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libapp_video.a

&emsp;&emsp;头文件：ak_video.h

<br/>

## ak_video_sample使用示例

运行sample前需要先加载insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko以及ak_venc_adapter.ko 和ak_venc_bridge.ko ，具体命令请参考第7章开头的描述。

| **输入参数**        | **输入参数说明**                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chn_index       | vpss channel id [0:：主通道，1：从通道]                                                                                                                                                                                                                                                                                                              |
| frame_cnt       | 从vi采集的帧数量。                                                                                                                                                                                                                                                                                                                                  |
| chn_res_index   | vpss channel的分辨率<br />[0 - 17]  0 - 320\*184；1 - 320\*240;  2 - 640\*360;  3 - 640\*480;  4 - 736\*756;  5 - 1280\*720;  6 - 1280\*960;  7 - 1920\*1080;   8 - 2304\*1296;  9 - 2048\*1536;  10 - 2560\*1440;  11 - 2688\*1520;  12 - 2880\*1624;  13 - 2560\*1920;  14 - 2944\*1664;  15 - 3072\*1728;  16 - 3072\*2048;  17 - 3840\*2160; |
| chn_framerate   | 帧率                                                                                                                                                                                                                                                                                                                                          |
| enc_type        | 编码输出格式，h264,  h265,   jpeg                                                                                                                                                                                                                                                                                                                  |
| br_mode         | 码率控制模式，0 cbr， 1 vbr                                                                                                                                                                                                                                                                                                                         |
| target_kbps     | 目标码率                                                                                                                                                                                                                                                                                                                                        |
| isp_config_path | isp conf路径                                                                                                                                                                                                                                                                                                                                  |
| frame_save_path | 编码后保存的路径                                                                                                                                                                                                                                                                                                                                    |
| encode_mode     | 编码模式, 0:用户态，1:内核态完整帧模式                                                                                                                                                                                                                                                                                                                      |

<br/>

&emsp;&emsp;输出结果：输出编码后的视频码流文件，保存在指定的path目录下。

<br/>

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### param

| 参数                              | 说明                       |
| ------------------------------- | ------------------------ |
| Chns%d:%d                       | chn src，源chn的模块id和通道id   |
| Chnd%d:%d                       | chn dest，目的chn的模块id和通道id |
| Chns%d:%d_Chnd%d:%d_frame_rate  | 帧率                       |
| Chns%d:%d_Chnd%d:%d_frame_depth | 帧深度                      |
| Chns%d:%d_Chnd%d:%d_mode        | 模式                       |

### stat

| 参数                               | 说明                 |
| -------------------------------- | ------------------ |
| version                          | 版本号                |
| Chns%d:%d_Chnd%d:%d":    "bind", | 模块状态：bind / unbind |

<br/>

## 错误码说明

| 错误代码       | 宏定义                                          | 含义            |
| ---------- | -------------------------------------------- | ------------- |
| 0x1a000000 | ERROR_EXT_VIDEO_WRONG_SRC_MODULE             | 源模块错误         |
| 0x1a000001 | ERROR_EXT_VIDEO_WRONG_MODULE_ID              | 模块id错误        |
| 0x1a000002 | ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION      | 打开次数太多        |
| 0x1a000003 | ERROR_EXT_VIDEO_DST_CHN_MUTLEPLE_BINDED      | 目的通道多次绑定      |
| 0x1a000004 | ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED           | 目的通道没有绑定      |
| 0x1a000005 | ERROR_EXT_VIDEO_SRC_HHN_NOT_BINDED           | 源通道没有绑定       |
| 0x1a000006 | ERROR_EXT_VIDEO_SRC_CHN_OUTOF_RANGE          | 源通道超出范围       |
| 0x1a000007 | ERROR_EXT_VIDEO_SRC_DST_CHN_PARAM_NOT_MATCH  | 源通道、目的通道参数不匹配 |
| 0x1a000008 | ERROR_EXT_VIDEO_GENERATE_GOBJ_FAILED         | GOBJ注册失败      |
| 0x1a000009 | ERROR_EXT_VIDEO_GENERATE_OBJ_FAILED          | OBJ注册失败       |
| 0x1a00000a | ERROR_EXT_VIDEO_ENCODRE_HAS_NO_DATA          | 编码没有数据        |
| 0x1a00000b | ERROR_EXT_VIDEO_FRAME_COUNT_OUTOF_LIMITATION | 帧数量超过限制       |
| 0x1a00000c | ERROR_EXT_VIDEO_DST_CHN_NOT_DISABLED         | 目的通道没有禁用      |

<br/>
