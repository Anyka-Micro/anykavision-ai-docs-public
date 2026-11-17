# 视频处理子系统（效果部分）

## 概述

&emsp;&emsp;视频处理子系统模块（效果部分）主要提供两方面的功能：

&emsp;&emsp;1、提供ISP相关基础操作接口，包括Exposure、WB、Focus、3DNR设置；

&emsp;&emsp;2、提供一些高阶图像处理功能，包括OSD、MD、Effect、MASK、DRAW等。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示：

| **库接口**                            | **描述**                    |
| ---------------------------------- | ------------------------- |
| ISP_MD_INFO_S                      | md参数结构                    |
| ISP_OD_INFO_S                      | OD参数结构                    |
| ISP_EFFECT_TYPE_E                  | effect类型枚举                |
| PP_MASK_TYPE_E                     | 隐私遮挡类型                    |
| PP_MASK_MASIC_ATTR_S               | 马赛克小块尺寸                   |
| PP_MASK_COLOR_INFO_S               | 隐私遮挡颜色参数结构                |
| PP_RECTANGLE_AREA_S                | 矩形区域参数结构                  |
| PP_TRIANGLE_AREA_S                 | 三角形/菱形区域参数结构              |
| PP_MASK_AREA_S                     | 隐私遮挡单个区域参数结构              |
| PP_MASK_AREA_INFO_S                | 隐私遮挡区域参数结构                |
| PP_SHAPE_TYPE_E                    | 形状类型                      |
| PP_BOX_S                           | draw box单个区域参数结构          |
| PP_BOX_GROUP_S                     | 画框参数结构                    |
| ISP_AF_ATTR_S                      | 自动对焦信息结构                  |
| ISP_AF_INFO_S                      | 自动对焦统计信息结构                |
| ISP_OP_TYPE_E                      | 自动手动类型                    |
| ISP_AE_EX_CONVER_ATTR_S            | 自动曝光收敛外部控制属性              |
| ISP_AE_STRGY_MODEL_E               | 自动曝光策略模式                  |
| ISP_RAW_G_HIST_ATTR_S              | RAW域直方图结构                 |
| ISP_RGB_HIST_ATTR_S                | RGB域直方图结构                 |
| ISP_YUV_HIST_ATTR_S                | YUV域直方图结构                 |
| ISP_AE_STRGY_ATTR_S                | 自动曝光策略属性                  |
| ISP_AE_ROUTE_NODE_ATTR_S           | 自动曝光分配路线节点属性              |
| ISP_AE_ROUTE_ATTR_S                | 自动曝光分配路线属性                |
| ISP_WDR_AE_ATTR_S                  | 宽动态自动曝光结构                 |
| ISP_AE_ATTR_S                      | 自动曝光参数结构                  |
| ISP_ME_ATTR_S                      | 手动曝光参数结构                  |
| ISP_RAW_HIST_STAT_INFO_S           | RAW域直方图统计信息               |
| ISP_RGB_HIST_STAT_INFO_S           | RGB域直方图统计信息               |
| ISP_YUV_HIST_STAT_INFO_S           | YUV域直方图统计信息               |
| ISP_WDR_HIST_STAT_INFO_S           | 长短帧直方图统计信息                |
| ISP_AE_STAT_INFO_S                 | 自动曝光状态信息                  |
| ISP_AE_RUN_INFO_S                  | 自动曝光运行信息结构                |
| ISP_AWB_BLK_AVG_STAT_INFO_S        | RGB通道分区平均值统计结果            |
| ISP_AWB_BLK_WP_STAT_INFO_S         | RGB通道分区白点平均值统计结果          |
| ISP_AWB_RUN_INFO_S                 | 白平衡运行信息结构                 |
| ISP_AWB_STAT_INFO_S                | 白平衡统计信息结构                 |
| ISP_MWB_ATTR_S                     | 手动白平衡参数结构                 |
| ISP_AWB_ALGO_TYPE_E                | 自动白平衡算法类型                 |
| ISP_AWB_STAT_CALIB_PARA_S          | 自动白平衡统计参数                 |
| ISP_AWB_ATTR_S                     | 自动白平衡参数结构                 |
| ISP_HDR_S                          | 宽动态信息                     |
| ISP_HDR_ATTR_S                     | 宽动态信息结构体                  |
| ISP_GAIN_STAT_E                    | 增益状态                      |
| ISP_FPS_LEVEL_S                    | 三档帧率结构体                   |
| ISP_3DNR_S                         | 3d降噪结构信息                  |
| ISP_3DNR_ATTR_S                    | 3d降噪信息结构体                 |
| ISP_LENS_COEF_S                    | coef结构体                   |
| ISP_LSC_ATTR_S                     | 镜头校正结构信息                  |
| ISP_SENSOR_REG_INFO_S              | sensor寄存器信息结构体            |
| ISP_EX_ZWEIGHT_ATTR_S              | 扩展区域权重结构                  |
| ISP_EFFECT_ATTR_S                  | YUV效果结构体                  |
| ISP_RGB_GAMMA_S                    | RGB gamma曲线结构体            |
| ISP_RGB_GAMMA_ATTR_S               | RGB gamma参数结构体            |
| ISP_CONTRAST_S                     | 手动对比度参数结构体                |
| ISP_AUTO_CONTRAST_S                | 自动对比度参数结构体                |
| ISP_CONTRAST_ATTR_S                | 对比度参数结构体                  |
| ISP_LCE_S                          | 局部对比度增强参数                 |
| ISP_LCE_ATTR_S                     | 局部对比度增强参数结构体              |
| ISP_Y_GAMMA_ATTR_S                 | y gamma参数参数结构体            |
| ISP_DAY_NIGHT_MODE_E               | 日夜模式                      |
| ISP_NIGHT_TYPE_E                   | 夜视类型                      |
| ISP_IR_LED_NIGHT_PARAM_S           | 红外夜视软光敏参数                 |
| ISP_WHITE_LED_NIGHT_PARAM_S        | 白光灯夜视软光敏参数                |
| ISP_BLACKLIGHT_NIGHT_PARAM_S       | 黑光彩色夜视软光敏参数               |
| ISP_SOFT_PS_ATTR_S                 | 软光敏参数结构                   |
| ISP_NON_INFRARED_RATIO_ATTR_S      | 计算非红外块比率的参数结构             |
| ISP_3D_NR_REF_SIZE_STAT_INFO       | 3DNR的buf使用统计信息结构体         |
| AK_MPI_ISP_GetIspSdkVersion        | 获取ISP SDK库的版本号            |
| AK_MPI_ISP_GetOdInfo               | 获取OD需要的数据信息               |
| AK_MPI_ISP_GetMdStat               | 获取MD统计信息                  |
| AK_MPI_ISP_SetEffect               | 设置效果                      |
| AK_MPI_ISP_GetEffect               | 获取效果                      |
| AK_MPI_PP_MaskSetArea              | 设置mask 区域                 |
| AK_MPI_PP_MaskGetArea              | 获取mask 区域                 |
| AK_MPI_PP_MaskSetColor             | 设置mask 颜色                 |
| AK_MPI_PP_MaskGetColor             | 获取mask 颜色                 |
| AK_MPI_PP_SetBoxColorTable         | 设置画框的调色板                  |
| AK_MPI_PP_DrawBox                  | 设置画框参数                    |
| AK_MPI_ISP_SetAfAttr               | 设置自动对焦结构                  |
| AK_MPI_ISP_GetAfAttr               | 获取自动对焦结构                  |
| AK_MPI_ISP_GetAfStat               | 获取自动对焦统计信息                |
| AK_MPI_ISP_GetExpType              | 获取曝光类型信息                  |
| AK_MPI_ISP_SetExpType              | 设置曝光类型信息                  |
| AK_MPI_ISP_GetAeRunInfo            | 获取自动曝光统计信息                |
| AK_MPI_ISP_GetAeAttr               | 获取自动曝光结构信息                |
| AK_MPI_ISP_SetAeAttr               | 设置自动曝光结构信息                |
| AK_MPI_ISP_GetAeConvergenceRate    | 获取自动曝光收敛速度                |
| AK_MPI_ISP_SetAeConvergenceRate    | 设置自动曝光收敛速度                |
| AK_MPI_ISP_CheckAeStable           | 检测自动曝光是否稳定                |
| AK_MPI_ISP_SetAeSuspend            | 设置ae挂起/恢复                 |
| AK_MPI_ISP_GetMeAttr               | 获取手动曝光结构信息                |
| AK_MPI_ISP_SetMeAttr               | 设置手动曝光结构信息                |
| AK_MPI_ISP_GetExZweightAttr        | 获取扩展权重系数信息                |
| AK_MPI_ISP_SetExZweightAttr        | 设置扩展权重系数信息                |
| AK_MPI_ISP_GetAwbStatInfo          | 获取白平衡统计信息                 |
| AK_MPI_ISP_GetWbType               | 获取白平衡类型信息                 |
| AK_MPI_ISP_SetWbType               | 设置白平衡类型信息                 |
| AK_MPI_ISP_GetMwbAttr              | 获取手动白平衡结构信息               |
| AK_MPI_ISP_SetMwbAttr              | 设置手动白平衡结构信息               |
| AK_MPI_ISP_GetAwbAttr              | 获取自动白平衡结构信息               |
| AK_MPI_ISP_SetAwbAttr              | 设置自动白平衡结构信息               |
| AK_MPI_ISP_GetHdrAttr              | 获取宽动态参数                   |
| AK_MPI_ISP_SetHdrAttr              | 设置宽动态参数                   |
| AK_MPI_ISP_SetSoftPsParam          | 设置无光敏日夜切换参数               |
| AK_MPI_ISP_GetSoftPsLevel          | 获取无光敏日夜level状态            |
| AK_MPI_ISP_SwitchMode              | 切换日夜                      |
| AK_MPI_ISP_GetFpsCtrlStat          | 获取帧率控制状态                  |
| AK_MPI_ISP_ChangeSensorFps         | 切换sensor帧率                |
| AK_MPI_ISP_SetFpsLevel             | 设置sensor三档帧率参数            |
| AK_MPI_ISP_GetFpsLevel             | 获取sensor三档帧率参数            |
| AK_MPI_ISP_SetSensorFps            | 设置sensor帧率                |
| AK_MPI_ISP_GetSensorFps            | 获取sensor帧率                |
| AK_MPI_ISP_Get3dnrAttr             | 获取3dnr结构信息                |
| AK_MPI_ISP_Set3dnrAttr             | 设置3dnr结构信息                |
| AK_MPI_ISP_GetLscAttr              | 获取镜头校正结构信息                |
| AK_MPI_ISP_SetLscAttr              | 设置镜头校正结构信息                |
| AK_MPI_ISP_GetYuvEffectAttr        | 获取YUV效果结构信息               |
| AK_MPI_ISP_SetYuvEffectAttr        | 设置YUV效果结构信息               |
| AK_MPI_ISP_GetRgbGammaAttr         | 获取RGB Gamma 结构信息          |
| AK_MPI_ISP_SetRgbGammaAttr         | 设置RGB Gamma结构信息           |
| AK_MPI_ISP_GetYgammaAttr           | 获取Y Gamma 结构信息            |
| AK_MPI_ISP_SetYgammaAttr           | 设置Y Gamma结构信息             |
| AK_MPI_ISP_GetContrastAttr         | 获取对比度 结构信息                |
| AK_MPI_ISP_SetContrastAttr         | 设置对比度结构信息                 |
| AK_MPI_ISP_GetLceAttr              | 获取局部对比度增强结构信息             |
| AK_MPI_ISP_SetLceAttr              | 设置局部对比度增强结构信息             |
| AK_MPI_ISP_GetCurLumi              | 获取亮度                      |
| AK_MPI_ISP_SetForceAntiFlickerFlag | 设置强制抗闪标记                  |
| AK_MPI_ISP_GetForceAntiFlickerFlag | 获取强制抗闪标记                  |
| AK_MPI_ISP_SetAntiFlickerStrength  | 设置抗闪强度                    |
| AK_MPI_ISP_GetAntiFlickerStrength  | 获取抗闪强度                    |
| AK_MPI_ISP_GetRgbAverage           | 获取RGB平均值                  |
| AK_MPI_ISP_GetSensorReg            | 获取sensor寄存器值              |
| AK_MPI_ISP_SwitchFlipMirror        | 相对于isp配置文件初始值的翻转镜像设置      |
| AK_MPI_ISP_GetFlipMirror           | 获取翻转镜像状态，相对于isp配置文件初始值的状态 |
| AK_MPI_ISP_WaitExpStable           | 等待曝光稳定                    |
| AK_MPI_ISP_GetEv                   | 获取环境EV值                   |
| AK_MPI_ISP_GetRgbDis               | 获取RGB差异值                  |
| AK_MPI_ISP_GetNonInfraredRatio     | 获取非红外块占所有有效块的百分比          |
| AK_MPI_ISP_Get3dnrRefSizeStat      | 获取3DNR的buf使用统计信息          |

<br/>

## 数据结构

### **ISP_MD_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;md参数结构

&emsp;&emsp;【定义】

```c
typedef struct akISP_MD_INFO_S {
    AK_U16  u16Stat[ISP_MD_DIMENSION_V_MAX][ISP_MD_DIMENSION_H_MAX];
} ISP_MD_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                                      |
| -------- | ------------------------------------------- |
| u16Stat  | 运动信息统计数据，把全屏分成64\*36个小块，统计每个小块的当前帧与前一帧的差异值。 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetMdStat(AK_S32 s32GrpId, ISP_MD_INFO_S *pstMd);
```

<br/>

### **ISP_OD_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;OD参数结构

&emsp;&emsp;【定义】

```c
typedef struct akISP_OD_INFO_S {
    AK_U32   u32AfStatics[8][16][5];
    AK_U32   u32RgbHist[256];
    AK_U64   u64RgbTotal;
} ISP_OD_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**   |
| ------------ | -------- |
| u32AfStatics | 自动对焦统计信息 |
| u32RgbHist   | RGB直方图信息 |
| u64RgbTotal  | RGB统计    |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetOdInfo(AK_S32 s32GrpId, ISP_OD_INFO_S *pstOd);
```

<br/>

### **ISP_EFFECT_TYPE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;effect类型枚举。

&emsp;&emsp;【定义】

```c
typedef enum akISP_EFFECT_TYPE_E {
    /* HUE to WDR, value: [-50, 50], 0 means use the value in ISP config file */
    ISP_EFFECT_HUE = 0x00,
    ISP_EFFECT_BRIGHTNESS,
    ISP_EFFECT_SATURATION,
    ISP_EFFECT_CONTRAST,
    ISP_EFFECT_SHARP,
    ISP_EFFECT_HDR,

    ISP_POWER_HZ,        //50 or 60
    ISP_FLIP_MIRROR    //[0, 3]
} ISP_EFFECT_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                                                                    |
| --------------------- | ------------------------------------------------------------------------- |
| ISP_EFFECT_HUE        | 色调， [-50,50]， 0表示用ISP配置文件的参数                                              |
| ISP_EFFECT_BRIGHTNESS | 亮度， [-50,50]，0表示用ISP配置文件的参数，设置后，根据当前使用的ISP 配置文件里面目标亮度的数值，此参数的生效范围可能达不到-50 |
| ISP_EFFECT_SATURATION | 饱和度， [-50,50]， 0表示用ISP配置文件的参数                                             |
| ISP_EFFECT_CONTRAST   | 对比度， [-50,50]， 0表示用ISP配置文件的参数                                             |
| ISP_EFFECT_SHARP      | 锐度， [-50,50]， 0表示用ISP配置文件的参数                                              |
| ISP_EFFECT_HDR        | 宽动态， [-50,50]， 0表示用ISP配置文件的参数                                             |
| ISP_POWER_HZ          | 电源频率，50或60                                                                |
| ISP_FLIP_MIRROR       | 翻转镜像，0正常、1仅做flip、2仅做mirror，3 flip和mirror都做                                |

&emsp;&emsp;【相关数据类型及函数接口】

```c
    AK_S32 AK_MPI_ISP_SetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 s32Value);
    AK_S32 AK_MPI_ISP_GetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 *ps32Value);
