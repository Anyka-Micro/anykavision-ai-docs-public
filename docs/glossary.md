# Translation glossary (ZH → EN)

Terms for translating `docs/zh_CN` into `docs/en`. Use these consistently. Add a row when a new term comes up.

## Conventions

- **Same structure in both trees.** Keep file paths, heading levels, code blocks, tables and image references identical, so the two trees stay in sync and the language switcher lands on the same page.
- **Anchors.** Headings are translated, so heading-derived anchors differ between the trees. For any heading that another page links to, put the same explicit target above it in both trees, for example `(connect-and-flash)=`, and link to the label with `[text](#connect-and-flash)`. Sphinx resolves the label across the whole language tree; GitHub's file view does not.
- **Don't translate identifiers.** API names, macros, structs, enums, error codes, register names, file paths and shell commands stay as they are.
- **Do translate comments and strings in sample code.** Replace full-width punctuation (`，`, `；`, `（`) in code with its ASCII form.
- **Spelling and style.** British spelling (stabilisation, equaliser, licence as a noun). Title Case for page titles; sentence case for headings inside a page.
- **Units.** State memory sizes unambiguously. `Mib`/`Gib` in the source are mebibits/gibibits: write `512 Mbit (64 MiB)`, not `512Mib`. Keep other units as written (`4GiB`, `24MHz`).
- **Images.** Reuse the images under `docs/zh_CN` with a relative path, for example `../../../zh_CN/hardware/chips/img/ak1090-block-diagram.png`. Most diagrams have Chinese labels; redraw them only if Anyka provides English sources.
- **UI labels.** Quote app menus and buttons exactly as the app's English UI shows them (see the UI column below), in quotation marks.
- **"AI" is ambiguous.** In the audio API, AI means *audio input* (and AO *audio output*), not artificial intelligence. Spell it out on first use on each page.

## Product and document names

| 中文 | English | Notes |
|---|---|---|
| AnykaVision AI | AnykaVision AI | Product name; never translated |
| AI拍摄眼镜 | AI camera glasses | |
| AI智能眼镜 | AI smart glasses | |
| 产品板 | reference board | Not "product board" |
| KM02G系列芯片 | KM02G series chip | Likewise "AK1090 series chip" |
| 主控芯片 | main controller | |
| 中间件 | middleware | |
| 平台中间件接口说明 / 中间件接口说明 | Platform Middleware API Reference | Page title and list entries; "middleware API reference" in running prose |
| 快速入门 / 入门指南 | Getting Started | |
| 软件开发 / 硬件开发 | Software Development / Hardware Development | |
| 编译环境配置 | Build Environment Setup | |
| 应用开发说明 | Application Development | |
| 快速开发指南 | Quick Development Guide | |
| 固件烧写 | Firmware Flashing | |
| SDK下载 | SDK Download | |
| 芯片介绍 | Chip Overview | |
| 产品板使用指南 | Reference Board User Guide | |
| 产品板设计指南 | Reference Board Design Guide | |
| 使用说明 | User Guide | |
| 打包与调试说明 | Packaging and Debugging | |
| 代码说明 | Code Walkthrough | |
| 常见问题 | FAQ | |
| Git操作指南 | Git Guide | |

## Device features and the app

| 中文 | English | Notes |
|---|---|---|
| 防抖 | stabilisation (EIS) | Electronic image stabilisation |
| 快启 | fast boot | |
| 拍照 | photo capture | |
| 录像 | video recording | |
| 抓拍 | snapshot | Protocol command 0x75 |
| 小图抓拍 | small-image snapshot | Low-resolution capture, e.g. for AI image recognition |
| 导图 | media transfer | Glasses to phone over Wi-Fi P2P |
| 直播 | live streaming | |
| 视频直播 | live video | UI: "Video Live" |
| 配网 | network provisioning | Wi-Fi setup |
| 绑定 / 解除绑定 | bind / unbind | UI: "Bind Device" / "Unbind Device". Binding is a separate step from Bluetooth pairing |
| 配对 / 已配对 | pair / paired | Bluetooth pairing. UI: "Paired" |
| 上下电 | power cycle | |
| 图库管理 | photo library | UI: "Photo Library" |
| AI对话 | AI chat | UI: "AI Chat" |
| AI识图 | AI image recognition | |
| OTA升级 / 升级包 | OTA update / update package | UI: "OTA Upgrade" |
| EQ调试 | EQ tuning | UI: "EQ Debug" |
| 串口 | serial port (UART) | |
| 波特率 | baud rate | |
| U盘 | USB storage | On the board, its USB mass-storage drive |

## API reference

