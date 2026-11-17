# 音效处理

## 概述

&emsp;&emsp;音频质量增强模块（AUDIO_EFFECT模块）通过重采样（resample）、数字放大（aslc）和均衡器（EQ）处理AI模块和AO模块的PCM裸数据，优化音频质量。还支持音量检测(VAD)、纯软件算法方式哭声检测(CRY)、NPU方式哭声检测(AI_CRY，该方式目前只支持16K采样率）关键词识别（KWS，目前暂不支持）等检测类的处理。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示。

### 结构体列表

| **数据结构**                       | **描述**                                             |
| ---------------------------------- | ---------------------------------------------------- |
| AUDIO_DATA_ATTR_S                  | 音频基本属性                                         |
| AUDIO_EFFECT_TYPE_E                | 音频效果处理类型                                     |
| AUDIO_EFFECT_REG_S                 | 注册音效模块：RES/VAD/CRY/AI_CRY，ASLC和EQ不需要注册 |
| AUDIO_EQ_ATTR_S                    | 音频均衡器的参数                                     |
| AUDIO_ASLC_ATTR_S                  | 音频数字放大的参数                                   |
| ARRAY_GEOMETRY_S                   | 几何麦克阵列                                         |
| AUDIO_SSL_ATTR_S                   | 声源定位参数                                         |
| AUDIO_LSSL_ATTR_S                  | 均匀线性声源定位参数                                 |
| AUDIO_VAD_ATTR_S                   | 音量检测参数                                         |
| AUDIO_CRY_ATTR_S                   | 哭声检测参数                                         |
| AUDIO_AI_CRY_ATTR_S                | AI算法哭声检测参数                                   |
| AUDIO_AI_KWS_ATTR_S                | 关键字识别参数                                       |
| AUDIO_AI_KWSASR_ATTR_S             | 关键字识别ASR参数                                    |
| SOUND_SPHERICAL_DIRECTION          | 声源三维空间位置                                     |
| AUDIO_EFFECT_RESULT_S              | AUDIO_EFFECT处理结果                                 |
| AUDIO_EFFECT_DATA_PROCESS_RESULT_S | 数据处理类的返回结果, RES/EQ/ASLC共用这同一个结构体  |
| AUDIO_VAD_RESULT_S                 | 音量检测的返回结果                                   |
| AUDIO_CRY_RESULT_S                 | 纯软件算法方式哭声检测的返回结果                     |
| AUDIO_AI_CRY_RESULT_S              | NPU方式的哭声检测的返回结果                          |
| AUDIO_SSL_RESULT_S                 | 声源定位返回结果                                     |
| AUDIO_LSSL_RESULT_S                | 均匀线阵声源定位返回结果                             |
| RESULT_S                           | EQ ASLC RES返回结果                                  |
| AUDIO_EFFECT_RESULT_S              | 音效处理返回结果                                     |
| AUDIO_AIKWS_RESULT_S               | 关键词识别返回结果                                   |
| AUDIO_AIKWSASR_RESULT_S            | 关键词识别ASR返回结果                                |

<br/>

### 函数接口列表

| **函数接口**                         | **描述**                                                     |
| ------------------------------------ | ------------------------------------------------------------ |
| AK_MPI_AUDIO_EFFECT_GetVersion       | 获取模块的版本号。                                           |
| AK_MPI_AUDIO_EFFECT_GetFilterVersion | 获取libakaudiofilter库版本号。                               |
| AK_MPI_AUDIO_EFFECT_Register         | 注册音效处理的API。                                          |
| AK_MPI_AUDIO_EFFECT_Init             | 初始化音频效果处理。                                         |
| AK_MPI_AUDIO_EFFECT_DeInit           | 析构音频效果处理。                                           |
| AK_MPI_AUDIO_EFFECT_Process          | 对输入的音频源数据进行音效处理，输出处理后的音频数据或者对音频数据进行检测，输出检测结果。 |
| AK_MPI_AUDIO_EFFECT_SetLibPrintLevel | 设置libaudiofilter在audio effect模块中的打印优先级           |
| AK_MPI_AUDIO_EFFECT_SetAttr          | 设置音频效果参数                                             |
| AK_MPI_AUDIO_EFFECT_GetAttr          | 获取音频效果参数                                             |

<br/>

### 错误码

AUDIO_EFFECT_ERROR_TYPE_E

| 错误码                                                       | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR<br />= (MODULE_ID_AUDIO_EFFECT << 24) + 0 | 打开filter库失败     |
| ERROR_AUDIO_EFFECT_LIB_ERROR                                 | 调用filter接口时失败 |
| ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR                          | 输出buf的长度错误    |
| ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE                         | VAD TPYE类型不匹配   |
| ERROR_AUDIO_EFFECT_RESULT_NO_RETURN                          | 没有结果返回         |

## 结构体和枚举类型说明

### AUDIO_EFFECT_ERROR_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;AUDIO EFFECT的错误码

&emsp;&emsp;【定义】

```c
enum akAUDIO_EFFECT_ERROR_TYPE_E
{
    ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR = (MODULE_ID_AUDIO_EFFECT << 24) + 0,
    ERROR_AUDIO_EFFECT_LIB_ERROR,
    ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR,
    ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE,
    ERROR_AUDIO_EFFECT_RESULT_NO_RETURN,
} AUDIO_EFFECT_ERROR_TYPE_E;
```

【成员】

| **成员名称**                         | **描述**                    |
| ------------------------------------ | --------------------------- |
| ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR    | 打开filter库时出错          |
| ERROR_AUDIO_EFFECT_LIB_ERROR         | 调用filter库接口时出错      |
| ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR  | 传入的outbuf的长度错误      |
| ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE | 设置的VAD类型参数没有匹配的 |
| ERROR_AUDIO_EFFECT_RESULT_NO_RETURN  | 没有结果返回                |

&emsp;&emsp;【相关函数接口】

<br/>

### AUDIO_EFFECT_USER_MAX_NUM

&emsp;&emsp;【说明】

&emsp;&emsp;AUDIO EFFECT通道数量的最大值。

&emsp;&emsp;【定义】

```c
#define     AUDIO_EFFECT_USER_MAX_NUM   10
```

<br/>

### AUDIO_EFFECT_USER_MAX_NUM

&emsp;&emsp;【说明】

&emsp;&emsp;音效处理最多支持麦克风

&emsp;&emsp;【定义】

```c
#define     FILTER_ALGORITHM_MAX_MIC_NUM   4
```

<br/>

### **AUDIO_DATA_ATTR_S**

&emsp;&emsp;【说明】

&emsp;&emsp;音频基本属性。

&emsp;&emsp;【定义】

```c
    typedef struct akAUDIO_DATA_ATTR_S
    {
        AUDIO_SAMPLE_RATE_E 		enSampleRate;
        AUDIO_SAMPLE_BIT_E  		enSampleBits;
        AUDIO_SOUND_MODE_E  		enSoundMode;
    } AUDIO_DATA_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**     |
| ------------ | ------------ |
| enSampleRate | 音频采样率   |
| enSampleBits | 音频采样精度 |
| enSoundMode  | 音频声道数   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

<br/>

### AUDIO_EFFECT_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;音效处理类型。

&emsp;&emsp;【定义】

```c
	typedef enum akAUDIO_EFFECT_TYPE_E
	{
        AK_AUDIO_RESAMPLE = 0,
        AK_AUDIO_VAD,
        AK_AUDIO_CRY,
        AK_AUDIO_ASLC,
        AK_AUDIO_EQ,
        AK_AUDIO_AI_CRY,
		AK_AUDIO_SSL,
		AK_AUDIO_LSSL,
		AK_AUDIO_AI_KWS,
        AK_AUDIO_AI_KWSASR,
        AK_AUDIO_TYPE_NUM,
	} AUDIO_EFFECT_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称**       | **描述**                                     |
| ------------------ | -------------------------------------------- |
| AK_AUDIO_RESAMPLE  | 重采样音效类型ID                             |
| AK_AUDIO_VAD       | 音量检测类型ID                               |
| AK_AUDIO_CRY       | 纯软件算法方式哭声检测类型ID                 |
| AK_AUDIO_ASLC      | 数字音量放大类型ID                           |
| AK_AUDIO_EQ        | 音频均衡器类型ID                             |
| AK_AUDIO_AI_CRY    | NPU方式哭声检测类型ID  (目前只支持16K采样率) |
| AK_AUDIO_SSL       | 声源定位类型ID                               |
| AK_AUDIO_LSSL      | 均匀线阵声源定位ID                           |
| AK_AUDIO_AI_KWS    | 关键词识别ID                                 |
| AK_AUDIO_AI_KWSASR | 关键词识别ASR ID                                 |
| AK_AUDIO_TYPE_NUM  | 音效处理类型总数                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

<br/>

### AUDIO_EFFECT_REG_S

&emsp;&emsp;【说明】

&emsp;&emsp;注册音效模块。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_EFFECT_REG_S {
    AUDIO_EFFECT_TYPE_E enEffectType;

    AK_VOID* (*EffectOpen)(
        AK_VOID             *pstOpenArg,
        AK_VOID             *pstEffectAttr
    );

    AK_S32 (*EffectClose)(AK_VOID *pstEffectHandle);

    AK_S32 (*EffectProcess)(
        AK_VOID             *pstEffectHandle,
        AK_VOID             *pstProcArg
    );
} AUDIO_EFFECT_REG_S;

```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                              |
| ------------- | ------------------------------------- |
| enEffectType  | 音频效果类型，参考AUDIO_EFFECT_TYPE_E |
| EffectOpen    | open回调函数，参考子库的h文件         |
| EffectClose   | close回调函数，参考子库的h文件        |
| EffectProcess | 音效处理回调函数，参考子库的h文件     |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Register(AUDIO_EFFECT_REG_S *pstAudioEffect);

```

​	</br>

### AUDIO_SSL_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;声源定位属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_SSL_ATTR_S {
    AK_U16                  u16FrameSize;   // frame size in bytes
    AK_U16                  u16Reserve1;//u16SoundSpeed;  // speed of sound // Notice: no use
    AK_U32                  u32Reserve2;//u32SrcNum;      // number of sound sources  // Notice: no use
    ARRAY_GEOMETRY_S        stArrayGeometry;
    AK_S32                  s32Reserve3;
} AUDIO_SSL_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述** |
| --------------- | -------- |
| u16FrameSize    | 帧大小   |
| u16Reserve1     | 预留参数 |
| u32Reserve2     | 预留参数 |
| stArrayGeometry | 多麦位置 |
| s32Reserve3     | 预留参数 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