```

<br/>

### **PP_MASK_TYPE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;隐私遮挡类型。

&emsp;&emsp;【定义】

```c
typedef enum akPP_MASK_TYPE_E {
    PP_MASK_ORIGINAL_COLOR_RECTANGLE = 0,    /* masked with original color rectangle */
    PP_MASK_ORIGINAL_COLOR_TRIANGLE,        /* masked with original color triangle or diamond*/
    PP_MASK_MOSAIC_VIDEO_RECTANGLE,         /* masked with mosaic video data */
} PP_MASK_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                         | **描述**   |
| -------------------------------- | -------- |
| PP_MASK_ORIGINAL_COLOR_RECTANGLE | 纯色矩形     |
| PP_MASK_ORIGINAL_COLOR_TRIANGLE  | 纯色三角形/菱形 |
| PP_MASK_MOSAIC_VIDEO_RECTANGLE   | 马赛克矩形    |

&emsp;&emsp;【相关数据类型及函数接口】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_MASK_MASIC_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;马赛克小块尺寸。

&emsp;&emsp;【定义】

```c
typedef struct akPP_MASK_MASIC_ATTR_S{
    AK_U16    u16MosaiSizeHor;
    AK_U16    u16MosaiSizeVec;
} PP_MASK_MASIC_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**                                        |
| --------------- | --------------------------------------------- |
| u16MosaiSizeHor | 马赛克小块水平宽度，[0，7]，0 表示1像素；1 表示2像素；...，7表示128像素； |
| u16MosaiSizeVec | 马赛克小块垂直宽度，保留位，暂未实现。                           |

&emsp;&emsp;【相关数据类型及函数接口】

&emsp;&emsp;PP_MASK_COLOR_INFO_S

<br/>

### **PP_MASK_COLOR_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;隐私遮挡颜色参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akPP_MASK_COLOR_INFO_S {
    /* range [0, 0xff]. if 0xff mask video opaquely, then can not see image */
    AK_U8 u8Alpha;

    /* range [0, 0xff] */
    AK_U8 u8RColor;
    /* range [0, 0xff] */
    AK_U8 u8GColor;
    /* range [0, 0xff] */
    AK_U8 u8BColor;

    PP_MASK_MASIC_ATTR_S stMasicAttr;
} PP_MASK_COLOR_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**                               |
| ----------- | ------------------------------------ |
| u8Alpha     | 遮挡透明度，范围[0,0xff]，取值为255表示完全遮挡，看不到图像； |
| u8RColor    | 颜色r分量，范围[0,0xff]                     |
| u8GColor    | 颜色g分量，范围[0,0xff]                     |
| u8BColor    | 颜色b分量，范围[0,0xff]                     |
| stMasicAttr | 马赛克小块大小                              |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_PP_MaskSetColor(AK_S32 s32GrpId, const PP_MASK_COLOR_INFO_S *pstColor);
    AK_S32 AK_MPI_PP_MaskGetColor(AK_S32 s32GrpId, PP_MASK_COLOR_INFO_S *pstColor);
```

<br/>

### **PP_RECTANGLE_AREA_S**

&emsp;&emsp;【说明】

&emsp;&emsp;矩形区域参数结构。

【定义】

```c
typedef struct akPP_RECTANGLE_AREA_S {
    AK_U16 u16X;
    AK_U16 u16Y;
    AK_U16 u16Width;
    AK_U16 u16Height;
} PP_RECTANGLE_AREA_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述** |
| --------- | ------ |
| u16X      | 左上角x坐标 |
| u16Y      | 左上角y坐标 |
| u16Width  | 矩形宽度   |
| u16Height | 矩形高度   |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_TRIANGLE_AREA_S**

&emsp;&emsp;【说明】

&emsp;&emsp;三角形/菱形区域参数结构。

【定义】

```c
typedef struct akPP_TRIANGLE_AREA_S {
    AK_U16 u16X;
    AK_U16 u16Y;
    AK_U8  u8HalfWidth;
    AK_U8  u8Bitmap;
} PP_TRIANGLE_AREA_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**                                                       |
| ----------- | ------------------------------------------------------------ |
| u16X        | 菱形中心点x坐标                                                     |
| u16Y        | 菱形中心点y坐标                                                     |
| u8HalfWidth | 菱形对角线半长                                                      |
| u8Bitmap    | 菱形子区域使能位图，[0,15];bit 0:左上三角；bit 1:右上三角；bit 2:左下三角；bit 3:右下三角 |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_MASK_AREA_S**

&emsp;&emsp;【说明】

&emsp;&emsp;隐私遮挡单个区域参数结构。

【定义】

```c
typedef struct akPP_MASK_AREA_S {
    AK_U8                   u8Enable;
    PP_MASK_TYPE_E          enType;
    union
    {
        PP_RECTANGLE_AREA_S stRectangleArea;
        PP_TRIANGLE_AREA_S  stTriangleArea;
    };
} PP_MASK_AREA_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**   |
| --------------- | -------- |
| u8Enable        | 区域使能     |
| enType          | 区域类型     |
| stRectangleArea | 矩形参数     |
| stTriangleArea  | 三角形/菱形参数 |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;PP_MASK_AREA_INFO_S

<br/>

### **PP_MASK_AREA_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;隐私遮挡区域参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akPP_MASK_AREA_INFO_S {
    PP_MASK_AREA_S stArea[PP_MASK_AREA_MAX];
    AK_U8          u8SyncToSubChn;
} PP_MASK_AREA_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**              |
| -------------- | ------------------- |
| stArea         | 通道区域结构              |
| u8SyncToSubChn | 是否同步给子通道，0 不同步，1 同步 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_PP_MaskSetArea(AK_S32 s32GrpId, AK_U32 u32ChnId, const PP_MASK_AREA_INFO_S *pstArea);
    AK_S32 AK_MPI_PP_MaskGetArea(AK_S32 s32GrpId, AK_U32 u32ChnId, PP_MASK_AREA_INFO_S *pstArea);
```

<br/>

### **PP_SHAPE_TYPE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;形状类型。

&emsp;&emsp;【定义】

```c
typedef enum akPP_SHAPE_TYPE_E {
    PP_SHAPE_TYPE_RECTANGLE_HOLLOW = 0,        /* rectangle hollow */
    PP_SHAPE_TYPE_RECTANGLE_SOLID,            /* rectangle solid */
    PP_SHAPE_TYPE_TRIANGLE_HOLLOW,            /* triangle or diamond hollow */
    PP_SHAPE_TYPE_TRIANGLE_SOLID,            /* triangle or diamond solid */
} PP_SHAPE_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                       | **描述**     |
| ------------------------------ | ---------- |
| PP_SHAPE_TYPE_RECTANGLE_HOLLOW | 空心矩形       |
| PP_SHAPE_TYPE_RECTANGLE_SOLID  | 实心矩形       |
| PP_SHAPE_TYPE_TRIANGLE_HOLLOW  | 空心菱形/三角形斜边 |
| PP_SHAPE_TYPE_TRIANGLE_SOLID   | 实心菱形/三角形   |

&emsp;&emsp;【相关数据类型及函数接口】

&emsp;&emsp;PP_BOX_S

<br/>

### **PP_BOX_S**

&emsp;&emsp;【说明】

&emsp;&emsp;draw box单个区域参数结构。

【定义】

```c
typedef struct akPP_BOX_S {
    AK_U8                   u8Enable;       //[0-1]
    PP_SHAPE_TYPE_E         enType;          //0 rectangle; 1 triangle or diamond
    AK_U16                  u16ColorId;    //[0-6]
    AK_U16                  u16LineWidth;  //[1-16]

    // -1 draw forever ; 0 not draw; >0 draw frame num
    AK_S32                  s32DrawFrameNum;

    union
    {
        PP_RECTANGLE_AREA_S stRectangleArea;
        PP_TRIANGLE_AREA_S  stTriangleArea;
    };
} PP_BOX_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**                   |
| --------------- | ------------------------ |
| u8Enable        | 区域使能                     |
| enType          | 区域类型                     |
| u16ColorId      | 颜色号                      |
| u16LineWidth    | 线宽                       |
| s32DrawFrameNum | 帧数，-1 一直画， 0 不画，大于0 画的帧数 |
| stRectangleArea | 矩形参数                     |
| stTriangleArea  | 三角形/菱形参数                 |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;PP_BOX_GROUP_S

<br/>

### **PP_BOX_GROUP_S**

&emsp;&emsp;【说明】

&emsp;&emsp;画框参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akPP_BOX_GROUP_S {
    PP_BOX_S stBox[BOX_MAX_NUM];
} PP_BOX_GROUP_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述** |
| -------- | ------ |
| stBox    | 画框参数   |

&emsp;&emsp;【相关函数接口】

```c
    int AK_MPI_PP_DrawBox(AK_S32 s32GrpId, AK_U32 u32ChnId, PP_BOX_GROUP_S *pstBoxGroup);
```

<br/>

### **ISP_AF_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动对焦信息结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AF_ATTR_S {
    AK_U16  u16AfStatEnable;
    AK_U8   u8AfSpotlightLumTh;       //[0 ,255]
    AK_U8   u8AfSpotlightEdgeTh;   //[0 ,255]
    AK_U8   u8AfSpotlightEdgeGain; //[0, 15]
    AK_U8   u8AfClipTh;               //[0, 63]
    AK_U8   u8AfPeakCtrl;           //[0, 255]
    AK_U8   u8AfRshift;               //[0, 15]
} ISP_AF_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**        |
| --------------------- | ------------- |
| u16AfStatEnable       | 自动对焦模块使能      |
| u8AfSpotlightLumTh    | 聚光灯像素统计阈值     |
| u8AfSpotlightEdgeTh   | 聚光灯边缘判别阈值     |
| u8AfSpotlightEdgeGain | 聚光灯边缘抑制增益     |
| u8AfClipTh            | 自动聚焦统计裁剪下限    |
| u8AfPeakCtrl          | 强边缘权重         |
| u8AfRshift            | 像素fv值输出前的右移位数 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

<br/>

### **ISP_AF_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动对焦统计信息结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AF_INFO_S {
    AK_U32   u32AfStatics[8][16][5];
    AK_U8    u8AfLocalHighlight[64][128];
} ISP_AF_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**  |
| ------------------ | ------- |
| u32AfStatics       | af统计结果  |
| u8AfLocalHighlight | 高亮度统计结果 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAfStat(AK_S32 s32GrpId, ISP_AF_INFO_S *pstAfStat);
```

<br/>

### **ISP_OP_TYPE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;自动手动类型。

&emsp;&emsp;【定义】

```c
typedef enum akISP_OP_TYPE_E{
    ISP_OP_TYPE_MANUAL = 0,
    ISP_OP_TYPE_AUTO = 1,
    ISP_OP_TYPE_BUTT,
} ISP_OP_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**  |
| ------------------ | ------- |
| ISP_OP_TYPE_MANUAL | 手动      |
| ISP_OP_TYPE_AUTO   | 自动      |
| ISP_OP_TYPE_BUTT   | 预留，暂未使用 |

&emsp;&emsp;【相关数据类型及函数接口】

<br/>

### **ISP_AE_EX_CONVER_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光收敛外部控制属性。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_EX_CONVER_ATTR_S {
    AK_U8    u8AeExConvergenceEn;
    AK_U16   u16ControlZone1;
    AK_U16   u16ControlZone2;
    AK_U16   u16ControlZone3;
    AK_U16   u16ControlZone4;
    AK_U16   u16ControlStep1;
    AK_U16   u16ControlStep2;
    AK_U16   u16ControlStep3;
    AK_U16   u16ControlStep4;
    AK_U16   u16ControlStepMax;
} ISP_AE_EX_CONVER_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**            | **描述**                 |
| ------------------- | ---------------------- |
| u8AeExConvergenceEn | AE 收敛外部控制使能，0：禁用  1：启用 |
| u16ControlZone1     | AE 收敛控制区域1，[1,4096]    |
| u16ControlZone2     | AE 收敛控制区域2，[1,4096]    |
| u16ControlZone3     | AE 收敛控制区域3，[1,4096]    |
| u16ControlZone4     | AE 收敛控制区域4，[1,4096]    |
| u16ControlStep1     | AE 收敛控制步长1，[1,512]     |
| u16ControlStep2     | AE 收敛控制步长2，[1,512]     |
| u16ControlStep3     | AE 收敛控制步长3，[1,512]     |
| u16ControlStep4     | AE 收敛控制步长4，[1,512]     |
| u16ControlStepMax   | AE内收敛门限，[1,512]        |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_STRGY_MODEL_E**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光策略模式。

&emsp;&emsp;【定义】

```c
typedef enum akISP_AE_STRGY_MODEL_E {
    ISP_AE_EXP_HIGHLIGHT_PRIOR = 0,
    ISP_AE_EXP_LOWLIGHT_PRIOR,
    ISP_AE_STRGY_MODEL_BUFF,
} ISP_AE_STRGY_MODEL_E;
```

&emsp;&emsp;【成员】

| **成员名称**                   | **描述**     |
| -------------------------- | ---------- |
| ISP_AE_EXP_HIGHLIGHT_PRIOR | 高光优先，即强光抑制 |
| ISP_AE_EXP_LOWLIGHT_PRIOR  | 低光优先，即背光补偿 |
| ISP_AE_STRGY_MODEL_BUFF    | 预留         |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_RAW_G_HIST_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RAW域直方图结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RAW_G_HIST_ATTR_S{
    AK_U8  u8Enable;
    AK_U8  u8RawRshift;    //[0, 15]
    AK_U8  u8ZoneWeight[8][16];
} ISP_RAW_G_HIST_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**       |
| ------------ | ------------ |
| u8Enable     | RAW直方图统计使能   |
| u8RawRshift  | 右移位数         |
| u8ZoneWeight | RAW域自动曝光区域权重 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_RGB_HIST_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB域直方图结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RGB_HIST_ATTR_S{
    AK_U8  u8RgbHistEnable;
    AK_U8  u8ZoneWeight[8][16];
} ISP_RGB_HIST_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**       |
| --------------- | ------------ |
| u8RgbHistEnable | RGB直方图统计使能   |
| u8ZoneWeight    | RGB域自动曝光区域权重 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_YUV_HIST_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;YUV域直方图结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_YUV_HIST_ATTR_S{
    AK_U16  u16YuvHistEnable;
    AK_U8   u8ZoneWeight[8][16];
} ISP_YUV_HIST_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**       |
| ---------------- | ------------ |
| u16YuvHistEnable | YUV直方图统计使能   |
| u8ZoneWeight     | YUV域自动曝光区域权重 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_STRGY_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光策略属性。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_STRGY_ATTR_S {
    AK_U32    u32HistWeight[16];
} ISP_AE_STRGY_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**           |
| ------------- | ---------------- |
| u32HistWeight | 自动曝光策略权重表，[0,15] |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### ISP_AE_ROUTE_NODE_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光分配路线节点属性。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_ROUTE_NODE_ATTR_S {
    AK_U32   u32ExpTime;
    AK_U32   u32Again;
    AK_U32   u32Dgain;
    AK_U32   u32IspDgain;
} ISP_AE_ROUTE_NODE_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**                   |
| ----------- | ------------------------ |
| u32ExpTime  | 节点曝光时间，[1,65535]         |
| u32Again    | 节点sensor模拟增益，[256,65535] |
| u32Dgain    | 节点sensor数字增益，[256,65535] |
| u32IspDgain | 节点isp数字增益，[256,65535]    |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_ROUTE_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光分配路线属性。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_ROUTE_ATTR_S{
    AK_U8   u8AeRouteEn;
    AK_U8   u8AeRouteNodeNum;
    ISP_AE_ROUTE_NODE_ATTR_S  stAeRouteNode[10];
} ISP_AE_ROUTE_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**        |
| ---------------- | ------------- |
| u8AeRouteEn      | 曝光路径设置使能      |
| u8AeRouteNodeNum | 曝光路径节点数[1,16] |
| stAeRouteNode    | 曝光路径节点属性      |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_WDR_AE_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光分配路线属性。

