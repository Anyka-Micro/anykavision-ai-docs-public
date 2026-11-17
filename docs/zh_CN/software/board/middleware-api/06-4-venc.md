# 视频编码

## 概述

&emsp;&emsp;视频编码模块（VENC模块）主要负责接收VI模块输出的图像数据，然后按不同协议进行编码并输出相应码流。

&emsp;&emsp;VENC模块支持H.264、H.265、MJPEG格式编码，不同芯片，支持的格式不同：

| **芯片简称**    | **H.264** | **H.265** | **MJPEG** |
| ----------- | --------- | --------- | --------- |
| KM02G系列芯片 | 支持        | 支持        | 支持        |

&emsp;&emsp;VENC模块支持不同的视频帧数据输入格式，不同的芯片，支持的输入格式不同：

| **芯片简称**    | **YUV420P** | **YUV422P** | **YUV400** | **YUV420SP** | **YUV422SP** |
| ----------- | ----------- | ----------- | ---------- | ------------ | ------------ |
| KM02G系列芯片 | 不支持         | 不支持         | 不支持        | 支持           | 不支持          |

## API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **数据结构**                   | **描述**                    |
| -------------------------- | ------------------------- |
| VENC_BITRATE_CTRL_MODE_E   | 码率控制模式                    |
| VENC_OUTPUT_TYPE_E         | 编码输出类型                    |
| VENC_PROFILE_MODE_E        | Profile模式                 |
| VENC_CHROMA_MODE_E         | Chrome 编码输入格式             |
| VENC_GDR_MODE_E            | gdr模式                     |
| VENC_ENCODE_LEVEL_E        | 编码级别                      |
| VENC_CU_BLOCK_SIZE_E       | CU块结构                     |
| VENC_SMART_MODE_E          | 智能编码模式                    |
| VENC_SPEC_PARAM_TYPE_E     | 特殊编码参数设置                  |
| VENC_CHN_ATTRS_S           | 视频编码参数结构                  |
| VENC_ATTR_S                | 编码通道使用的基础参数               |
| VENC_RC_ATTRS_S            | 编码码率控制模式及参数               |
| VENC_EXT_ATTRS_S           | 扩展参数属性                    |
| VENC_RC_AVC_HEVC_ADVANCE_S | 扩展参数属性                    |
| VENC_RC_AVC_HEVC_SMART_S   | 智能编码模式参数                  |
| VENC_H264_ATTR_S           | H264编码的基础参数               |
| VENC_H265_ATTR_S           | H265编码的基础参数               |
| VENC_RC_H264_CBR_S         | H264编码码率控制CBR模式的参数        |
| VENC_RC_H264_VBR_S         | H264编码码率控制VBR模式的参数        |
| VENC_RC_H264_CAPPED_VBR_S  | H264编码码率控制CAPPED_VBR模式的参数 |
| VENC_RC_H264_CONST_QP_S    | H264编码码率控制CONST QP模式的参数   |
| VENC_RC_MJPEG_S            | MJPEG编码码率控制的参数            |
| VENC_RC_H265_CBR_S         | H265编码码率控制CBR模式的参数        |
| VENC_RC_H265_VBR_S         | H265编码码率控制VBR模式的参数        |
| VENC_RC_H265_CAPPED_VBR_S  | H265编码码率控制CAPPED_VBR模式的参数 |
| VENC_RC_H265_AVBR_S        | H265编码码率控制AVBR模式的参数       |
| VENC_RC_H265_CONST_QP_S    | H265编码码率控制CONST QP模式的参数   |
| VENC_CROP_CFG_S            | 裁剪编码配置参数                  |
| VENC_STAT_S                | 编码通道状态信息                  |
| VENC_SPEC_PARAM_S          | 特殊参数                      |
| ROI_SVP_INFO_S             | 感兴趣编码区域属性                 |
| AK_VENC_REQ_DMA_BLOCK      | dma块信息                    |
| RATE_CTRL_PARAM_S          | 外部码率控制参数                  |
| VENC_RC_STATUS_S           | 外部码率控制状态参数                |
| RC_TYPE_E                  | 码率控制模式                    |
| USER_EXIF_TAG_TYPE         | 图像文件格式标签类型                |
| USER_ExifRational          | 用户设定的分子和分母值               |
| EXIF_VALUE                 | 图像文件格式数值                  |
| EXIF_INFO                  | 图像文件格式信息结构                |

<br/>

| **函数接口**                          | **描述**                |
| --------------------------------- | --------------------- |
| AK_MPI_VENC_GetVersion            | 获取视频编码库的版本号           |
| AK_MPI_VENC_GetEncLibVersion      | 获取视频编码算法库的版本号         |
| AK_MPI_VENC_Open                  | 打开视频编码                |
| AK_MPI_VENC_Close                 | 关闭视频编码                |
| AK_MPI_VENC_EncodeFrame           | 编码接口                  |
| AK_MPI_VENC_ReleaseStream         | 释放编码输出的数据             |
| AK_MPI_VENC_SetAttr               | 设置VENC的属性参数           |
| AK_MPI_VENC_GetAttr               | 获取VENC的属性参数           |
| AK_MPI_VENC_RequestIdr            | 请求编I帧                 |
| AK_MPI_VENC_SetQp                 | 设置VENC的QP范围           |
| AK_MPI_VENC_ResetQp               | 重置VENC的QP范围为open时的初始值 |
| AK_MPI_VENC_SetIframeParam        | 设置VENC的I帧参数           |
| AK_MPI_VENC_GetIframeParam        | 获取VENC的I帧参数           |
| AK_MPI_VENC_SetRoiMdinfo          | 设置ROI相关参数             |
| AK_MPI_VENC_SetRoiSvpInfo         | 设置ROI区域参数             |
| AK_MPI_VENC_StriclylimitFrameSize | 设置硬限制帧大小              |
| AK_MPI_VENC_GetStat               | 获取VENC的统计信息           |
| AK_MPI_VENC_SetJpegSlice          | 设置jpeg slice编码        |
| AK_MPI_VENC_JpegSliceEncode       | 做jpeg slice编码         |
| AK_MPI_VENC_SetFps                | 设置编码的slice模式帧率        |
| AK_MPI_VENC_GetCrop               | 获取当前编码通道裁剪编码的信息       |
| AK_MPI_VENC_SetCrop               | 设置编码通道裁剪编码信息          |
| AK_MPI_VENC_SetFunction           | 修改动态场景切换逻辑方案          |
| AK_MPI_VENC_GetFunction           | 获取当前采用的动态场景切换逻辑方案     |
| AK_MPI_VENC_SetRcType             | 设置码率控制模式              |
| AK_MPI_VENC_SetRcParam            | 设置外部码率控制参数            |
| AK_MPI_VENC_GetRcStat             | 获取码率控制信息              |
| AK_MPI_VENC_SetStreamBufSize      | 设置编码库内部stream buf大小   |
| AK_MPI_VENC_SetExifEnable         | 使能Exif功能              |
| AK_MPI_VENC_SetExifInfo           | 设置Exif信息              |

## 数据结构

### VENC_BITRATE_CTRL_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;码率控制模式

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_BITRATE_CTRL_MODE_E {
        VENC_RC_MODE_H264_CBR,
        VENC_RC_MODE_H264_VBR,
        VENC_RC_MODE_H264_CAPPED_VBR,
        VENC_RC_MODE_H264_AVBR,
        VENC_RC_MODE_H264_CONST_QP,
        VENC_RC_MODE_MJPEG,
        VENC_RC_MODE_H265_CBR,
        VENC_RC_MODE_H265_VBR,
        VENC_RC_MODE_H265_CAPPED_VBR,
        VENC_RC_MODE_H265_AVBR,
        VENC_RC_MODE_H265_CONST_QP,
        VENC_RC_MODE_TYPE_TOTAL
    }VENC_BITRATE_CTRL_MODE_E;
