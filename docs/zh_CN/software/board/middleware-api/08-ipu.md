# IPU图像处理单元

## 概述

&emsp;&emsp;2D图像处理单元IPU（Image Processing Unit）主要负责对图像做二维处理，包括格式转换、贴图、缩放、旋转、融合、畸变矫正等。

<br/>

## API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **数据结构**         | **描述**           |
| ---------------- | ---------------- |
| IPU_COLOR_FMT_E  | 颜色格式             |
| IPU_COLOR_TYPE_E | 颜色空间             |
| IPU_DITHER_E     | 色彩抖动类型           |
| IPU_ALPHA_CHN_E  | 图片的Alpha通道选择     |
| IPU_DIRECTION_E  | 图像预处理的旋转翻转       |
| IPU_ATTR_S       | IPU设备属性          |
| IPU_RECT_S       | 操作区域矩形描述区域       |
| IPU_DMA_S        | IPU分配dma内存的描述结构体 |
| IPU_CMD_QUEUE_S  | 单个指令队列的管理结构体     |
| IPU_PLANE_S      | 图像的蒙板信息          |
| IPU_SURFACE_S    | 图像图层信息           |

<br/>

| **函数接口**                   | **描述**               |
| -------------------------- | -------------------- |
| AK_MPI_IPU_Open            | 打开IPU设备              |
| AK_MPI_IPU_Close           | 关闭IPU设备              |
| AK_MPI_IPU_StartQue        | 标志一组图像处理过程的开始        |
| AK_MPI_IPU_EndQue          | 完成一组指令的组织并运行         |
| AK_MPI_IPU_WaitForDone     | 等待整个指令队列执行完成。非必须调用接口 |
| AK_MPI_IPU_QuickFill       | 色块颜色填充操作             |
| AK_MPI_IPU_QuickCopy       | 图层拷贝操作               |
| AK_MPI_IPU_CompositeResize | 图层缩放操作               |
| AK_MPI_IPU_Blend           | 图层融合操作               |
| AK_MPI_IPU_Trans4          | 畸变矫正4点变形操作           |

<br/>

## 数据结构

### IPU_COLOR_FMT_E

&emsp;&emsp;【说明】

&emsp;&emsp;颜色格式

&emsp;&emsp;【定义】

```c
typedef enum akIPU_COLOR_FMT_E
{
    IPU_COLOR_FMT_FULLPLANE_GREY  = 0X01, //Not support now
    IPU_COLOR_FMT_FULLPLANE_RGB   = 0X02,
    IPU_COLOR_FMT_FULLPLANE_YV24  = 0X03,
    IPU_COLOR_FMT_FULLPLANE_YV16  = 0X04,
    IPU_COLOR_FMT_FULLPLANE_YV12  = 0X05,

    IPU_COLOR_FMT_SEMIPLANE_NV24  = 0X10,
    IPU_COLOR_FMT_SEMIPLANE_NV42  = 0X11,
    IPU_COLOR_FMT_SEMIPLANE_NV16  = 0X12,
    IPU_COLOR_FMT_SEMIPLANE_NV61  = 0X13,
    IPU_COLOR_FMT_SEMIPLANE_NV12  = 0X14,
    IPU_COLOR_FMT_SEMIPLANE_NV21  = 0X15,

    IPU_COLOR_FMT_PACKED_ARGB32   = 0X20,
    IPU_COLOR_FMT_PACKED_ABGR32   = 0X21,
    IPU_COLOR_FMT_PACKED_BGRA32   = 0X22,
    IPU_COLOR_FMT_PACKED_RGBA32   = 0X23,
    IPU_COLOR_FMT_PACKED_RGB24    = 0X24,
    IPU_COLOR_FMT_PACKED_BGR24    = 0X25,
    IPU_COLOR_FMT_PACKED_RGB565   = 0X26,
    IPU_COLOR_FMT_PACKED_BGR565   = 0X27,
    IPU_COLOR_FMT_PACKED_RGB555   = 0X28,
    IPU_COLOR_FMT_PACKED_BGR555   = 0X29,

    IPU_COLOR_FMT_PACKED_AYUV     = 0X30,
    IPU_COLOR_FMT_PACKED_AVUY     = 0X31,
    IPU_COLOR_FMT_PACKED_VUYA     = 0X32,
    IPU_COLOR_FMT_PACKED_YUVA     = 0X33,
    IPU_COLOR_FMT_PACKED_YUV      = 0X34,
    IPU_COLOR_FMT_PACKED_VUY      = 0X35,
    IPU_COLOR_FMT_PACKED_IYU2     = 0X36,
    IPU_COLOR_FMT_PACKED_YUYV     = 0X37,
    IPU_COLOR_FMT_PACKED_YVYU     = 0X38,
    IPU_COLOR_FMT_PACKED_UYVY     = 0X39,
    IPU_COLOR_FMT_PACKED_VYUY     = 0X3A,
    IPU_COLOR_FMT_PACKED_IYU1     = 0X3B,

    IPU_COLOR_FMT_INDEX_1BIT      = 0X60, // input. Not support now
    IPU_COLOR_FMT_INDEX_2BITS     = 0X61, // input. Not support now
    IPU_COLOR_FMT_INDEX_4BITS     = 0X62, // input. Not support now
    IPU_COLOR_FMT_INDEX_8BITS     = 0X63, // input. Not support now

}IPU_COLOR_FMT_E;
```

