# 移动侦测算法

## 概述

&emsp;&emsp;移动侦测算法模块（MRD模块）支持灵敏度阈值、移动块数阈值等参数设置。

<br/>

##  API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **库接口 **                        | **描述 **                   |
| ---------------------------------- | --------------------------- |
| MD_SIZE                            | VPSS MD统计数组水平方向大小 |
| MAX_CAP                            | 侦测结果移动区域最大数量    |
| MRD_RECTANGLE                      | 侦测结果移动区域结构        |
| ak_mrd_get_version                 | 获取mrd算法库版本号         |
| ak_mrd_init                        | 初始化mrd模块               |
| ak_mrd_destroy                     | 销毁mrd模块                 |
| ak_mrd_set_filters                 | 设置侦测阈值                |
| ak_mrd_set_motion_region_size      | 设置侦测面积尺寸            |
| ak_mrd_set_mode                    | 设置侦测单帧多帧模式        |
| ak_mrd_set_floating_wadding_params | 设置多帧过滤参数            |
| ak_mrd                             | 侦测主功能接口              |
<br/>

##  数据结构

### MD_SIZE

&emsp;&emsp;【说明】

&emsp;&emsp;VPSS MD统计数组水平方向大小

&emsp;&emsp;【定义】

```c
    #define MD_SIZE  64
```

<br/>

### MAX_CAP

&emsp;&emsp;【说明】

&emsp;&emsp;侦测结果移动区域最大数量

&emsp;&emsp;【定义】

```c
    #define MAX_CAP  20
```

<br/>

###  MRD_RECTANGLE

&emsp;&emsp;【说明】

&emsp;&emsp;侦测结果移动区域结构

&emsp;&emsp;【定义】

```C
typedef struct
{
	int left;
	int top;
	int right;
	int bottom;
	int count;
}MRD_RECTANGLE;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **                                             |
| ------------- | ----------------------------------------------------- |
| left          | 区域左上角水平坐标（坐标是相对32\*24/32\*16的，下同） |
| top           | 区域左上角垂直坐标                                    |
| right         | 区域右下角水平坐标                                    |
| bottom        | 区域右下角垂直坐标                                    |
| count         | 移动区域数量                                          |

&emsp;&emsp;【相关接口】

```C
    int ak_mrd(void *mrd_handle, unsigned short md[][MD_SIZE], int len, MRD_RECTANGLE boxes[MAX_CAP]);
```

<br/>

## 版本信息获取

###  ak_mrd_get_version

&emsp;&emsp;【描述】

&emsp;&emsp;获取mrd库的版本号

&emsp;&emsp;【语法】

```C
    char* ak_mrd_get_version();
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 ** | **取值范围 ** | **输入/输出 ** |
| ------------- | --------- | ------------- | -------------- |
| 无            | -         | -             |                |

&emsp;&emsp;【返回值】

| **返回值 **             | **描述 ** |
| ----------------------- | --------- |
| mrd模块版本号字符串指针 | 成功      |
| NULL                    | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

## 移动侦测流程

###  ak_mrd_init

&emsp;&emsp;【描述】

&emsp;&emsp;初始化mrd模块，并返回MRD句柄指针。

&emsp;&emsp;【语法】

```C
    void *ak_mrd_init(void);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 ** | **取值范围 ** | **输入/输出 ** |
| ------------- | --------- | ------------- | -------------- |
| void          | -         | -             | -              |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **   |
| ----------- | ----------- |
| 非NULL      | MRD句柄指针 |
| NULL        | 失败        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

###  ak_mrd_destroy

&emsp;&emsp;【描述】

&emsp;&emsp;销毁mrd模块

&emsp;&emsp;【语法】

```C
    int ak_mrd_destroy(void *mrd_handle);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **   | **取值范围 ** | **输入/输出 ** |
| ------------- | ----------- | ------------- | -------------- |
| mrd_handle    | MRD句柄指针 | -             | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 ** |
| ----------- | --------- |
| 0           | 成功。    |
| -1          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

###  ak_mrd

&emsp;&emsp;【描述】

&emsp;&emsp;移动侦测主功能接口