&emsp;&emsp;【定义】

```c
typedef struct akISP_WDR_AE_ATTR_S
{
    AK_U16 u16ExpRatioType;
    AK_U16 u16ExpRatioLS;
    AK_U16 u16ExpRatioSVS;
    AK_U16 u16ExpRatioMax;
    AK_U16 u16ExpRatioMin;
    AK_U8  u8ExpRatioSpeed;
    AK_U8  u8ExpHighlightCtrl;
} ISP_WDR_AE_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                             |
| ------------------ | ---------------------------------- |
| u16ExpRatioType    | 多帧合成曝光比策略，0：固定曝光比；1：自动曝光比。         |
| u16ExpRatioLS      | 长短帧曝光比，[16, 4095]                  |
| u16ExpRatioSVS     | 短帧/超短帧曝光比，[16, 4095]               |
| u16ExpRatioMax     | 自动曝光比模式下的最大曝光比，[0, 16384]          |
| u16ExpRatioMin     | 自动曝光比模式下的最小曝光比，[0, u16ExpRatioMax] |
| u8ExpRatioSpeed    | 自动曝光比模式下的曝光比调整速度，[0, 255]          |
| u8ExpHighlightCtrl | 自动曝光比模式下的高亮过曝区域抑制强度，[0, 255]       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_ATTR_S {
    AK_U32  u32ExpTimeMax;
    AK_U32  u32AGainMax;
    AK_U32  u32DGainMax;
    AK_U32  u32IspDGainMax;
    AK_U16  u16ExpTimeMin;
    AK_U16  u16AGainMin;
    AK_U16  u16DGainMin;
    AK_U16  u16IspDGainMin;
    AK_U16  u16BlacklightRateMax;
    AK_U16  u16BlacklightRateMin;
    AK_U16  u16ExpStep;
    AK_U8   u8ExpStableRange;
    AK_U8   u8ExpHoldRange;
    AK_U8   u8ExpSpeed;
    AK_U8   u8AntiFlickerTargetLumi;
    AK_U8   u8AntiFlickerStartExp;
    AK_U8   u8ExpLumiFilterPara;
    AK_U8   u8TtargetLumiance[12];
    AK_U8   u8BlacklightCompensationEn;
    AK_U8   u8BlacklightDetectScope;
    ISP_RAW_G_HIST_ATTR_S      stRawGHistAttr;
    ISP_RGB_HIST_ATTR_S        stRgbHistAttr;
    ISP_YUV_HIST_ATTR_S        stYuvHistAttr;
    AK_U16                      u16EnviGainRange[12][2];
    ISP_AE_EX_CONVER_ATTR_S    stAeExConvergencePara;
    ISP_AE_STRGY_MODEL_E       enAeStrgyType;
    ISP_AE_STRGY_ATTR_S        stAeStrgyPara[3];
    ISP_AE_ROUTE_ATTR_S        stExpRoutePara;
    ISP_WDR_AE_ATTR_S          stWdrAePara;
}ISP_AE_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**                   | **描述**                 |
| -------------------------- | ---------------------- |
| u32ExpTimeMax              | 曝光时间最大值，[1,65535]      |
| u16ExpTimeMin              | 曝光时间最小值，[1,65535]      |
| u32DGainMax                | 数字增益最大值，[256,65535]    |
| u16DGainMin                | 数字增益最小值，[256,65535]    |
| u16IspDGainMin             | ISP数字增益最小值，[256,65535] |
| u32IspDGainMax             | ISP数字增益最大值，[256,65535] |
| AK_U32  u32ExpTimeMax;     | 模拟增益最大值，[256,65535]    |
| u16AGainMin                | 模拟增益最小值，[256,65535]    |
| u16ExpStep                 | 曝光调整步长，[1,65535]       |
| u8ExpStableRange           | AE内收敛门限，[1,100]        |
| u8ExpHoldRange             | AE外收敛门限，[1,100]。       |
| u8ExpSpeed                 | 收敛速度控制参数，[1,100]。      |
| u8AntiFlickerTargetLumi    | 亚抗闪目标亮度，[0,255]。       |
| u8AntiFlickerStartExp      | 亚抗闪起效曝光时间范围，[1,10]。    |
| u8ExpLumiFilterPara        | 亮度平滑参数，[1,100]。        |
| u8TtargetLumiance          | 不同EnX下的目标亮度，[1,255]    |
| u16EnviGainRange           | EnvX范围控制参数，[0,65535]   |
| u8BlacklightCompensationEn | 背光补偿使能，[0,1]。          |
| u8BlacklightDetectScope    | 暗区像素检测区域，[0,255]。      |
| u16BlacklightRateMax       | 背光暗区像素最大比例，[1,128]。    |
| u16BlacklightRateMin       | 背光暗区像素最小比例，[1,128]。    |
| stRawGHistAttr             | raw直方图。                |
| stRgbHistAttr              | rgb直方图。                |
| stYuvHistAttr              | yuv直方图。                |
| stAeExConvergencePara      | 自动曝光收敛外部控制参数。          |
| enAeStrgyType              | 曝光策略模式。                |
| stAeStrgyPara              | 曝光策略参数。                |
| stExpRoutePara             | 自动曝光路径分配。              |
| stWdrAePara                | 宽动态自动曝光参数              |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_ME_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;手动曝光参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_ME_ATTR_S {
    AK_U32   u32ExpTime;
    AK_U32   u32AGain;
    AK_U32   u32DGain;
    AK_U32   u32IspDGain;
} ISP_ME_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**              |
| ----------- | ------------------- |
| u32ExpTime  | 曝光时间，[1,65535]      |
| u32AGain    | 模拟增益，[256,65535]    |
| u32DGain    | 数字增益，[256,65535]    |
| u32IspDGain | ISP数字增益，[256,65535] |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
    AK_S32 AK_MPI_ISP_SetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

<br/>

### **ISP_RAW_HIST_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RAW域直方图统计信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RAW_HIST_STAT_INFO_S {
    AK_U32  u32rawGHist[256];
    AK_U64  u32RawGTotal;
} ISP_RAW_HIST_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**      |
| ------------ | ----------- |
| u32rawGHist  | RAW域直方图统计信息 |
| u32RawGTotal | RAW域总亮度     |

&emsp;&emsp;【相关函数接口】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_RGB_HIST_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB域直方图统计信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RGB_HIST_STAT_INFO_S {
    AK_U32  u32RgbHist[256];
    AK_U64  u32RgbTotal;
} ISP_RGB_HIST_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**      |
| ----------- | ----------- |
| u32RgbHist  | RGB域直方图统计信息 |
| u32RgbTotal | RGB域总亮度     |

&emsp;&emsp;【相关函数接口】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_YUV_HIST_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;YUV域直方图统计信息。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_YUV_HIST_STAT_INFO_S {
    AK_U32  u32YHist[256];
    AK_U64  u32YTotal;
} ISP_YUV_HIST_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**      |
| --------- | ----------- |
| u32YHist  | YUV域直方图统计信息 |
| u32YTotal | YUV域总亮度     |

&emsp;&emsp;【相关函数接口】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_WDR_HIST_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;长短帧直方图统计信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_WDR_HIST_STAT_INFO_S{
    AK_U32  u32WdrHistShort[256];
    AK_U32    u32WdrHistLong[256];
} ISP_WDR_HIST_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**    |
| --------------- | --------- |
| u32WdrHistShort | 短帧直方图统计信息 |
| u32WdrHistLong  | 长帧直方图统计信息 |

&emsp;&emsp;【相关函数接口】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_AE_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光状态信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_STAT_INFO_S{
    ISP_RAW_HIST_STAT_INFO_S           stRawHistStatPara;
    ISP_RGB_HIST_STAT_INFO_S           stRgbHistStatPara;
    ISP_YUV_HIST_STAT_INFO_S           stYuvHistStatPara;
    ISP_WDR_HIST_STAT_INFO_S           stRawWdrCombStatPara;
} ISP_AE_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**             | **描述**   |
| -------------------- | -------- |
| stRawHistStatPara    | raw直方图信息 |
| stRgbHistStatPara    | rgb直方图信息 |
| stYuvHistStatPara    | yuv直方图信息 |
| stRawWdrCombStatPara | 长短帧直方图信息 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

<br/>

### **ISP_AE_RUN_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动曝光运行信息结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AE_RUN_INFO_S {
    AK_U8    u8CurrentCalcAvgLumi;
    AK_U8    u8CurrentCalcAvgCompensationLumi;
    AK_U8    u8CurrentTargetLumi;
    AK_U8    u8IsStable;

    AK_U32  u32CurrentAGain;
    AK_U32  u32CurrentDGain;
    AK_U32  u32CurrentIspDGain;
    AK_U32  u32CurrentExpTime;

    AK_U32  u32CurrentAGainStep;
    AK_U32  u32CurrentDGainStep;
    AK_U32  u32CurrentIspDGainStep;
    AK_U32  u32CurrentExpTimeStep;

    AK_U32  u32CurrentRefExpRatio;
    AK_U32  u32CurrentLongExpTime;
    AK_U32  u32CurrentShortExpTime;
    AK_U8   u8CurrentShortAvgLumi;
    AK_U8   u8CurrentLongAvgLumi;

    ISP_AE_STAT_INFO_S stAeStatInfo;
} ISP_AE_RUN_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**                         | **描述**      |
| -------------------------------- | ----------- |
| u8CurrentCalcAvgLumi             | 平均亮度        |
| u8CurrentCalcAvgCompensationLumi | 曝光补偿后的平均亮度  |
| u8CurrentTargetLumi              | 目标亮度        |
| u8IsStable                       | 曝光稳定标记      |
| u32CurrentAGain                  | 当前模拟增益      |
| u32CurrentDGain                  | 当前数字增益      |
| u32CurrentIspDGain               | 当前ISP数字增益   |
| u32CurrentExpTime                | 当前曝光时间      |
| u32CurrentAGainStep              | 当前模拟增益步长    |
| u32CurrentDGainStep              | 当前数字增益步长    |
| u32CurrentIspDGainStep           | 当前ISP数字增益步长 |
| u32CurrentExpTimeStep            | 当前曝光时间步长    |
| u32CurrentRefExpRatio            | 参考曝光比       |
| u32CurrentLongExpTime            | 当前长曝光帧的曝光时间 |
| u32CurrentShortExpTime           | 当前短曝光帧的曝光时间 |
| u8CurrentShortAvgLumi            | 当前短曝光帧的平均亮度 |
| u8CurrentLongAvgLumi             | 当前长曝光帧的平均亮度 |
| stAeStatInfo                     | 自动曝光状态信息    |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

<br/>

### **ISP_AWB_BLK_AVG_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB通道分区平均值统计结果。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AWB_BLK_AVG_STAT_INFO_S{
    AK_U32 u32WbRavgStat[16][16];
    AK_U32 u32WbGavgStat[16][16];
    AK_U32 u32WbBavgStat[16][16];
} ISP_AWB_BLK_AVG_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**       |
| ------------- | ------------ |
| u32WbRavgStat | R通道分区平均值统计结果 |
| u32WbGavgStat | G通道分区平均值统计结果 |
| u32WbBavgStat | B通道分区平均值统计结果 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_BLK_WP_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB通道分区白点平均值统计结果。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AWB_BLK_WP_STAT_INFO_S{
    AK_U32 u32WpRStat[16][16];
    AK_U32 u32WpGStat[16][16];
    AK_U32 u32WpBStat[16][16];
    AK_U32 u32WpCntStatics[16][16];
} ISP_AWB_BLK_WP_STAT_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**        | **描述**         |
| --------------- | -------------- |
| u32WpRStat      | R通道分区白点平均值统计结果 |
| u32WpGStat      | G通道分区白点平均值统计结果 |
| u32WpBStat      | B通道分区白点平均值统计结果 |
| u32WpCntStatics | 白点总数统计         |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_RUN_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;白平衡运行信息结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AWB_RUN_INFO_S{
    AK_U16  u16RGain;
    AK_U16  u16GGain;
    AK_U16  u16BGain;
    AK_S16  s16ROffset;
    AK_S16  s16GOffset;
    AK_S16  s16BOffset;
    AK_U8   u8IsStable;
    AK_U8   u8CurrentColortempIndex;
    AK_U16  u16ColortempStableCnt[10];
    AK_U16  u16CurrentColortemp;
} ISP_AWB_RUN_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**                | **描述**               |
| ----------------------- | -------------------- |
| u16RGain                | 红色分量增益值              |
| u16GGain                | 绿色分量增益值              |
| u16BGain                | 蓝色分量增益值              |
| s16ROffset              | 红色分量偏移值              |
| s16GOffset              | 绿色分量偏移值              |
| s16BOffset              | 蓝色分量偏移值              |
| u8IsStable              | 是否稳定                 |
| u8CurrentColortempIndex | 环境色温标记，是参数随环境变化的色温指标 |
| u16ColortempStableCnt   | 每一种色温稳定的帧数计数         |
| u16CurrentColortemp     | 环境色温                 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_STAT_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;白平衡统计信息结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AWB_STAT_INFO_S {
    AK_U32   u32TotalR[10];
    AK_U32   u32TotalG[10];
    AK_U32   u32TotalB[10];
    AK_U32   u32TotalCnt[10];
    ISP_AWB_BLK_AVG_STAT_INFO_S    stWbBlkAvgStat;
    ISP_AWB_BLK_WP_STAT_INFO_S     stWbBlkWpStat;
    ISP_AWB_RUN_INFO_S             stWbRunInfo;
} ISP_AWB_STAT_INFO_S;
```

<br/>

&emsp;&emsp;【成员】