<br/>

### IPU_COLOR_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;颜色空间标准

&emsp;&emsp;【定义】

```c
typedef enum akIPU_COLOR_TYPE_E
{
    IPU_COLOR_TYPE_UNKNOWN     = 0,
    IPU_COLOR_TYPE_RGB         = 1,
    IPU_COLOR_TYPE_YUV601_PC   = 2,
    IPU_COLOR_TYPE_YUV601_TV   = 3,
    IPU_COLOR_TYPE_YUV709_PC   = 4,
    IPU_COLOR_TYPE_YUV709_TV   = 5,
    IPU_COLOR_TYPE_YUV2020_PC  = 6,
    IPU_COLOR_TYPE_YUV2020_TV  = 7,

}IPU_COLOR_TYPE_E;
```

<br/>

### IPU_DITHER_E

&emsp;&emsp;【说明】

&emsp;&emsp;色彩抖动类型
&emsp;&emsp;当色彩转换时，是否使用抖动。
&emsp;&emsp;如果输入格式RGB565，也可以控制是否通过抖动到RGB888。

&emsp;&emsp;【定义】

```c
    typedef enum akIPU_DITHER_E
    {
        IPU_DITHER_NONE   = 0,
        IPU_DITHER_BLUE16 = 1,

    }IPU_DITHER_E;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**                 |
| ----------------- | ---------------------- |
| IPU_DITHER_NONE   | 不抖动                    |
| IPU_DITHER_BLUE16 | Order-dither（16x16蓝噪声） |

<br/>

### IPU_ALPHA_CHN_E

&emsp;&emsp;【说明】

&emsp;&emsp;图片的Alpha通道选择

&emsp;&emsp;【定义】

```c
    typedef enum akIPU_ALPHA_CHN_E
    {
        IPU_ALPHA_CHN_NONE         = 0,
        IPU_ALPHA_CHN_PACKED       = 1,
        IPU_ALPHA_CHN_TRANS_IDX    = 2,
        IPU_ALPHA_CHN_PLANE_1BIT   = 4,
        IPU_ALPHA_CHN_PLANE_2BIT   = 5,
        IPU_ALPHA_CHN_PLANE_4BIT   = 6,
        IPU_ALPHA_CHN_PLANE_8BIT   = 7,
    }IPU_ALPHA_CHN_E;
```

&emsp;&emsp;【成员】

| **成员名称**                 | **描述**                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------ |
| IPU_ALPHA_CHN_NONE       | 图像没有Alpha通道或不使用Alpha通道，所有像素的alpha = 255                                              |
| IPU_ALPHA_CHN_PACKED     | 使用Packed ARGB中的Alpha通道或调色板中的Alpha通道；其它格式时，所有像素的alpha = 255。                          |
| IPU_ALPHA_CHN_TRANS_IDX  | 使用Transparent Index指定的索引值产生蒙板。等于指定索引值的像素的alpha=0，其它索引值的像素的alpha=255；只能在Indexed色彩中使用。 |
| IPU_ALPHA_CHN_PLANE_1BIT | 使用Plane 3指示的1bit位图作为蒙板                                                               |
| IPU_ALPHA_CHN_PLANE_2BIT | 使用Plane 3指示的2bit位图作为蒙板                                                               |
| IPU_ALPHA_CHN_PLANE_4BIT | 使用Plane 3指示的4bit位图作为蒙板                                                               |
| IPU_ALPHA_CHN_PLANE_8BIT | 使用Plane 3指示的8bit位图作为蒙板                                                               |

<br/>

### IPU_DIRECTION_E

&emsp;&emsp;【说明】

&emsp;&emsp;图像预处理的旋转翻转

&emsp;&emsp;【定义】

```c
    typedef enum akIPU_DIRECTION_E     //图像预处理的旋转翻转
    {
        IPU_DIRECTION_UNCHANGE    = 0,
        IPU_DIRECTION_FLIP_VER    = 1,
        IPU_DIRECTION_FLIP_HOR    = 2,
        IPU_DIRECTION_ROTATE_180  = 3,
        IPU_DIRECTION_ROTATE_90   = 4,
        IPU_DIRECTION_ROTATE_270  = 5,

    }IPU_DIRECTION_E;