</br>

### AUDIO_LSSL_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;均匀线性声源定位属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_LSSL_ATTR_S {
    AK_U16                  u16FrameSize;   // frame size in bytes
    AK_U16                  u16Reserve;//u16SoundSpeed;  // speed of sound   // Notice: no use
    AK_U16                  u16NumMic;      // number of mic
    AK_U16                  u16MicSpace;
    AK_S32                  s32Thresh;
    AK_S32                  s32Level;
    AK_S32                  s32Reserve;
} AUDIO_LSSL_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**          |
| --------------- | ----------------- |
| u16FrameSize    | 帧大小            |
| u16Reserve      | 预留参数          |
| u16NumMic       | 麦克风数量        |
| stArrayGeometry | 多麦位置          |
| u16MicSpace     | 麦之间的距离      |
| s32Thresh       | 阈值[0.00 , 1.00] |
| s32Level        | 敏感度等级[0,4]   |
| s32Reserve      | 预留参数          |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

</br>

### AUDIO_AI_KWS_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;关键词识别属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AI_KWS_ATTR_S {
    AK_U32                  u32AiKwsEna;     // enable AI keyword spotting
    AK_U16                  u16frameShift;   // 帧步进长度 samples. 0: use default
    AK_U16                  u16frameSize;    // 帧长度     samples. 0: use default
    AK_U16                  u16FftSize;      // FFT 长度   samples. 0: use default
    AK_U16                  u16Frames;
    AK_U16                  u16Bands;
    AK_U16                  s16Reserve;
    AK_S8                   *ps8ModelName;  // AI关键词检测模型名称 0:    use default "model_aikws"
    AK_S32                  s32Reserve;
} AUDIO_AI_KWS_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**             |
| ------------- | -------------------- |
| u32AiKwsEna   | 关键词识别长度       |
| u16frameShift | 帧步进长度           |
| u16frameSize  | 帧长度               |
| u16FftSize    | FFT 长度             |
| u16Frames     | 保留参数             |
| u16Bands      | 保留参数             |
| s16Reserve    | 预留参数             |
| ps8ModelName  | AI关键词检测模型名称 |
| s32Reserve    | 预留参数             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