| **成员名称**       | **描述**             |
| -------------- | ------------------ |
| u32TotalR      | 10个色温，每个色温下的r分量像素值 |
| u32TotalG      | 10个色温，每个色温下的g分量像素值 |
| u32TotalB      | 10个色温，每个色温下的b分量像素值 |
| u32TotalCnt    | 在白平衡统计参数范围内的像素数量值  |
| stWbBlkAvgStat | RGB通道分区平均值统计结果     |
| stWbBlkWpStat  | RGB通道分区白点平均值统计结果   |
| stWbRunInfo    | 白平衡运行信息结构          |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_MWB_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;手动白平衡参数结构。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_MWB_ATTR_S
{
    AK_U16    u16RGain;
    AK_U16    u16GGain;
    AK_U16    u16BGain;
    AK_S16    s16ROffset;
    AK_S16    s16GOffset;
    AK_S16    s16BOffset;
} ISP_MWB_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**            |
| ---------- | ----------------- |
| u16RGain   | r通道增益值，[0,4095]   |
| u16GGain   | g通道增益值，[0,4095]   |
| u16BGain   | b通道增益值，[0,4095]   |
| s16ROffset | r通道偏移值，[-512,511] |
| s16GOffset | g通道偏移值，[-512,511] |
| s16BOffset | b通道偏移值，[-512,511] |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
    AK_S32 AK_MPI_ISP_SetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

<br/>

### ISP_AWB_ALGO_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;自动白平衡算法类型。

&emsp;&emsp;【定义】

```c
typedef enum akISP_AWB_ALGO_TYPE_E{
    ISP_AWB_ALGO_DEFAULT = 0,
    ISP_AWB_ALGO_AVERAGE_WEIGHT = 1,
    ISP_AWB_ALGO_BLOCK_ASSIST,
    ISP_AWB_ALGO_GW,
    ISP_AWB_ALGO_BUTT,
} ISP_AWB_ALGO_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**                    | **描述**      |
| --------------------------- | ----------- |
| ISP_AWB_ALGO_DEFAULT        | 自动白平衡默认算法   |
| ISP_AWB_ALGO_AVERAGE_WEIGHT | 自动白平衡平均加权算法 |
| ISP_AWB_ALGO_BLOCK_ASSIST   | 利用白平衡分块信息算法 |
| ISP_AWB_ALGO_GW             | 灰度世界法       |
| ISP_AWB_ALGO_BUTT           | 预留的方法       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_AWB_STAT_CALIB_PARA_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动白平衡统计参数。

&emsp;&emsp;【定义】

```c
typedef struct akISP_AWB_STAT_CALIB_PARA_S{
    AK_U16     u16GrLow[10];            //gr_low[i]<=gr_high[i]
    AK_U16     u16GrHigh[10];
    AK_U16     u16GbLow[10];            //gb_low[i]<=gb_high[i]
    AK_U16     u16GbHigh[10];
    AK_U16     u16RbLow[10];           //rb_low[i]<=rb_high[i]
    AK_U16     u16RbHigh[10];
} ISP_AWB_STAT_CALIB_PARA_S;
```

&emsp;&emsp;【成员】

| **成员名称**                                                 | **描述**                                            |
| -------------------------------------------------------- | ------------------------------------------------- |
| u16GrLow、u16GbLow、u16GrHigh、u16GbHigh、u16RbLow、u16RbHigh | 下标0-8的是白平衡标定白点统计区域范围;<br/>下标为9的是当前整幅图像R/G/B统计区域范围 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_AWB_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动白平衡参数结构。

&emsp;&emsp;【定义】

```c
typedef  struct akISP_AWB_ATTR_S {
    AK_U8                        u8GWeight[16];
    AK_U8                        u8YLow;                 //y_low<=y_high
    AK_U8                        u8YHigh;
    AK_U8                        u8ErrEst;
    AK_U8                        u8AwbIsoTrackEnable;
    AK_U8                        u8ColortempEnvi[10];
    ISP_AWB_STAT_CALIB_PARA_S  stAwbStatCalibPara[12];

    AK_U16                        u16AutoWbStep;
    AK_U16                        u16TotalCntThresh;
    AK_U16                        u16ColortempStableCntThresh;
    ISP_AWB_ALGO_TYPE_E        enAlgType;
} ISP_AWB_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**                    | **描述**                        |
| --------------------------- | ----------------------------- |
| u8GWeight                   | 不同亮度权重，改变不同亮度像素对白平衡的影响，[0,15] |
| u8YLow                      | 白平衡统计最低亮度阈值，[0,255]           |
| u8YHigh                     | 白平衡统计最高亮度阈值，[0,255]           |
| u8ErrEst                    | 误差估计值，[0,255]                 |
| u8AwbIsoTrackEnable         | 随增益调整AWB统计参数使能位               |
| stAwbStatCalibPara          | 自动白平衡统计参数，[0, 1023]。          |
| u16AutoWbStep               | 白平衡步长计算，[0,255]               |
| u16TotalCntThresh           | 像素个数阈值，[0, 65535]             |
| u16ColortempStableCntThresh | 稳定帧数，多少帧一样认为环境色温改变，[0, 255]   |
| u8ColortempEnvi             | [0, 3]，每个色温参数对应的色温环境，[0, 8]   |
| enAlgType                   | 自动白平衡算法类型。                    |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_HDR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;宽动态信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_HDR_S {
    AK_U8   u8HdrEnable;
    AK_U8   u8HdrUvAdjustEnable;
    AK_U16    u16HdrTh1;      //0-1023
    AK_U16    u16HdrTh2;      //0-1023
    AK_U16    u16HdrTh3;      //0-1023
    AK_U16    u16HdrTh4;      //0-1023
    AK_U16    u16HdrTh5;      //0-1023

    AK_U16    u16AreaTb1[65];
    AK_U16    u16AreaTb2[65];
    AK_U16    u16AreaTb3[65];
    AK_U16    u16AreaTb4[65];
    AK_U16    u16AreaTb5[65];
    AK_U16    u16AreaTb6[65];

    AK_U16    u16Area1Key[16];
    AK_U16    u16Area2Key[16];
    AK_U16    u16Area3Key[16];
    AK_U16    u16Area4Key[16];
    AK_U16    u16Area5Key[16];
    AK_U16    u16Area6Key[16];

    AK_U16  u16HdrCnoiseSuppressYth1;
    AK_U16    u16HdrCnoiseSuppressYth2;
    AK_U16  u16HdrC_cnoiseSuppressGain;
    AK_U8   u8HdrCnoiseSuppressSlop;
    AK_U8    u8HdrUvAdjustLevel;
    AK_U8    u8HdrSpatialfiltK;
}ISP_HDR_S;
```

&emsp;&emsp;【成员】

| **成员名称**                        | **描述**             |
| ------------------------------- | ------------------ |
| u8HdrEnable                     | 使能标记               |
| u8HdrUvAdjustEnable             | uv调整使能             |
| u16HdrTh1~u16HdrTh5             | 5个阈值，[0, 255]      |
| u16AreaTb1[65]~u16AreaTb6[65]   | 6个区域曲线，[0,1023]    |
| u16Area1Key[16]~u16Area6Key[16] | 6条曲线的关键点信息         |
| u16HdrCnoiseSuppressYth1        | 色彩噪声亮度阈值1，[0,1023] |
| u16HdrCnoiseSuppressYth2        | 色彩噪声亮度阈值2，[0,1023] |
| u16HdrC_cnoiseSuppressGain      | 色差抑制，[0,1023]      |
| u8HdrCnoiseSuppressSlop         | 抑制斜率，[0,128]       |
| u8HdrUvAdjustLevel              | uv调整程度, [0,31]     |
| u8HdrSpatialfiltK               | 空域滤波系数, [0,5]      |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;ISP_HDR_ATTR_S

<br/>

### **ISP_HDR_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;宽动态信息结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_HDR_ATTR_S
{
    ISP_OP_TYPE_E    enHdrMode;
    ISP_HDR_S        stManualHdr;
    ISP_HDR_S         stLinkageHdr[12];
} ISP_HDR_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**        |
| ------------ | ------------- |
| enHdrMode    | 模式选择，0 手动，1联动 |
| stManualHdr  | 手动宽动态参数       |
| stLinkageHdr | 联动宽动态参数       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
    AK_S32 AK_MPI_ISP_SetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

<br/>

### **ISP_GAIN_STAT_E**

&emsp;&emsp;【说明】

&emsp;&emsp;增益状态。

&emsp;&emsp;【定义】

```c
typedef enum akISP_GAIN_STAT_E {
    ISP_GAIN_NO_CHANGE_STAT = 0,
    ISP_GAIN_LOW_STAT,
    ISP_GAIN_HIGH_STAT,
    ISP_GAIN_MID_STAT,
} ISP_GAIN_STAT_E;
```

&emsp;&emsp;【成员】

| **成员名称**                | **描述** |
| ----------------------- | ------ |
| ISP_GAIN_NO_CHANGE_STAT | 增益未改变  |
| ISP_GAIN_LOW_STAT       | 低增益状态  |
| ISP_GAIN_HIGH_STAT      | 高增益状态  |
| ISP_GAIN_MID_STAT       | 中等增益状态 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetFpsCtrlStat(AK_S32 s32GrpId, ISP_GAIN_STAT_E *penStat, AK_S32 *ps32NeedFps);
```

<br/>

### **ISP_FPS_LEVEL_S**

&emsp;&emsp;【说明】

&emsp;&emsp;三档帧率结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_FPS_LEVEL_S {
    AK_U32 u32HighFps;
    AK_U32 u32HighFpsExpTime;
    AK_U32 u32HighFpsToLowerFpsGain;

    AK_U32 u32MidFps;                //set 0 means no use middle fps
    AK_U32 u32MidFpsExpTime;         //set 0 means no use middle fps
    AK_U32 u32MidFpsToLowFpsGain;    //set 0 means no use middle fps

    AK_U32 u32LowFps;
    AK_U32 u32LowFpsExpTime;
    AK_U32 u32LowFpsToHigherFpsGain;
} ISP_FPS_LEVEL_S;
```

&emsp;&emsp;【成员】

| **成员名称**                 | **描述**                                    |
| ------------------------ | ----------------------------------------- |
| u32HighFps               | 高帧率，[1,60]                                |
| u32HighFpsExpTime        | 高帧率对应的最大曝光时间，[100,65535]                  |
| u32HighFpsToLowerFpsGain | 高帧率往较低帧率切换的增益阈值，[1,512]；                  |
| u32MidFps                | 中间档帧率（设置为0则不使用中间档帧率），[5,60]               |
| u32MidFpsExpTime         | 中间档帧率对应的最大曝光时间（设置为0则不使用中间档帧率），[100,65535] |
| u32MidFpsToLowFpsGain    | 中间档帧率往低帧率切换的增益阈值（设置为0则不使用中间档帧率），[1,512]；  |
| u32LowFps                | 低帧率，[1,60]                                |
| u32LowFpsExpTime         | 低帧率对应的最大曝光时间，[100,65535]                  |
| u32LowFpsToHigherFpsGain | 低帧率往较高帧率切换的增益阈值，[1,512]；                  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
    AK_S32 AK_MPI_ISP_GetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

<br/>

### **ISP_3DNR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;3d降噪结构信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_3DNR_S {
    AK_U8        u8TnrEnable;            //default:1(GUI edit)
    AK_U8        u8TnrRefFrameFormat;
    AK_U8         u8YnrDPCStr;                    //[0, 127]
    AK_U8         u8YnrDPCCap;                    //[0, 127]
    AK_U8         u8YnrDPCDiffGain[8];            //[0,7]
    AK_U8         u8YnrK;            //[0,15]
    AK_U8        u8YnrLumStr[32]; //[0, 15]
    AK_U8        u8YlpK1;            //[0, 15],default:7(GUI edit)
    AK_U8        u8YlpK2;            //[0, 15],default:0(GUI edit)
    AK_U8         u8YDiffUVWgt;        //[0, 15]
    AK_U8         u8YDiffEdgeWgt;    //[0, 15]
    AK_U8        u8TYLow1;        //[0,127]
    AK_U8        u8TYLow2;        //[0,127]
    AK_U8        u8TYK1;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TYK2;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TYExK;         //[0, 15]
    AK_U8        u8TYKslop1;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TYKslop2;        //[0, 127]
    AK_U8        u8TYSrcChooseKTh;         //[0, 127]
    AK_U8        u8TYUpdateTh;

    AK_U8        u8UvnrK;         //[0, 15],default:8(GUI edit)
    AK_U8        u8UvlpK1;         //[0, 15],default:7(GUI edit)
    AK_U8        u8UvlpK2;         //[0, 15],default:0(GUI edit)
    AK_U8        u8TUvDiffScale;//[0, 15]
    AK_U8        u8TUvKLow1;        //[0, 127]
    AK_U8        u8TUvKLow2;    //[0, 127]
    AK_U8        u8TUvK1;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TUvK2;         //[0, 127]
    AK_U8        u8TUvExK;         //[0, 15],
    AK_U8        u8TUvKslop1;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TUvKslop2;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TUvSrcChooseKTh; //[0, 127]

    AK_U8        u8MfactorKTh;             //[0, 127]
    AK_U8        u8MfactorSlop;         //[0, 15]
    AK_U8         u8MotionStatTh;            //[0, 15]
    AK_U8        u8SfactorStatTh;        //[0, 3]
    AK_U8         u8MotionFilter;            //[0,15]
    AK_U8         u8MotionAreaExpand;     //[0, 1]
    AK_U8         u8LumStr[32];                //[0, 15]
    AK_U16        u16TMfTh1;     //[0, 8191],default:300(GUI edit)
    AK_U16        u16TMfTh2;    //[0, 8191],default:500(GUI edit)
    AK_U16        u16YnrCalcK;        //[0,65535](GUI edit)
    AK_U16        u16YnrWeightTbl[17];//ynr_strength(GUI edit)
    AK_U16        u16TYTh1;        //[0, 511],default:48(GUI edit)
    AK_U16        u16TYTh2;        //[0, 511],default:16(GUI edit)
    AK_U16        u16YUvTh1;        //[0, 511],default:48(GUI edit)
    AK_U16        u16YUvTh2;        //[0, 511],default:16(GUI edit)
    AK_U16        u16MdTh;            //[0, 65535]
    AK_U16        u16Weight4_7X5;    //[0,8695]
    AK_U16      u16TnrMotionFlagTh;
}ISP_3DNR_S;
```

<br/>

&emsp;&emsp;【成员】