```

&emsp;&emsp;【成员】

| **成员名称**                 | **描述**    |
| ------------------------ | --------- |
| IPU_DIRECTION_UNCHANGE   | 保持原样      |
| IPU_DIRECTION_FLIP_VER   | 垂直翻转      |
| IPU_DIRECTION_FLIP_HOR   | 水平翻转（镜像）  |
| IPU_DIRECTION_ROTATE_180 | 180度顺时针旋转 |
| IPU_DIRECTION_ROTATE_90  | 90度顺时针旋转  |
| IPU_DIRECTION_ROTATE_270 | 270度顺时针旋转 |

<br/>

### IPU_BLEND_OPT_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;BLEND的操作模式。

&emsp;&emsp;【定义】

```c
    typedef enum akIPU_BLEND_OPT_TYPE_E
    {
        IPU_OPT_SOLID_COLOR_BLENDING     = 0x30,
        IPU_OPT_COLOR_KEY_BLENDING       = 0x31,
        IPU_OPT_SPECIFIED_ALPHA_BLENDING = 0x32,
        IPU_OPT_SOLID_BG_BLENDING        = 0x33,
        IPU_OPT_SOLID_FG_BLENDING        = 0x34,
        IPU_OPT_GRADIENT_BLENDING        = 0x35,
    }IPU_BLEND_OPT_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**   |
| -------- | -------- |
| IPU_OPT_SOLID_COLOR_BLENDING       |前景到混合到实色背景模式。前景到混合到实色背景，将前景图（可以包含Alpha通道）贴到实色背景图（不包含Alpha通道，或忽略Alpha通道）上，输出实色的图像（不包含Alpha通道）。 |
| IPU_OPT_COLOR_KEY_BLENDING         |范围色彩镂空模式。给前景图或背景图（不含Alpha通道或忽略Alpha通道）指定一种颜色和偏差数值，选择数值落在偏差范围内视为选中区域，否则视为反选区域。给正选和反选分别指定一个Alpha值，进行Blend操作，输出图像（不含Alpha通道）。 |
| IPU_OPT_SPECIFIED_ALPHA_BLENDING   |半透明图层比例混合模式。使用两个全局Alpha值混合图层A和B（可以带有Alpha通道），限幅后输出（可以带有Alpha通道）。输入图像自带的Alpha通道只会被视为数值，与颜色一样参与全局Alpha混合。|
| IPU_OPT_SOLID_BG_BLENDING          |前景图与纯色背景混合模式。将图像（可带有Alpha通道）作为前景层，与纯色背景（无Alpha）混合，输出图像（无Alpha通道）。|
| IPU_OPT_SOLID_FG_BLENDING          |纯色前景和背景图混合模式。将纯色前景（带Alpha值），与图像（不带Alpha通道）背景混合，与输出图像（无Alpha通道）。|
| IPU_OPT_GRADIENT_BLENDING          |前景到渐变混合到实色背景模式。制定4个顶点的不透明读，以线性渐变的方式，将实色前景图（不包含Alpha通道，或忽略Alpha通道）贴到实色背景图（不包含Alpha通道，或忽略Alpha通道）上，输出实色的图像（不包含Alpha通道）。|

<br/>

### IPU_BLEND_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;BLEND的输出效果。

&emsp;&emsp;【定义】

