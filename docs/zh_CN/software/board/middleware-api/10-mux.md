# 合成

## 概述

&emsp;&emsp;合成模块（MUX模块）主要负责把音频流数据和视频流（H264/H265/JPEG)数据合成为MP4格式或AVI格式的录像数据。

* **合成MP4、AVI文件支持的音频格式和视频格式组合如下：**

| 文件类型 | 视频格式           | 音频格式                   |
| ---- | -------------- | ---------------------- |
| MP4  | H264/H265      | AMR， AAC ，g711a/u      |
| AVI  | H264/H265/JPEG | MP3， AAC， g711a/u， PCM |

<br/>

## API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **数据结构**          | **描述**                          |
| ----------------- | ------------------------------- |
| MUX_CONF_S        | 媒体合成的输入参数                       |
| MUX_START_PARAM_S | 媒体合成开始时输入的参数                    |
| MUX_FILEINFO_S    | 合成文件视频文件修复后返回的视频信息              |
| MUX_STATUS_E      | 录像在录制的期间ak_mux_get_status返回的状态值 |
| MUX_NODE_E        | 录像在录制的时候产生的文件所定义的文件类型           |

<br/>

| **函数接口**                        | **描述**             |
| ------------------------------- | ------------------ |
| AK_MPI_MUX_Get_Version          | 打印合成模块的版本号         |
| AK_MPI_MUX_Open                 | 打开媒体合成库            |
| AK_MPI_MUX_Close                | 关闭媒体合成库            |
| AK_MPI_MUX_Start                | 合成开始，每次开始新录像即调用此接口 |
| AK_MPI_MUX_Stop                 | 合成停止               |
| AK_MPI_MUX_Add_Audio            | 合成添加音频             |
| AK_MPI_MUX_Add_Video            | 合成添加视频             |
| AK_MPI_MUX_Print_Runtime_Status | 打印MUX模块的debug信息    |
| AK_MPI_MUX_Fix_File             | 修复视频文件             |
| AK_MPI_MUX_Pause                | 暂停合成文件             |
| AK_MPI_MUX_Continue             | 继续合成文件             |
| AK_MPI_MUX_Get_Status           | 获取当前合成库状态          |

<br/>

## 数据结构

### MUX_CONF_S

&emsp;&emsp;【说明】

&emsp;&emsp;媒体合成的输入参数。

&emsp;&emsp;【定义】

```c
    typedef struct akMUX_CONF_S
    {
        /* video */
        VENC_OUTPUT_TYPE_E enVencOutputType;
        AK_U16 u16Width;
        AK_U16 u16Height;
        AK_U16 u16Fps;

        /* audio */
        AK_U8 u8CaptureAudio;
        enAudioType_E enAudioType;
        AUDIO_DATA_ATTR_S stAudioDataAttr;
        AK_S32 s32FrameLen;

        /* mux */
        MUX_TYPE_E enMuxType;
        MUX_DATA_DEST_E enMuxDataDest;
        AK_U32 u32RecordSec;
    }MUX_CONF_S;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**                               |
| ---------------- | ------------------------------------ |
| enVencOutputType | 视频的类型，参考VENC_OUTPUT_TYPE_E定义         |
| u16Width         | 图像的宽                                 |
| u16Height        | 图像的高                                 |
| u16Fps           | 图像帧率                                 |
| u8CaptureAudio   | 是否需要合成音频，0：不合成音频，1：合成音频              |
| enAudioType      | 音频类型，参考enum ak_enAudioType           |
| stAudioDataAttr  | 音频的属性，参考struct ak_audio_data_attr结构体 |
| s32FrameLen      | 音频数据的帧长度                             |
| enMuxType        | 合成的视频文件类型                            |
| enMuxDataDest    | 合成的视频文件存储类型                          |
| u32RecordSec     | 合成的视频文件时长                            |
| <br/>            |                                      |

### MUX_START_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;媒体合成开始时输入的参数。

&emsp;&emsp;【定义】

```c
    typedef struct akMUX_START_PARAM_S
    {
        AK_S8 *ps8FilePath;
        AK_S32 s32BuffRecord;
        AK_S8 *ps8BuffRecord;
        AK_S32 s32BuffIndex;
        AK_S8 *ps8BuffIndex;
    }MUX_START_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**            |