</br>

### AUDIO_AI_KWS_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;关键词识别属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AI_KWSASR_ATTR_S {
    AK_U32                  u32AiKwsAsrEna;   // enable AI keyword spotting ASR
    AK_U16                  u16frameShift;   // 帧步进长度 samples. 0: use default
    AK_U16                  u16frameSize;    // 帧长度     samples. 0: use default
    AK_U16                  u16FftSize;      // FFT 长度   samples. 0: use default
    AK_U16                  u16Frames;
    AK_U16                  u16Bands;
    AK_U16                  s16Reserve;
    AK_S8                   *ps8ModelName;  // AI关键词检测模型名称 0:    use default "model_aikws"
    AK_S32                  s32Reserve;
} AUDIO_AI_KWSASR_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**             |
| -------------- | -------------------- |
| u32AiKwsAsrEna | 关键词识别ASR长度       |
| u16frameShift  | 帧步进长度           |
| u16frameSize   | 帧长度               |
| u16FftSize     | FFT 长度             |
| u16Frames      | 保留参数             |
| u16Bands       | 保留参数             |
| s16Reserve     | 预留参数             |
| ps8ModelName   | AI关键词检测模型名称 |
| s32Reserve     | 预留参数             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

​	</br>

### AUDIO_AI_CRY_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;AI算法哭声检测属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AI_CRY_ATTR_S {
    AK_U16          u16FrameSize;    // samples. 0: use default
    AK_U16          u16FrameShift;   // samples. 0: use default
    AK_U16          u16FftSize;      // samples. 0: use default
    AK_U16          u16NBands;       // 0: use default
    AK_U16          u16NFrames;      // 0: use default
    AK_U32          u32LowFreq;      // 0: use default
    AK_U32          u32HighFreq;     // 0: use default
    AK_S8           *ps8ModelName;   // 0: use default mobilenetv1_aicrydet_opt
    AK_S32          s32Reserve;      //
    AK_U32          u32Probe;        // probe flag
    AK_S32          s32Reserve1;
    AK_S32          s32Level;        //cry detect level [0-5], 0: use default level 0
} AUDIO_AI_CRY_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                |
| ------------- | ----------------------- |
| u16FrameSize  | 保留参数 0: use default |
| u16FrameShift | 保留参数 0: use default |
| u16FftSize    | 保留参数 0: use default |
| u16NBands     | 保留参数 0: use default |
| u16NFrames    | 保留参数 0: use default |
| u32LowFreq    | 保留参数 0: use default |
| u32HighFreq   | 保留参数 0: use default |
| ps8ModelName  | 哭声检测模型名称        |
| s32Reserve    | 预留参数                |
| u32Probe      | 保留参数                |
| s32Reserve1   | 保留参数 0: use default |
| s32Level      | 检测等级[0-5]默认为0    |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

​	</br>

### AUDIO_CRY_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;传统哭声检测算法属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_CRY_ATTR_S {
    AK_S32          s32Reserve1;
    AK_S32          s32CryThresh;
    AK_S32          s32CryLevel;
    AK_S32          s32Reserve2;
} AUDIO_CRY_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**   |
| ------------ | ---------- |
| s32Reserve1  | 预留参数   |
| s32CryThresh | 阈值设置   |
| s32CryLevel  | 敏感度等级 |
| s32Reserve2  | 预留参数   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

​	</br>

### AUDIO_VAD_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;音量检测属性参数。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_VAD_ATTR_S {
    AK_S32          s32Reserve1;
    AK_U32          u32Probe;
    AK_S32          s32VadThresh; // threshold of signal amplitude. use the form of AK32Q15(x.xx) to set it
    AK_S32          s32VadLevel;  // sensitivity level.[0, 4],smaller is more sensible
    AK_S32          s32Reserve2;
} AUDIO_VAD_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                |
| ------------ | ----------------------- |
| s32Reserve1  | 预留参数                |
| u32Probe     | 保留参数 0: use default |
| s32VadThresh | 阈值设置[0.00 ,1.00]    |
| s32VadLevel  | 敏感度等级[0,4]         |
| s32Reserve2  | 预留参数                |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【注意】

目前该相关函数接口暂不支持配置此参数。

​	</br>