```c
    typedef enum akIPU_BLEND_MODE_E
    {
        IPU_BLEND_MODE_NORMAL      = 0x00,
        IPU_BLEND_MODE_LIGHTEN     = 0x01,
        IPU_BLEND_MODE_DARKEN      = 0x02,
        IPU_BLEND_MODE_MULTIPLY    = 0x03,
        IPU_BLEND_MODE_AVERAGE     = 0x04,
        IPU_BLEND_MODE_DIFFERENCE  = 0x05,
        IPU_BLEND_MODE_NEGATION    = 0x06,
        IPU_BLEND_MODE_SCREEN      = 0x07,
        IPU_BLEND_MODE_EXCLUSION   = 0x08,
        IPU_BLEND_MODE_OVERLAY     = 0x09,
        IPU_BLEND_MODE_SOFTLIGHT   = 0x0A,
        IPU_BLEND_MODE_HARDLIGHT   = 0x0B,
        IPU_BLEND_MODE_LINEARDODGE = 0x0C,
        IPU_BLEND_MODE_LINEARBURN  = 0x0D,
        IPU_BLEND_MODE_LINEARLIGHT = 0x0E,
        IPU_BLEND_MODE_PINLIGHT    = 0x0F,
    }IPU_BLEND_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**   |
| -------- | -------- |
|IPU_BLEND_MODE_NORMAL      |正常 |
|IPU_BLEND_MODE_LIGHTEN     |变亮 |
|IPU_BLEND_MODE_DARKEN      |变暗 |
|IPU_BLEND_MODE_MULTIPLY    |相乘 |
|IPU_BLEND_MODE_AVERAGE     |平均 |
|IPU_BLEND_MODE_DIFFERENCE  |差值 |
|IPU_BLEND_MODE_NEGATION    |反相 |
|IPU_BLEND_MODE_SCREEN      |滤色 |
|IPU_BLEND_MODE_EXCLUSION   |排除 |
|IPU_BLEND_MODE_OVERLAY     |叠加 |
|IPU_BLEND_MODE_SOFTLIGHT   |柔光 |
|IPU_BLEND_MODE_HARDLIGHT   |强光 |
|IPU_BLEND_MODE_LINEARDODGE |线性减淡 |
|IPU_BLEND_MODE_LINEARBURN  |线性加深 |
|IPU_BLEND_MODE_LINEARLIGHT |线性光 |
|IPU_BLEND_MODE_PINLIGHT    |点光 |

<br/>

### IPU_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;打开IPU设备的使用属性

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_ATTR_S
    {
        AK_U32 au32QueSize[AK_IPU_MAX_QUE];
        AK_U32 u32RespSize;
        AK_U32 u32TransBlendQueSize;
    }IPU_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**                    | **描述**                      |
| --------------------------- | --------------------------- |
| au32QueSize[AK_IPU_MAX_QUE] | 两个队列的内存大小                   |
| u32RespSize                 | 回执队列内存大小                    |
| u32TransBlendQueSize        | 畸变矫正所需的dma内存大小,通过conf大小进行评估 |

<br/>

### IPU_RECT_S

&emsp;&emsp;【说明】

&emsp;&emsp;操作区域矩形描述区域。

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_RECT_S
    {
        AK_S32 s32X;
        AK_S32 s32Y;
        AK_U32 u32W;
        AK_U32 u32H;
    }IPU_RECT_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**   |
| -------- | -------- |
| s32X     | 操作区域x坐标。 |
| s32Y     | 操作区域y坐标。 |
| u32W     | 操作区域宽度。  |
| u32H     | 操作区域高度。  |

<br/>

### IPU_DMA_S

&emsp;&emsp;【说明】

&emsp;&emsp;IPU分配dma内存的描述结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_DMA_S
    {
        AK_U64 u64PhyAddr;
        AK_VOID *pvAddr;
        AK_U32 u32Len;
        AK_U32 u32PhyAddrLow;
        AK_U8 u8PhyAddrHigh;
        AK_U32 u32W;
        AK_U32 u32H;
        IPU_COLOR_FMT_E enColorFmt;
        AK_U32 u32PlantArrange;
        IPU_DIRECTION_E enDirection;
        AK_VOID *pvExt;
    }IPU_DMA_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**              |
| --------------- | ------------------- |
| u64PhyAddr      | 物理地址                |
| *pvAddr         | 虚拟地址                |
| u32Len          | 内存长度                |
| u32PhyAddrLow   | 物理地址低32位,用于畸变矫正,可留空 |
| u8PhyAddrHigh   | 物理地址高8位,用于畸变矫正,可留空  |
| u32W            | 图层宽度,可留空            |
| u32H            | 图层高度,可留空            |
| enColorFmt      | 图层图像类型,可留空          |
| u32PlantArrange | 图层颜色分量排列,可留空        |
| enDirection     | 源图层的旋转方向,可留空        |
| *pvExt          | 图层额外信息,可留空          |

<br/>

### IPU_CMD_QUEUE_S

&emsp;&emsp;【说明】

&emsp;&emsp;单个指令队列的管理结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_CMD_QUEUE_S
    {
        AK_S32      s32InitFlag;
        AK_RWLOCK_T rwMutex;
        AK_VOID     *pvCmdStart;
        AK_VOID     *pvCmdOffset;
        AK_U32      u32LenCmd;
        IPU_DMA_S   stIpuAddrCmd;
        IPU_DMA_S   stIpuAddrResp;
        AK_U16      u16CmdId;
    }IPU_CMD_QUEUE_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**                 |
| ------------- | ---------------------- |
| s32InitFlag   | flag record init 初始化标记 |
| rwMutex       | rwlock 读写锁             |
| *pvCmdStart   | 指令开始的虚拟地址              |
| *pvCmdOffset  | 指令当前写入偏移地址             |
| u32LenCmd     | 指令缓存长度                 |
| stIpuAddrCmd  | 指令队列内存描述结构体            |
| stIpuAddrResp | 回执队列内存描述结构体            |
| u16CmdId      | 命令ID                   |

<br/>

### IPU_PLANE_S

&emsp;&emsp;【说明】

&emsp;&emsp;图像的蒙板信息

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_PLANE_S
    {
        AK_U64 u64PhyAddr;
        AK_U8  u8PixStride;
        AK_U32 u32PitchLine;
    }IPU_PLANE_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| u64PhyAddr   | 图片的基地址。对于不使用的plane，保持该位置为0。                                                                                                        |
| u8PixStride  | 图片同行相邻像素的地址偏移量，数字代表了Plane号。这是一个无符号数，可填入范围在1-4，代表1-4个byte。对于不使用的plane，保持该位置为0。                                                      |
| u32PitchLine | 图片相邻两行的行首像素的地址偏移量，数字代表了Plane号。这是一个有符号数，填入实际数字补码，取值范围[-0x80000, 0x80000)，如果Plane摆放顺序是垂直翻转的（比如BMP格式），那么这应该是一个负数。对于不使用的plane，保持该位置为0。 |

<br/>

### IPU_SURFACE_S

&emsp;&emsp;【说明】

&emsp;&emsp;图像图层信息

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_SURFACE_S
    {
        AK_U32           u32Width;
        AK_U32           u32Height;
        IPU_COLOR_FMT_E  enColorFmt;
        IPU_COLOR_TYPE_E enColorType;
        IPU_ALPHA_CHN_E  enAlphaChnChoice;
        IPU_DIRECTION_E  enDirection;
        AK_U8            u8ColorPadding;

        AK_U8            u8AlphaChnInv;
        AK_U8            u8AlphaDither;
        AK_U8            u8AlphaValue;
        AK_U16           u16PaletteOffset;
        AK_U16           u16PaletteTransp;
        IPU_PLANE_S      stPlant[4];

        AK_U32           u32Reserve1;
        AK_U32           u32Reserve2;
    }IPU_SURFACE_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| u32Width         | 图层宽                                                                             |
| 32Height         | 图层高                                                                             |
| enColorFmt       | 像素格式 输入的像素格式与输出的像素格式不同时会自动进行图像格式转换                                              |
| enColorType      | 颜色标准                                                                            |
| enAlphaChnChoice | Alpha通道选择                                                                       |
| enDirection      | 图像预处理的旋转翻转                                                                      |
| u8ColorPadding   | 当算法引用图片超界区域时,如何处理。0x0 复制边缘 0x1 黑色(必须准确设置Cache Color) 0x2  白色(必须准确设置Cache Color) |
| u8AlphaChnInv    | 对Alpha或者plane3的蒙板取反                                                             |
| u8AlphaDither    | 输入的Plane 3的bit数不足8bit时，是否使用抖动                                                   |
| u8AlphaValue     | Alpha参数                                                                         |
| u16PaletteOffset | 使用索引色格时，索引值在公共调色板上的偏移量                                                          |
| u16PaletteTransp | alpha channel为2时，使用这个参数指定一个序号，所有索引值等于该序号的像素被认为是透明像素                             |
| stPlant[4]       | plane3可为蒙板数据                                                                    |
| u32Reserve1      | 保留位1                                                                            |
| u32Reserve2      | 保留位2                                                                            |

<br/>

### IPU_BLEND_OPT_S

&emsp;&emsp;【说明】

&emsp;&emsp;图像图层信息

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_BLEND_OPT_S
    {
        IPU_BLEND_OPT_TYPE_E enOpt;
        union
        {
            IPU_SOLID_COLOR_BLEND_ATTR_S stSolidColorBlendAttr;
            IPU_COLOR_SCOPE_BLEND_ATTR_S stColorScopeBlendAttr;
            IPU_SPECI_ALPHA_BLEND_ATTR_S stSpeciAlphaBlendAttr;
            IPU_SOLID_BG_BLEND_ATTR_S    stSolidBgBlendAttr;
            IPU_SOLID_FG_BLEND_ATTR_S    stSolidFgBlendAttr;
            IPU_GRADIENT_BLEND_ATTR_S    stGradientBlendAttr;
        };
    }IPU_BLEND_OPT_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enOpt| blend操作模式        |
| stSolidColorBlendAttr|前景到混合到实色背景模式使用的结构体        |
| stColorScopeBlendAttr|范围色彩镂空模式使用的结构体。       |
| stSpeciAlphaBlendAttr|半透明图层比例混合模式使用的结构体。       |
| stSolidBgBlendAttr   |前景图与纯色背景混合模式使用的结构体。        |
| stSolidFgBlendAttr   |纯色前景和背景图混合模式使用的结构体。        |
| stGradientBlendAttr  |前景到渐变混合到实色背景模式使用的结构体。            |

<br/>

### IPU_SOLID_COLOR_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;前景到混合到实色背景模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_SOLID_COLOR_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U8 u8Opacity;
    }IPU_SOLID_COLOR_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode| blend效果选项        |
| u8Opacity|  前景图全局不透明度，255表示完全不透明 |

<br/>

### IPU_COLOR_SCOPE_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;范围色彩镂空模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_COLOR_SCOPE_BLEND_ATTR_S
    {
        AK_U8 u8OpacityPositive;
        AK_U8 u8OpacityNegative;
        IPU_LAYER_E enRefLayer;
        AK_U32 u32RefColor;
        AK_U8 u8Differ;
    }IPU_COLOR_SCOPE_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
|u8OpacityPositive| 正选区域的不透明度。   |
|u8OpacityNegative| 反选区域的不透明度。   |
|enRefLayer       | 混合操作选择哪个图层来进行色彩匹配。0x0 前景图;0x1 背景图 |
|u32RefColor      |  用于比较的参考色彩。  |
|u8Differ         | 像素与Ref. Color的偏差小于等于Differ，则认为是正选区域，否则视为反选区域。偏差计算使用曼哈顿距离，即RGB或YUV三个分辨率差值的绝对值之和，最大255。 |
<br/>

### IPU_SPECI_ALPHA_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;半透明图层比例混合模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_SPECI_ALPHA_BLEND_ATTR_S
    {
        AK_U8 u8gAlphaBg;
        AK_U8 u8gAlphaFg;
    }IPU_SPECI_ALPHA_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| u8gAlphaFg | 图层FG的权重。   |
| u8gAlphaBg | 图层BG的权重。   |

<br/>

### IPU_SOLID_BG_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;前景图与纯色背景混合模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_SOLID_BG_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U32 u32ColorBG;
        AK_U8 u8Opacity;
    }IPU_SOLID_BG_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | blend效果选项 |
| u32ColorBG  | 纯色背景图的色彩 |
| u8Opacity   | 前景图全局不透明度 |

<br/>

### IPU_SOLID_FG_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;纯色前景和背景图混合模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_SOLID_FG_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U32 u32ColorFG;
        AK_U8 u8Opacity;
    }IPU_SOLID_FG_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | blend效果选项 |
| u32ColorFG|  纯色背景图的色彩，需要在色彩中指定Alpha值。  |
| u8Opacity|  暂不使用  |
<br/>

### IPU_GRADIENT_BLEND_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;前景到渐变混合到实色背景模式使用的结构体

&emsp;&emsp;【定义】

```c
    typedef struct akIPU_GRADIENT_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U8 au8OpacityPoints[4];
    }IPU_GRADIENT_BLEND_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | blend效果选项 |
