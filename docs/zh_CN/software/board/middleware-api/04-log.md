# 日志打印

## 概述

&emsp;&emsp;日志打印模块属于基础设施类模块，主要负责打印输出各模块及系统日志的记录。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示。

| **数据结构** | **描述** |
| ------------ | -------- |
| MODULE_ID_E  | 模块id号 |
| LOG_LEVEL_E  | 打印等级 |

<br/>

| **函数接口**        | **描述**         |
| ------------------------- | ---------------------- |
| AK_BASE_PrintGetVersion | 获取日志模块的版本信息 |
| AK_BASE_PrintError | 输出错误信息           |
| AK_BASE_PrintWarning | 输出告警信息           |
| AK_BASE_PrintNotice | 输出提示信息           |
| AK_BASE_PrintNormal | 输出正常日志信息       |
| AK_BASE_PrintInfo | 输出Info信息           |
| AK_BASE_PrintDebug | 输出debug信息          |
| AK_BASE_PrintErrorEx | 输出错误信息           |
| AK_BASE_PrintWarningEx | 输出告警信息           |
| AK_BASE_PrintNoticeEx | 输出提示信息           |
| AK_BASE_PrintNormalEx | 输出正常日志信息       |
| AK_BASE_PrintInfoEx | 输出Info信息           |
| AK_BASE_PrintDebugEx | 输出debug信息          |
| AK_BASE_PrintSetLevel | 设置日志模块的物理串口实时打印级别 |
| AK_BASE_PrintSetSyslogLevel | 设置系统日志的打印级别 |

<br/>

## 数据结构

### MODULE_ID_E

&emsp;&emsp;【说明】

&emsp;&emsp;模块id号。

&emsp;&emsp;【定义】

```c
typedef enum akMODULE_ID_E {
    MODULE_ID_MEMORY                 = 0x0,
    MODULE_ID_THREAD,
    MODULE_ID_LOG,
    MODULE_ID_COMMON,
    MODULE_ID_IPCSRV,
    MODULE_ID_AI,
    MODULE_ID_AO,
    MODULE_ID_VI,
    MODULE_ID_VO,
    MODULE_ID_TIMER,
    MODULE_ID_VPSS,
    MODULE_ID_DRV,
    MODULE_ID_TDE,
    MODULE_ID_VENC,
    MODULE_ID_VDEC,
    MODULE_ID_AENC,// 15
    MODULE_ID_ADEC,
    MODULE_ID_OSD,
    MODULE_ID_MUX,
    MODULE_ID_DEMUX,
    MODULE_ID_DVR,
    MODULE_ID_MD,
    MODULE_ID_GUI,
    MODULE_ID_AED,
    MODULE_ID_AUDIO_TOOL,

    MODULE_ID_VQE,

    MODULE_ID_APP_VIDEO,
    MODULE_ID_DVR_IDX,
    MODULE_ID_NET,
    MODULE_ID_OSAL,
    MODULE_ID_APP_MEM,
    MODULE_ID_APP_AUDIO,
    MODULE_ID_UUID,
    MODULE_ID_ATC_ECHO,
    MODULE_ID_ATC_ADEC,
    MODULE_ID_ATC_AENC,
    MODULE_ID_AKV_VENC,
    MODULE_ID_AKV_VDEC,
    MODULE_ID_AKV_MUX,
    MODULE_ID_AKV_DEMUX,
    MODULE_ID_SVP,
    MODULE_ID_AKV_CNN,
    MODULE_ID_FR,
    MODULE_ID_AUDIO_EFFECT,

    MODULE_ID_APP                     = 0xFE,
    MODULE_ID_ALL                     = 0xFF,
}MODULE_ID_E;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**             |
| ---------------------- | -------------------- |
| MODULE_ID_MEMORY       | 内存管理模块id       |
| MODULE_ID_THREAD       | 多线程操作模块id     |
| MODULE_ID_LOG          | 日志打印模块id       |
| MODULE_ID_COMMON       | 公共服务模块id       |
| MODULE_ID_IPCSRV       | 目前不使用           |
| MODULE_ID_AI           | 音频采集模块id       |
| MODULE_ID_AO           | 音频播放模块id       |
| MODULE_ID_VI           | 视频采集模块id       |
| MODULE_ID_VO           | 视频播放模块id       |
| MODULE_ID_TIMER        | 内部timer视频id      |
| MODULE_ID_VPSS         | 视频处理子系统模块id |
| MODULE_ID_DRV          | 驱动适配层id         |
| MODULE_ID_TDE          | 图像二维引擎模块id   |
| MODULE_ID_VENC         | 视频编码模块id       |
| MODULE_ID_VDEC         | 视频解码模块id       |
| MODULE_ID_AENC         | 音频编码模块id       |
| MODULE_ID_ADEC         | 音频解码模块id       |
| MODULE_ID_OSD          | 视频叠加显示模块id   |
| MODULE_ID_MUX          | 录像合成模块id       |
| MODULE_ID_DEMUX        | 录像解析模块id       |
| MODULE_ID_DVR          | 目前不使用           |
| MODULE_ID_MD           | 移动侦测模块id       |
| MODULE_ID_GUI          | 目前不使用           |
| MODULE_ID_AED          | rtsp模块id           |
| MODULE_ID_AUDIO_TOOL   | 音频调试工具模块id   |
| MODULE_ID_VQE          | 声音增强模块id       |
| MODULE_ID_APP_VIDEO    | 视频流模式id         |
| MODULE_ID_DVR_IDX      | 目前不使用           |
| MODULE_ID_NET          | 网络适配层模块id     |
| MODULE_ID_OSAL         | 中间件适配层模块id   |
| MODULE_ID_APP_MEM      | 内存管理扩展模块id   |
| MODULE_ID_APP_AUDIO    | 音频流模式模块id     |
| MODULE_ID_UUID         | 获取芯片唯一ID模块id |
| MODULE_ID_ATC_ECHO     | 回音消除库打印id     |
| MODULE_ID_ATC_ADEC     | ATC音频解码库打印id  |
| MODULE_ID_ATC_AENC     | ATC音频编码库打印id  |
| MODULE_ID_AKV_VENC     | ATC视频编码库打印id  |
| MODULE_ID_AKV_VDEC     | ATC视频解码库打印id  |
| MODULE_ID_AKV_MUX      | ATC录像合成库打印id  |
| MODULE_ID_AKV_DEMUX    | ATC录像解析库打印id  |
| MODULE_ID_SVP          | 智能视觉处理模块id   |
| MODULE_ID_AKV_CNN      | ATC CNN库打印id      |
| MODULE_ID_FR           | FR模块id             |
| MODULE_ID_AUDIO_EFFECT | 音效模块id           |
| MODULE_ID_APP          | 用户使用的打印id     |
| MODULE_ID_ALL          | 模块id最大值         |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_BASE_PrintError(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintWarning(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNotice(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNormal(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintInfo(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintDebug(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintErrorEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintWarningEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNoticeEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNormalEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintInfoEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintDebugEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
    AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

<br/>

### LOG_LEVEL_E

【说明】

打印等级。

【定义】

```c
typedef enum akLOG_LEVEL_E {
    LOG_LEVEL_RESERVED = 0,
    LOG_LEVEL_ERROR,
    LOG_LEVEL_WARNING,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_NORMAL,
    LOG_LEVEL_INFO,
    LOG_LEVEL_DEBUG,
}LOG_LEVEL_E;
```

【成员】

| **成员名称**       | **描述**     |
| ------------------ | ------------ |
| LOG_LEVEL_RESERVED | 预留等级     |
| LOG_LEVEL_ERROR    | 错误等级     |
| LOG_LEVEL_WARNING  | 警告等级     |
| LOG_LEVEL_NOTICE   | 告知等级     |
| LOG_LEVEL_NORMAL   | 正常等级     |
| LOG_LEVEL_INFO     | 打印信息等级 |
| LOG_LEVEL_DEBUG    | 查询错误等级 |

【相关函数接口】

```c
AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