| **成员名称**            | **描述**                         |
| ------------------- | ------------------------------ |
| u8TnrEnable         | 3DNR使能位，0: 禁用    1: 启用。        |
| u8TnrRefFrameFormat | 参考帧压缩格式，[0, 2]。                |
| u8YnrDPCStr         | 滤波强度的相关系数，[0, 127]             |
| u8YnrDPCCap         | 最大滤波强度，[0, 127]                |
| u8YnrDPCDiffGain    | 滤波强度调整查找表，[0, 7]               |
| u8YnrK              | Y域2D滤波降噪系数, [0,15]             |
| u8YnrLumStr         | 不同亮度下的降噪强度查找表, [0,15]          |
| u8YlpK1             | Y域5\*5区域均差加权参数，[0, 15]。        |
| u8YlpK2             | Y域3\*3区域均差加权参数，[0, 15]。        |
| u8YDiffUVWgt        | UV辅助分量权重，[0, 15]。              |
| u8YDiffEdgeWgt      | 梯度辅助分量权重，[0, 15]。              |
| u8TYLow1            | Y域时空域滤波强度插值基准参数1，[0, 127]      |
| u8TYLow2            | Y域时空域滤波强度插值基准参数2，[0, 127]      |
| u8TYK1              | Y域静止区域最大时域滤波强度参数，[0, 127]      |
| u8TYK2              | Y域运动区域最大时域滤波强度参数，[0, 127]      |
| u8TYExK             | Y域静止区域时域滤波强度微调参数，[0, 15]。      |
| u8TYKslop1          | Y域静止区域时空滤波加权系数插值参数，[0, 127]    |
| u8TYKslop2          | Y域运动区域时空滤波加权系数插值参数，[0, 127]    |
| u8TYSrcChooseKTh    | Y域时域滤波基数选择阈值，[0, 127]          |
| u8TYUpdateTh        | 时域滤波更新阈值，[0, 15]。              |
| u8UvnrK             | uv域2D滤波降噪系数，[0, 15]。           |
| u8UvlpK1            | uv域3*3区域均差加权参数1，[0, 15]。       |
| u8UvlpK2            | uv域3*3区域均差加权参数2，[0, 15]。       |
| u8TUvDiffScale      | uv域区域帧差缩放阈值，[0, 15]。           |
| u8TUvKLow1          | uv域时空域滤波强度插值基准参数1，[0, 127]     |
| u8TUvKLow2          | uv域时空域滤波强度插值基准参数2，[0, 127]     |
| u8TUvK1             | uv域静止区域最大时域滤波强度参数，[0, 127]     |
| u8TUvK2             | uv域运动区域最大时域滤波强度参数，[0, 127]     |
| u8TUvExK            | uv域静止区域时域滤波强度微调参数, [0, 15]。    |
| u8TUvKslop1         | uv域静止区域时空滤波加权系数插值参数，[0, 127]   |
| u8TUvKslop2         | uv域运动区域时空滤波加权系数插值参数，[0, 127]   |
| u8TUvSrcChooseKTh   | uv域时域滤波基数选择阈值，[0, 127]         |
| u8MfactorKTh        | 像素锐化因子调整基准阈值，[0, 127]          |
| u8MfactorSlop       | 锐化因子调整平滑参数, [0, 15]。           |
| u8MotionStatTh      | 运动统计阈值, [0, 15]。               |
| u8SfactorStatTh     | 纹理统计阈值, [0, 3]。                |
| u8MotionFilter      | 运动检测结果滤波参数, [0, 15]。           |
| u8MotionAreaExpand  | 运动边界区域进行扩张使能位, [0, 1]。         |
| u8LumStr            | 帧差调整查找表, [0, 15]。              |
| u16TMfTh1           | 静止块判断阈值, [0, 8191]             |
| u16TMfTh2           | 运动块判别阈值, [0, 8191]             |
| u16YnrCalcK         | 高斯权重计算参数, [0,65535]            |
| u16YnrWeightTbl     | 高斯权重表, [0, 1023]。              |
| u16TYTh1            | Y域静止区域时域滤波加权系数选择阈值, [0, 511]   |
| u16TYTh2            | Y域运动区域时域滤波加权系数选择阈值, [0, 511]   |
| u16YUvTh1           | uv域静止区域时域滤波加权系数选择阈值, [0, 511]。 |
| u16YUvTh2           | uv域运动区域时域滤波加权系数选择阈值, [0, 511]。 |
| u16MdTh             | 运动水平参数, [0,65535]              |
| u16Weight4_7X5      | 7*5的邻域降噪时中心像素的权重值，[0, 8695]。   |
| u16TnrMotionFlagTh  | 运动静止块判决阈值，[0, 1024]。           |

&emsp;&emsp;【相关函数接口】

&emsp;&emsp;ISP_3DNR_ATTR_S

<br/>

### **ISP_3DNR_ATTR_S **

&emsp;&emsp;【说明】

&emsp;&emsp;3d降噪信息结构体。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_3DNR_ATTR_S {
    AK_U8             u8TnrDebugOutput;    //[0,1]
    AK_U8           u8MainTnrEnable;
    ISP_OP_TYPE_E    en3dnrMode;

    ISP_3DNR_S      stManual3dnr;
    ISP_3DNR_S      stLinkage3dnr[12];
} ISP_3DNR_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**               |
| ---------------- | -------------------- |
| u8TnrDebugOutput | 3dnr debug模式位, [0,1] |
| u8MainTnrEnable  | 3dnr 总使能位, [0,1]     |
| en3dnrMode       | 模式选择，0 手动，1联动        |
| stManual3dnr     | 手动3dnr参数             |
| stLinkage3dnr    | 联动3dnr参数             |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_Get3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
    AK_S32 AK_MPI_ISP_Set3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

<br/>

### **ISP_LENS_COEF_S**

&emsp;&emsp;【说明】

&emsp;&emsp;coef结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_LENS_COEF_S
{
    AK_U16 u16CoefB[10];    //[0,255]
    AK_U16 u16CoefC[10];    //[0,1023]
} ISP_LENS_COEF_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**            |
| -------- | ----------------- |
| u16CoefB | 分段拟合直线B\*Rx+C中的斜率 |
| u16CoefC | 分段拟合直线B\*Rx+C中的截距 |
| <br/>    |                   |

### **ISP_LSC_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;镜头校正结构信息。

&emsp;&emsp;【定义】

```c
typedef struct akISP_LSC_ATTR_S
{
    AK_U8               u16LscMode;
    AK_U8               u16LinkageStrength[13];  //[0,1023]
    AK_U16                u16LscEnable;
    //the reference point of lens correction
    AK_U16                u16Xref;      //[0,4096]
    AK_U16                u16Yref;      //[0,4096]
    AK_U16                u16Lsc_shift;   //[0,15]
    ISP_LENS_COEF_S    stLscRCoef;
    ISP_LENS_COEF_S    stLscGrCoef;
    ISP_LENS_COEF_S    stLscGbCoef;
    ISP_LENS_COEF_S    stLscBCoef;
    //the range of ten segment
    AK_U16                u16Range[10];   //[0,1023]
} ISP_LSC_ATTR_S;
```

<br/>

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                    |
| ------------------ | ------------------------- |
| u16LscEnable       | LSC矫正使能位                  |
| u16Xref            | 亮度中心点横坐标                  |
| u16Yref            | 亮度中心点纵坐标                  |
| u16Lsc_shift       | 半径偏移量，控制半径有效位为10位         |
| stLscRCoef         | R通道分段拟合直线参数               |
| stLscGrCoef        | Gr通道分段拟合直线参数              |
| stLscGbCoef        | Gb通道分段拟合直线参数              |
| stLscBCoef         | B通道分段拟合直线参数               |
| u16Range           | LSC分段矫正半径范围               |
| u16LscMode         | LSC矫正模式位。0 为手动模式，1位自动模式   |
| u16LinkageStrength | LSC各个Env下的矫正强度系数，强度越大矫正越强 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
    AK_S32 AK_MPI_ISP_SetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

<br/>

### **ISP_SENSOR_REG_INFO_S**

&emsp;&emsp;【说明】

&emsp;&emsp;sensor寄存器信息结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_SENSOR_REG_INFO_S {
    AK_U16 u16RegAddr;
    AK_U16 u16Value;
} ISP_SENSOR_REG_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述** |
| ---------- | ------ |
| u16RegAddr | 寄存器地址  |
| u16Value   | 寄存器数值  |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetSensorReg(AK_S32 s32GrpId, ISP_SENSOR_REG_INFO_S *pstSensorRegInfo);
```

<br/>

### **ISP_EX_ZWEIGHT_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;扩展区域权重结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_EX_ZWEIGHT_ATTR_S {
    AK_U8    u8WinWeight[8][16];
    AK_U8    u8ExZoneWeightStr;
} ISP_EX_ZWEIGHT_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**                      |
| ----------------- | --------------------------- |
| u8WinWeight       | 重点区域属性，[0，1]，0：非重点区域；1：重点区域 |
| u8ExZoneWeightStr | 重点区域曝光权重属性，[0，15]           |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_GetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
    AK_S32 AK_MPI_ISP_SetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight)
```

<br/>

### **ISP_EFFECT_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;YUV效果结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_EFFECT_ATTR_S
{
    AK_U8   u8YuvOutEnable;
    AK_U8   u8DarkMarginEn;
    AK_U8   u8YA;      // [0, 255]
    AK_S8   s8YB;     //[-128, 127]
    AK_S16  s16UvA;    //[-256, 255]
    AK_S16  s16UvB;    //[-256, 255]
} ISP_EFFECT_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**                 |
| -------------- | ---------------------- |
| u8YA           | 亮度增益参数，[0,255]         |
| s8YB           | 亮度偏移参数，[-128,127]      |
| s16UvA         | UV增益参数，[-256,255]      |
| s16UvB         | UV偏移参数，[-256,255]      |
| u8DarkMarginEn | 变黑使能位，0: 禁用    1: 启用   |
| u8YuvOutEnable | YUV输出使能，0: 禁用    1: 启用 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
    AK_S32 AK_MPI_ISP_GetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect)
```

<br/>

### **ISP_RGB_GAMMA_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB gamma曲线结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RGB_GAMMA_S {
    AK_U16  u16RgbGammaEnable;
    AK_U16  u16RGamma[129];   //10bit
    AK_U16  u16GGamma[129];   //10bit
    AK_U16  u16BGamma [129];  //10bit
    AK_U16  u16RKey[16];
    AK_U16  u16GKey[16];
    AK_U16  u16BKey[16];
} ISP_RGB_GAMMA_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**                      |
| ----------------- | --------------------------- |
| u16RGamma         | R通道Gamma曲线，[0,1023]         |
| u16GGamma         | R通道Gamma曲线，[0,1023]         |
| u16BGamma         | R通道Gamma曲线，[0,1023]         |
| u16RKey           | R通道曲线关键点，[0,128]            |
| u16GKey           | R通道曲线关键点，[0,128]            |
| u16BKey           | R通道曲线关键点，[0,128]            |
| u16RgbGammaEnable | RGB gamma使能位，0: 禁用    1: 启用 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>

### **ISP_RGB_GAMMA_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;RGB gamma参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_RGB_GAMMA_ATTR_S {
    AK_U16      u16GainTh1;
    AK_U16      u16GainTh2;
    ISP_RGB_GAMMA_S  stLinkageRgbGamma[3];
} ISP_RGB_GAMMA_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**               | **描述**             |
| ---------------------- | ------------------ |
| u16GainTh1, u16GainTh2 | Gamma切换阈值，[0,1023] |
| stLinkageRgbGamma      | 联动RGB gamma        |

&emsp;&emsp;【相关函数接口】

```c
     AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>

### **ISP_CONTRAST_S**

&emsp;&emsp;【说明】

&emsp;&emsp;手动对比度参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_CONTRAST_S
{
     AK_U8   u8ContrastEnable;
     AK_U16  u16YContrast;  //[0,511]
     AK_S16  s16YShift;    //[0, 511]
} ISP_CONTRAST_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**              |
| ---------------- | ------------------- |
| u8ContrastEnable | 手动对比度使能位            |
| u16YContrast     | 手动对比度增强系数，[0,511]   |
| s16YShift        | 手动亮度黑平衡偏移系数，[0,511] |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_AUTO_CONTRAST_S**

&emsp;&emsp;【说明】

&emsp;&emsp;自动对比度参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_AUTO_CONTRAST_S
{
    AK_U8   u8ContrastEnable;
    AK_U8   u8ShiftMax;    //[0, 127]
    AK_U16  u16DarkPixelArea; //[0, 511]
    AK_U16  u8DarkPixelRate;  //[1, 256]
} ISP_AUTO_CONTRAST_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**               |
| ---------------- | -------------------- |
| u8ContrastEnable | 自动对比度使能位             |
| u16DarkPixelArea | 直方图中亮度暗区像素区域，[0,511] |
| u8DarkPixelRate  | 暗区像素比例，[1,256]       |
| u8ShiftMax       | 最大偏移阈值，[0,127]       |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_CONTRAST_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;对比度参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct  akISP_CONTRAST_ATTR_S
{
    ISP_OP_TYPE_E            enContrastMode;
    ISP_CONTRAST_S            stManualContrast;
    ISP_AUTO_CONTRAST_S    stLinkageContrast[12];
} ISP_CONTRAST_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**           |
| ----------------- | ---------------- |
| enContrastMode    | 对比度模式，0：手动  1：联动 |
| stManualContrast  | 手动对比度参数          |
| stLinkageContrast | 联动对比度调整参数        |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_LCE_S**

&emsp;&emsp;【说明】

&emsp;&emsp;局部对比度增强参数。

&emsp;&emsp;【定义】

```c
typedef struct akISP_LCE_S {
    AK_U8    u8LceEnable;
    AK_U8    u8LceUvAdjustEn;
    AK_U8   u8LceUvAdjustLevel;
    AK_U8    u8LceHeStr;
    AK_U8     u8LceHeStrLow;
    AK_U8   u8LceLumFilterK;//[0,8]
    AK_U8   u8LceSpatFilterK;//[0,8]
    AK_U8   u8LceTempFilterK;//[0,15]
    AK_U8   u8LceStrength[4][8];
} ISP_LCE_S;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                   |
| ------------------ | ------------------------ |
| u8LceEnable        | 局部对比度增强使能，0: 禁用    1: 启用 |
| u8LceUvAdjustEn    | UV调整使能，0: 禁用    1: 启用    |
| u8LceUvAdjustLevel | UV调整强度，[0,31]            |
| u8LceHeStr         | 块内各级亮度剪裁阈值，[0,255]       |
| u8LceHeStrLow      | 块内暗区亮度剪裁阈值，[0,255]       |
| u8LceLumFilterK    | 亮度滤波系数，[0,8]             |
| u8LceSpatFilterK   | 空域滤波系数，[0,8]             |
| u8LceTempFilterK   | 时域滤波系数，[0,15]            |
| u8LceStrength      | 局部对比度强度权重，[0,255]        |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

<br/>

### **ISP_LCE_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;局部对比度增强参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_LCE_ATTR_S{
    ISP_OP_TYPE_E  enLceMode;
    ISP_LCE_S      stManualLce;
    ISP_LCE_S      stLinkageLce[12];
} ISP_LCE_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**     | **描述**               |
| ------------ | -------------------- |
| enLceMode    | 局部对比度增强模式，0：手动  1：联动 |
| stManualLce  | 手动局部对比度增强            |
| stLinkageLce | 联动局部对比度增强            |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

<br/>

### **ISP_Y_GAMMA_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;y gamma参数参数结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_Y_GAMMA_ATTR_S
{
    AK_U16  u16YgammaEnable;
    AK_U8   u8YgammaUvAdjustEnable;
    AK_U8   u8YgammaUvAdjustLevel;
    AK_U16  u16Ygamma[129];    //10bit
    AK_U16  u16YgammaKey[16];
    AK_U16  u16YgammaCnoiseYth1;
    AK_U16  u16YgammaCnoiseYth2 ;
    AK_U16  u16YgammaCnoiseGain ;
} ISP_Y_GAMMA_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**               | **描述**                       |
| ---------------------- | ---------------------------- |
| u16Ygamma              | Ygamma亮度查找表，[0,1023]         |
| u16YgammaKey           | 曲线关键点，[0,128]                |
| u8YgammaUvAdjustEnable | YGamma UV调整使能，0: 禁用    1: 启用 |
| u8YgammaUvAdjustLevel  | UV调整强度，[0，31]                |
| u16YgammaCnoiseYth1    | 色差抑制门限值1，[0,1023]            |
| u16YgammaCnoiseYth2    | 色差抑制门限值2，[0,1023]            |
| u16YgammaEnable        | YGamma使能位，0: 禁用    1: 启用     |
| u16YgammaCnoiseGain    | UV调整增益，[0,1023]              |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
    AK_S32 AK_MPI_ISP_GetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

<br/>

### **ISP_DAY_NIGHT_MODE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;日夜模式。

&emsp;&emsp;【定义】

```c
typedef enum akISP_DAY_NIGHT_MODE_E {
    MODE_DAY,
    MODE_NIGHT,
    MODE_USR_DEFINE_1,
    MODE_USR_DEFINE_2,
    MODE_USR_DEFINE_3,
    MODE_NUM
} ISP_DAY_NIGHT_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述** |
| ----------------- | ------ |
| MODE_DAY          | 白天     |
| MODE_NIGHT        | 夜视     |
| MODE_USR_DEFINE_1 | 用户自定义1 |
| MODE_USR_DEFINE_2 | 用户自定义2 |
| MODE_USR_DEFINE_3 | 用户自定义2 |
| MODE_NUM          | 模式总数   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SwitchMode(AK_S32 s32GrpId, ISP_DAY_NIGHT_MODE_E enMode);
```

<br/>

### **ISP_NIGHT_TYPE_E**

&emsp;&emsp;【说明】

&emsp;&emsp;夜视类型。

&emsp;&emsp;【定义】

```c
typedef enum akISP_NIGHT_TYPE_E {
    IR_LED_NIGHT,
    WHITE_LED_NIGHT,
    BLACKLIGHT_NIGHT,
    TYPE_NUM
} ISP_NIGHT_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述** |
| ---------------- | ------ |
| IR_LED_NIGHT     | 红外夜视   |
| WHITE_LED_NIGHT  | 白光灯夜视  |
| BLACKLIGHT_NIGHT | 黑光彩色夜视 |
| TYPE_NUM         | 类型总数   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_IR_LED_NIGHT_PARAM_S**