| ------------- | ----------------- |
| ps8FilePath   | 录像文件的全路径，包括路径和文件名 |
| s32BuffRecord | 录像内容写入缓存的长度       |
| ps8BuffRecord | 录像内容写入缓存的传入地址     |
| s32BuffIndex  | 录像索引写入缓存的长度       |
| ps8BuffIndex  | 录像索引写入缓存的传入地址     |

<br/>

> **注意**：ps8FilePath传入文件全路径即可，无需用户创建文件，MUX库会创建录像文件。

<br/>

### MUX_FILEINFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;合成文件视频文件修复后返回的视频信息

&emsp;&emsp;【定义】

```c
    typedef struct akMUX_FILEINFO_S
    {
        AK_U64 u64TotalMs ;
    }MUX_FILEINFO_S;
```

&emsp;&emsp;【成员】

| **成员名称**   | **描述**     |
| ---------- | ---------- |
| u64TotalMs | 录像文件修复后的时长 |

<br/>

### MUX_STATUS_E

&emsp;&emsp;【说明】

&emsp;&emsp;录像在录制的期间ak_mux_get_status返回的状态值

如果获取的状态值为下列状态值：

MUX_STATUS_SYSERR
MUX_STATUS_MEMFULL
MUX_STATUS_SYNERR

则说明当前合成 库无法恢复，请关闭当前的录像合成文件，重新开始新的录像合成。

&emsp;&emsp;【定义】

```c
typedef enum akMUX_STATUS_E
{
    MUX_STATUS_OPEN,
    MUX_STATUS_STOP,
    MUX_STATUS_DOING,
    MUX_STATUS_SYSERR,
    MUX_STATUS_MEMFULL,
    MUX_STATUS_SYNERR,
    MUX_STATUS_WAITING,
    MUX_STATUS_PAUSE,
    MUX_STATUS_NUM,
}MUX_STATUS_E;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                                                         |
| ------------------ | -------------------------------------------------------------- |
| MUX_STATUS_OPEN    | 调用AK_MPI_MUX_Start后未开始录制期间的媒体库的状态，为媒体库打开状态。                    |
| MUX_STATUS_STOP    | 调用AK_MPI_MUX_Stop后媒体库的状态，为媒体库停止状态。                             |
| MUX_STATUS_DOING   | 调用AK_MPI_MUX_Start后媒体库的状态，为媒体库合成过程中的正常状态。                      |
| MUX_STATUS_SYSERR  | 为媒体库出错状态，合成过程中出错一般返回该状态，                                       |
| MUX_STATUS_MEMFULL | 媒体库在合成过程中malloc内存失败或合成的媒体文件大小超过限制等情况会报该错误。                     |
| MUX_STATUS_SYNERR  | 为媒体库重新同步失败的状态。                                                 |
| MUX_STATUS_WAITING | 为媒体库等待状态。                                                      |
| MUX_STATUS_PAUSE   | 调用ak_mux_pause后媒体库的状态，为媒体库暂停状态。暂停后若想继续合成，应调用ak_mux_continue接口。 |
| MUX_STATUS_NUM     | 合成媒体库的状态数量                                                     |

<br/>

### MUX_NODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;录像在录制的时候产生的文件所定义的文件类型

&emsp;&emsp;【定义】

```c
    typedef enum akMUX_NODE_E {
        MUX_NODE_RECORD = 0x00,
        MUX_NODE_IDX,
        MUX_NODE_MP4_MOOV,
        MUX_NODE_MP4_STBL,
        MUX_NODE_NUM
    }MUX_NODE_E;