```

&emsp;&emsp;【成员】

| 成员名称                         | 描述             |
| ---------------------------- | -------------- |
| VENC_RC_MODE_H264_CBR        | 恒定码率模式         |
| VENC_RC_MODE_H264_VBR        | 可变码率模式         |
| VENC_RC_MODE_H264_CAPPED_VBR | 上限可变比特率        |
| VENC_RC_MODE_H264_AVBR       | 较高级的VBR模式      |
| VENC_RC_MODE_H264_CONST_QP   | 固定QP模式         |
| VENC_RC_MODE_MJPEG           | MJPEG的编码大小控制模式 |
| VENC_RC_MODE_H265_CBR        | 恒定码率模式         |
| VENC_RC_MODE_H265_VBR        | 可变码率模式         |
| VENC_RC_MODE_H265_CAPPED_VBR | 上限可变比特率        |
| VENC_RC_MODE_H265_AVBR       | 较高级的VBR模式      |
| VENC_RC_MODE_H265_CONST_QP   | 固定QP模式         |
| VENC_RC_MODE_TYPE_TOTAL      | 码率控制模式总数       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_OUTPUT_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;编码输出格式。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_OUTPUT_TYPE_E {
        H264_ENC_TYPE,
        MJPEG_ENC_TYPE,
        HEVC_ENC_TYPE
    }VENC_OUTPUT_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**  |
| -------------- | ------- |
| H264_ENC_TYPE  | H.264格式 |
| MJPEG_ENC_TYPE | MJPEG格式 |
| HEVC_ENC_TYPE  | H.265格式 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_PROFILE_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;Profile配置选择。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_PROFILE_MODE_E {
        VENC_PROFILE_MAIN,
        VENC_PROFILE_HIGH,
        VENC_PROFILE_BASE,
        VENC_PROFILE_C_BASE,
        VENC_PROFILE_HEVC_MAIN,
        VENC_PROFILE_HEVC_MAIN_STILL,
        VENC_PROFILE_HEVC_MAIN_INTRA,
        VENC_PROFILE_JPEG
    }VENC_PROFILE_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                     | **描述**                     |
| ---------------------------- | -------------------------- |
| VENC_PROFILE_MAIN            | H.264格式的main profile       |
| VENC_PROFILE_HIGH            | H.264格式的high profile       |
| VENC_PROFILE_BASE            | H.264格式的base profile       |
| VENC_PROFILE_C_BASE          | H.264格式的c base profile     |
| VENC_PROFILE_HEVC_MAIN       | H.265格式的main profile       |
| VENC_PROFILE_HEVC_MAIN_STILL | H.265格式的main still profile |
| VENC_PROFILE_HEVC_MAIN_INTRA | H.265格式的main intra profile |
| VENC_PROFILE_JPEG            | jpeg格式的profile             |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CHROMA_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;Chrome 编码输入格式选择。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_CHROMA_MODE_E {
        VENC_CHROMA_MONO,
        VENC_CHROMA_YUV420
    }VENC_CHROMA_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**        |
| ------------------ | ------------- |
| VENC_CHROMA_MONO   | 灰度图像,，仅用于jpeg |
| VENC_CHROMA_YUV420 | 彩色图像，YUV420sp |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_GDR_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;GDR模式，优化高码率I帧限制带宽的问题。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_GDR_MODE_E {
        VENC_GDR_OFF,
        VENC_GDR_VERTICAL,
        VENC_GDR_HORIZONTAL
    }VENC_GDR_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**            | **描述**  |
| ------------------- | ------- |
| VENC_GDR_OFF        | 关闭gdr   |
| VENC_GDR_VERTICAL   | 垂直方向gdr |
| VENC_GDR_HORIZONTAL | 水平方向gdr |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_ENCODE_LEVEL_E

&emsp;&emsp;【说明】

&emsp;&emsp;编码级别

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_ENCODE_LEVEL_E {
        VENC_HEVC_AVC_LEVEL_1   = 10,
        VENC_AVC_LEVEL_1_1      = 11, //only for avc
        VENC_AVC_LEVEL_1_2      = 12, //only for avc
        VENC_AVC_LEVEL_1_3      = 13, //only for avc
        VENC_HEVC_AVC_LEVEL_2     = 20,
        VENC_HEVC_AVC_LEVEL_2_1 = 21,
        VENC_AVC_LEVEL_2_2      = 22, //only for avc
        VENC_HEVC_AVC_LEVEL_3   = 30,
        VENC_HEVC_AVC_LEVEL_3_1 = 31,
        VENC_AVC_LEVEL_3_2      = 32, //only for avc
        VENC_HEVC_AVC_LEVEL_4   = 40,
        VENC_HEVC_AVC_LEVEL_4_1 = 41,
        VENC_AVC_LEVEL_4_2      = 42, //only for avc
        VENC_HEVC_AVC_LEVEL_5   = 50,
        VENC_HEVC_AVC_LEVEL_5_1 = 51,
        VENC_HEVC_AVC_LEVEL_5_2 = 52,
        VENC_HEVC_AVC_LEVEL_6   = 60,
        VENC_HEVC_AVC_LEVEL_6_1 = 61,
        VENC_HEVC_AVC_LEVEL_6_2 = 62
    }VENC_ENCODE_LEVEL_E;
```

  &emsp; 【成员】

| **成员名称**                | **描述**               |
| ----------------------- | -------------------- |
| VENC_HEVC_AVC_LEVEL_1   | Level 10 适用H264/H265 |
| VENC_AVC_LEVEL_1_1      | Level 11 适用H264      |
| VENC_AVC_LEVEL_1_2      | Level 12 适用H264      |
| VENC_AVC_LEVEL_1_3      | Level 13 适用H264      |
| VENC_HEVC_AVC_LEVEL_2   | Level 20 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_2_1 | Level 21 适用H264/H265 |
| VENC_AVC_LEVEL_2_2      | Level 22 适用H264      |
| VENC_HEVC_AVC_LEVEL_3   | Level 30 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_3_1 | Level 31 适用H264/H265 |
| VENC_AVC_LEVEL_3_2      | Level 32 适用H264      |
| VENC_HEVC_AVC_LEVEL_4   | Level 40 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_4_1 | Level 41 适用H264/H265 |
| VENC_AVC_LEVEL_4_2      | Level 42 适用H264      |
| VENC_HEVC_AVC_LEVEL_5   | Level 50 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_5_1 | Level 51 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_5_2 | Level 52 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_6   | Level 60 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_6_1 | Level 61 适用H264/H265 |
| VENC_HEVC_AVC_LEVEL_6_2 | Level 62 适用H264/H265 |

````{only} anyka_review
```{admonition} TODO
:class: warning

图片已移除：第三方来源，待安凯重新绘制。

Figure removed: third-party source, pending redraw by Anyka.
```
````