&emsp;&emsp;【语法】

```C
    int ak_mrd(void *mrd_handle, unsigned short md[][MD_SIZE], int len, MRD_RECTANGLE boxes[MAX_CAP]);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **         | **取值范围 ** | **输入/输出 ** |
| ------------- | ----------------- | ------------- | -------------- |
| mrd_handle    | MRD句柄指针       | -             | 输入           |
| md            | vpss_md数组       |               | 输入           |
| len           | vpss_md数组的高度 | 24或32        | 输入           |
| boxes         | 运动区域位置坐标  |               | 输出           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **              |
| ----------- | ---------------------- |
| -1          | 失败                   |
| 其他        | 检测到的运动区域的个数 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

## 参数设置

### ak_mrd_set_filters

&emsp;&emsp;【描述】

&emsp;&emsp;设置侦测阈值

&emsp;&emsp;【语法】

```C
    int ak_mrd_set_filters(void *mrd_handle, unsigned short flt_big, unsigned short flt_small);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **   | **取值范围 ** | **输入/输出 ** |
| ------------- | ----------- | ------------- | -------------- |
| mrd_handle    | MRD句柄指针 | -             | 输入           |
| flt_big       | 较大的阈值  | [0, 65535]    | 输入           |
| flt_small     | 较小的阈值  | [0, 65535]    | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 ** |
| ----------- | --------- |
| 0           | 成功。    |
| -1          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

### ak_mrd_set_motion_region_size

&emsp;&emsp;【描述】

&emsp;&emsp;设置侦测面积尺寸

&emsp;&emsp;【语法】

```C
    int ak_mrd_set_motion_region_size(void *mrd_handle, int size_min, int size_max);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **        | **取值范围 ** | **输入/输出 ** |
| ------------- | ---------------- | ------------- | -------------- |
| mrd_handle    | MRD句柄指针      | -             | 输入           |
| size_min      | 最小侦测面积尺寸 | [1, size_max] | 输入           |
| size_max      | 最大侦测面积尺寸 | [1, 768]      | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 ** |
| ----------- | --------- |
| 0           | 成功。    |
| -1          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

### ak_mrd_set_mode

&emsp;&emsp;【描述】

&emsp;&emsp;设置侦测模式（多帧模式或单帧模式）

&emsp;&emsp;【语法】

```C
    int ak_mrd_set_mode(void *mrd_handle, unsigned char mode);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **   | **取值范围 **                       | **输入/输出 ** |
| ------------- | ----------- | ----------------------------------- | -------------- |
| mrd_handle    | MRD句柄指针 | -                                   | 输入           |
| mode          | 侦测模式    | [0, 255]， 0 多帧模式，其他单帧模式 | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 ** |
| ----------- | --------- |
| 0           | 成功。    |
| -1          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>

### ak_mrd_set_floating_wadding_params

&emsp;&emsp;【描述】

&emsp;&emsp;设置多帧过滤参数

&emsp;&emsp;【语法】

```C
    int ak_mrd_set_floating_wadding_params(void *mrd_handle, int m_frames, int s_frames, int extra_frames,
	int dis, int m_width, int m_height);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **                      | **取值范围 **    | **输入/输出 ** |
| ------------- | ------------------------------ | ---------------- | -------------- |
| mrd_handle    | MRD句柄指针                    | -                | 输入           |
| m_frames      | 连续移动帧数                   | [2, 10]          | 输入           |
| s_frames      | 不必连续移动帧数               | [1,extra_frames] | 输入           |
| extra_frames  | 等待s_frames条件达成的额外帧数 | [1, 20]          | 输入           |
| dis           | 最大有效运动距离的平方         | [1, 64]          | 输入           |
| m_width       | 最小检测宽度                   | [1, 32]          | 输入           |
| m_height      | 最小检测高度                   | [1, 24]          | 输入           |
&emsp;&emsp;【返回值】

| **返回值 ** | **描述 ** |
| ----------- | --------- |
| 0           | 成功。    |
| -1          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libak_mrd.a 或 libak_mrd.so

&emsp;&emsp;头文件：ak_mrd.h

<br/>