| au8OpacityPoints |  前景图全局不透明度，分别对应4个角。 数组序号顺序为左上、右上、左下、右下  |

<br/>

## 版本信息获取

### AK_MPI_IPU_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取IPU库的版本号。

&emsp;&emsp;【语法】

```c
    const AK_CHAR* AK_MPI_IPU_GetVersion(void);
```

&emsp;&emsp;【返回值】

| **返回值**  | **描述** |
| -------- | ------ |
| IPU模块版本号 | 成功     |
| NULL     | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

## 打开/关闭模块

### AK_MPI_IPU_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开IPU设备。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_Open(const IPU_ATTR_S *pstIpuAttr);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**     | **取值范围** | **输入/输出** |
| ---------- | ---------- | -------- | --------- |
| pstIpuAttr | IPU配置参数结构体 | -        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**   |
| ------- | -------- |
| 0       | 成功       |
| 非0      | 失败，返回错误码 |

&emsp;&emsp;【错误码列表】

| **错误码**                | **描述**    |
| ---------------------- | --------- |
| ERROR_IPU_OPEN_FAILURE | IPU设备打开失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

> **注意：**支持重入，若IPU设备已经打开，则不会重复打开，只会在内部计数器进行+1操作。AK_MPI_IPU_Open和AK_MPI_IPU_Close需要成对执行。