```

&emsp;&emsp;【成员】

| **成员名称**          | **描述**             |
| ----------------- | ------------------ |
| MUX_NODE_RECORD   | 录像文件内容的写入          |
| MUX_NODE_IDX      | 录像索引信息写入           |
| MUX_NODE_MP4_MOOV | MP4文件格式录像的MOOV信息写入 |
| MUX_NODE_MP4_STBL | MP4文件格式录像的STBL信息写入 |
| MUX_NODE_NUM      | 录像期间产生的文件类型数       |

<br/>

## 版本信息获取

### AK_MPI_MUX_Get_Version

&emsp;&emsp;【描述】

&emsp;&emsp;打印合成模块的版本号。

&emsp;&emsp;【语法】

```c
    const AK_S8* AK_MPI_MUX_Get_Version(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 合成模块版本号 | 成功     |
| NULL    | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 打开/关闭模块

### AK_MPI_MUX_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开媒体合成库。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Open(const MUX_CONF_S *pstMuxParam, AK_S32 *s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围**              | **输入/输出** |
| -------------- | ------------------- | --------------------- | --------- |
| pstMuxParam    | 合成库输入参数             | 参考struct akMUX_CONF_S | 输入        |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3                   | 输出        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                         | **描述**    |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG          | 参数不合法     |
| ERROR_TYPE_MALLOC_FAILED        | Malloc 失败 |
| ERROR_TYPE_POINTER_NULL         | 参数为空      |
| ERROR_MUX_OPEN_TOO_MANY         | 用户数太多     |
| ERROR_MUX_SET_AUDIO_INPUT_ERROR | 合成音频的参数错误 |
| ERROR_MUX_SET_VIDEO_INPUT_ERROR | 合成视频的参数错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId, &stMuxStartParam );
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