以下为 H.265 各 level 的通用限制，数据来自 [ITU-T H.265](https://www.itu.int/rec/T-REC-H.265) 附录 A。

| Level | 最大亮度图像尺寸（样点） | 最大亮度采样率（样点/秒） | Main tier 最大码率（kbit/s） | High tier 最大码率（kbit/s） | 最小压缩比 |
| --- | --- | --- | --- | --- | --- |
| 1 | 36,864 | 552,960 | 128 | – | 2 |
| 2 | 122,880 | 3,686,400 | 1,500 | – | 2 |
| 2.1 | 245,760 | 7,372,800 | 3,000 | – | 2 |
| 3 | 552,960 | 16,588,800 | 6,000 | – | 2 |
| 3.1 | 983,040 | 33,177,600 | 10,000 | – | 2 |
| 4 | 2,228,224 | 66,846,720 | 12,000 | 30,000 | 4 |
| 4.1 | 2,228,224 | 133,693,440 | 20,000 | 50,000 | 4 |
| 5 | 8,912,896 | 267,386,880 | 25,000 | 100,000 | 6 |
| 5.1 | 8,912,896 | 534,773,760 | 40,000 | 160,000 | 8 |
| 5.2 | 8,912,896 | 1,069,547,520 | 60,000 | 240,000 | 8 |
| 6 | 35,651,584 | 1,069,547,520 | 60,000 | 240,000 | 8 |
| 6.1 | 35,651,584 | 2,139,095,040 | 120,000 | 480,000 | 8 |
| 6.2 | 35,651,584 | 4,278,190,080 | 240,000 | 800,000 | 6 |

​                                                                                Level对照表

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CU_BLOCK_SIZE_E

&emsp;&emsp;【说明】

&emsp;&emsp;CU块大小，仅H.265格式支持。

&emsp;&emsp;【定义】

```c
typedef enum akVENC_CU_BLOCK_SIZE_E {
    VENC_CUSize32x32,          /*!< CU size 32x32, just for HEVC */
    VENC_CUSize16x16,          /*!< CU size 16x16, just for HEVC */
    VENC_CUSize8x8             /*!< CU size 8x8, just for HEVC */
}VENC_CU_BLOCK_SIZE_E;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                |
| ---------------- | --------------------- |
| VENC_CUSize32x32 | CU块大小32*32，仅H.265格式支持 |
| VENC_CUSize16x16 | CU块大小16*16，仅H.265格式支持 |
| VENC_CUSize8x8   | CU块大小8*8，仅H.265格式支持   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_SMART_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp; 智能编码模式。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_SMART_MODE_E {
        VENC_SMART_OFF,
        VENC_SMART_LTR,
        VENC_SMART_GOP_CHANGE,
        VENC_SMART_SKIP_REF,
        VENC_SMART_LTRC,
        VENC_SMART_SKIP_REF_LTRC
    }VENC_SMART_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                 | **描述**      |
| ------------------------ | ----------- |
| VENC_SMART_OFF           | 不开启         |
| VENC_SMART_LTR           | 长期参考帧模式     |
| VENC_SMART_GOP_CHANGE    | GOP可变模式     |
| VENC_SMART_SKIP_REF      | 跳帧参考模式      |
| VENC_SMART_LTRC          | 长期参考帧候选模式   |
| VENC_SMART_SKIP_REF_LTRC | LTRC的跳帧参考模式 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_SPEC_PARAM_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp; 特殊编码参数设置。

&emsp;&emsp;【定义】

```c
    typedef enum akVENC_SPEC_PARAM_TYPE_E {
        VENC_SPEC_PARAM_START_TYPE,
        VENC_MAX_REORDER_PICS_NUM,
        VENC_SPEC_PARAM_END_TYPE
    }VENC_SPEC_PARAM_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                   | **描述**                |
| -------------------------- | --------------------- |
| VENC_SPEC_PARAM_START_TYPE | 起始值                   |
| VENC_MAX_REORDER_PICS_NUM  | 设置reorder pics num 的值 |
| VENC_SPEC_PARAM_END_TYPE   | 结束值                   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CHN_ATTRS_S

&emsp;&emsp;【说明】

&emsp;&emsp;视频编码参数结构，open/set attr时传入。

&emsp;&emsp;【定义】

```c
    typedef struct akVENC_CHN_ATTRS_S
    {
        VENC_ATTR_S stVencAttrs;
        VENC_RC_ATTRS_S stRcAttrs;
        VENC_EXT_ATTRS_S stExtAttrs;
    }VENC_CHN_ATTRS_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**      |
| ----------- | ----------- |
| stVencAttrs | 编码通道基础参数    |
| stRcAttrs   | 码率控制参数      |
| stExtAttrs  | 扩展编码属性，高阶参数 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;编码通道使用的基础参数。

&emsp;&emsp;【定义】

```c
    typedef struct akVENC_ATTR_S
    {
        AK_U16 u16Width;
        AK_U16 u16Height;
        VENC_OUTPUT_TYPE_E enOutputType;
        AK_U32 u32MaxBufSize;
        AK_U32 u32MaxDMASize;
        VENC_CHROMA_MODE_E enChromaMode; //color formats
        AK_U32 u32Priority;
        union
        {
            VENC_H264_ATTR_S stH264Attr;
            VENC_H265_ATTR_S stH265Attr;
        };
    }VENC_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**              |
| ------------- | ------------------- |
| u16Width      | 编码宽度                |
| u16Height     | 编码高度                |
| enOutputType  | 编码输出类型              |
| u32MaxBufSize | 编码缓存大小，单位KBytes     |
| u32MaxDMASize | 编码器使用DMA大小，单位KBytes |
| enChromaMode  | 输入编码的图像格式           |
| u32Priority   | 编码通道优先级             |
| stH264Attr    | 编码H264所需参数          |
| stH265Attr    | 编码H265所需参数          |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_ATTRS_S

&emsp;&emsp;【说明】

&emsp;&emsp;编码码率控制模式及参数。

&emsp;&emsp;【定义】

```c
    typedef struct akVENC_RC_ATTRS_S
    {
        VENC_BITRATE_CTRL_MODE_E enRcMode;
        union
        {
        VENC_RC_H264_CBR_S stH264Cbr;
        VENC_RC_H264_VBR_S stH264Vbr;
        VENC_RC_H264_CAPPED_VBR_S stH264CappedVbr;
        VENC_RC_H264_AVBR_S stH264Avbr;
        VENC_RC_H264_CONST_QP_S stH264ConstQp;
        VENC_RC_MJPEG_S stMjpegRc;
        VENC_RC_H265_CBR_S stH265Cbr;
        VENC_RC_H265_VBR_S stH265Vbr;
        VENC_RC_H265_CAPPED_VBR_S stH265CappedVbr;
        VENC_RC_H265_AVBR_S stH265Avbr;
        VENC_RC_H265_CONST_QP_S stH265ConstQp;
        };
    }VENC_RC_ATTRS_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**              |
| --------------- | ------------------- |
| enRcMode        | 编码码率控制模式            |
| stH264Cbr       | H264 CBR模式参数        |
| stH264Vbr       | H264 VBR模式参数        |
| stH264CappedVbr | H264 CAPPED_VBR模式参数 |
| stH264Avbr      | H264 AVBR模式参数       |
| stH264ConstQp   | H264 const-qp模式参数   |
| stMjpegRc       | MJPEG码率控制参数         |
| stH265Cbr       | H265 CBR模式参数        |
| stH265Vbr       | H265 VBR模式参数        |
| stH265CappedVbr | H265 CAPPED_VBR模式参数 |
| stH265Avbr      | H265 AVBR模式参数       |
| stH265ConstQp   | H265 const-qp模式参数   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_EXT_ATTRS_S

&emsp;&emsp;【说明】

&emsp;&emsp;扩展参数属性。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_EXT_ATTRS_S
{
    VENC_RC_AVC_HEVC_ADVANCE_S stAdvance;
    VENC_RC_AVC_HEVC_SMART_S stSmart;
}VENC_EXT_ATTRS_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                 |
| --------- | ---------------------- |
| stAdvance | 编码高阶参数一般无需设置           |
| stSmart   | H264/265适用的smart编码模式参数 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_AVC_HEVC_ADVANCE_S

&emsp;&emsp;【说明】

&emsp;&emsp;扩展参数属性。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_AVC_HEVC_ADVANCE_S
{
    VENC_CU_BLOCK_SIZE_E enCuBlock;
    AK_U16 u16MinQP[3];
    AK_U16 u16MaxQP[3];
    AK_S16 s16IPDelta;
    AK_U32 u32MaxPictureISize;
    AK_U32 u32MaxPicturePSize;
    AK_U32 u32MaxPictureBSize;
    AK_BOOL bEnableSRD;
    AK_U8 u8SRDThreshold;
    AK_BOOL bEnableMMA;
}VENC_RC_AVC_HEVC_ADVANCE_S;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                                       |
| ------------------ | -------------------------------------------- |
| enCuBlock          | 编码高阶参数一般无需设置                                 |
| u16MinQP           | I\P\B帧最小qp值，一般使用在CBR和VBR两种不能单独设置QP的模式        |
| u16MaxQP           | I\P\B帧最大qp值，一般使用在CBR和VBR两种不能单独设置QP的模式        |
| s16IPDelta         | Delta值，I帧和P帧QP 差值                            |
| u32MaxPictureISize | 最大I帧大小，单位Kbits;                              |
| u32MaxPicturePSize | 最大P帧大小，单位Kbits;                              |
| u32MaxPictureBSize | 最大B帧大小，单位Kbits;                              |
| bEnableSRD         | 使能静态区域检测功能                                   |
| u8SRDThreshold     | 静态区域检测阈值                                     |
| bEnableMMA         | Minimum Memory Allocation mode,参考帧和重构帧共享一个缓存 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_AVC_HEVC_SMART_S

&emsp;&emsp;【说明】

&emsp;&emsp;智能编码模式进一步降低码率适用于H264和H265编码。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_AVC_HEVC_SMART_S
{
    VENC_SMART_MODE_E enSmartMode;
    AK_U16 u16SmartGopLen;
    AK_U16 u16SmartQuality;
    AK_U16 u16StaticValue;
}VENC_RC_AVC_HEVC_SMART_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**    |
| --------------- | --------- |
| enSmartMode     | smart编码模式 |
| u16SmartGopLen  | 智能gop长度   |
| u16SmartQuality | Smart编码质量 |
| u16StaticValue  | 静态阈值      |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_H264_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码的基础参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_H264_ATTR_S
{
    AK_U16    u16Framerate;
    AK_U16    u16GopLen;
    VENC_GDR_MODE_E    enGdrMode;
    VENC_PROFILE_MODE_E    enProfileMode;
    VENC_ENCODE_LEVEL_E enEncLevel;
}VENC_H264_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                                                                   |
| ------------- | ---------------------------------------------------------------------------------------- |
| u16Framerate  | 编码帧率。<br />支持小数帧率表示。高8位表示分母，低8位表示分子，高8位为0或者1，都表示分母为1。例如：12.5帧率，输入0xA7D，编码库显示帧率12500/1000 |
| u16GopLen     | I帧间隔                                                                                     |
| enGdrMode     | GDR模式                                                                                    |
| enProfileMode | Profile模式                                                                                |
| enEncLevel    | 编码level                                                                                  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_H265_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码的基础参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_H265_ATTR_S
{
    AK_U16    u16Framerate;
    AK_U16    u16GopLen;
    VENC_GDR_MODE_E    enGdrMode;
    VENC_PROFILE_MODE_E    enProfileMode;
    VENC_ENCODE_LEVEL_E enEncLevel;
}VENC_H265_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**    |
| ------------- | --------- |
| u16Framerate  | 编码帧率      |
| u16GopLen     | I帧间隔      |
| enGdrMode     | GDR模式     |
| enProfileMode | Profile模式 |
| enEncLevel    | 编码level   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码码率控制CBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H264_CBR_S
{
    AK_U16 u16TargetBitrate;
}VENC_RC_H264_CBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**   |
| ---------------- | -------- |
| u16TargetBitrate | 目标码率kbit |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_VBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码码率控制VBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H264_VBR_S
{
    AK_U16 u16MaxBitrate;
    AK_U16 u16Quality;
}VENC_RC_H264_VBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**    |
| ------------- | --------- |
| u16MaxBitrate | 最大码率Kbits |
| u16Quality    | 编码质量      |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CAPPED_VBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码码率控制CAPPED_VBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H264_CAPPED_VBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitRate;
    AK_U16 u16ChangePos;  //[0, 100]
    AK_DOUBLE d64MinPSNR; //[0, 100]
    AK_DOUBLE d64MaxPSNR; //[0, 100]
}VENC_RC_H264_CAPPED_VBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                        |
| ------------- | --------------------------------------------- |
| u16MinQP      | 编码最小qp值                                       |
| u16MaxQP      | 编码最大qp值                                       |
| u16MaxBitRate | 最大码率Kbits                                     |
| u16ChangePos  | targetBitrate = maxBitrate*changePos/100,比例因子 |
| d64MinPSNR    | 最小信噪比 [0, 100]                                |
| d64MaxPSNR    | 最大信噪比 [0, 100]                                |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_AVBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码码率控制AVBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H264_AVBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitrate;
    AK_U16 u16ChangePos;
}VENC_RC_H264_AVBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                        |
| ------------- | --------------------------------------------- |
| u16MinQP      | 编码最小qp值                                       |
| u16MaxQP      | 编码最大qp值                                       |
| u16MaxBitrate | 最大码率Kbits                                     |
| u16ChangePos  | targetBitrate = maxBitrate*changePos/100,比例因子 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CONST_QP_S

&emsp;&emsp;【说明】

&emsp;&emsp;H264编码码率控制CONST QP模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H264_CONST_QP_S
{
    AK_U16 u16QP;
}VENC_RC_H264_CONST_QP_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述** |
| -------- | ------ |
| u16QP    | 编码qp值  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_MJPEG_S

&emsp;&emsp;【说明】

&emsp;&emsp;MJPEG编码码率控制的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_MJPEG_S
{
    AK_U16 u16Quality;
}VENC_RC_MJPEG_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**                 |
| ---------- | ---------------------- |
| u16Quality | 编码质量， 范围[0, 100]，推荐值75 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码码率控制CBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H265_CBR_S
{
    AK_U16 u16TargetBitrate;
}VENC_RC_H265_CBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**   |
| ---------------- | -------- |
| u16TargetBitrate | 目标码率kbit |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_VBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码码率控制VBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H265_VBR_S
{
    AK_U16 u16MaxBitrate;
    AK_U16 u16Quality;
}VENC_RC_H265_VBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                                   |
| ------------- | -------------------------------------------------------- |
| u16MaxBitrate | 最大码率Kbits                                                |
| u16Quality    | 编码质量，MinQP计算公式：MinQP = MaxQP - Quality*（MaxQP-MinQP）/100 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CAPPED_VBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码码率控制CAPPED_VBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H265_CAPPED_VBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitRate;
    AK_U16 u16ChangePos;  //[0, 100]
    AK_DOUBLE d64MinPSNR; //[0, 100]
    AK_DOUBLE d64MaxPSNR; //[0, 100]
}VENC_RC_H265_CAPPED_VBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                        |
| ------------- | --------------------------------------------- |
| u16MinQP      | 编码最小qp值                                       |
| u16MaxQP      | 编码最大qp值                                       |
| u16MaxBitRate | 最大码率Kbits                                     |
| u16ChangePos  | targetBitrate = maxBitrate*changePos/100,比例因子 |
| d64MinPSNR    | 最小信噪比 [0, 100]                                |
| d64MaxPSNR    | 最大信噪比 [0, 100]                                |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_AVBR_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码码率控制AVBR模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H265_AVBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitrate;
    AK_U16 u16ChangePos;
}VENC_RC_H265_AVBR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                                        |
| ------------- | --------------------------------------------- |
| u16MinQP      | 编码最小qp值                                       |
| u16MaxQP      | 编码最大qp值                                       |
| u16MaxBitrate | 最大码率Kbits                                     |
| u16ChangePos  | targetBitrate = maxBitrate*changePos/100,比例因子 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CONST_QP_S

&emsp;&emsp;【说明】

&emsp;&emsp;H265编码码率控制CONST QP模式的参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_H265_CONST_QP_S
{
    AK_U16 u16QP;
}VENC_RC_H265_CONST_QP_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述** |
| -------- | ------ |
| u16QP    | 编码qp值  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CROP_CFG_S

&emsp;&emsp;【说明】

&emsp;&emsp;裁剪编码配置参数。

&emsp;&emsp;【定义】

```c
typedef struct RECT_S {
    AK_U32 u32Width;
    AK_U32 u32Height;
    AK_U32 u32X;
    AK_U32 u32Y;
}RECT_S;

typedef struct akVENC_CROP_CFG_S
{
    AK_BOOL bEnable;
    RECT_S stRect;
}VENC_CROP_CFG_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**   |
| -------- | -------- |
| bEnable  | 使能裁剪编码参数 |
| stRect   | 裁剪坐标及宽高  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_SetCrop(AK_S32 s32ChnId, const VENC_CROP_CFG_S *pstCrop);
```

<br/>

### VENC_STAT_S

&emsp;&emsp;【说明】

&emsp;&emsp;编码通道状态信息。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_STAT_S
{
    AK_U32 u32Fps;
    AK_U32 u32GopLen;
    AK_U64 u32Kbps;
    AK_U64 u64MaxPictureSize;
}VENC_STAT_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**   |
| ----------------- | -------- |
| u32Fps            | 编码实际帧率统计 |
| u32GopLen         | Gop长度    |
| u32Kbps           | 编码实际码率统计 |
| u64MaxPictureSize | 最大编码帧大小  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_VENC_GetStat(AK_S32 s32ChnId, VENC_STAT_S *pstStat);
```

<br/>

### VENC_SPEC_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;特殊参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_SPEC_PARAM_S
{
    VENC_SPEC_PARAM_TYPE_E enSpecType;
    union{
        VENC_HEVC_SPEC_PARAM_S stHevcSpecReorder;
    };
}VENC_SPEC_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**   |
| ----------------- | -------- |
| enSpecType        | 特殊编码参数枚举 |
| stHevcSpecReorder | 特殊参数设置   |

<br/>

### VENC_HEVC_SPEC_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;特殊参数设置。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_HEVC_SPEC_PARAM_S
{
    AK_U8 u8MaxNumReorderPics;
}VENC_HEVC_SPEC_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**            | **描述**                                                         |
| ------------------- | -------------------------------------------------------------- |
| u8MaxNumReorderPics | 设置VPS和SPS中的vps_max_num_reorder_pics和sps_max_num_reorder_pics参数 |

<br/>

### ROI_SVP_INFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;感兴趣编码区域属性。

&emsp;&emsp;【定义】

```c
typedef struct akROI_SVP_INFO_S
{
    AK_U16 u16RoiNum;
    AK_U16 u16RoiLeft[10];
    AK_U16 u16RoiTop[10];
    AK_U32 u32RoiWidth[10];
    AK_U32 u32RoiHeigh[10];
    AK_S32 s32RoiQuality[10];
}ROI_SVP_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                    |
| ------------- | ------------------------- |
| u16RoiNum     | ROI 的数量，最大设置10            |
| u16RoiLeft    | ROI 的起始坐标像素X              |
| u16RoiTop     | ROI 的起始坐标像素Y              |
| u32RoiWidth   | ROI 的宽度                   |
| u32RoiHeigh   | ROI 的高度                   |
| s32RoiQuality | ROI区域周围的QP差值，[-15 ,15] 取值 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetRoiSvpInfo(AK_S32 s32ChnId, ROI_SVP_INFO_S *pstRoiParam);
```

<br/>

### AK_VENC_REQ_DMA_BLOCK

&emsp;&emsp;【说明】

​        dma块信息。

&emsp;&emsp;【定义】

```c
    #define AK_VENC_MAX_DMA_BLOCK_NUM    20
    typedef struct ak_venc_req_dma_block{
        unsigned int block_num;
        unsigned int block_size[AK_VENC_MAX_DMA_BLOCK_NUM];
    }AK_VENC_REQ_DMA_BLOCK;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述** |
| ---------- | ------ |
| block_num  | 块数量    |
| block_size | 块大小    |

<br/>

### RATE_CTRL_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;外部码率控制参数。

&emsp;&emsp;【定义】

```c
typedef struct akRATE_CTRL_PARAM_S
{
    AK_U16 u16SliceQP;
}RATE_CTRL_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述** |
| ---------- | ------ |
| u16SliceQP | QP值    |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetRcParam(AK_S32 s32ChnId, RATE_CTRL_PARAM_S *pstRcParam);
```

<br/>

### VENC_RC_STATUS_S

&emsp;&emsp;【说明】

&emsp;&emsp;外部码率控制状态参数。

&emsp;&emsp;【定义】

```c
typedef struct akVENC_RC_STATUS_S
{
    AK_U32 u32SumCplx;
    VIDEO_FRAME_TYPE_E eSliceType;
}VENC_RC_STATUS_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**  |
| ---------- | ------- |
| u32SumCplx | LCU复杂度和 |
| eSliceType | 下一帧的类型  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_GetRcStat(AK_S32 s32ChnId, VENC_RC_STATUS_S *pstRcStatus);
```

<br/>

### CUR_QP_PARAM

&emsp;&emsp;【说明】

&emsp;&emsp;获取当前qp值结构体

&emsp;&emsp;【定义】

```c
typedef struct CUR_QP_PARAM_S
{
    AK_S32 s32CurQp;
}CUR_QP_PARAM;
```

&emsp;&emsp;【成员】

| 成员名称     | 描述    |
| -------- | ----- |
| s32CurQp | 当前qp值 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_GetCurQp(AK_S32 s32ChnId, CUR_QP_PARAM *pstCurQpParam);
```

<br/>

### QP_TABLE_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;QP Table结构体

&emsp;&emsp;【定义】

```c
typedef struct  akQP_TABLE_PARAM_S
{
    AK_U32 u32NumLCUs;
    AK_U32 u32NumQPPerLCU;
    AK_U32 u32NumBytesPerLCU;
}QP_TABLE_PARAM_S;
```

&emsp;&emsp;【成员】

| 成员名称              | 描述                  |
| ----------------- | ------------------- |
| u32NumLCUs        | 一帧图像中LCU的数目         |
| u32NumQPPerLCU    | 一个LCU块的QP值数目        |
| u32NumBytesPerLCU | QpTable中一个LCU占多少个字节 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_GetQpTableParam(AK_S32 s32ChnId, QP_TABLE_PARAM_S * pstQpTableParam);
```

<br/>

### RC_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;码率控制模式。

&emsp;&emsp;【定义】

```c
typedef enum akRC_TYPE_E
{
    INTERNAL = 0x00,  // Use internal Rate Ctrl of encoder lib.
    EXTERNAL = 0x01,  // Use external Rate Ctrl of user.
}RC_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述** |
| -------- | ------ |
| INTERNAL | 内部码率控制 |
| EXTERNAL | 外部码率控制 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetRcType(AK_S32 s32ChnId, RC_TYPE_E eRcType);
```

<br/>

### USER_EXIF_TAG_TYPE

&emsp;&emsp;【说明】

&emsp;&emsp;图像文件格式标签类型。

&emsp;&emsp;【定义】

```c
typedef enum {
    USER_EXIF_TAG_EXPOSURE_TIME = 0,    // 对应驱动层的 EXIF_TAG_EXPOSURE_TIME
    USER_EXIF_TAG_ISO_SPEED_RATINGS = 1, // 对应驱动层的 EXIF_TAG_ISO_SPEED_RATINGS
    USER_EXIF_TAG_MAX
} USER_EXIF_TAG_TYPE;
```

&emsp;&emsp;【成员】

| **成员名称**                        | **描述** |
| ------------------------------- | ------ |
| USER_EXIF_TAG_EXPOSURE_TIME     | 快门     |
| USER_EXIF_TAG_ISO_SPEED_RATINGS | ISO    |
| USER_EXIF_TAG_MAX               | 最大值    |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### USER_ExifRational

&emsp;&emsp;【说明】

&emsp;&emsp;用户设定的分子和分母值

&emsp;&emsp;【定义】

```c
typedef struct {
    AK_U32    numerator;
    AK_U32    denominator;
} USER_ExifRational;
```

&emsp;&emsp;【成员】

| 成员名称        | 描述  |
| ----------- | --- |
| numerator   | 分子  |
| denominator | 分母  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### EXIF_VALUE

&emsp;&emsp;【说明】

&emsp;&emsp;Exif数值

&emsp;&emsp;【定义】

```c
typedef union {
    USER_ExifRational rational_value;
    AK_U16 short_value;
} EXIF_VALUE;
```

&emsp;&emsp;【成员】

| 成员名称           | 描述          |
| -------------- | ----------- |
| rational_value | 用户设定的分子和分母值 |
| short_value    | 数值          |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### EXIF_INFO

&emsp;&emsp;【说明】

&emsp;&emsp;Exif信息结构体

&emsp;&emsp;【定义】

```c
typedef struct {
    USER_EXIF_TAG_TYPE user_tag;
    EXIF_VALUE value;
} EXIF_INFO;
```

&emsp;&emsp;【成员】

| 成员名称     | 描述       |
| -------- | -------- |
| user_tag | Exif标签类型 |
| value    | Exif数值   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>
## 版本信息获取

### AK_MPI_VENC_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取视频编码库的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR* AK_MPI_VENC_GetVersion(void);
```

&emsp;&emsp;【返回值】

| **返回值**   | **描述** |
| --------- | ------ |
| 视频编码模块版本号 | 成功     |
| NULL      | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_GetEncLibVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取视频编码算法库的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR* AK_MPI_VENC_GetEncLibVersion(void);
```

&emsp;&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| 视频编码算法库版本号 | 成功     |
| NULL       | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

## 打开/关闭模块

### AK_MPI_VENC_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开视频编码，支持多路编码，每个编码器对应一个句柄。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**     | **取值范围**            | **输入/输出** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | 视频编码模块句柄ID | [0,VENC_MAX_USER-1] | 输入        |
| pstChnAttrs | 视频编码输入参数   | 参考struct 结构体        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                   | **描述**     |
| ------------------------- | ---------- |
| ERROR_VENC_INVALID_PARAM  | 参数错误       |
| ERROR_VENC_INIT_LIB_ERROR | 编码库初始化失败   |
| ERROR_VENC_OPEN_TOO_MANY  | 打开次数已满     |
| ERROR_TYPE_MALLOC_FAILED  | Buffer申请失败 |
| ERROR_VENC_OPEN_LIB_ERROR | 编码库打开失败    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_VENC_Close(AK_S32 s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**函数可重入，可以对VENC模块进行多次open；

<br/>

### AK_MPI_VENC_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭视频编码。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_VENC_Close(AK_S32 s32ChnId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围**            | **输入/输出** |
| -------- | ---------- | ------------------- | --------- |
| s32ChnId | 视频编码模块句柄ID | [0,VENC_MAX_USER-1] | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                         | **描述**           |
| ------------------------------- | ---------------- |
| ERROR_VENC_USER_NULL            | s32ChnId对应的用户不存在 |
| ERROR_VENC_DELETE_CHN_FAILED    | 编码通道销毁失败         |
| ERROR_VENC_DEL_DMA_BLOCK_FAILED | dma pool销毁失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 编码流程

### AK_MPI_VENC_EncodeFrame

&emsp;&emsp;【描述】

&emsp;&emsp;编码接口。

&emsp;&emsp;【语法】

```C
AK_S32 AK_MPI_VENC_EncodeFrame(AK_S32 s32ChnId, const AK_U8 *pu8Frame,AK_U32 u32FrameLen,
                                AK_VOID *pvMdinfo, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**        | **取值范围**            | **输入/输出** |
| ----------- | ------------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id      | [0,VENC_MAX_USER-1] | 输入        |
| pu8Frame    | 待编码一帧yuv数据    | 非空                  | 输入        |
| u32FrameLen | pu8Frame数据的大小 | -                   | 输入        |
| pvMdinfo    | Md统计信息数组      | 非空                  | 输入        |
| pstStream   | 编码后的一帧数据      | -                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**               |
| ------------------------ | -------------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在     |
| ERROR_VENC_INVALID_PARAM | pu8Frame或pstStream为空 |
| ERROR_TYPE_MALLOC_FAILED | 数据Buf申请失败            |
| ERROR_TYPE_INVALID_ARG   | 无效参数                 |
| ERROR_VENC_ENCODE_FAILED | 编码出错                 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_VENC_ReleaseStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_ReleaseStream

&emsp;&emsp;【描述】

&emsp;&emsp;释放编码输出的数据。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_ReleaseStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**   | **取值范围**            | **输入/输出** |
| --------- | -------- | ------------------- | --------- |
| s32ChnId  | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pstStream | 编码后的一帧数据 | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                          | **描述**           |
| -------------------------------- | ---------------- |
| ERROR_VENC_INVALID_PARAM         | pstStream为空      |
| ERROR_VENC_USER_NULL             | s32ChnId对应的用户不存在 |
| ERROR_VENC_RELEASE_STREAM_FAILED | 释放该编码帧失败         |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```C
AK_S32 AK_MPI_VENC_EncodeFrame(AK_S32 s32ChnId, const AK_U8 *pu8Frame,AK_U32 u32FrameLen,
                                AK_VOID *pvMdinfo, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 参数设置/获取

### AK_MPI_VENC_SetAttr

&emsp;&emsp;【描述】

&emsp;&emsp;设置VENC的属性参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetAttr(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**     | **取值范围**            | **输入/输出** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id   | [0,VENC_MAX_USER-1] | 输入        |
| pstChnAttrs | VENC属性参数结构 | 参考struct venc_param | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | 参数错误             |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetAttr(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_GetAttr

&emsp;&emsp;【描述】

&emsp;&emsp;获取VENC的属性参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_GetAttr(AK_S32 s32ChnId, VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**     | **取值范围**            | **输入/输出** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄ID   | [0,VENC_MAX_USER-1] | 输入        |
| pstChnAttrs | VENC属性参数结构 | -                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | pstChnAttrs为空    |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetAttr(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_GetAttr(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_RequestIdr

&emsp;&emsp;【描述】

&emsp;&emsp;请求编I帧。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_RequestIdr(AK_S32 s32ChnId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**            | **输入/输出** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄ID | [0,VENC_MAX_USER-1] | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_SetQp

&emsp;&emsp;【描述】

&emsp;&emsp;设置VENC的qp范围。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetQp(AK_S32 s32ChnId, AK_U32 u32Minqp, AK_U32 u32Maxqp);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**            | **输入/输出** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄ID | [0,VENC_MAX_USER-1] | 输入        |
| u32Minqp | Qp最小值    | [10,51]，一般在20-30之间  | 输入        |
| u32Maxqp | Qp最大值    | [10,51]，一般在40-50之间  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | 参数错误             |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**若设置了恒定qp模式，则此接口调用无效。

<br/>

### AK_MPI_VENC_ResetQp

&emsp;&emsp;【描述】

&emsp;&emsp;重置VENC的qp范围为open时的初始值。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

&emsp;&emsp;【语法】

```c
     AK_S32 AK_MPI_VENC_ResetQp(AK_S32 s32ChnId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**            | **输入/输出** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄ID | [0,VENC_MAX_USER-1] | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    AK_MPI_VENC_ResetQp(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**若设置了恒定qp模式，则此接口调用无效。

<br/>

### AK_MPI_VENC_SetIframeParam

&emsp;&emsp;【描述】

&emsp;&emsp;设置VENC的I帧参数。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_SetIframeParam(AK_S32 s32ChnId, AK_U32 u32Minqp, AK_U32 u32Maxqp,
                                        AK_U32 u32MinFrameSize, AK_U32 u32MaxFrameSize);
```

&emsp;&emsp;【参数】

| **参数名称**        | **描述**   | **取值范围**                               | **输入/输出** |
| --------------- | -------- | -------------------------------------- | --------- |
| s32ChnId        | 视频编码句柄ID | [0,VENC_MAX_USER-1]                    | 输入        |
| u32Minqp        | I帧Qp最小值  | [10,51]，一般在20-30之间，设置0为defaut使用编码库默认配置 | 输入        |
| u32Maxqp        | I帧Qp最大值  | [10,51]，一般在40-50之间，设置0为defaut使用编码库默认配置 | 输入        |
| u32MinFrameSize | I帧最小帧大小  | 单位为KByte，设置0为defaut使用编码库默认配置           | 输入        |
| u32MaxFrameSize | I帧最大帧大小  | 单位为KByte，设置0为defaut使用编码库默认配置           | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_GetIframeParam

&emsp;&emsp;【描述】

&emsp;&emsp;获取VENC的I帧参数。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_GetIframeParam(AK_S32 s32ChnId, AK_U32 *pu32Minqp, AK_U32 *pu32Maxqp,
                                    AK_U32 *u32MinFrameSize, AK_U32 *pu32MaxFrameSize);
```

&emsp;&emsp;【参数】

| **参数名称**         | **描述**   | **取值范围**            | **输入/输出** |
| ---------------- | -------- | ------------------- | --------- |
| s32ChnId         | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pu32Minqp        | I帧Qp最小值  | [10,51]，一般在20-30之间  | 输出        |
| pu32Maxqp        | I帧Qp最大值  | [10,51]，一般在40-50之间  | 输出        |
| u32MinFrameSize  | I帧最小帧大小  | 单位为KByte            | 输出        |
| pu32MaxFrameSize | I帧最大帧大小  | 单位为KByte            | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |
| ERROR_VENC_INVALID_PARAM | 参数错误             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_GetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_SetRoiMdinfo

&emsp;&emsp;【描述】

&emsp;&emsp;设置ROI相关参数。ROI的功能用于减轻夜视图像中的噪声。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。

> **注意：**AK3918EV200L不支持此接口。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_SetRoiMdinfo(AK_S32 s32ChnId, AK_U32 u32Threshold, AK_S32 u32Quality,                         AK_S32 u32RecoverStep, AK_U32 u32WaitIntra, AK_U32 u32WaitSkip);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                            | **取值范围**                          | **输入/输出** |
| -------------- | ------------------------------------------------- | --------------------------------- | --------- |
| s32ChnId       | 视频编码句柄id                                          | [0,VENC_MAX_USER-1]               | 输入        |
| u32Threshold   | 移动侦测判断动静态的阈值                                      | [0,65535]                         | 输入        |
| u32Quality     | 最大增加的qp值                                          | 0<当前qp + u32Quality<=51           | 输入        |
| u32RecoverStep | 恢复时每次减少的qp值                                       | u32RecoverStep<=u32Quality        | 输入        |
| u32WaitIntra   | 帧数，此时开始强制帧内编码，0 ：不强制帧内编码                          | 一般设在u32Quality/u32RecoverStep+1之内 | 输入        |
| u32WaitSkip    | 帧数，此时开始强制 skip。0: 不强制 skip。<br/>skip是不编码直接用参考帧的数据 | 一般设在u32Quality/u32RecoverStep+1之内 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetRoiMdinfo(s32ChnId, u32Threshold, u32Quality,
                             RecoverStep, u32WaitIntra, u32WaitSkip);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_SetRoiSvpInfo

&emsp;&emsp;【描述】

&emsp;&emsp;设置ROI区域相关参数。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_SetRoiSvpInfo(AK_S32 s32ChnId, ROI_SVP_INFO_S *pstRoiParam);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**   | **取值范围**            | **输入/输出** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pstRoiParam | ROI参数    | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述** |
| ------------------------ | ------ |
| ERROR_VENC_INVALID_PARAM | 参数错误   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetRoiSvpInfo(s32ChnId, &stRoiParam);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_StriclylimitFrameSize

&emsp;&emsp;【描述】

&emsp;&emsp;设置硬限制帧大小。此函数只在H.264/H.265编码格式时使用，其他编码格式使用会报错。不建议设置过小，否则会引起图像损失严重，还有呼吸效应产生

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_StriclylimitFrameSize(AK_S32 s32ChnId, AK_U32 u32MaxSize);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**       | **取值范围**            | **输入/输出** |
| ---------- | ------------ | ------------------- | --------- |
| s32ChnId   | 视频编码句柄ID     | [0,VENC_MAX_USER-1] | 输入        |
| u32MaxSize | 帧大小，单位KBytes | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |
| ERROR_VENC_INVALID_PARAM | u32MaxSize小于0    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_StriclylimitFrameSize(s32ChnId, u32MaxSize);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_GetStat

&emsp;&emsp;【描述】

&emsp;&emsp;获取VENC的统计信息。此函数只在H.264/H.265编码格式时使用，其他编码格式使用无意义。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_GetStat(AK_S32 s32ChnId, VENC_STAT_S *pstStat);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**         | **取值范围**            | **输入/输出** |
| -------- | -------------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄ID       | [0,VENC_MAX_USER-1] | 输入        |
| pstStat  | VENC统计信息的结构体指针 | 参考struct 结构体        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |
| ERROR_VENC_INVALID_PARAM | pstStat为空指针      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
   AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
   AK_MPI_VENC_GetStat(s32ChnId, &stStat);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_SetJpegSlice

&emsp;&emsp;【描述】

&emsp;&emsp;设置jpeg slice编码参数。slice编码是把待编码数据切割成若干部分，每次传输其中一部分到编码器进行编码，主要是在内存不足或者待编码图像数据较大的情况下使用。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetJpegSlice(AK_S32 s32ChnId, AK_U32 u32PicHeight,
                                                        AK_U32 u32FirstSliceHeight);
```

&emsp;&emsp;【参数】

| **参数名称**            | **描述**   | **取值范围**               | **输入/输出** |
| ------------------- | -------- | ---------------------- | --------- |
| s32ChnId            | 视频编码句柄ID | [0,VENC_MAX_USER-1]    | 输入        |
| u32PicHeight        | 总的帧高度    | 大于0，，单位：像素行            | 输入        |
| u32FirstSliceHeight | 第一片的高度   | slice的高度要是16的倍数，单位：像素行 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**                             |
| ------------------------ | ---------------------------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在                   |
| ERROR_VENC_INVALID_PARAM | u32PicHeight或u32FirstSliceHeight为0 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetJpegSlice(s32ChnId, u32PicHeight, u32FirstSliceHeight);
    for(int i = 0; i < u32PicHeight / u32FirstSliceHeight; i++)
    {   u32SliceIdx = i;
        AK_MPI_VENC_JpegSliceEncode(s32ChnId, pu8Frame, u32FrameLen,
                                    u32SliceIdx, u32SliceHeight, pstStream);
    }
   // Do something
   AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```c
AK_S32  AK_MPI_VENC_JpegSliceEncode(AK_S32 s32ChnId, const AK_U8 *pu8Frame,
                        AK_U32 u32FrameLen, AK_U32 u32SliceIdx, AK_U32 u32SliceHeight,
                                                    VIDEO_STREAM_S  *pstStream);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_JpegSliceEncode

&emsp;&emsp;【描述】

&emsp;&emsp;做jpeg slice编码

&emsp;&emsp;【语法】

```c
AK_S32  AK_MPI_VENC_JpegSliceEncode(AK_S32 s32ChnId, const AK_U8 *pu8Frame,
                        AK_U32 u32FrameLen, AK_U32 u32SliceIdx, AK_U32 u32SliceHeight,
                                                    VIDEO_STREAM_S  *pstStream);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**    | **取值范围**                                     | **输入/输出** |
| -------------- | --------- | -------------------------------------------- | --------- |
| s32ChnId       | 视频编码句柄ID  | [0,VENC_MAX_USER-1]                          | 输入        |
| pu8Frame       | 待编码的一帧数据  | -                                            | 输入        |
| u32FrameLen    | 待编码帧的数据长度 | -                                            | 输入        |
| u32SliceIdx    | slice的序号  | 大于0                                          | 输入        |
| u32SliceHeight | slice的高度  | 第一个slice的高度要是16的倍数，最后一个slice的高度要是8的倍数，单位：像素行 | 输入        |
| pstStream      | 编码后的一帧数据  | 参考struct 结构体                                 | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**                 |
| ------------------------ | ---------------------- |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在       |
| ERROR_VENC_INVALID_PARAM | pu8Frame或pstStream为空指针 |
| ERROR_TYPE_MALLOC_FAILED | malloc失败               |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetJpegSlice(s32ChnId, u32PicHeight, u32FirstSliceHeight);
    for(int i = 0; i < u32PicHeight / u32FirstSliceHeight; i++)
    {   u32SliceIdx = i;
        AK_MPI_VENC_JpegSliceEncode(s32ChnId, pu8Frame, u32FrameLen,
                                    u32SliceIdx, u32SliceHeight, pstStream);
    }
   // Do something
   AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_VENC_SetJpegSlice(AK_S32 s32ChnId, AK_U32 u32PicHeight,
                                                        AK_U32 u32FirstSliceHeight);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_VENC_SetFps

&emsp;&emsp;【描述】

&emsp;&emsp;设置编码的slice模式帧率。

> **注意：**此接口仅在slice模式编码时支持。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetFps(AK_S32 s32ChnId, AK_U32 u32Fps);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**            | **输入/输出** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| u32Fps   | 帧率       | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**           |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | 参数错误             |
| ERROR_VENC_USER_NULL     | s32ChnId对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

> **注意：**此接口仅在slice模式编码时支持。

<br/>

### AK_MPI_VENC_GetCrop

&emsp;&emsp;【描述】

&emsp;&emsp;获取当前通道的裁剪编码信息。

&emsp;&emsp;【语法】

```c
     AK_S32 AK_MPI_VENC_GetCrop(AK_S32 s32ChnId, VENC_CROP_CFG_S *pstCrop);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**            | **输入/输出** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pstCrop  | 裁剪框信息    | -                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

> **注意：**在使用AK_MPI_VENC_SetCrop设置后需要编码一帧才能更新最新设置的剪裁参数，即该接口要在编码一帧后再去调用获取裁剪信息才能取得正确的信息。

<br/>

### AK_MPI_VENC_SetCrop

&emsp;&emsp;【描述】

&emsp;&emsp;设置当前通道的裁剪编码信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetCrop(AK_S32 s32ChnId, const VENC_CROP_CFG_S *pstCrop);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**                                             | **输入/输出** |
| -------- | -------- | ---------------------------------------------------- | --------- |
| s32ChnId | 视频编码句柄id | [0,VENC_MAX_USER-1]                                  | 输入        |
| pstCrop  | 裁剪框信息    | 宽高要大于8，小于最大宽高，起始点水平坐标需是32的倍数，垂直坐标需是2的倍数，起始点坐标要大于或等于0 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetFunction

&emsp;&emsp;【描述】

&emsp;&emsp;动态场景切换使能逻辑,及其他功能使能逻辑。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetFunction(AK_S32 s32ChnId,AK_U32 u32Function);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**        | **取值范围**            | **输入/输出** |
| ----------- | ------------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id      | [0,VENC_MAX_USER-1] | 输入        |
| u32Function | 功能开启bit位置位后参数 | 大于0小于等于1023         | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_GetFunction

&emsp;&emsp;【描述】

&emsp;&emsp;获取当前动态场景切换使用的逻辑方案。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_GetFunction(AK_S32 s32ChnId,AK_U32 *pu32Function);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**       | **取值范围**            | **输入/输出** |
| ------------ | ------------ | ------------------- | --------- |
| s32ChnId     | 视频编码句柄id     | [0,VENC_MAX_USER-1] | 输入        |
| pu32Function | 功能开启bit置位后的值 | -                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetRcType

&emsp;&emsp;【描述】

&emsp;&emsp;设置码率控制模式。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetRcType(AK_S32 s32ChnId, RC_TYPE_E eRcType);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**   | **取值范围**                | **输入/输出** |
| -------- | -------- | ----------------------- | --------- |
| s32ChnId | 视频编码句柄id | [0,VENC_MAX_USER-1]     | 输入        |
| eRcType  | 码率控制模式   | 0： 内部码率控制模式； 1：外部码率控制模式 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetRcParam

&emsp;&emsp;【描述】

&emsp;&emsp;设置外部码率控制参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetRcParam(AK_S32 s32ChnId, RATE_CTRL_PARAM_S *pstRcParam);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**   | **取值范围**            | **输入/输出** |
| ---------- | -------- | ------------------- | --------- |
| s32ChnId   | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pstRcParam | 外部码率控制参数 | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_GetRcStat

&emsp;&emsp;【描述】

&emsp;&emsp;获取码率控制信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_GetRcStat(AK_S32 s32ChnId, VENC_RC_STATUS_S *pstRcStatus);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**   | **取值范围**            | **输入/输出** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| pstRcStatus | 码率控制信息   | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetStreamBufSize

&emsp;&emsp;【描述】

&emsp;&emsp;设置编码库内部stream buf大小。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetStreamBufSize(AK_S32 s32ChnId, AK_U32 u32Size);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**       | **取值范围**            | **输入/输出** |
| -------- | ------------ | ------------------- | --------- |
| s32ChnId | 视频编码句柄id     | [0,VENC_MAX_USER-1] | 输入        |
| u32Size  | stream buf大小 | >0,  单位KBytes       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                  | **描述**       |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | 参数错误         |
| ERROR_VENC_USER_NULL     | 找不到编码句柄对应的通道 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetQpTable

&emsp;&emsp;【描述】

&emsp;&emsp;设置QP Table

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetQpTable(AK_S32 s32ChnId, AK_U8 * pu8QpTable, AK_S32 s32QpTableSize, bool bRelativeQp, bool bAutoQp, bool bQpTableEnable);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**           | **取值范围**             | **输入/输出** |
| -------------- | ---------------- | -------------------- | --------- |
| s32ChnId       | 视频编码句柄ID         | [0,VENC_MAX_USER-1]  | 输入        |
| pu8QpTable     | QP Table指针       | -                    | 输入        |
| s32QpTableSize | QP Table大小       | -                    | 输入        |
| bRelativeQp    | QP Table中是否为相对QP | 0: 绝对qp,   1:   相对QP | 输入        |
| bAutoQp        | 是否使能自动QP         | 0: 不使能， 1： 使能        | 输入        |
| bQpTableEnable | 是否使能QpTable功能    | 0: 不使能， 1： 使能        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**            |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | handle_id对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

### AK_MPI_VENC_GetQpTableParam

&emsp;&emsp;【描述】

&emsp;&emsp;获取QP Table

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_GetQpTableParam(AK_S32 s32ChnId, QP_TABLE_PARAM_S * pstQpTableParam);
```

&emsp;&emsp;【参数】

| **参数名称**        | **描述**        | **取值范围**            | **输入/输出** |
| --------------- | ------------- | ------------------- | --------- |
| s32ChnId        | 视频编码句柄ID      | [0,VENC_MAX_USER-1] | 输入        |
| pstQpTableParam | QP Table结构体指针 |                     | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**            |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | handle_id对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

### AK_MPI_VENC_GetCurQp

&emsp;&emsp;【描述】

&emsp;&emsp;获取当前qp 值

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_GetCurQp(AK_S32 s32ChnId, CUR_QP_PARAM *pstCurQpParam);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**   | **取值范围**            | **输入/输出** |
| ------------- | -------- | ------------------- | --------- |
| s32ChnId      | 视频编码句柄ID | [0,VENC_MAX_USER-1] | 输入        |
| pstCurQpParam | qp 值     |                     | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**            |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | handle_id对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

### AK_MPI_VENC_GetStream

&emsp;&emsp;【描述】

&emsp;&emsp;获取缓存池中的编码帧，用于快启应用直接获取编码好的帧

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_VENC_GetStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**   | **取值范围**            | **输入/输出** |
| --------- | -------- | ------------------- | --------- |
| s32ChnId  | 视频编码句柄ID | [0,VENC_MAX_USER-1] | 输入        |
| pstStream | 码流结构体    |                     | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**            |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | handle_id对应的用户不存在 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetExifEnable

&emsp;&emsp;【描述】

&emsp;&emsp;使能Exif功能。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetExifEnable(AK_S32 s32ChnId, bool bExifEnable);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**   | **取值范围**            | **输入/输出** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id | [0,VENC_MAX_USER-1] | 输入        |
| bExifEnable | Exif使能开关 | 0不使能；1使能            | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |
| AK_FAILED            | 设置失败             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>

### AK_MPI_VENC_SetExifInfo

&emsp;&emsp;【描述】

&emsp;&emsp;设置Exif信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**    | **取值范围**            | **输入/输出** |
| ----------- | --------- | ------------------- | --------- |
| s32ChnId    | 视频编码句柄id  | [0,VENC_MAX_USER-1] | 输入        |
| pstExifInfo | Exif信息结构体 | -                   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**              | **描述**           |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | s32ChnId对应的用户不存在 |
| AK_FAILED            | 设置失败             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_venc.so或者libmpi_venc.a

&emsp;&emsp;头文件：ak_venc.h

<br/>
## 接口使用场景

| **函数名**                           | **H.264** | **H.265** | **MJPEG** |
| --------------------------------- | --------- | --------- | --------- |
| AK_MPI_VENC_GetVersion            | 支持        | 支持        | 支持        |
| AK_MPI_VENC_GetEncLibVersion      | 支持        | 支持        | 支持        |
| AK_MPI_VENC_Open                  | 支持        | 支持        | 支持        |
| AK_MPI_VENC_Close                 | 支持        | 支持        | 支持        |
| AK_MPI_VENC_EncodeFrame           | 支持        | 支持        | 支持        |
| AK_MPI_VENC_ReleaseStream         | 支持        | 支持        | 支持        |
| AK_MPI_VENC_SetAttr               | 支持        | 支持        | 支持        |
| AK_MPI_VENC_GetAttr               | 支持        | 支持        | 支持        |
| AK_MPI_VENC_RequestIdr            | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetQp                 | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_ResetQp               | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetIframeParam        | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_GetIframeParam        | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetRoiMdinfo          | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetRoiSvpInfo         | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_StriclylimitFrameSize | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_GetStat               | 支持        | 支持        | 支持        |
| AK_MPI_VENC_SetJpegSlice          | 不支持       | 不支持       | 支持        |
| AK_MPI_VENC_JpegSliceEncode       | 不支持       | 不支持       | 支持        |
| AK_MPI_VENC_SetRcType             | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetRcParam            | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_GetRcStat             | 支持        | 支持        | 不支持       |
| AK_MPI_VENC_SetStreamBufSize      | 支持        | 支持        | 支持        |

<br/>

## ak_venc_sample使用示例

运行sample前需要先加载insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko以及ak_venc_adapter.ko 和ak_venc_bridge.ko ，具体命令请参考第7章开头的描述。

| **输入参数**       | **输入参数说明**                                                                                                                                                                                                                                                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| frame-num      | 从vi采集的帧数量。                                                                                                                                                                                                                                                                                                                                |
| data-output    | 编码输出格式，h264,  h265,   jpeg。                                                                                                                                                                                                                                                                                                               |
| br_mode        | 码率控制模式，0 cbr， 1 vbr。jpeg格式不需要设置这项参数。                                                                                                                                                                                                                                                                                                      |
| target_kbps    | 目标码率。jpeg格式不需要设置这项参数。                                                                                                                                                                                                                                                                                                                     |
| frame-rate     | 帧率。jpeg格式不需要设置这项参数。                                                                                                                                                                                                                                                                                                                       |
| main-res       | 主通道分辨率，[0, 17]。<br/>[0 - 17]  0 - 320\*184；1 - 320\*240;  2 - 640\*360;  3 - 640\*480;  4 - 736\*756;  5 - 1280\*720;  6 - 1280\*960;  7 - 1920\*1080;   8 - 2304\*1296;  9 - 2048\*1536;  10 - 2560\*1440;  11 - 2688\*1520;  12 - 2880\*1624;  13 - 2560\*1920;  14 - 2944\*1664;  15 - 3072\*1728;  16 - 3072\*2048;  17 - 3840\*2160; |
| sub-res        | 子通道分辨率[0, 3]。不超过主通道分辨率<br/> [0 - 3]  0 - 320\*184；1 - 320\*240;  2 - 640\*360;  3 - 640\*480 。                                                                                                                                                                                                                                            |
| third_res      | 第三通道分辨率[0, 3]。<br/> [0 - 3] 0 - 320\*184；1 - 320\*240; 2 - 640\*360; 3 - 640\*480 。                                                                                                                                                                                                                                                       |
| save-path      | 保存编码后的码流路径                                                                                                                                                                                                                                                                                                                                |
| channel        | Vi通道，0 主通道，1 子通道。                                                                                                                                                                                                                                                                                                                         |
| input-mode     | Yuv数据输入模式，0 vi，1 从文件读取                                                                                                                                                                                                                                                                                                                    |
| input-path     | 输入源路径，若从vi采集，则是isp conf路径；若从文件读取，则是文件所在路径。AK37E芯片不需要isp conf。                                                                                                                                                                                                                                                                             |
| dev_cnt        | 设备数量[1, 2]，默认1，双目版本用2                                                                                                                                                                                                                                                                                                                     |
| cycle          | 循环次数，默认 1                                                                                                                                                                                                                                                                                                                                 |
| save_file_flag | 保存标记，0 表示不保存；1表示保存，默认1。                                                                                                                                                                                                                                                                                                                   |

<br/>

&emsp;&emsp;输出结果：输出编码后的视频码流文件，保存在指定的path目录下。

<br/>

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### param

| 参数                     | 说明          |
| ---------------------- | ----------- |
| venc0_width            | 编码宽度        |
| venc0_height           | 编码高度        |
| venc0_enc_type         | 编码类型        |
| venc0_fps              | 编码帧率        |
| venc0_goplen           | gop长度       |
| venc0_enc_level        | 编码等级        |
| venc0_profile          | 编码profile   |
| venc0_chroma_mode      | chroma mode |
| venc0_max_picture_size | 外部缓存大小      |
| venc0_br_mode          | 码率模式        |

### stat

| 参数                       | 说明                  |
| ------------------------ | ------------------- |
| version                  | venc中间件版本号          |
| akv_enc_version          | 编码库版本号              |
| "venc0":        "opened" | 编码通道状态：open / close |

<br/>

## 错误码说明

| 错误代码       | 宏定义                                 | 含义             |
| ---------- | ----------------------------------- | -------------- |
| 0x0d000000 | ERROR_VENC_INIT_LIB_ERROR           | 初始化库错误         |
| 0x0d000001 | ERROR_VENC_OPEN_LIB_ERROR           | 打开库错误          |
| 0x0d000002 | ERROR_VENC_OPEN_TOO_MANY            | 打开次数太多         |
| 0x0d000003 | ERROR_VENC_INVALID_PARAM            | grp已经创建        |
| 0x0d000004 | ERROR_VENC_USER_NULL                | 模块没有工作         |
| 0x0d000005 | ERROR_VENC_PARAM_CANNOT_DYNAMIC_SET | 参数不支持动态设置      |
| 0x0d000006 | ERROR_VENC_ENCODE_FAILED            | 编码失败           |
| 0x0d000007 | ERROR_VENC_DEV_OPEN_FAILED          | grp已经使能        |
| 0x0d000008 | ERROR_VENC_CREATE_CHN_FAILED        | 通道创建失败         |
| 0x0d000009 | ERROR_VENC_DELETE_CHN_FAILED        | 通道删除失败         |
| 0x0d00000a | ERROR_VENC_QUERY_DMA_INFO_FAILED    | query dma 信息失败 |
| 0x0d00000b | ERROR_VENC_SET_DMA_BLOCK_FAILED     | 设置dma block失败  |
| 0x0d00000c | ERROR_VENC_DEL_DMA_BLOCK_FAILED     | 删除dma block失败  |
| 0x0d00000d | ERROR_VENC_GET_STREAM_FAILED        | 获取stream失败     |
| 0x0d00000e | ERROR_VENC_RELEASE_STREAM_FAILED    | 是否stream失败     |
| 0x0d00000f | ERROR_VENC_CLEAN_STREAM_FAILED      | 清除stream失败     |
| 0x0d000010 | ERROR_VENC_SET_JPEG_SLICE_FAILED    | 设置jpeg slice失败 |
| 0x0d000011 | ERROR_VENC_DMA_NO_ENOUGH            | dma不足          |
| 0x0d000012 | ERROR_VENC_SET_ATTR_ERROR           | 设置属性结构错误       |

<br/>