<br/>

### AK_MPI_IPU_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭IPU设备。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_Close( AK_VOID );
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| -------- | ------ | -------- | --------- |
| AK_VOID  | -      | -        | -         |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                       | **描述**   |
| ----------------------------- | -------- |
| ERROR_IPU_NOT_OPENED          | IPU设备没打开 |
| ERROR_IPU_MUTEX_CLOSE_FAILURE | 锁关闭失败    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

> **注意：**支持重入，AK_MPI_IPU_Open和AK_MPI_IPU_Close需要成对执行。

<br/>

## 指令队列管理

### AK_MPI_IPU_StartQue

&emsp;&emsp;【描述】

&emsp;&emsp;开始一组指令队列的执行。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_StartQue( AK_S32 s32QueId );
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围**           | **输入/输出** |
| -------- | ------ | ------------------ | --------- |
| s32QueId | 队列编号   | 0-AK_IPU_MAX_QUE-1 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_EndQue

&emsp;&emsp;【描述】

&emsp;&emsp;完成一组指令的组织并运行。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_EndQue( AK_S32 s32QueId, AK_BOOL bSync, AK_BOOL bBlock );
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围**           | **输入/输出** |
| -------- | ---------- | ------------------ | --------- |
| s32QueId | 队列编号       | 0-AK_IPU_MAX_QUE-1 | 输入        |
| bSync    | 是否异步执行     | 0-AK_IPU_MAX_QUE-1 | 输入        |
| bBlock   | 是否阻塞到指令完成。 | 0-AK_IPU_MAX_QUE-1 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_WaitForDone