```c
    int AK_MPI_MUX_Close(int s32MuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;调用AK_MPI_MUX_Open可以open多次，每次open相当于增加一个新的用户，但是最多支持打开4个用户。

<br/>

### AK_MPI_MUX_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭媒体合成库。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Close(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围** | **输入/输出** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**             | **描述** |
| ------------------- | ------ |
| ERROR_MUX_USER_NULL | 用户指针为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

```c
    int AK_MPI_MUX_Open(const struct akMUX_CONF_S *pstMuxParam, int *s32MuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;调用AK_MPI_MUX_Close可以多次关闭。关闭不存在mux_handle_id会报错。

<br/>

## 合成操作接口

### AK_MPI_MUX_Start

&emsp;&emsp;【描述】

&emsp;&emsp;合成开始，每次开始新录像即调用此接口。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Start(AK_S32 s32MuxHandleId, MUX_START_PARAM_S *pstStartParam);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围**                 | **输入/输出** |
| -------------- | ------------------- | ------------------------ | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3                      | 输入        |
| pstStartParam  | 开启合成路线时的输入参数        | 参考akMUX_START_PARAM_S结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ------- | ------- |
| 0       | 成功      |
| 其他      | 请参考错误码。 |

&emsp;&emsp;【错误码】

| **错误码**                      | **描述**    |
| ---------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG       | 参数不合法     |
| ERROR_TYPE_MALLOC_FAILED     | Malloc 失败 |
| ERROR_TYPE_POINTER_NULL      | 参数为空      |
| ERROR_MUX_OPEN_LIB_ERROR     | 打开合成库失败   |
| ERROR_MUX_GET_LIB_INFO_ERROR | 获取合成库信息失败 |
| ERROR_MUX_START_LIB_ERROR    | 开始合成失败    |
| ERROR_MUX_USER_NULL          | 用户指针为空    |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_MUX_Stop(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入，每次开始新录像即调用AK_MPI_MUX_Start，录像完成即调用AK_MPI_MUX_Stop。

<br/>

### AK_MPI_MUX_Stop

&emsp;&emsp;【描述】

&emsp;&emsp;合成停止。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Stop(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围** | **输入/输出** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3      | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                   | **描述**  |
| ------------------------- | ------- |
| ERROR_MUX_CLOSE_LIB_ERROR | 关闭合成库失败 |
| ERROR_MUX_STOP_LIB_ERROR  | 停止合成失败  |
| ERROR_MUX_USER_NULL       | 用户指针为空  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

```c
    AK_S32 AK_MPI_MUX_Start(AK_S32 s32MuxHandleId, MUX_START_PARAM_S *pstStartParam);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入，每次开始新录像即调用AK_MPI_MUX_Start，录像完成即调用AK_MPI_MUX_Stop。

<br/>

### AK_MPI_MUX_Add_Audio

&emsp;&emsp;【描述】

&emsp;&emsp;合成添加音频。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Add_Audio(AK_S32 s32MuxHandleId, const AUDIO_STREAM_S *pstAudioStream);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围**            | **输入/输出** |
| -------------- | ------------------- | ------------------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3                 | 输入        |
| pstAudioStream | 音频流数据               | 参考AUDIO_STREAM_S结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                         | **描述**    |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG          | 参数不合法     |
| ERROR_TYPE_POINTER_NULL         | 参数为空      |
| ERROR_MUX_USER_NULL             | 用户指针为空    |
| ERROR_MUX_SET_AUDIO_INPUT_ERROR | 合成音频的参数错误 |
| ERROR_MUX_ADD_ERROR             | 合成时出错     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libakmedia.a

&emsp;&emsp;头文件：media_demuxer_lib.h、medialib_global.h、medialib_struct.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;如果是解析录像文件，与以下接口配对使用：

```c
    AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

> **注意：**对于MP4合成格式，合成库中视频按时间戳分别保存了每帧的时长，而音频默认每帧的时长是相等的，所以在合成过程中，可以不需要保证持续有视频帧送到合成库，但是必须保证持续有音频帧送到合成库，如果合成库在合成过程中没有收到音频帧，可以尝试应用在合成过程中插入音频空帧（pcm数据为全零的帧送给编码器模块能够编码得到音频空帧），保证音频数据持续送入合成库。如果合成过程中音频帧有缺失，同时应用不插入音频空帧，则可能导致合成MP4音视频不同步。

<br/>

### AK_MPI_MUX_Add_Video

&emsp;&emsp;【描述】

&emsp;&emsp;合成添加视频。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Add_Video(AK_S32 s32MuxHandleId, const VIDEO_STREAM_S *pstVideoStream);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围**            | **输入/输出** |
| -------------- | ------------------- | ------------------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3                 | 输入        |
| pstVideoStream | 视频流数据               | 参考VIDEO_STREAM_S结构体 | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                         | **描述**    |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG          | 参数不合法     |
| ERROR_TYPE_POINTER_NULL         | 参数为空      |
| ERROR_MUX_USER_NULL             | 用户指针为空    |
| ERROR_MUX_SET_VIDEO_INPUT_ERROR | 合成视频的参数错误 |
| ERROR_MUX_ADD_ERROR             | 合成时出错     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;如果是解析录像文件，与以下接口配对使用：

```c
    AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

### AK_MPI_MUX_Pause

&emsp;&emsp;【描述】

&emsp;&emsp;在录制期间暂停录制

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_MUX_Pause(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围** | **输入/输出** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3      | 输入        |

&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| AK_SUCCESS | 成功     |
| AK_FAILED  | 失败     |

&emsp;&emsp;【错误码】

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId,mux_start_param);
    AK_MPI_MUX_Pause( s32MuxHandleId);
    AK_MPI_MUX_Continue( s32MuxHandleId );
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

AK_MPI_MUX_Continue

&emsp;&emsp;【接口重入性】
不支持重入

<br/>

### AK_MPI_MUX_Continue

&emsp;&emsp;【描述】

&emsp;&emsp;在录制期间重启录制，在重启录制的时候，第一帧视频帧必须为I帧。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_MUX_Continue(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**              | **取值范围** | **输入/输出** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | 媒体合成库open的handle ID | 0~3      | 输入        |

&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| AK_SUCCESS | 成功     |
| AK_FAILED  | 失败     |

&emsp;&emsp;【错误码】

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId,mux_start_param);
    AK_MPI_MUX_Pause( s32MuxHandleId);
    AK_MPI_MUX_Continue( s32MuxHandleId );
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口配对关系】

AK_MPI_MUX_Pause

&emsp;&emsp;【接口重入性】
不支持重入

<br/>

### AK_MPI_MUX_Fix_File

&emsp;&emsp;【描述】

&emsp;&emsp;修复因为断电等原因未完整保存的录像文件

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Fix_File( FILE *pFILERecord, FILE *pFILEIndex, FILE *pFILEMoov,
                                FILE *pFILEStbl, MUX_TYPE_E enMuxType, MUX_FILEINFO_S *pstMuxFileinfo );
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**          | **取值范围**                     | **输入/输出** |
| -------------- | --------------- | ---------------------------- | --------- |
| pFILERecord    | 打开录像文件的指针       | FILE指针                       | 输入        |
| pFILEIndex     | 打开AVI索引文件的指针    | FILE指针                       | 输入        |
| pFILEMoov      | 打开MP4 MOOV文件的指针 | FILE指针                       | 输入        |
| pFILEStbl      | 打开MP4 STBL文件的指针 | FILE指针                       | 输入        |
| enMuxType      | 录像文件类型          | MUX_TYPE_AVI \| MUX_TYPE_MP4 | 输入        |
| pstMuxFileinfo | 修复后返回的录像文件信息    | -                            | 输出        |

&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| AK_SUCCESS | 成功     |
| AK_FAILED  | 失败     |

&emsp;&emsp;【错误码】

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

与其他接口无依赖关系，一般在应用启动的时候调用。

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;【接口重入性】
不支持重入

<br/>

## debug接口

### AK_MPI_MUX_Print_Runtime_Status

&emsp;&emsp;【描述】

&emsp;&emsp;打印MUX模块的debug信息。会打印以下信息：

add_audio_count：添加音频的次数；

add_video_count：添加视频的次数；

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Print_Runtime_Status(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**    | **取值范围** | **输入/输出** |
| -------------- | --------- | -------- | --------- |
| s32MuxHandleId | MUX模块句柄ID | [0,3]    | 输入        |

&emsp;&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| AK_SUCCESS | 成功     |
| 其他         | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**             | **描述** |
| ------------------- | ------ |
| ERROR_MUX_USER_NULL | 参数为空   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Print_Runtime_Status(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入

<br/>

### AK_MPI_MUX_Get_Status

&emsp;&emsp;【描述】

&emsp;&emsp;获取MUX模块的合成媒体库当前状态。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_MUX_Get_Status(AK_S32 s32MuxHandleId, MUX_STATUS_E *penMuxStatus );
```

&emsp;&emsp;【参数】

| **参数名称**       | **描述**        | **取值范围**       | **输入/输出** |
| -------------- | ------------- | -------------- | --------- |
| s32MuxHandleId | MUX模块句柄ID     | [0,3]          | 输入        |
| penMuxStatus   | 用于返回当前合成媒体库状态 | akMUX_STATUS_E | 输出        |

&emsp;&emsp;【返回值】

| **返回值**    | **描述** |
| ---------- | ------ |
| AK_SUCCESS | 成功     |
| AK_FAILED  | 获取失败   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_mux.so、libakmedia.so或者libmpi_mux.a、libakmedia.a

&emsp;&emsp;头文件：ak_mux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Get_Status(s32MuxHandleId,penMuxStatus);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入

<br/>

## 接口调用依赖关系

&emsp;&emsp;MUX模块对外提供的接口函数在调用时存在一定的依赖关系，如下表所示：

| **接口**                          | **接口依赖关系**           |
| ------------------------------- | -------------------- |
| AK_MPI_MUX_Get_Version          | 无依赖                  |
| AK_MPI_MUX_Open                 | 开始时调用                |
| AK_MPI_MUX_Start                | AK_MPI_MUX_Open之后调用  |
| AK_MPI_MUX_Add_Audio            | AK_MPI_MUX_Start之后调用 |
| AK_MPI_MUX_Add_Video            | AK_MPI_MUX_Start之后调用 |
| AK_MPI_MUX_Stop                 | AK_MPI_MUX_Start之后调用 |
| AK_MPI_MUX_Get_Status           | AK_MPI_MUX_Start之后调用 |
| AK_MPI_MUX_Print_Runtime_Status | AK_MPI_MUX_Open之后调用  |
| AK_MPI_MUX_Close                | AK_MPI_MUX_Open之后调用  |
| <br/>                           |                      |

## ak_mux_sample使用示例

运行此sample前，需要先加载采集相关的驱动，包括ak_vi.ko、sensor_xxx.ko、ak_vicap.ko、ak_isp.ko、ak_pp.ko，一般是运行脚本，以GC5603的CIS为例，可以参考脚本gc5603.sh，具体命令如下：

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        其他CIS请参考对应的加载脚本xxx.sh。

还需要加载编码的驱动：ak_venc_adapter.ko和ak_venc_bridge.ko。命令如下：

​        insmod /usr/modules/ak_venc_adapter.ko

​        insmod /usr/modules/ak_venc_bridge.ko

| **输入参数**        | **输入参数说明**                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| path_save       | 录像保存路径                                                                                                                                           |
| record_sec      | 录像时长                                                                                                                                             |
| record_num      | 录像录制文件个数                                                                                                                                         |
| ai_sample_rate  | AI采样率 <br/>可选值: 8000,11025,12000,16000,22050,24000,32000,44100,48000                                                                             |
| vi_isp_cfg      | sensor的配置文件，需要指定完整路径。                                                                                                                            |
| vi_width        | vi分辨率宽                                                                                                                                           |
| vi_height       | vi分辨率高                                                                                                                                           |
| vi_channel      | vi通道id                                                                                                                                           |
| vi_fps          | vi帧率                                                                                                                                             |
| venc_goplen     | 视频编码I帧间隔                                                                                                                                         |
| aenc_type       | 音频编码格式<br/>AVI格式可选值:MP3:2, AAC:4, PCM:6,(g711a)PCM_ALAW:17, (g711u)PCM_ULAW:18<br/>mp4格式可选值:AMR:3, AAC:4, (g711a)PCM_ALAW:17, (g711u)PCM_ULAW:18 |
| venc_type       | venc编码类型 (可选值: 0,H264 1,JPEG 2,H265 )                                                                                                            |
| muxType         | 合成文件类型<br/>可选值: 0,MUX_TYPE_AVI 1,MUX_TYPE_MP4. JPEG编码格式仅仅支持AVI                                                                                   |
| path_template   | 目录模板,默认:%Y%M%D  <br/>可选值:%Y-年,%M-月,,%D-日,%h-时,%m-分,%s-秒,%S-录制长度ms                                                                                |
| file_template   | 文件模板,默认:%Y%M%D.%h%m%s.%S <br/>可选值:%Y-年,%M-月,,%D-日,%h-时,%m-分,%s-秒,%S-录制长度ms                                                                       |
| path_tmp        | 录像合成的暂存目录                                                                                                                                        |
| buff_video      | 待合成的视频缓存长度,默认2048k,0则不限制                                                                                                                         |
| buff_audio      | 待合成的音频缓存长度,默认128k,0则不限制                                                                                                                          |
| ai_frame_len    | 音频的帧长度                                                                                                                                           |
| vi_frame_depth  | 视频的采集buffer数量2-4                                                                                                                                 |
| ai_conf_file    | ai配置文件                                                                                                                                           |
| ai_conf_section | ai配置文件使用的配置小节                                                                                                                            |

<br/>

## 错误码说明

| 错误代码       | 宏定义                             | 含义       |
| ---------- | ------------------------------- | -------- |
| 0x12000000 | MUX_ERROR_OPEN_LIB_ERROR        | 打开库失败    |
| 0x12000001 | MUX_ERROR_CLOSE_LIB_ERROR       | 关闭库失败    |
| 0x12000002 | MUX_ERROR_GET_LIB_INFO_ERROR    | 获取库信息失败  |
| 0x12000003 | MUX_ERROR_START_LIB_ERROR       | 开启库失败    |
| 0x12000004 | MUX_ERROR_STOP_LIB_ERROR        | 停止库失败    |
| 0x12000005 | MUX_ERROR_OPEN_TOO_MANY         | 打开次数太多   |
| 0x12000006 | MUX_ERROR_USER_NULL             | 用户为空     |
| 0x12000007 | MUX_ERROR_SET_AUDIO_INPUT_ERROR | 合成音频参数错误 |
| 0x12000008 | MUX_ERROR_SET_VIDEO_INPUT_ERROR | 合成视频参数错误 |
| 0x12000009 | MUX_ERROR_ADD_ERROR             | 合成出错     |
| 0x1200000a | MUX_ERROR_ADD_VIDEO_FIRST       | 先合成视频    |
| 0x1200000b | MUX_ERROR_VALUE_INVAILD         | 数值无效     |

<br/>