&emsp;&emsp;【说明】

&emsp;&emsp;红外夜视软光敏参数。

&emsp;&emsp;【定义】

```c
typedef struct akISP_IR_LED_NIGHT_PARAM_S {
    AK_U32    u32DayToNightLum;    // day to night lum value
    AK_U32    u32NightToDayLum;    // night to day lum value
    AK_U32    u32AwbNightDisMin;
    AK_U32    u32AwbNightDisMax;
    AK_U32    u32GainR;
    AK_S32    s32OffsetR;
    AK_U32    u32GainB;
    AK_S32    s32OffsetB;
    AK_U32    u32GainRB;
    AK_S32    s32OffsetRB;
    AK_U32    u32BlkCheckFlag;
    AK_U32    u32LowLumiTh;
    AK_U32    u32HighLumiTh;
    AK_U32    u32NonInfraredRatioTh;
    AK_U32    u32RevisedDisMaxRatio;
} ISP_IR_LED_NIGHT_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                                                                                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| u32DayToNightLum      | 白天切换到夜视的亮度值。大于此阈值，认为亮度方面达到夜视。                                                                                                                                         |
| u32NightToDayLum      | 夜视切换到白天的亮度值。小于此阈值，认为亮度方面达到白天。                                                                                                                                         |
| u32AwbNightDisMin     | 预留，暂未使用                                                                                                                                                               |
| u32AwbNightDisMax     | 夜视切换到白天的RGB差异阈值。RGB差异值大于此阈值，认为RGB差异达到白天。                                                                                                                              |
| u32GainR              | R增益，默认1024。（u32GainR、s32OffsetR、u32GainB 、s32OffsetB、u32GainRB、s32OffsetRB 为线性化参数，主要作用是把850nm红外光下某些sensor的QE曲线相差较大的sensor响应值利用线性化的方式把sensor输出的响应值做成相等，更加方便的区分白天夜视判断。） |
| s32OffsetR            | R偏移，默认0。                                                                                                                                                              |
| u32GainB              | B增益，默认1024。                                                                                                                                                           |
| s32OffsetB            | B偏移，默认0。                                                                                                                                                              |
| u32GainRB             | RB增益，默认1024                                                                                                                                                           |
| s32OffsetRB           | RB偏移，默认0。                                                                                                                                                             |
| u32BlkCheckFlag       | 分块差异检测使能，0 不使能分块差异检测，用整体差异检测；1 使能分块差异检测。                                                                                                                              |
| u32LowLumiTh          | 有效块的低亮度阈值（分块差异检测使用）。取值范围[0,255]。                                                                                                                                      |
| u32HighLumiTh         | 有效块的高亮度阈值（分块差异检测使用）。取值范围(0,255]。                                                                                                                                      |
| u32NonInfraredRatioTh | 非红外块占所有有效块的百分比阈值（分块差异检测使用）。取值范围(0,100)。                                                                                                                               |
| u32RevisedDisMaxRatio | DisMax提升比率。取值范围[0,1024]。                                                                                                                                              |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_WHITE_LED_NIGHT_PARAM_S**

&emsp;&emsp;【说明】

&emsp;&emsp;白光灯夜视软光敏参数。

&emsp;&emsp;【定义】

```c
typedef struct akISP_WHITE_LED_NIGHT_PARAM_S {
    AK_U32    u32DayToNightLum;    // day to night lum value
    AK_U32    u32NightToDayLum;    // night to day lum value
    AK_U32    u32HighlightLumiTh;
    AK_U32    u32HighlightBlkCntMax;
} ISP_WHITE_LED_NIGHT_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                        |
| --------------------- | ----------------------------- |
| u32DayToNightLum      | 白天切换到夜视的亮度值。大于此阈值，认为亮度方面达到夜视。 |
| u32NightToDayLum      | 夜视切换到白天的亮度值。小于此阈值，认为亮度方面达到白天。 |
| u32HighlightLumiTh    | 高亮度阈值                         |
| u32HighlightBlkCntMax | 高亮度块数最大值                      |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_BLACKLIGHT_NIGHT_PARAM_S**

&emsp;&emsp;【说明】

&emsp;&emsp;黑光彩色夜视软光敏参数。

&emsp;&emsp;【定义】

```c
typedef struct akISP_BLACKLIGHT_NIGHT_PARAM_S {
    AK_U32  u32DayToNightAGain;
    AK_U32  u32DayToNightDGain;
    AK_U32  u32DayToNightIspDGain;
    AK_U32  u32DayToNightExpTime;
    AK_U32  u32DayToNightDarkPixelRate;
    AK_U32  u32NightToDayAGain;
    AK_U32  u32NightToDayDGain;
    AK_U32  u32NightToDayIspDGain;
    AK_U32  u32NightToDayExpTime;
    AK_U32  u32NightToDayDarkPixelRate;
} ISP_BLACKLIGHT_NIGHT_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**                   | **描述**            |
| -------------------------- | ----------------- |
| u32DayToNightAGain         | 白天切换到夜视的A增益值。     |
| u32DayToNightDGain         | 白天切换到夜视的D增益值。     |
| u32DayToNightIspDGain      | 白天切换到夜视的Isp Ｄ增益值。 |
| u32DayToNightExpTime       | 白天切换到夜视的曝光时间。     |
| u32DayToNightDarkPixelRate | 白天切换到夜视的暗区像素比率。   |
| u32NightToDayAGain         | 夜视切换到白天的A增益值。     |
| u32NightToDayDGain         | 夜视切换到白天的D增益值。     |
| u32NightToDayIspDGain      | 夜视切换到白天的Isp D增益值。 |
| u32NightToDayExpTime       | 夜视切换到白天的曝光时间。     |
| u32NightToDayDarkPixelRate | 夜视切换到白天的暗区像素比率。   |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_SOFT_PS_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;无光敏日夜切换参数结构（新算法）。

&emsp;&emsp;【定义】

```c
typedef struct akISP_SOFT_PS_ATTR_S {
    ISP_NIGHT_TYPE_E    enNightType;
    AK_U32              u32DayCheckFrameNum;
    AK_U32              u32NightCheckFrameNum;
    AK_U32              u32ExpStableCheckFrameNum;
    AK_S32              s32ExpStableTimeOutMs;
    AK_U32              u32LockCntTh;
    AK_U32              u32LockTimeMs;

    union
    {
        ISP_IR_LED_NIGHT_PARAM_S        stIrLedNightParm;
        ISP_WHITE_LED_NIGHT_PARAM_S     stWhiteLedNightParm;
        ISP_BLACKLIGHT_NIGHT_PARAM_S    stBlackLightNightParm;
    };
} ISP_SOFT_PS_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**                  | **描述**                                                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enNightType               | 夜视类型                                                                                                                                                                       |
| u32DayCheckFrameNum       | 白天状态时检测帧数                                                                                                                                                                  |
| u32NightCheckFrameNum     | 夜视状态时检测帧数                                                                                                                                                                  |
| u32ExpStableCheckFrameNum | 曝光稳定检测帧数                                                                                                                                                                   |
| s32ExpStableTimeOutMs     | 曝光稳定等待超时，单位毫秒                                                                                                                                                              |
| u32LockCntTh              | 切换次数阈值。程序每隔2分钟会检查日、夜切换次数（日切到夜，计1次，夜切到日，也计1次）。若日、夜切换次数大于等于这个值，若当前是夜视，则锁住在夜视。若当前是白天，则等到切换到夜视再锁住在夜视。（若超过2分钟还没切换到夜视，则认为已经不震荡了，不锁了。）lock_cnt_th和lock_time_ms任意一个设置为0，则不使能震荡锁功能。 |
| u32LockTimeMs             | 锁住的时长，单位ms。若锁住时间超过这个时长，或者EV值变化大于10%，会解锁恢复切换。lock_cnt_th和lock_time_ms任意一个设置为0，则不使能震荡锁功能。                                                                                    |
| stIrLedNightParm          | 红外夜视软光敏参数                                                                                                                                                                  |
| stWhiteLedNightParm       | 白光灯夜视软光敏参数                                                                                                                                                                 |
| stBlackLightNightParm     | 黑光彩色夜视软光敏参数                                                                                                                                                                |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_NON_INFRARED_RATIO_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;计算非红外比率需要的参数结构。

&emsp;&emsp;【定义】

```c
typedef struct akISP_NON_INFRARED_RATIO_ATTR_S {
    AK_U32    u32AwbNightDisMax;
    AK_U32    u32GainR;
    AK_S32    s32OffsetR;
    AK_U32    u32GainB;
    AK_S32    s32OffsetB;
    AK_U32    u32GainRB;
    AK_S32    s32OffsetRB;
    AK_U32    u32LowLumiTh;
    AK_U32    u32HighLumiTh;
    AK_U32    u32RevisedDisMaxRatio;
}ISP_NON_INFRARED_RATIO_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                                                                                                                                                    |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| u32AwbNightDisMax     | 夜视切换到白天的RGB差异阈值。RGB差异值大于此阈值，认为RGB差异达到白天。                                                                                                                  |
| u32GainR              | R增益，默认1024。（gain_r、offset_r 、gain_b、offset_b、 gain_rb、offset_rb为线性化参数，主要作用是把850nm红外光下某些sensor的QE曲线相差较大的sensor响应值利用线性化的方式把sensor输出的响应值做成相等，更加方便的区分白天夜视判断。） |
| s32OffsetR            | R偏移，默认0。                                                                                                                                                  |
| u32GainB              | B增益，默认1024。                                                                                                                                               |
| s32OffsetB            | B偏移，默认0。                                                                                                                                                  |
| u32GainRB             | RB增益，默认1280。                                                                                                                                              |
| s32OffsetRB           | RB偏移，默认0。                                                                                                                                                 |
| u32LowLumiTh          | 有效块的低亮度阈值（分块差异检测使用）。取值范围[0,255]。                                                                                                                          |
| u32HighLumiTh         | 有效块的高亮度阈值（分块差异检测使用）。取值范围(0,255]。                                                                                                                          |
| u32RevisedDisMaxRatio | DisMax提升比率。取值范围[0,1024]。                                                                                                                                  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_ISP_GetNonInfraredRatio(AK_S32 s32GrpId,
    ISP_NON_INFRARED_RATIO_ATTR_S *pstNirAttr, AK_U32 *pu32NonInfraredRatio);
```

<br/>

### **ISP_3D_NR_REF_SIZE_STAT_INFO**

&emsp;&emsp;【说明】

&emsp;&emsp;3DNR的buf使用统计信息结构体。

&emsp;&emsp;【定义】

```c
typedef struct akISP_3D_NR_REF_SIZE_STAT_INFO{
    AK_U32  u32RefSizeStatis[3];/* 0-y used size; 1-u used size; 2-v used size*/
}ISP_3D_NR_REF_SIZE_STAT_INFO;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                                                        |
| ---------------- | ------------------------------------------------------------- |
| u32RefSizeStatis | 3DNR buf使用大小。下标0的数值表示Y分量使用大小；下标1的数值表示U分量使用大小；下标2的数值表示V分量使用大小。 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_ISP_Get3dnrRefSizeStat(AK_S32 s32GrpId, ISP_3D_NR_REF_SIZE_STAT_INFO *pstRefSize);
```

<br/>

## 版本信息获取

### **AK_MPI_ISP_GetIspSdkVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取ISP SDK库的版本号。

&emsp;&emsp;【语法】