&emsp;&emsp;【描述】

&emsp;&emsp;等待整个指令队列执行完成。非必须调用接口。若干条endQue指令组设置了非block模式，可以最后使用该函数判断该队列指令是否都执行完毕。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_WaitForDone(AK_S32 s32QueId, AK_U32 u32Timeout);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**   | **取值范围**           | **输入/输出** |
| ---------- | -------- | ------------------ | --------- |
| s32QueId   | 队列编号     | 0-AK_IPU_MAX_QUE-1 | 输入        |
| u32Timeout | 超时等待时间ms | 10-5000            | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

## 图像处理接口

### AK_MPI_IPU_QuickFill

&emsp;&emsp;【描述】

&emsp;&emsp;色块填充操作。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_QuickFill(AK_S32 s32QueId,
                                IPU_SURFACE_S *pstDstImg,
                                IPU_RECT_S *pstDstRect,
                                AK_U32 u32FillColor);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述** | **取值范围**           | **输入/输出** |
| ------------ | ------ | ------------------ | --------- |
| s32QueId     | 队列编号   | 0-AK_IPU_MAX_QUE-1 | 输入        |
| pstDstImg    | 目标图层   | -                  | 输入        |
| pstDstRect   | 目标坐标   | -                  | 输入        |
| u32FillColor | 颜色值    | 0x0 - 0xFFFFFFFF   | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_QuickCopy

&emsp;&emsp;【描述】

&emsp;&emsp;图层拷贝操作。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_IPU_QuickCopy( AK_S32 s32QueId,
                                 IPU_SURFACE_S *pstIpuSurfaceSrc,
                                 IPU_RECT_S *pstIpuRectSrc,
                                 IPU_SURFACE_S *pstIpuSurfaceDst,
                                 IPU_RECT_S *pstIpuRectDst );
```

&emsp;&emsp;【参数】

| **参数名称**         | **描述** | **取值范围**           | **输入/输出** |
| ---------------- | ------ | ------------------ | --------- |
| s32QueId         | 队列编号   | 0-AK_IPU_MAX_QUE-1 | 输入        |
| pstIpuSurfaceSrc | 源图层    | -                  | 输入        |
| pstIpuRectSrc    | 源坐标    | -                  | 输入        |
| pstIpuSurfaceDst | 目标图层   | -                  | 输入        |
| pstIpuRectDst    | 目标坐标   | -                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_CompositeResize

&emsp;&emsp;【描述】

&emsp;&emsp;对图层进行缩放操作

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_IPU_CompositeResize(AK_S32 s32QueId,
                                  IPU_SURFACE_S *pstSrcImg,
                                  IPU_RECT_S *pstSrcRect,
                                  IPU_SURFACE_S *pstDstImg,
                                  IPU_RECT_S *pstDstRect );
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述** | **取值范围**           | **输入/输出** |
| ---------- | ------ | ------------------ | --------- |
| s32QueId   | 队列编号   | 0-AK_IPU_MAX_QUE-1 | 输入        |
| pstSrcImg  | 源图层    | -                  | 输入        |
| pstSrcRect | 源坐标    | -                  | 输入        |
| pstDstImg  | 目标图层   | -                  | 输入        |
| pstDstRect | 目标坐标   | -                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_Blend

&emsp;&emsp;【描述】

&emsp;&emsp;对图层进行融合操作

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_IPU_Blend( AK_S32 s32QueId,
                         IPU_SURFACE_S *pstBackGround, IPU_RECT_S *pstBackGroundRect,
                         IPU_SURFACE_S *pstForeGround, IPU_RECT_S *pstForeGroundRect,
                         IPU_SURFACE_S *pstDst,        IPU_RECT_S *pstDstRect,
                         IPU_BLEND_OPT_S *pstBlendOpt );
```

&emsp;&emsp;【参数】

| **参数名称**          | **描述**  | **取值范围**           | **输入/输出** |
| ----------------- | ------- | ------------------ | --------- |
| s32QueId          | 队列编号    | 0-AK_IPU_MAX_QUE-1 | 输入        |
| pstBackGround     | 背景图层    | -                  | 输入        |
| pstBackGroundRect | 背景图层坐标  | -                  | 输入        |
| pstForeGround     | 前景图层    | -                  | 输入        |
| pstForeGroundRect | 前景图层坐标  | -                  | 输入        |
| pstDst            | 目标图层    | -                  | 输入        |
| pstDstRect        | 目标图层坐标  | -                  | 输入        |
| pstBlendOpt       | 融合选项结构体 | -                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_Trans4