### AUDIO_EFFECT_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;AUDIO_EFFECT处理结果。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_EFFECT_RESULT_S {
    AUDIO_EFFECT_TYPE_E                         u32EffectType;
    /* sizeof(AUDIO_EFFECT_DATA_PROCESS_RESULT_S) / sizeof(AUDIO_XXX_RESULT_S) */
    AK_U32                                      u32UnionBufSize;
    RESULT_S                                    unEffectResult;
} AUDIO_EFFECT_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**    | **描述**                                                     |
| --------------- | ------------------------------------------------------------ |
| u32EffectType   | 必填项，AUDIO_EFFECT_TYPE_E                                  |
| u32UnionBufSize | 必填项，对应的共用体的长度。<br />例如，VAD则是填入sizeof(AUDIO_VAD_RESULT_S),在解析具体结果时，也要注意转成VAD的共用体来获取。 |
| unEffectResult  | 数据处理类和检测类处理结果的共用体                           |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_EFFECT_DATA_PROCESS_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;RES/ASLC/EQ等数据处理类的处理结果

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_EFFECT_DATA_PROCESS_RESULT_S
{
    AK_U8           *pu8OutBuf;
    AK_U32          u32OutDataLen;
    AK_S32          s32Reserve;
} AUDIO_EFFECT_DATA_PROCESS_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**           |
| ------------- | ------------------ |
| pu8OutBuf     | 处理后数据的首地址 |
| u32OutDataLen | 处理后数据的长度   |
| s32Reserve    | 保留项             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_VAD_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;音量检测结果。

&emsp;&emsp;【定义】

```c
/* vad result output*/
typedef struct akAUDIO_VAD_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_VAD_RESULT_S;

```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | 音量检测到的结果在输入帧的多少时间处 |
| s32Reserve    | 音量检测的详细检测结果，目前不支持   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_CRY_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;基于传统算法的哭声检测结果。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_CRY_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_CRY_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | 哭声检测到的结果在输入帧的多少时间处 |
| s32Reserve    | 保留                                 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AI_CRY_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;基于NPU方式的音量检测结果。

&emsp;&emsp;【定义】

```c
/* AI cry result output*/
typedef struct akAUDIO_AICRY_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_AICRY_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | 哭声检测到的结果在输入帧的多少时间处 |
| s32Reserve    | 保留                                 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_SSL_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;声源定位输出结果。

&emsp;&emsp;【定义】

```c
/* SSL result output*/
typedef struct akAUDIO_SSL_RESULT_S {
    AK_U64                      u64TimeOffset;
    AK_U32                      u32SrcNum;      // number of sound sources
    SOUND_SPHERICAL_DIRECTION   *pastSndSrcDir;
    AK_S32                      s32Reserve;
} AUDIO_SSL_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                         |
| ------------------------- | -------------------------------- |
| u64TimeOffset             | 检测到的结果在输入帧的多少时间处 |
| u32SrcNum                 | 声源数                           |
| SOUND_SPHERICAL_DIRECTION | 参考SOUND_SPHERICAL_DIRECTION    |
| s32Reserve                | 保留                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_LSSL_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;均匀线阵声源定位输出结果。

&emsp;&emsp;【定义】

```c
/* SSL result output*/
typedef struct akAUDIO_LSSL_RESULT_S {
    AK_U64                      u64TimeOffset;
    AK_U32                      u32SrcNum;      // number of sound sources
    SOUND_SPHERICAL_DIRECTION   *pastSndSrcDir;
    AK_S32                      s32Reserve;
} AUDIO_LSSL_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**              | **描述**                         |
| ------------------------- | -------------------------------- |
| u64TimeOffset             | 检测到的结果在输入帧的多少时间处 |
| u32SrcNum                 | 声源数                           |
| SOUND_SPHERICAL_DIRECTION | 参考SOUND_SPHERICAL_DIRECTION    |
| s32Reserve                | 保留                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWS_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;关键词识别输出结果。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AIKWS_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S16          s16ProbValue;
} AUDIO_AIKWS_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**  | **描述**                         |
| ------------- | -------------------------------- |
| u64TimeOffset | 检测到的结果在输入帧的多少时间处 |
| s16ProbValue  | 识别关键字序号                   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWSASR_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;关键词识别输出结果。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AIKWSASR_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S16          s16ProbValue;
    AK_S16          s16KeyWordResult;
} AUDIO_AIKWSASR_RESULT_S;
```

&emsp;&emsp;【成员】