<br/>

## 版本信息获取

### **AK_BASE_PrintGetVersion**

&emsp;&emsp;【描述】

&emsp;&emsp;获取日志模块的版本信息。

&emsp;&emsp;【语法】

```C
    const AK_CHAR* AK_BASE_PrintGetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述**         |
| ---------------- | ---------------------- |
| 返回日志模块的版本信息 | 成功。 |
| NULL | 失败。 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 分级打印输出

### **AK_BASE_PrintError**

&emsp;&emsp;【描述】

&emsp;&emsp;输出错误信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintError(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintWarning**

&emsp;&emsp;【描述】

&emsp;&emsp;输出告警信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintWarning(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0          | 成功           |
| 其他       | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintNotice**

&emsp;&emsp;【描述】

&emsp;&emsp;输出提示信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintNotice(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintNormal**

&emsp;&emsp;【描述】

&emsp;&emsp;输出正常日志信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintNormal(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintInfo**

&emsp;&emsp;【描述】

&emsp;&emsp;输出Info信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintInfo(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintDebug**

&emsp;&emsp;【描述】

&emsp;&emsp;输出debug信息。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintDebug(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**     | **取值范围** | **输入/输出** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintErrorEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出错误信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintErrorEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值**   | **描述**  |
| ------------ | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintWarningEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出告警信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintWarningEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值**   | **描述**  |
| ------------ | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintNoticeEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出提示信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintNoticeEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ---------- | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintNormalEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出正常日志信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintNormalEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ---------- | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintInfoEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出Info信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintInfoEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ---------- | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintDebugEx**

&emsp;&emsp;【描述】

&emsp;&emsp;输出debug信息。包括函数名和行数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintDebugEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**           | **取值范围** | **输入/输出** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | 调用此接口的模块ID | 参考enum module_id            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ---------- | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误 |
| ERROR_TYPE_MALLOC_FAILED | 申请内存失败 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 打印等级设置

### **AK_BASE_PrintSetLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;设置日志模块的物理串口实时打印等级。当配置了某个等级之后，小于等于此等级的打印都会打印出来。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述** | **取值范围** | **输入/输出** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| s32ModuleId | 待设置的模块ID | 参考enum module_id                  | 输入                                    |
| s32Level      | 打印级别       | 参考enum LOG_LEVEL                  | 输入                                    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误或者level输入值错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### **AK_BASE_PrintSetSyslogLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;设置保存到系统log：/var/log/messages的打印级别。当配置了某个等级之后，小于等于此等级的打印都会印保存于/var/log/messages中。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**       | **取值范围** | **输入/输出** |
| ------------ | -------------- | ------------ | ------------- |
| s32ModuleId | 待设置的模块ID | 参考enum module_id            | 输入          |
| s32Level | 打印级别       | 参考enum LOG_LEVEL            | 输入          |

&emsp;&emsp;【返回值】

| **返回值** | **描述**  |
| ---------- | --------- |
| 0    | 成功    |
| 其他 | 请参考错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码** | **描述** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | module_id输入值错误或者level输入值错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libplat_log.a或者libplat_log.so

&emsp;&emsp;头文件：ak_log.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

#### stat

| 参数    | 说明        |
| ------- | ----------- |
| Version | LOG库版本号 |