&emsp;&emsp;【描述】

&emsp;&emsp;对图层进行四点变形畸变矫正操作

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_IPU_Trans4( AK_S32 s32QueId,
                          IPU_SURFACE_S *pstSrcImg,
                          IPU_SURFACE_S *pstDstImg,
                          IPU_DMA_S *pstIpuDmaBranch );
```

&emsp;&emsp;【参数】

| **参数名称**        | **描述** | **取值范围**           | **输入/输出** |
| --------------- | ------ | ------------------ | --------- |
| s32QueId        | 队列编号   | 0-AK_IPU_MAX_QUE-1 | 输入        |
| pstSrcImg       | 源图层    | -                  | 输入        |
| pstDstImg       | 目标图层   | -                  | 输入        |
| pstIpuDmaBranch | 畸变矫正指令 | -                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_SetColorTable

&emsp;&emsp;【描述】

&emsp;&emsp;设置全局调色板，用于1、2、4、8bits位图的颜色支持。

&emsp;&emsp;【语法】

```c

AK_S32 AK_MPI_IPU_SetColorTable( AK_U8 u8Num,
                                 AK_U8 u8Offset,
                                 AK_U32 *pu32Argb );

```

&emsp;&emsp;【参数】

| **参数名称**        | **描述** | **取值范围**           | **输入/输出** |
| --------------- | ------ | ------------------ | --------- |
| u8Num        | 调色板数量   | 1-16 | 输入        |
| u8Offset       | 调色板内偏移数    | 0-15                  | 输入        |
| pu32Argb       | 输入的颜色首地址   | -                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

### AK_MPI_IPU_Reset

&emsp;&emsp;【描述】

&emsp;&emsp;重置IPU模块

&emsp;&emsp;【语法】

```c

AK_S32 AK_MPI_IPU_Reset( )

```

&emsp;&emsp;【参数】
无
&emsp;&emsp;【返回值】

| **返回值** | **描述**    |
| ------- | --------- |
| 0       | 成功。       |
| 非0      | 失败，返回错误码。 |

&emsp;&emsp;【错误码列表】

&emsp;&emsp;参见akIPU_ERROR_E函数错误码列表。

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_ipu.a或libmpi_ipu.so

&emsp;&emsp;头文件：ak_ipu.h

<br/>

## ak_ipu_sample 使用示例

运行此sample前，需要先insmod /usr/modules/ak_ipu.ko。

| **输入参数**      | **输入参数说明**                                             |
| ------------- | ------------------------------------------------------ |
| -h, --help    | 打印帮助信息                                                 |
| -a, --opt     | [OptCmd] [OptExtra] IPU操作指令 指令额外数据                     |
| -b, --file-s  | [Format] [w] [h] [Rotate] [Filename] 格式 宽 高 旋转方式 源图文件名 |
| -c, --file-d  | [Format] [w] [h] [Filename] 格式 宽 高 目标图文件名              |
| -d, --rect-s  | x y w h\" 源图坐标参数                                       |
| -e, --rect-d  | x y w h\" 目标图坐标参数                                      |
| -f, --times   | [NUM] 重复运行次数                                           |
| -g, --no-save | 不保存目标图结果                                               |

<br/>

## 错误码说明

| 错误代码       | 宏定义                               | 含义        |
| ---------- | --------------------------------- | --------- |
| 0x2c000000 | ERROR_IPU_OPEN_FAILURE            | IPU打开失败   |
| 0x2c000001 | ERROR_IPU_ALREADY_OPEN            | IPU已经打开   |
| 0x2c000002 | ERROR_IPU_NOT_OPENED              | IPU没有打开   |
| 0x2c000003 | ERROR_IPU_IPU_FLUSH_CACHE_FAILURE | 刷新cache失败 |
| 0x2c000004 | ERROR_IPU_CLOSE_FAILURE           | IPU关闭失败   |
| 0x2c000005 | ERROR_IPU_MUTEX_INIT_FAILURE      | 互斥锁初始化失败  |
| 0x2c000006 | ERROR_IPU_MUTEX_CLOSE_FAILURE     | 互斥锁关闭失败   |
| 0x2c000007 | ERROR_IPU_IOCTL_FAILURE           | IOCTL失败   |
| 0x2c000008 | ERROR_IPU_QUEUE_NUM               | 队列数量错误    |
| 0x2c000009 | ERROR_IPU_VALUE_ILLEGAL           | 数值非法      |

<br/>