```c
    const char* AK_MPI_ISP_GetIspSdkVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**     | **描述** |
| ----------- | ------ |
| ISP SDK库版本号 | 成功     |
| NULL        | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

<br/>

## MD/OD信息获取

### **AK_MPI_ISP_GetOdInfo**

&emsp;&emsp;【描述】

&emsp;&emsp;获取OD需要的数据信息。上层可以用OD统计数据信息来实现遮挡侦测算法。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetOdInfo(AK_S32 s32GrpId, ISP_OD_INFO_S *pstOd);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstOd    | OD数据信息                                         | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetMdStat**

&emsp;&emsp;【描述】

&emsp;&emsp;获取MD统计信息。上层可以用MD统计信息来实现移动侦测算法。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetMdStat(AK_S32 s32GrpId, ISP_MD_INFO_S *pstMd);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstMd    | md统计信息                                         | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 当前图像效果设置/获取

### AK_MPI_ISP_SetEffect

&emsp;&emsp;【描述】

&emsp;&emsp;设置效果。由于ISP底层接口比较复杂，参数很多，effect模块提供了简单的个性化效果设置接口，可实现类似电视机、显示器等调节效果的功能。请尽可能不要用AK_MPI_ISP_SetEffect接口设置翻转镜像，而是使用AK_MPI_ISP_SwitchFlipMirror接口。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 s32Value);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| enType   | 效果类型                                           | 输入        |
| s32Value | 效果数值                                           | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误     |
| ERROR_TYPE_DEV_CTRL_FAILED | 底层设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

> **注意：**若isp参数配置文件里YUV effect模块里勾选了Auto Y Gain，则无法设置Contrast的参数。

<br/>

### **AK_MPI_ISP_GetEffect**

&emsp;&emsp;【描述】

&emsp;&emsp;获取效果。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 *ps32Value);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| enType    | 效果类型                                           | 输入        |
| ps32Value | 效果数值                                           | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG  | 参数错误   |
| ERROR_TYPE_POINTER_NULL | 参数为空   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 隐私遮挡参数设置/获取

### **AK_MPI_PP_MaskSetArea**

&emsp;&emsp;【描述】

&emsp;&emsp;设置mask 区域。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_PP_MaskSetArea(AK_S32 s32GrpId, AK_S32 s32ChnId, const PP_MASK_AREA_INFO_S *pstArea);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                               | **输入/输出** |
| -------- | ---------------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。       | 输入        |
| s32ChnId | VPSS的通道id, [0, 1]。默认主通道的ChnId为0，次通道的ChnId为1。第三通道不支持。 | 输入        |
| pstArea  | mask区域参数                                             | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_PP_MaskGetArea**

&emsp;&emsp;【描述】

&emsp;&emsp;获取mask 区域。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_PP_MaskGetArea(AK_S32 s32GrpId, AK_S32 s32ChnId, PP_MASK_AREA_INFO_S *pstArea);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                               | **输入/输出** |
| -------- | ---------------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。       | 输入        |
| s32ChnId | VPSS的通道id, [0, 1]。默认主通道的ChnId为0，次通道的ChnId为1。第三通道不支持。 | 输入        |
| pstArea  | mask区域参数                                             | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_PP_MaskSetColor**

&emsp;&emsp;【描述】

&emsp;&emsp;设置mask 颜色。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_PP_MaskSetColor(AK_S32 s32GrpId, const PP_MASK_COLOR_INFO_S *pstColor);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstColor | mask颜色参数                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_PP_MaskGetColor**

&emsp;&emsp;【描述】

&emsp;&emsp;获取mask 颜色。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_PP_MaskGetColor(AK_S32 s32GrpId, PP_MASK_COLOR_INFO_S *pstColor);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstColor | mask颜色参数                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 画框参数设置

### AK_MPI_PP_SetBoxColorTable

&emsp;&emsp;【描述】

&emsp;&emsp;设置画框的调色板。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_PP_SetBoxColorTable(AK_S32 s32GrpId, AK_U32 *pu32ColorTable);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                                                                                 | **输入/输出** |
| -------------- | ------------------------------------------------------------------------------------------------------ | --------- |
| s32GrpId       | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。                                                         | 输入        |
| pu32ColorTable | 画框的调色板数组，维度为7。每个颜色32bit，从低到高为r、g、b、a。a是透明度，0为完全透明，255为不透明。r:0-7bit, g:8-15bit, b:16-23bit, a:24-31bit。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_PP_DrawBox**

&emsp;&emsp;【描述】

&emsp;&emsp;设置画框参数。

&emsp;&emsp;【语法】

```c
    int AK_MPI_PP_DrawBox(AK_S32 s32GrpId, AK_S32 s32ChnId, PP_BOX_GROUP_S *pstBoxGroup);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                               | **输入/输出** |
| ----------- | ---------------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。       | 输入        |
| s32ChnId    | VPSS的通道id, [0, 1]。默认主通道的ChnId为0，次通道的ChnId为1。第三通道不支持。 | 输入        |
| pstBoxGroup | 画框参数                                                 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 自动对焦参数、状态获取/设置

### **AK_MPI_ISP_SetAfAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置自动对焦结构。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAfAttr | AF结构信息                                         | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.so、libplat_isp_sdk.so或者libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAfAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动对焦结构。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAfAttr | AF结构信息                                         | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAfStat**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动对焦统计信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAfStat(AK_S32 s32GrpId, ISP_AF_INFO_S *pstAfStat);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAfStat | AF统计信息                                         | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 曝光参数、状态获取/设置

### **AK_MPI_ISP_GetExpType**

&emsp;&emsp;【描述】

&emsp;&emsp;获取曝光类型信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetExpType(AK_S32 s32GrpId, ISP_OP_TYPE_E *penExpType);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| penExpType | 曝光类型信息                                         | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetExpType**

&emsp;&emsp;【描述】

&emsp;&emsp;设置曝光类型信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetExpType(AK_S32 s32GrpId, ISP_OP_TYPE_E enExpType);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| enExpType | 曝光类型信息                                         | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAeRunInfo**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动曝光统计信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAeRunInfo | 自动曝光统计信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAeAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动曝光结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAeAttr | 自动曝光结构信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetAeAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置自动曝光结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAeAttr | 自动曝光结构信息                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAeConvergenceRate**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动曝光收敛速度。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAeConvergenceRate(AK_S32 s32GrpId, AK_U32 *pu32Value);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pu32Value | 自动曝光收敛速度                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetAeConvergenceRate**

&emsp;&emsp;【描述】

&emsp;&emsp;设置自动曝光收敛速度。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAeConvergenceRate(AK_S32 s32GrpId, AK_U32 u32Value);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| u32Value | 自动曝光收敛速度                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_CheckAeStable**

&emsp;&emsp;【描述】

&emsp;&emsp;检测自动曝光是否稳定。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_CheckAeStable(AK_S32 s32GrpId, AK_U32 *pu32Stable);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pu32Stable | 稳定状态，0 不稳定，1 稳定                                | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetAeSuspend**

&emsp;&emsp;【描述】

&emsp;&emsp;设置ae挂起/恢复。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAeSuspend(AK_S32 s32GrpId,  AK_U32 u32AeSuspendFlag);
```

&emsp;&emsp;【参数】

| **参数名称**         | **描述**                                         | **输入/输出** |
| ---------------- | ---------------------------------------------- | --------- |
| s32GrpId         | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| u32AeSuspendFlag | Ae 挂起标记，1 挂起，0 恢复                              | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetMeAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取手动曝光结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstMeAttr | 手动曝光结构信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetMeAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置手动曝光结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstMeAttr | 手动曝光结构信息                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 区域权重系数设置/获取

### **AK_MPI_ISP_GetExZweightAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取扩展权重系数信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstExZweight | 扩展权重系数信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetExZweightAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置权重系数信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstExZweight | 扩展权重系数信息                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 白平衡参数设置/获取

### **AK_MPI_ISP_GetAwbStatInfo**

&emsp;&emsp;【描述】

&emsp;&emsp;获取白平衡统计信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                         | **输入/输出** |
| -------------- | ---------------------------------------------- | --------- |
| s32GrpId       | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAwbStatInfo | 白平衡统计信息                                        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetWbType**

&emsp;&emsp;【描述】

&emsp;&emsp;获取白平衡类型信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetWbType(AK_S32 s32GrpId, ISP_OP_TYPE_E *penWbType);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| penWbType | 白平衡类型信息                                        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetWbType**

&emsp;&emsp;【描述】

&emsp;&emsp;设置白平衡类型信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetWbType(AK_S32 s32GrpId, ISP_OP_TYPE_E enWbType);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| enWbType | 白平衡类型信息                                        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetMwbAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取手动白平衡结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstMwbAttr | 手动白平衡结构信息                                      | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetMwbAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置手动白平衡结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstMwbAttr | 手动白平衡结构信息                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetAwbAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取自动白平衡结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAwbAttr | 自动白平衡结构信息                                      | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetAwbAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置自动白平衡结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstAwbAttr | 自动白平衡结构信息                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 宽动态参数设置/获取

### **AK_MPI_ISP_GetHdrAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取宽动态参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstHdr   | 宽动态参数                                          | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**    |
| -------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误      |
| ERROR_TYPE_POINTER_NULL    | p_wdr参数为空 |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetHdrAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置宽动态参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstHdr   | 宽动态参数                                          | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**    |
| -------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误      |
| ERROR_TYPE_POINTER_NULL    | p_wdr参数为空 |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 无光敏日夜切换参数设置/获取

### **AK_MPI_ISP_SetSoftPsParam**

&emsp;&emsp;【描述】

&emsp;&emsp;设置无光敏日夜切换参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstParam | 无光敏日夜切换参数                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                     | **描述**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG      | 参数错误          |
| ERROR_TYPE_POINTER_NULL     | 参数为空          |
| ERROR_TYPE_FUNC_NOT_SUPPORT | 不能与无光敏旧算法接口混用 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

参数示例：

```c
ISP_SOFT_PS_ATTR_S param = {0};

param.enNightType = IR_LED_NIGHT;
param.u32DayCheckFrameNum = 10;
param.u32NightCheckFrameNum = 10;
param.u32ExpStableCheckFrameNum = 10;
param.s32ExpStableTimeOutMs = -1;
param.u32LockCntTh = 5;
param.u32LockTimeMs = 60000;

param.stIrLedNightParm.u32DayToNightLum = 87961300;
param.stIrLedNightParm.u32NightToDayLum = 12000000;
param.stIrLedNightParm.u32AwbNightDisMax = 400;
param.stIrLedNightParm.u32AwbNightDisMin = 200;

param.stIrLedNightParm.u32GainR = 1024;
param.stIrLedNightParm.u32GainB = 1024;
param.stIrLedNightParm.u32GainRB = 1024;
param.stIrLedNightParm.s32OffsetR = 0;
param.stIrLedNightParm.s32OffsetB = 0;
param.stIrLedNightParm.s32OffsetRB = 0;
param.stIrLedNightParm.u32BlkCheckFlag = 1;
param.stIrLedNightParm.u32LowLumiTh = 12;
param.stIrLedNightParm.u32HighLumiTh = 252;
param.stIrLedNightParm.u32NonInfraredRatioTh = 35;
param.stIrLedNightParm.u32RevisedDisMaxRatio = 400;


AK_MPI_ISP_SetSoftPsParam(dev, &param);
```

<br/>

### **AK_MPI_ISP_GetSoftPsLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;获取无光敏日夜level状态。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetSoftPsLevel(AK_S32 s32GrpId, AK_S32 s32PreIrLevel, AK_S32 *ps32NewIrLevel);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**                                         | **输入/输出** |
| -------------- | ---------------------------------------------- | --------- |
| s32GrpId       | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32PreIrLevel  | 之前的ircut level，0 白天，1 夜视                       | 输入        |
| ps32NewIrLevel | 新的ircut level， 0 白天，1 夜视                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述**                                    |
| ----------------------- | ----------------------------------------- |
| ERROR_TYPE_INVALID_ARG  | 参数错误                                      |
| ERROR_TYPE_POINTER_NULL | 参数为空                                      |
| ERROR_TYPE_NOT_INIT     | 无光敏没有初始化（没有调用ak_vpss_set_soft_ps_param接口） |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

```c
        /* 先设置参数 */
        AK_MPI_ISP_SetSoftPsParam(dev, &param);

        /* 创建一个线程，每隔一定时间获取状态 */
        while (1)
        {
            ret = AK_MPI_ISP_GetSoftPsLevel(dev, pre_status, &cur_status);

            if ((pre_status != cur_status) && (AK_SUCCESS == ret))
            {
                if (STATE_DAY == cur_status)
                {
                    /* 切换到白天 */
                    ...
                    pre_status = STATE_DAY;    /* store new state */
                }
                else
                {
                    /* 切换到夜视 */
                    ...
                    pre_status = STATE_NIGHT;    /* store new state */
                }
        }
        AK_BASE_SleepMs(100);
    }
```

<br/>

### **AK_MPI_ISP_SwitchMode**

&emsp;&emsp;【描述】

&emsp;&emsp;切换日夜。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SwitchMode(AK_S32 s32GrpId, ISP_DAY_NIGHT_MODE_E enMode);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| enMode   | 日夜状态                                           | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                     | **描述**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG      | 参数错误          |
| ERROR_TYPE_MALLOC_FAILED    | 申请内存失败        |
| ERROR_TYPE_FILE_READ_FAILED | ISP conf文件读失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

## 帧率参数设置/获取

### **AK_MPI_ISP_GetFpsCtrlStat**

&emsp;&emsp;【描述】

&emsp;&emsp;获取帧率控制状态。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetFpsCtrlStat(AK_S32 s32GrpId, ISP_GAIN_STAT_E *penStat, AK_S32 *ps32NeedFps);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| penStat     | 增益状态                                           | 输出        |
| ps32NeedFps | 需要切换的帧率                                        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述**           |
| ----------------------- | ---------------- |
| ERROR_TYPE_INVALID_ARG  | 参数错误             |
| ERROR_TYPE_POINTER_NULL | stat或need_fps指针空 |
| ERROR_TYPE_NOT_INIT     | 未初始化             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

> **注意：**当应用需要在白天实现低照降帧控制时，可以建立一个线程，定时调用此接口。需要切换帧率时，调用AK_MPI_ISP_ChangeSensorFps接口。

<br/>

### **AK_MPI_ISP_ChangeSensorFps**

&emsp;&emsp;【描述】

&emsp;&emsp;切换sensor帧率。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_ChangeSensorFps(AK_S32 s32GrpId, AK_S32 s32NeedFps);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32NeedFps | 需要切换的帧率，由AK_MPI_ISP_GetFpsCtrlStat获得           | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                | **描述**           |
| ---------------------- | ---------------- |
| ERROR_TYPE_INVALID_ARG | dev或need_fps参数错误 |
| ERROR_TYPE_NOT_INIT    | 未初始化             |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

> **注意：**当应用需要在白天实现低照降帧控制时，可以建立一个线程，定时调用ak_vpss_get_fps_ctrl_stat接口。需要切换帧率时，调用此接口。Sensor的帧率不可随意设置。此接口的need_fps是由ak_vpss_get_fps_ctrl_stat输出得到的。

<br/>

### **AK_MPI_ISP_SetFpsLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;设置sensor三档帧率参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstFpsLevel | Sensor的3档帧率参数，见ISP_FPS_LEVEL_S                 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误     |
| ERROR_TYPE_POINTER_NULL    | fps参数为空  |
| ERROR_TYPE_DEV_CTRL_FAILED | 底层驱动操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

> **注意：**每次切换过日夜后，需要再调用此接口设置，否则又被isp参数文件覆盖了。

<br/>

### **AK_MPI_ISP_GetFpsLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;获取sensor三档帧率参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstFpsLevel | Sensor的3档帧率参数，见ISP_FPS_LEVEL_S                 | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述**    |
| ----------------------- | --------- |
| ERROR_TYPE_INVALID_ARG  | 参数错误      |
| ERROR_TYPE_POINTER_NULL | fps参数为空   |
| ERROR_TYPE_NOT_INIT     | 帧率参数没有初始化 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

### **AK_MPI_ISP_SetSensorFps**

&emsp;&emsp;【描述】

&emsp;&emsp;设置sensor帧率并调整最大曝光时间参数。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetSensorFps(AK_S32 s32GrpId, AK_S32 s32Fps);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32Fps   | Sensor的帧率                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误     |
| ERROR_TYPE_POINTER_NULL    | fps参数为空  |
| ERROR_TYPE_DEV_CTRL_FAILED | 底层驱动操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

  VPSS模块正常运行起来后，才能调用。

### **AK_MPI_ISP_GetSensorFps**

&emsp;&emsp;【描述】

&emsp;&emsp;获取sensor帧率。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetSensorFps(AK_S32 s32GrpId, AK_S32 *ps32Fps);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| ps32Fps  | Sensor的帧率                                      | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述**    |
| ----------------------- | --------- |
| ERROR_TYPE_INVALID_ARG  | 参数错误      |
| ERROR_TYPE_POINTER_NULL | fps参数为空   |
| ERROR_TYPE_NOT_INIT     | 帧率参数没有初始化 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

  VPSS模块正常运行起来后，才能调用。

<br/>

## 3D降噪参数设置/获取

### **AK_MPI_ISP_Get3dnrAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取3dnr结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_Get3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pst3dnrAttr | 3dnr结构信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_Set3dnrAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置3dnr结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_Set3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pst3dnrAttr | 3dnr结构信息                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 镜头校正参数设置/获取

### **AK_MPI_ISP_GetLscAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取镜头校正结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstLsc   | 镜头校正结构信息                                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetLscAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置镜头校正结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstLsc   | 镜头校正结构信息                                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## YUV效果参数设置/获取

### **AK_MPI_ISP_GetYuvEffectAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取YUV效果结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstYuvEffect | YUV效果结构信息                                      | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetYuvEffectAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置YUV效果结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstYuvEffect | YUV效果结构信息                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## Gamma相关参数设置/获取

### **AK_MPI_ISP_GetRgbGammaAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取RGB Gamma 结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstRgbGamma | RGB Gamma结构信息                                  | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetRgbGammaAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置RGB Gamma结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstRgbGamma | RGB Gamma结构信息                                  | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetYgammaAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取Y Gamma 结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstYgamma | Y Gamma结构信息                                    | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetYgammaAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置Y Gamma结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

&emsp;&emsp;【参数】

| **参数名称**  | **描述**                                         | **输入/输出** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstYgamma | Y Gamma结构信息                                    | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 对比度相关参数设置/获取

### **AK_MPI_ISP_GetContrastAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取对比度 结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstContrast | 对比度结构信息                                        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetContrastAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置对比度结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstContrast | 对比度结构信息                                        | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetLceAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;获取局部对比度增强结构信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstLce   | 局部对比度增强结构信息                                    | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetLceAttr**

&emsp;&emsp;【描述】

&emsp;&emsp;设置局部对比度增强结构信息。

&emsp;&emsp;【语法】

```c
   AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstLce   | 局部对比度增强结构信息                                    | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