|   **成员名称**    | **描述**                         |
| ----------------- | -------------------------------- |
| u64TimeOffset     | 检测到的结果在输入帧的多少时间处    |
| s16ProbValue      | 识别关键字序号                    |
| s16KeyWordResult  | 识别到的特定关键字的ID             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_VAD_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;&emsp;音量检测输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_VAD_RESULT_LIST_S {
    AUDIO_VAD_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_VAD_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                         |
| ------------ | -------------------------------- |
| stResult     | 输出结果，参考AUDIO_VAD_RESULT_S |
| next         | 链表                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_CRY_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;&emsp;哭声输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_CRY_RESULT_LIST_S {
    AUDIO_CRY_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_CRY_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                         |
| ------------ | -------------------------------- |
| stResult     | 输出结果，参考AUDIO_CRY_RESULT_S |
| next         | 链表                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AICRY_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;&emsp;AI哭声输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AICRY_RESULT_LIST_S {
    AUDIO_AICRY_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_AICRY_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                           |
| ------------ | ---------------------------------- |
| stResult     | 输出结果，参考AUDIO_AICRY_RESULT_S |
| next         | 链表                               |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_SSL_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;&emsp;声源定位结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_SSL_RESULT_LIST_S {
    AUDIO_SSL_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_SSL_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                         |
| ------------ | -------------------------------- |
| stResult     | 输出结果，参考AUDIO_SSL_RESULT_S |
| next         | 链表                             |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_LSSL_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;均匀线阵声源定位输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_LSSL_RESULT_S {
    AUDIO_LSSL_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_LSSL_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                          |
| ------------ | --------------------------------- |
| stResult     | 输出结果，参考AUDIO_LSSL_RESULT_S |
| next         | 链表                              |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWS_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;关键字识别输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AIKWS_RESULT_LIST_S {
    AUDIO_AIKWS_RESULT_S    *stResult;
    SLList                  *next;
} AUDIO_AIKWS_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                           |
| ------------ | ---------------------------------- |
| stResult     | 输出结果，参考AUDIO_AIKWS_RESULT_S |
| next         | 链表                               |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWSASR_RESULT_LIST_S

&emsp;&emsp;【说明】

&emsp;关键字ASR识别输出结果链表。

&emsp;&emsp;【定义】

```c
typedef struct akAUDIO_AIKWSASR_RESULT_LIST_S {
    AUDIO_AIKWSASR_RESULT_S    *stResult;
    SLList                  *next;
} AUDIO_AIKWSASR_RESULT_LIST_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                             |
| ------------ | ------------------------------------ |
| stResult     | 输出结果，参考AUDIO_AIKWSASR_RESULT_S |
| next         | 链表                                 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;RES EQ ASLC输出结果。

&emsp;&emsp;【定义】

```c
typedef union akRESULT_S {
    AUDIO_EFFECT_DATA_PROCESS_RESULT_S      stDataProcessResult;// RES / ASLC / EQ
    void                                    *pstDetResult;      // detect result list
} RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称**                       | **描述**                                         |
| ---------------------------------- | ------------------------------------------------ |
| AUDIO_EFFECT_DATA_PROCESS_RESULT_S | 输出结果，参考AUDIO_EFFECT_DATA_PROCESS_RESULT_S |
| pstDetResult                       | 检测类结果输出                                   |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

>**注意：**
>
>pstDetResult是内部分配内部释放的变量，如果用户记录了pstDetResult的指针地址，请保证在AK_MPI_AUDIO_EFFECT_DeInit之后不会对pstDetResult进行调用，否则会造成指针地址错误的问题。

<br/>

## 版本信息获取

### AK_MPI_AUDIO_EFFECT_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取模块的版本号。

&emsp;&emsp;【语法】

```c
const AK_CHAR* AK_MPI_AUDIO_EFFECT_GetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| 模块版本号 | 成功     |
| NULL       | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_AUDIO_EFFECT_GetFilterVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取libakaudiofilter库版本号。

&emsp;&emsp;【语法】

```c
AK_CHAR* AK_MPI_AUDIO_EFFECT_GetFilterVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**               | **描述** |
| ------------------------ | -------- |
| libakaudiofilter库版本号 | 成功     |
| NULL                     | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 注册模块

### AK_MPI_AUDIO_EFFECT_Register

&emsp;&emsp;【描述】

&emsp;&emsp;注册音效处理的API。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Register(AUDIO_EFFECT_REG_S *pstAudioEffect);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**             | **取值范围**           | **输入/输出** |
| -------------- | -------------------- | ---------------------- | ------------- |
| pstAudioEffect | 配置音效处理回调函数 | 参考AUDIO_EFFECT_REG_S | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ---------- | ------------ |
| 0          | 成功         |
| 其他       | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**          | **描述**               |
| ------------------- | ---------------------- |
| ERROR_VQE_USER_NULL | 用户指针为空           |
| ERROR_VQE_NO_USER   | 当前无用户             |
| ERROR_VQE_LIB_ERROR | 关闭声音质量增强库错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;请参见AK_MPI_AUDIO_EFFECT_Init举例。

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;无

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 初始化模块

### **AK_MPI_AUDIO_EFFECT_Init**

&emsp;&emsp;【描述】

&emsp;&emsp;初始化音频效果处理。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

&emsp;&emsp;【参数】

| **参数名称**    | **描述**           | **取值范围**                                                 | **输入/输出** |
| --------------- | ------------------ | ------------------------------------------------------------ | ------------- |
|                  |                    |                                |               |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1]                               | 输入          |
| pstAudioDataAttr | 音频基本属性 | 参考AUDIO_DATA_ATTR_S | 输入 |
| enEffectType    | 音频效果类型       | 参考AUDIO_EFFECT_TYPE_E                                      | 输入          |
| pchFile          | 音频配置文件名     | 非空 | 输入          |
| pchSection       | 音频配置项         | 非空 | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**       |
| ---------- | -------------- |
| 0          | 成功。         |
| 其他       | 请参考错误码。 |

&emsp;&emsp;【错误码】

| **错误码**              | **描述**     |
| ----------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL | 参数指针为空 |
| ERROR_TYPE_INVALID_ARG  | 参数不正确   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_ai.so、libakaudiofilter.so、libplat_vqe.so或者libplat_ai.a、	libakaudiofilter.a、libplat_vqe.a

&emsp;&emsp;头文件：ak_ai.h

&emsp;&emsp;【接口配对关系】

```C
    AK_S32 AK_MPI_AUDIO_EFFECT_DeInit(AK_S32 s32EffectUserId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

## 销毁模块

### AK_MPI_AUDIO_EFFECT_DeInit

&emsp;&emsp;【描述】

&emsp;&emsp;析构音频效果处理。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_DeInit(AK_S32 s32EffectUserId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**      | **取值范围** | **输入/输出** |
| ------------ | ------------- | ------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ---------- | ------------ |
| 0          | 成功         |
| 其他       | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**          | **描述**               |
| ------------------- | ---------------------- |
| ERROR_VQE_USER_NULL | 用户指针为空           |
| ERROR_VQE_NO_USER   | 当前无用户             |
| ERROR_VQE_LIB_ERROR | 关闭声音质量增强库错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;请参见AK_MPI_AUDIO_EFFECT_Init举例。

&emsp;&emsp;【接口配对关系】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 处理或检测数据

### AK_MPI_AUDIO_EFFECT_Process

&emsp;&emsp;【描述】

&emsp;&emsp;对输入的音频源数据进行音效处理，输出处理后的音频数据或者对音频数据进行检测，输出检测结果。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Process(AK_S32 s32EffectUserId,
                              AK_U8 *pu8InBuf, AK_U32 u32InDataLen,
                              AUDIO_EFFECT_RESULT_S   *pstEffectResult);
```

&emsp;&emsp;【参数】

| **参数名称**   | **描述**           | **取值范围** | **输入/输出** |
| -------------- | ------------------ | ------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |
| pu8InBuf       | 输入数据的地址指针 | 非空         | 输入          |
| u32InDataLen   | 输入数据的长度     | 大于0        | 输入          |
| pstEffectResult | 处理或检测的结果 | 详见AUDIO_EFFECT_RESULT_S | 输出          |

&emsp;&emsp;【返回值】

| **错误码**          | **描述**     |
| ------------------- | ------------ |
| ERROR_VQE_USER_NULL | 用户指针为空 |
| ERROR_VQE_NO_USER   | 当前无用户   |
| ERROR_VQE_LIB_ERROR | 声效库错误   |

在返回值为AK_SUCCESS后，还需要继续解析pstEffectResult。

对于RES/ASLC/EQ这类，也就是数据处理类，pstEffectResult中的unEffectResult要当做AUDIO_EFFECT_DATA_PROCESS_RESULT_S类型来解析

| AUDIO_EFFECT_DATA_PROCESS_RESULT_S 子项参数 | **描述**           |
| ------------------------------------------- | ------------------ |
| pu8OutBuf                                   | 数据处理后的首地址 |
| u32OutDataLen                               | 数据处理的长度     |
| s32Reserve                                  | 保留项             |

对于CRY/VAD/AI CRY这类，也就是检测类，pstEffectResult中的unEffectResult要当做对应的检测类返回值类型来解析，例如VAD，就要当做AUDIO_VAD_RESULT_LIST_S来解析。

【错误码】

| **错误码**                 | **描述**           |
| -------------------------- | ------------------ |
| ERROR_TYPE_INVALID_ARG     | 参数不正确         |
| ERROR_TYPE_MALLOC_FAILED   | Malloc 失败        |
| ERROR_TYPE_POINTER_NULL    | 参数为空           |
| ERROR_VQE_USER_NULL        | 用户指针为空       |
| ERROR_VQE_OUTBUF_LEN_ERROR | 输出buffer大小错误 |
| ERROR_VQE_LIB_ERROR        | 库运行错误         |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;请参见AK_MPI_AUDIO_EFFECT_Init举例。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

> **注意：**
>
> Process对不同音效和数据组织的支持
>
> |        | MONO | STEREO | QUEUE |
> | ------ | ---- | ------ | ----- |
> | RES    | YES  | YES    | NO    |
> | VAD    | YES  | NO     | NO    |
> | CRY    | YES  | NO     | NO    |
> | AI_CRY | YES  | NO     | NO    |
>
> 如果需要对STEREO和QUEUE的数据做VAD或CRY的处理，可将STEREO和QUEUE的数据，参考AI中的数据组织进行拆解，拆解成单路音频数据，多个单路混合成一路或不混合，然后使用process做处理。
>
> 另外，多麦阵列算法处理成一路音频数据后，也可以采用MONO方式经过process做VAD&CRY&AI_CRY处理

<br/>

### AK_MPI_AUDIO_EFFECT_Reset

&emsp;&emsp;【描述】

&emsp;&emsp;清除audio effect 内部缓存

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Reset(AK_S32 s32EffectUserId);
```

【参数】

| **参数名称**    | **描述**           | **取值范围**                   | **输入/输出** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |

&emsp;&emsp;【返回值】

| **返回值**                   | **描述**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG       | 错误参数                   |
| ERROR_AUDIO_EFFECT_LIB_ERROR | 音效处理内部库调用接口失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;AK_MPI_AUDIO_EFFECT_Process之后

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

​		【注意】

​		目前只支持音效处理类型为LSSL适用。

<br/>

## 设置参数

### AK_MPI_AUDIO_EFFECT_LoadConf

【描述】

&emsp;&emsp;从配置文件获取相关参数并设置。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_LoadConf(AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection);
```

【参数】

| **参数名称**    | **描述**           | **取值范围**                   | **输入/输出** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |
| enEffectType    | 音频效果类型       | 参考AUDIO_EFFECT_TYPE_E        | 输入          |
| pchFile         | 音频配置文件名     | 非空                           | 输入          |
| pchSection      | 音频配置项         | 非空                           | 输入          |

【返回值】

| **返回值**                   | **描述**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG       | 错误参数                   |
| ERROR_AUDIO_EFFECT_LIB_ERROR | 音效处理内部库调用接口失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;AK_MPI_AUDIO_EFFECT_Init之后

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

### AK_MPI_AUDIO_EFFECT_SetAttr

【描述】

&emsp;&emsp;设置音频效果参数。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr(AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr);
```

【参数】

| **参数名称**    | **描述**           | **取值范围**                   | **输入/输出** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |
| enEffectType    | 音频效果类型       | 参考AUDIO_EFFECT_TYPE_E        | 输入          |
| pstEffectAttr   | 音频效果配置参数   | 非空                           | 输入          |

【返回值】

| **返回值**                   | **描述**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG       | 错误参数                   |
| ERROR_AUDIO_EFFECT_LIB_ERROR | 音效处理内部库调用接口失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;AK_MPI_AUDIO_EFFECT_Init之后

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

​		【注意】

​		目前只支持音效处理类型eq aslc resample调用。

### AK_MPI_AUDIO_EFFECT_GetAttr

【描述】

&emsp;&emsp;获取音频效果参数。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);
```

【参数】

| **参数名称**    | **描述**           | **取值范围**                   | **输入/输出** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | 音频效果模块用户Id | [0, AUDIO_EFFECT_USER_NUM - 1] | 输入          |
| enEffectType    | 音频效果类型       | 参考AUDIO_EFFECT_TYPE_E        | 输入          |
| pstEffectAttr   | 音频效果配置参数   | 非空                           | 输出          |

【返回值】

| **返回值**                   | **描述**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG       | 错误参数                   |
| ERROR_AUDIO_EFFECT_LIB_ERROR | 音效处理内部库调用接口失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;AK_MPI_AUDIO_EFFECT_Init之后

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

​		【注意】

​		目前只支持音效处理类型eq aslc resample调用。

<br/>

## 调试模块

### AK_MPI_AUDIO_EFFECT_SetLibPrintLevel

&emsp;&emsp;【描述】

&emsp;&emsp;设置filter在audio effect模块的打印优先级。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

【参数】

| **参数名称**  | **描述**         | **取值范围**                                  | **输入/输出** |
| ------------- | ---------------- | --------------------------------------------- | ------------- |
| u32PrintLevel | 设置的打印优先级 | 参考ak_common_audio.h中的ATCLIB_PRINT_LEVEL_E | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------- | -------- |
| AK_SUCCESS | 成功     |
| AK_FAILED  | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_vqe.a、libakaudiofilter.a或者libplat_vqe.so、libakaudiofilter.so

&emsp;&emsp;头文件：ak_audio_effect.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

## 接口调用依赖关系说明

&emsp;&emsp;AUDIO_EFFECT模块对外提供的接口函数在调用时存在一定的依赖关系，如下表所示：

| **函数接口**                         | **描述**                               |
| ------------------------------------ | -------------------------------------- |
| AK_MPI_AUDIO_EFFECT_GetVersion       | 无依赖                                 |
| AK_MPI_AUDIO_EFFECT_GetFilterVersion | 无依赖                                 |
| AK_MPI_AUDIO_EFFECT_Register         | 在AK_MPI_AUDIO_EFFECT_Init之前调用     |
| AK_MPI_AUDIO_EFFECT_Init             | 在AK_MPI_AUDIO_EFFECT_Register之后调用 |
| AK_MPI_AUDIO_EFFECT_DeInit           | 在AK_MPI_AUDIO_EFFECT_Process之后调用  |
| AK_MPI_AUDIO_EFFECT_Reset            | 在AK_MPI_AUDIO_EFFECT_Process之后调用  |
| AK_MPI_AUDIO_EFFECT_Process          | 在AK_MPI_AUDIO_EFFECT_Init之后调用     |
| AK_MPI_AUDIO_EFFECT_SetLibPrintLevel | 无依赖                                 |
| AK_MPI_AUDIO_EFFECT_SetAttr          | 在AK_MPI_AUDIO_EFFECT_Init之前调用     |
| AK_MPI_AUDIO_EFFECT_GetAttr          | 在AK_MPI_AUDIO_EFFECT_Init之前调用     |

<br/>

## sample相关说明

### 1 vad sample命令和参数

运行此sample前，需要先insmod ak_pcm.ko，一般开启都会默认加载。

| 输入参数（短参） | 输入参数（长参）    | **输入参数说明**                                             |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| h                | help                | 打印帮助信息。                                               |
| s                | sample-rate         | 音频采样率，支持8000和16000采样率。                          |
| p                | path                | PCM文件保存路径，无需指定文件名，在文件路径末尾要带"/"符号， 例如路径可以配置为: /mnt/。 |
| t                | second              | 采集时间，以秒为单位。                                       |
| d                | device-type         | 设备类型,0:DEV_ADC,1:DEV_PDM,2:DEV_I2S0_AI。                 |
| f                | config-file         | 音频配置文件全路径。                                         |
| e                | config-section      | 音频配置文件section name， def_near：用于ai单麦克风；two_array_near：用于AI双麦克风; def_far：用于AO。 |
| i                | vad-config -section | vad配置文件section name                                      |

<br/>

### vad sample存储和文件命令

（1）sample输出的文件格式默认使用PCM格式。
（2）sample输出的文件默认存储到/mnt/目录下。
（3）sample输出的文件名默认使用yyyymmdd-ddmmss采样率通道数时长（ms）设备.pcm 。

### vad sample应用案例

ak_vad_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini -e def_near -i vad_1

<br/>

### 2 vqe sample命令和参数

| 输入参数（短参） | 输入参数（长参）         | **输入参数说明**                                             |
| ---------------- | ------------------------ | ------------------------------------------------------------ |
| h                | help                     | 打印帮助信息。                                               |
| s                | sample-rate              | 音频采样率，支持8000和16000采样率。                          |
| p                | path                     | PCM文件保存路径，无需指定文件名，在文件路径末尾要带"/"符号， 例如路径可以配置为: /mnt/。 |
| t                | second                   | 采集时间，以秒为单位。                                       |
| d                | device-type              | 设备类型,0:DEV_ADC,1:DEV_PDM,2:DEV_I2S0_AI。                 |
| f                | config-file              | 音频配置文件全路径。                                         |
| e                | config-section           | 音频配置文件section name， def_near：用于ai单麦克风；two_array_near：用于AI双麦克风; def_far：用于AO。 |
| r                | resample -config-section | resample 配置文件section name                                |
| a                | aslc-config -section     | aslc 配置文件section name                                    |
| q                | eq-config -section       | eq 配置文件section name                                      |
| v                | probe-mode               | 音量[-90~20db]                                               |

### vqe sample存储和文件命令

（1）sample输出的文件格式默认使用PCM格式。
（2）sample输出的文件默认存储到/mnt/目录下。
（3）sample输出的文件名默认使用yyyymmdd-ddmmss采样率通道数时长（ms）设备_vqe类型.pcm 。

### vqe sample应用案例

ak_vqe_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini   -e def_near -r res_1 -a aslc_1 -q eq_1 -v 10

###   3 ssl_sample  命令和参数

运行此sample前，需要先insmod ak_pcm.ko，一般开启都会默认加载。

| 输入参数（短参） | 输入参数（长参） | **输入参数说明**                                             |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| h                | help             | 打印帮助信息。                                               |
| s                | sample-rate      | 音频采样率，支持8000和16000采样率。                          |
| p                | path             | PCM文件保存路径，无需指定文件名，在文件路径末尾要带"/"符号， 例如路径可以配置为: /mnt/。 |
| t                | second           | 采集时间，以秒为单位。                                       |
| d                | device-type      | 设备类型,0:DEV_ADC,1:DEV_PDM,2:DEV_I2S0_AI。                 |
| f                | config-file      | 音频配置文件全路径。                                         |
| e                | config-section   | 音频配置文件section name， def_near：用于ai单麦克风；two_array_near：用于AI双麦克风; def_far：用于AO。 |

### ssl sample存储和文件命令

（1）sample输出的文件格式默认使用PCM格式。
（2）sample输出的文件默认存储到/mnt/目录下。
（3）sample输出的文件名默认使用yyyymmdd-ddmmss采样率通道数时长（ms）设备.pcm 。

### ssl sample应用案例

  ak_ssl_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini -e def_lssl

注意：

### 4 cry_sample  命令和参数

| 输入参数（短参） | 输入参数（长参）    | **输入参数说明**                                             |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| h                | help                | 打印帮助信息。                                               |
| s                | sample-rate         | 音频采样率，支持8000和16000采样率。                          |
| p                | path                | PCM文件保存路径，无需指定文件名，在文件路径末尾要带"/"符号， 例如路径可以配置为: /mnt/。 |
| t                | second              | 采集时间，以秒为单位。                                       |
| d                | device-type         | 设备类型,0:DEV_ADC,1:DEV_PDM,2:DEV_I2S0_AI。                 |
| f                | config-file         | 音频配置文件全路径。                                         |
| e                | config-section      | 音频配置文件section name， def_near：用于ai单麦克风；two_array_near：用于AI双麦克风; def_far：用于AO。 |
| c                | cry-config- section | cry 音频配置文件section name ai_cry_1:基于NPU 方式的哭声检测; cry_1:基于CPU 方式的哭声检测 |
| m                | detect-mode         | 0:纯软件算法方式检测哭声,1:NPU方式检测哭声                   |

### cry sample存储和文件命令

（1）sample输出的文件格式默认使用PCM格式。
（2）sample输出的文件默认存储到/mnt/目录下。
（3）sample输出的文件名默认使用yyyymmdd-ddmmss采样率通道数时长（ms）设备.pcm 。

### cry sample应用案例

ak_cry_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini  -e def_near  -m 1 -c ai_cry_1

注意：在ai_cry_1的section下，modelName需要模型的全路径。

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### var/platform/AUDIO_EFFECT/stat

| 参数                     | 说明                 |
| ------------------------ | -------------------- |
| AudioEffect_version      | 平台音效处理版本号   |
| filter_version           | filter版本号         |
| LineArraySsl_version     | 均匀线阵定位库版本号 |
| SoundLevelDetect_version | 音量检测库版本号     |
| AiCryDetect_version      | AI哭声检测版本号     |

### var/platform/VQE/stat

| 参数                        | 说明                               |
| --------------------------- | ---------------------------------- |
| vqe_version                 | 平台音效处理版本号                 |
| filter_version              | filter版本号                       |
| NearJitterBufLen            | ai jiterbuff 大小                  |
| NearSampleRate              | ai端的采样率                       |
| NearHwSampleRate            | 硬件采样率                         |
| NearSoundMode               | ai端的声道                         |
| NearSampleBits              | ai端的采样精度                     |
| NearSyncedInputs            | ai默认0                            |
| NearSyncBufLen              | ai和ao共同使用的buffe大小默认      |
| NearSyncCompensate          | ai默认170                          |
| NearVqe0_AslcLimit          | ai增幅限制                         |
| NearVqe0_Volume             | ai数字音量                         |
| NearVqe0_EqEnable           | aieq使能                           |
| NearVqe0_EqBandsNum         | aieq滤波个数                       |
| NearVqe0_EqPreGain          | aieq前项增益                       |
| NearVqe0_AgcEnable          | aiagc使能                          |
| NearVqe0_AgcLevel           | aiagc增益等级                      |
| NearVqe0_AgcMaxGain         | ai对动态调整增益设置放大倍数上限   |
| NearVqe0_AgcMinGain         | ai对动态调整增益设置放小倍数下限   |
| NearVqe0_NearSensitivity    | ai对近端声音的灵敏度               |
| NearVqe0_NrEnable           | ai降噪使能                         |
| NearVqe0_NoiseSuppressDb    | ai降噪强度                         |
| NearVqe0_AecEnable          | aec使能                            |
| NearVqe0_Tail               | 默认512                            |
| NearVqe0_FarBreakdownThresh | 半双工/全双工切换阈值范围          |
| NearVqe0_AudioOutDigiGain   | 输出端限幅                         |
| NearVqe0_AudioInDigiGain    | 输入端限幅                         |
| FarJitterBufLen             | ao jiterbuff 大小                  |
| FarSampleRate               | ao端的采样率                       |
| FarHwSampleRate             | 硬件采样率                         |
| FarSoundMode                | ao端的声道                         |
| FarSyncedInputs             | ao默认0                            |
| FarSyncBufLen               | ai和ao共同使用的buffe大小，用于aec |
| FarSyncCompensate           | 默认170                            |
| FarVqe0_AslcLimit           | ao增幅限制                         |
| FarVqe0_Volume              | ao数字音量                         |
| FarVqe0_EqEnable            | aoeq使能                           |
| FarVqe0_EqBandsNum          | aoeq滤波个数                       |
| FarVqe0_EqPreGain           | aoeq前项增益                       |
| FarVqe0_NrEnable            | ao降噪使能                         |
| FarVqe0_NoiseSuppressDb     | ao降噪强度                         |

<br/>

## 错误码说明

| 错误代码   | 宏定义                          | 含义               |
| ---------- | ------------------------------- | ------------------ |
| 0x2b000000 | ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR       | 打开库失败                  |
| 0x2b000001 | ERROR_AUDIO_EFFECT_LIB_ERROR            | 音效处理内部库调用接口失败  |
| 0x2b000002 | ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR     | 输出buf长度错误             |
| 0x2b000003 | ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE    | 声音类型不匹配              |
| 0x2b000004 | ERROR_AUDIO_EFFECT_RESULT_NO_RETURN     | 音效处理结果没有返回        |

<br/>