| 中文 | English | Notes |
|---|---|---|
| 概述 | Overview | |
| API参考 | API reference | |
| 函数接口列表 | Function list | |
| 数据结构 | Data structures | |
| 结构体 / 枚举 | struct / enum | |
| 错误码 / 错误码说明 / 【错误码】 | Error codes | |
| 版本信息获取 | Getting version information | |
| 打开/关闭模块 | Opening and closing the module | |
| 接口调用依赖关系 | Call dependencies | |
| 【语法】 | **Syntax** | Fixed labels: keep the bold style |
| 【描述】 | **Description** | |
| 【参数】 | **Parameters** | |
| 【返回值】 | **Return value** | |
| 【需求】 | **Requirements** | Header and library needed |
| 【说明】 | **Notes** | |
| 【注意】 | **Caution** | Distinct from **Notes** |
| 【定义】 | **Definition** | |
| 【成员】 | **Members** | |
| 【错误码列表】 | **Error codes** | |
| 【相关函数接口】 / 【相关接口】 | **See also** | |
| 【接口调用】 | **Usage** | |
| 【相关数据类型及函数接口】 | **Related types and functions** | |
| 【相关结构体定义】 / 【相关结构体】 | **Related structs** | |
| 【接口调用顺序】 | **Call sequence** | |
| 【调用流程】 | **Call flow** | |
| 【接口配对关系】 | **Paired calls** | |
| 【接口重入性】 | **Reentrancy** | |
| 【举例】 | **Example** | |
| 输入 / 输出 | Input / Output | Parameter direction |
| 任何位置都可以调用 | Can be called at any time. | |

## Audio and video modules

| 中文 | English | Notes |
|---|---|---|
| 音频输入 (AI) | audio input (AI) | See the note on "AI" above |
| 音频输出 (AO) | audio output (AO) | |
| 音频编码 / 音频解码 | audio encoding (AENC) / audio decoding (ADEC) | |
| 音效处理 / 音频质量增强 / 音效增强 | audio effects | Module AUDIO_EFFECT, also called VQE |
| 降噪 | noise reduction (NR) | |
| 自动增益控制 | automatic gain control (AGC) | |
| 均衡器 | equaliser (EQ) | |
| 重采样 | resampling | |
| 数字放大 | digital gain (ASLC) | |
| 哭声检测 | cry detection | |
| 声源定位 | sound source localisation | |
| 单麦 / 双麦 / 多麦 | single-mic / dual-mic / multi-mic | |
| 采样率 / 采样精度 | sample rate / sample precision (bit depth) | |
| 视频输入 | video input (VI) | |
| 视频处理子系统 | video processing subsystem (VPSS) | |
| 视频编码 | video encoding (VENC) | |
| 视频叠加显示 | on-screen display (OSD) | |
| 画布 / 区域 | canvas / region | OSD terms |
| 图像处理单元 | image processing unit (IPU) | 2D image processing |
| 图形处理器 | 2D graphics processor | KM02G spec heading; not a GPU. Likely the IPU: Anyka to confirm |
| 解析 / 合成 | demuxing (DEMUX) / muxing (MUX) | |
| 移动侦测 / 移动侦测算法 | motion detection / motion detection algorithm (MRD) | Page title: "Motion Detection Algorithm (MRD)" |
| 智能视觉处理 | smart vision processing (SVP) | |
| 码流 / 码率 / 帧率 | stream / bitrate / frame rate | |
| 通道 | channel | |
| 宽动态 | wide dynamic range (WDR) | |
| 白平衡 / 曝光 / 对焦 | white balance / exposure / focus | |
| 坏点校正 | defective pixel correction | |
| 畸变矫正 / 畸变校正 | distortion correction | Both spellings occur |
| 隐私遮挡 | privacy mask | |
| 图像信号处理器 | image signal processor (ISP) | |
| 神经网络处理器 | neural processing unit (NPU) | |
| 摄像头 / CIS | camera / CMOS image sensor (CIS) | |
| 陀螺仪 | gyroscope | |

## Hardware design

| 中文 | English | Notes |
|---|---|---|
| 原理图 | schematic | |
| 规格书 | datasheet | |
| 参考设计 | reference design | |
| 晶振 | crystal | |
| 复位 | reset | |
| 上电时序 | power-up sequence | |
| 退耦电容 / 去耦电容 | decoupling capacitor | |
| 走线 / 布线 | trace / routing | |
| 布局 | placement | "layout" for the PCB as a whole |
| 包地 | ground guarding | |
| 等长 | length matching | |
| 蛇形线 / 蛇行线 | serpentine trace | Both spellings occur |
| 差分线 | differential pair | |
| 层叠 | stack-up | |
| 阻抗控制 | impedance control | |
| 短桩 | stub | |
| 馈线 | feed line | |
| 回波损耗 | return loss | |
| 匹配网络 | matching network | |
| 辐射方向图 / 通讯死角 | radiation pattern / dead zone | |
| 缓启动 | soft start | |
| 锂电池保护 | lithium battery protection | |
| 单线通信 | single-wire communication | |
| 硅麦 | silicon microphone | |
| 模拟MIC / 数字MIC | analogue microphone (AMIC) / digital microphone (DMIC) | |
| 喇叭 / 扬声器 | speaker | |
| PA | power amplifier (PA) | |