## 其他

### **AK_MPI_ISP_GetCurLumi**

&emsp;&emsp;【描述】

&emsp;&emsp;获取亮度。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetCurLumi(AK_S32 s32GrpId, AK_U32 *pu32Lumi);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pu32Lumi | 亮度                                             | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SetForceAntiFlickerFlag**

&emsp;&emsp;【描述】

&emsp;&emsp;设置强制抗闪标记。某些场景受日光和灯光共同影响，图像会产生水波纹，可以设置强制抗闪来解决，但是在环境比较亮的情况，图像效果会过曝。与AK_MPI_ISP_SetAntiFlickerStrength接口不能同时使用。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetForceAntiFlickerFlag(AK_S32 s32GrpId, AK_S32 s32ForceFlag);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32ForceFlag | 强制抗闪标记，0 关闭，1 打开                               | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetForceAntiFlickerFlag**

&emsp;&emsp;【描述】

&emsp;&emsp;获取强制抗闪标记。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetForceAntiFlickerFlag(AK_S32 s32GrpId, AK_S32 *s32ForceFlag);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| s32ForceFlag | 强制抗闪标记，0 关闭，1 打开                               | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG  | 参数错误   |
| ERROR_TYPE_POINTER_NULL | 参数为空   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

**AK_MPI_ISP_SetAntiFlickerStrength**

&emsp;&emsp;【描述】

&emsp;&emsp;设置抗闪强度。某些场景受日光和灯光共同影响，图像会产生水波纹，可以设置强度来解决。与AK_MPI_ISP_SetForceAntiFlickerFlag接口不能同时使用。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SetAntiFlickerStrength(AK_S32 s32GrpId, AK_U32 u32Strength);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                         | **输入/输出** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| u32Strength | 抗闪强度，0 关闭，1-100 打开，100最强                       | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

  VPSS模块正常运行起来后，才能调用。

### **AK_MPI_ISP_GetAntiFlickerStrength**

&emsp;&emsp;【描述】

&emsp;&emsp;获取抗闪强度。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetAntiFlickerStrength(AK_S32 s32GrpId, AK_U32 *pu32Strength);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                         | **输入/输出** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pu32Strength | 抗闪强度，0 关闭，1-100 打开，100最强                       | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG  | 参数错误   |
| ERROR_TYPE_POINTER_NULL | 参数为空   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

  VPSS模块正常运行起来后，才能调用。

### **AK_MPI_ISP_GetRgbAverage**

&emsp;&emsp;【描述】

&emsp;&emsp;获取RGB平均值。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetRgbAverage(AK_S32 s32GrpId,
        AK_U32 *u32RAvr, AK_U32 *u32GAvr, AK_U32 *u32BAvr);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| u32RAvr  | r平均值                                           | 输出        |
| u32GAvr  | g平均值                                           | 输出        |
| u32BAvr  | b平均值                                           | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetSensorReg**

&emsp;&emsp;【描述】

&emsp;&emsp;获取sensor寄存器值。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetSensorReg(AK_S32 s32GrpId, ISP_SENSOR_REG_INFO_S *pstSensorRegInfo);
```

&emsp;&emsp;【参数】

| **参数名称**         | **描述**                                         | **输入/输出**         |
| ---------------- | ---------------------------------------------- | ----------------- |
| s32GrpId         | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入                |
| pstSensorRegInfo | Sensor寄存器结构信息                                  | 寄存器地址是输入，寄存器数值是输出 |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数为空   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_SwitchFlipMirror**

&emsp;&emsp;【描述】

&emsp;&emsp;相对于isp配置文件初始值的翻转镜像设置。 请尽可能不要用AK_MPI_ISP_SetEffect接口设置翻转镜像，而是使用AK_MPI_ISP_SwitchFlipMirror接口。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_SwitchFlipMirror(AK_S32 s32GrpId, AK_U32 u32FlipEn, AK_U32 u32MirrorEn);
```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**                                                    | **输入/输出** |
| ----------- | --------------------------------------------------------- | --------- |
| s32GrpId    | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。            | 输入        |
| u32FlipEn   | 垂直方向翻转使能。若想和isp conf里的效果一致，则设置为0；若想和isp conf里的效果相反，则设置为1。 | 输入        |
| u32MirrorEn | 水平方向翻转使能。若想和isp conf里的效果一致，则设置为0；若想和isp conf里的效果相反，则设置为1。 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述**  |
| -------------------------- | ------- |
| ERROR_TYPE_INVALID_ARG     | 参数错误    |
| ERROR_TYPE_NOT_INIT        | isp未初始化 |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetFlipMirror**

&emsp;&emsp;【描述】

&emsp;&emsp;获取翻转镜像状态，相对于isp配置文件初始值的状态。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetFlipMirror(AK_S32 s32GrpId, AK_U32 *pu32FlipEn, AK_U32 *pu32MirrorEn);
```

&emsp;&emsp;【参数】

| **参数名称**     | **描述**                                                                                                                     | **输入/输出** |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| s32GrpId     | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。                                                                             | 输入        |
| pu32FlipEn   | 垂直方向翻转使能。若当前效果和isp conf里的效果一致，则为0；若当前效果和isp conf里的效果相反，则为1。设备初始化后若没有调用过api接口ak_vpss_switch_flip_mirror设置翻转镜像，则此接口获取出来的值为0。 | 输出        |
| pu32MirrorEn | 水平方向翻转使能。若当前效果和isp conf里的效果一致，则为0；若当前效果和isp conf里的效果相反，则为1。设备初始化后若没有调用过api接口ak_vpss_switch_flip_mirror设置翻转镜像，则此接口获取出来的值为0。 | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                 | **描述**  |
| ----------------------- | ------- |
| ERROR_TYPE_INVALID_ARG  | 参数错误    |
| ERROR_TYPE_POINTER_NULL | 参数为空    |
| ERROR_TYPE_NOT_INIT     | isp未初始化 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_WaitExpStable**

&emsp;&emsp;【描述】

&emsp;&emsp;等待曝光稳定。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_WaitExpStable(AK_S32 s32GrpId, AK_U32 u32ExpStableCheckFrameNum, AK_S32 s32TimeOutMs);
```

&emsp;&emsp;【参数】

| **参数名称**                  | **描述**                                         | **输入/输出** |
| ------------------------- | ---------------------------------------------- | --------- |
| s32GrpId                  | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| u32ExpStableCheckFrameNum | 曝光稳定检测帧数                                       | 输入        |
| s32TimeOutMs              | 等待超时，单位毫秒                                      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### AK_MPI_ISP_GetEv

&emsp;&emsp;【描述】

&emsp;&emsp;获取环境EV值。建议等待曝光稳定后再调用，否则获取的值可能不稳定。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetEv(AK_S32 s32GrpId, AK_U32 *pu32Ev);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                         | **输入/输出** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pu32Ev   | 环境EV值，值越大表示环境越暗                                | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### **AK_MPI_ISP_GetRgbDis**

&emsp;&emsp;【描述】

&emsp;&emsp;获取RGB差异值。建议等待曝光稳定后再调用，否则获取的值可能不稳定。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetRgbDis(AK_S32 s32GrpId, AK_U32 u32GainR, AK_S32 s32OffsetR,
        AK_U32 u32GainB, AK_S32 s32OffsetB, AK_U32 *pu32Dis);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                                                                                                                  | **输入/输出** |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。                                                                                          | 输入        |
| u32GainR   | R增益，默认1024。（gain_r、offset_r 、gain_b、offset_b 为线性化参数，主要作用是把850nm红外光下某些sensor的QE曲线相差较大的sensor响应值利用线性化的方式把sensor输出的响应值做成相等，更加方便的区分白天夜视判断。） | 输入        |
| s32OffsetR | R偏移，默认0。                                                                                                                                | 输入        |
| u32GainB   | B增益，默认1024。                                                                                                                             | 输入        |
| s32OffsetB | B偏移，默认0。                                                                                                                                | 输入        |
| pu32Dis    | RGB差异值，值越大表示环境可见光越多                                                                                                                     | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VPSS模块正常运行起来后，才能调用。

<br/>

### AK_MPI_ISP_GetNonInfraredRatio

&emsp;&emsp;【描述】

&emsp;&emsp;获取非红外块占所有有效块的百分比。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_GetNonInfraredRatio(AK_S32 s32GrpId,
        ISP_NON_INFRARED_RATIO_ATTR_S *pstNirAttr, AK_U32 *pu32NonInfraredRatio);
```

&emsp;&emsp;【参数】

| **参数名称**             | **描述**                                         | **输入/输出** |
| -------------------- | ---------------------------------------------- | --------- |
| s32GrpId             | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstNirAttr           | 计算非红外比率需要的参数结构                                 | 输入        |
| pu32NonInfraredRatio | 非红外块百分比                                        | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VI模块正常运行起来后，才能调用。

<br/>

### AK_MPI_ISP_Get3dnrRefSizeStat

&emsp;&emsp;【描述】

&emsp;&emsp;获取3DNR的buf使用统计信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_ISP_Get3dnrRefSizeStat(AK_S32 s32GrpId, ISP_3D_NR_REF_SIZE_STAT_INFO *pstRefSize);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**                                         | **输入/输出** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS的group id, [0-4]。多目情况下，不同的设备对应不同的group id。 | 输入        |
| pstRefSize | 3DNR的buf使用统计信息结构                               | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功。        |
| 非0      | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码**                    | **描述** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG     | 参数错误   |
| ERROR_TYPE_POINTER_NULL    | 参数错误   |
| ERROR_TYPE_DEV_CTRL_FAILED | 设备操作失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vpss.a、libplat_isp_sdk.a

&emsp;&emsp;头文件：ak_vpss_isp.h

&emsp;&emsp;【调用流程】

&emsp;&emsp;VI模块正常运行起来后，才能调用。

<br/>

## vpss示例

### **个性化效果 ak_vpss_effect_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**     | **输入参数说明**                                                    |
| ------------ | ------------------------------------------------------------- |
| type         | 效果类型，brightness/hue/sharp/contrast/saturation/wdr/flip_mirror |
| degree       | 效果设置取值，flip_mirror[0, 3]，其他 [-50, 50]，默认0。                    |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。                               |
| path         | 保存yuv图像数据的路径                                                  |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2                                         |

<br/>

&emsp;&emsp;输出结果：输出效果处理之前和之后的YUV数据，保存在指定的path目录下。

<br/>

### **隐私遮挡 ak_vpss_mask_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko 。

| **输入参数**     | **输入参数说明**                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------- |
| rect0        | [x] [y] [width] [height/bitmap] [enable] [type] rect0 参数信息，默认disable。type见PP_MASK_TYPE_E枚举。 |
| rect1        | [x] [y] [width] [height/bitmap] [enable] [type] rect1 参数信息，默认disable。type见PP_MASK_TYPE_E枚举。 |
| rect2        | [x] [y] [width] [height/bitmap] [enable] [type] rect2 参数信息，默认disable。type见PP_MASK_TYPE_E枚举。 |
| rect3        | [x] [y] [width] [height/bitmap] [enable] [type] rect3 参数信息，默认disable。type见PP_MASK_TYPE_E枚举。 |
| alpha        | [0, 255]，默认0                                                                                |
| color_r      | [0, 255]，默认0                                                                                |
| color_g      | [0, 255]，默认0                                                                                |
| color_b      | [0, 255]，默认0                                                                                |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。                                                             |
| path         | 保存yuv图像数据的路径。                                                                               |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2                                                                       |

<br/>

&emsp;&emsp;输出结果：输出遮挡处理之前和之后的YUV数据，保存在指定的path目录下。

<br/>

### **画框 ak_vpss_draw_box_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**     | **输入参数说明**                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| channel      | 通道号                                                                                                                  |
| rect0        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] rect0 参数信息，默认disable。type见PP_SHAPE_TYPE_E枚举。 |
| rect1        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] rect1 参数信息，默认disable。type见PP_SHAPE_TYPE_E枚举。 |
| rect2        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] rect2 参数信息，默认disable。type见PP_SHAPE_TYPE_E枚举。 |
| rect3        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] rect3 参数信息，默认disable。type见PP_SHAPE_TYPE_E枚举。 |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。                                                                                      |
| path         | 保存yuv图像数据的路径。                                                                                                        |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2                                                                                                |

<br/>

&emsp;&emsp;输出结果：输出遮挡处理之前和之后的YUV数据，保存在指定的path目录下。

<br/>

### **MD信息获取 ak_vpss_md_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**     | **输入参数说明**                      |
| ------------ | ------------------------------- |
| time         | 运行时间，默认20秒。                     |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。 |
| path         | 保存md统计信息数据的路径                   |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2           |

<br/>

&emsp;&emsp;输出结果：输出MD统计信息数据，保存在指定的path目录下。

<br/>

### **OD信息获取 ak_vpss_od_sample**

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**     | **输入参数说明**                      |
| ------------ | ------------------------------- |
| time         | 运行时间，默认20秒。                     |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。 |
| path         | 保存od统计信息数据的路径                   |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2           |

<br/>

&emsp;&emsp;输出结果：输出OD统计信息数据，保存在指定的path目录下。

<br/>

### 二维码效果 ak_vpss_qr_sample

运行此sample前，需要先insmod ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko ，具体命令请参考第7章开头的描述。

| **输入参数**     | **输入参数说明**                      |
| ------------ | ------------------------------- |
| isp_cfg_path | ISP config file 保存路径，默认为空，需要填写。 |
| path         | 保存YUV图像数据的路径                    |
| dev_cnt      | 设备数量[1, 2]，默认1，双目版本用2           |

<br/>

&emsp;&emsp;输出结果：输出三帧YUV数据，保存在指定的path目录下。第一帧是原始图像效果，第二帧是适合二维码识别的图像效果，第三帧是恢复原始图像效果。

<br/>
