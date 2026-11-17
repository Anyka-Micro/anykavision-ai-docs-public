# 代码说明

```{note}
配套的 Anyka_Glasses APP 尚未随本次版本发布：没有提供安装包和源码。开发者可在后续版本中补充；本页目前仅供参考。
```

## 一、项目总体概览

本项目是基于 **Flutter + GetX** 的多平台应用，主要用于配合智能眼镜 / 摄像设备，实现：

1. 设备绑定与蓝牙连接管理（BLE / SPP 双模式）
2. 实时视频预览（RTSP）、媒体导入与管理、视频防抖
3. AI 对话（语音问答 + AI 识图，接入阿里百炼大模型）
4. 通话录音与翻译、EQ 均衡器调试、OTA 固件升级

**技术栈：**
- Flutter + GetX（状态管理 + 路由 + 依赖注入）
- easy_localization（中英文双语国际化）
- flutter_bluetooth_serial（SPP 经典蓝牙）/ flutter_blue_plus（BLE 低功耗蓝牙）
- fijkplayer（本地插件，RTSP 视频播放）
- Android 原生 Kotlin：P2P/FTP 数据通道、阿里百炼 LLM、OPUS 音频编解码

业务代码主要集中在 `lib/app/` 和 `android/app/src/main/kotlin/` 两个目录下。

---

## 二、架构分层说明

```
Flutter UI 层（Pages + Views）
    ↓
Controller 层（GetX Controller，业务逻辑）
    ↓
ServiceFactory（服务门面，单例，屏蔽实现差异）
    ↓
AnykaService 抽象接口
    ├── FlutterService（Flutter 侧蓝牙 + 协议实现）
    └── NativeService（通过 MethodChannel 调用 Android 原生，暂未使用）
    ↓
Android 原生层（蓝牙、P2P/FTP、LLM、音频编解码）
```

- **Controller** 只与 `ServiceFactory.getInstance()` 交互，不直接依赖蓝牙库或 MethodChannel。
- **ServiceFactory** 根据 `AppConstants.useNativeBlueTooth` 在运行时决定使用 Flutter 实现还是原生实现，支持热切换。
- **AppConstants**（`lib/app/common/data/app_constants.dart`）集中管理所有全局配置开关，包括蓝牙类型、心跳间隔、AI 对话超时、防抖缩放比等，方便调试和功能裁剪。

---

## 三、lib/app 目录结构

### 1. bindings/
GetX 的依赖注入配置，在路由跳转时按需注入 Controller 和 Service。
- `initial_binding.dart`：应用启动时的全局初始化绑定。
- `repository_bindings.dart`：数据层绑定。

新增模块时，通常需要在此目录创建对应的 Binding 类，并在 `routes/app_pages.dart` 中注册。

---

### 2. bluetooth/
蓝牙通信的核心抽象层，屏蔽 BLE 与 SPP 的底层差异。

| 文件 | 说明 |
|---|---|
| `base_bluetooth.dart` | 蓝牙抽象基类，定义扫描、连接、收发数据等统一接口 |
| `ble_bluetooth.dart` | BLE（低功耗蓝牙）实现，使用 flutter_blue_plus |
| `spp_bluetooth.dart` | SPP（经典蓝牙串口）实现，使用 flutter_bluetooth_serial |
| `bluetooth_manager.dart` | 单例管理器，持有当前活跃的蓝牙实例，统一对外暴露操作 |
| `blue_protocol_helper.dart` | 设备通信协议封装，负责组包/解包所有蓝牙指令（AI 对话、EQ、OTA、P2P 配网、心跳等） |

**蓝牙类型切换：** 通过 `AppConstants.bluetoothConnectType`（`BluetoothType.spp` 或 `BluetoothType.ble`）在运行时决定，不需要修改业务代码。

---

### 3. common/
全项目共用的基础能力和 UI 组件。

- **data/app_constants.dart**：全局常量与运行时配置开关（详见第二章）。
- **views/**：
  - `any_page_title.dart`：统一页面标题栏，含返回按钮和右侧操作按钮插槽。
  - `anyka_toast_view.dart`：自定义 Toast 视图样式。
  - `log_text_view.dart`：调试日志展示组件。
  - `photo_detail_page.dart`：图片全屏预览，支持左右翻页。
- **observer/**：GetX 相关的响应式观察者辅助类。

---

### 4. routes/
GetX 路由统一管理。
- `app_routes.dart`：所有页面路由常量字符串（如 `AppRoutes.home`、`AppRoutes.eq` 等）。
- `app_pages.dart`：`GetPage` 列表，将路由字符串、页面 Widget 和 Binding 三者绑定在一起。

新增页面步骤：① 在 `app_routes.dart` 添加常量 → ② 在 `app_pages.dart` 添加 `GetPage` → ③ 创建 Binding 类。

---

### 5. services/
业务服务层，是 Flutter 层与原生层的桥接枢纽。

| 文件 | 说明 |
|---|---|
| `anyka_service.dart` | 抽象接口基类，定义所有蓝牙操作 + 设备控制接口；同时定义数据模型（`BluetoothDeviceInfo`、`BluetoothConnectionStatus`、`ChatStatus` 等） |
| `flutter_service.dart` | `AnykaService` 的 Flutter 侧实现，负责蓝牙协议解析、心跳管理、通话录音文件创建/关闭、Opus 音频缓冲发送、P2P 配网流程状态机等 |
| `native_service.dart` | `AnykaService` 的原生侧实现，将操作转发给 Android 原生通过 MethodChannel 处理，暂未使用 |
| `service_factory.dart` | 工厂单例，根据配置动态创建并持有 `FlutterService` 或 `NativeService`，支持运行时热切换 |

**flutter_service.dart 核心职责（重点）：**
- 蓝牙数据包解析（`_handleBluetoothProtocolFromDevice`）：处理全部设备指令，包括 AI 对话、EQ、OTA、通话录音、P2P、心跳等。
- 通话录音文件管理：创建 OPUS + WAV + LOG 三份文件，调用 Android 原生方法完成 OPUS→PCM 解码和 WAV 头写入。
- Opus 数据发送缓冲逻辑。
- P2P 配网状态机：KM02G 上电 → P2P 配网 → P2P 连接 → 成功/失败后 KM02G 掉电，全流程通过 `Completer` + 超时 `Timer` 管理。

---

### 6. utils/
工具类与基础设施，开发新功能时优先复用。

| 文件 | 说明 |
|---|---|
| `dialog_util.dart` | 统一封装 Dialog、ProgressDialog、Toast（使用 Get.dialog + FToast），支持 iOS 风格和 Material 风格 |
| `audio_util.dart` | PCM/WAV 文件创建与写入工具 |
| `audio_play_util.dart` | 音频播放工具，封装 just_audio |
| `audio_record_util.dart` | 手机麦克风录音工具，封装 record 插件 |
| `opus_util.dart` | OPUS 编解码工具（Flutter 侧实现） |
| `method_channel_util.dart` | Flutter ↔ 原生 MethodChannel 二次封装，单例模式，支持注册多个消息接收器 |
| `data_store_util.dart` | SharedPreferences 封装，统一管理本地持久化数据 |
| `permission_util.dart` | 定位、蓝牙、存储等权限申请封装 |
| `aes_decryptor.dart` | AES 解密工具（用于 License 验证等场景） |
| `network_util.dart` | 网络状态检测与 Wi-Fi 信息获取 |
| `flavors.dart` | 多 flavor 构建配置（anyBlue / glasses 渠道差异化） |
| `log/logger_util.dart` | 全局日志工具，统一管理调试输出 |

---

## 四、lib/app/modules 功能模块

每个模块均遵循 GetX 标准结构：`pages/`（UI）+ `controllers/`（业务逻辑）+ `bindings/`（依赖注入）。

---

### 1. home/
应用首页，是其他所有功能模块的导航入口。
- 展示设备连接状态、电量、固件版本号。
- 提供 AI 对话、图库管理、视频直播、设置等功能的入口卡片。
- 自动加载上次绑定的设备信息并尝试恢复连接状态。

---

### 2. aiChat/
AI 对话模块（Android 端实现大模型调用，Flutter 负责展示）。

**功能：**
- **语音问答**：从设备AK1090系列芯片或手机麦克风获取 Opus 音频流，发送到阿里百炼大模型，接收 TTS 回复后通过AK1090系列芯片播放给用户。
- **AI 识图**：通过AK1090系列芯片指令触发设备拍照，图片数据经AK1090系列芯片传输到 APP，调用大模型进行图片理解，返回文字结果。
- **聊天界面**：类似 IM 聊天窗口，区分用户/AI 角色，展示文字问答记录。

**Controller 核心职责：**
- 对话聊天状态：`idle → userAsking → recognizing → aiReplying → idle`，超时自动重置。
- 处理 AI 回复播放完成的回调。

---

### 3. blueToothConnect/
设备绑定与蓝牙连接，是所有依赖蓝牙功能的前置模块。

**流程：**
1. 检查并申请定位权限（Android 扫描蓝牙必须）和蓝牙权限。
2. 调用 `ServiceFactory.getInstance().startScan()` 开始扫描，实时展示扫描到的设备列表（含信号强度 RSSI 和已配对标记）。
3. 支持按设备名前缀过滤（默认过滤 "AK"，可在 settings 中调整）。
4. 用户点击设备后执行握手（handShake）→ 连接 → 保存绑定信息到 SharedPreferences。

---

### 4. bluetoothOta/
AK1090系列芯片 OTA 固件升级（针对AK1090系列主控芯片）。
- 通过蓝牙通道将固件文件分包发送给设备。
- 支持单耳/双耳模式（`isTwoEarBudOta`）。
- 显示升级进度、处理失败重试，升级完成后自动断开并提示重启。
- 通常从 settings 或 upgrade 模块跳转进入。

---

### 5. media_import/
媒体导入，通过 Wi-Fi P2P + FTP 从设备导入照片和视频到手机相册。

**完整流程：**
1. Flutter 层发起 P2P 配网指令（触发 KM02G 上电 → P2P 配网 → P2P 连接）。
2. P2P 连接成功后，FTPUtil 通过 FTP 协议扫描设备上的图片/视频目录。
3. 按文件类型分批下载，实时更新进度（`DialogUtil.showProgressDialog`）。
4. 下载完成后更新UI。
5. 流程结束后 KM02G 掉电，断开 P2P。

---

### 6. rtsp/
实时视频预览（直播）模块。
- 通过 P2P 连接后，设备推送 RTSP 视频流，APP 使用本地 `fijkplayer` 插件拉流播放。
- 支持横竖屏切换、全屏模式。
- 直播超时时间可在 settings 调试菜单中配置（`AppConstants.rtspLiveTimeout`）。

> **安全提示：** FTP 与 `rtsp://` 传输仅限临时、隔离的设备直连 P2P 网络。不要把该连接桥接或路由到办公网络、生产网络或互联网；媒体传输或实时预览结束后立即断开 P2P。

---

### 7. eq/
EQ 均衡器调试模块，用于调整设备侧的音频处理参数。

**数据结构：**
- `EQType`（如 A2DP、HFP 上行/下行等）→ 包含多个 `EQGroup` → 每组包含多个 `EQParam`（频段参数：类型、频率、增益、Q 值）。

**核心功能：**
- 从设备读取当前 EQ 配置（`getEqGroupInfoFromDevice`，3 秒超时）。
- 在 UI 上修改各频段参数后，一次性将所有 EQ 类型推送到设备（`setAllEqTypeToDevice`，5 秒超时，设置间隔冷却 2 秒）。
- A2DP 类型最多支持 8 组配置，非 A2DP 类型最多 1 组。
- 支持新增、重命名、删除 EQ 分组。

---

### 8. callManagement/
通话录音管理模块。
- 监听设备发起的通话录音请求（`cmdDeviceEnterCallMode`）或由 APP 主动触发。
- 录音数据以 OPUS 格式通过蓝牙实时传输，APP 同步写入 `.opus` 和 `.wav` 两种格式文件（WAV 通过 Android 原生 OPUS→PCM 解码后写入）。
- 同步写 `.log` 文件记录每个包的包序号和连续性，用于调试丢包问题。
- 提供通话录音文件列表的浏览和播放功能。
- 与 callTranslate 模块协作，可对录音内容进行翻译。

---

### 9. callTranslate/
通话翻译模块。
- 接收通话音频流数据（`cmdCallTranslateData`），支持近端/远端双通道。
- 实现音频数据延迟回传机制（`callTranslateDataSendBackDelayTime`，默认 2 秒），模拟真实通话翻译场景。
- 在 UI 中按角色（主叫/被叫）展示原文和译文。

---

### 10. settings/
设置模块，整合系统级功能入口。

- 版本信息展示（AK1090系列芯片固件版本、App 版本）。
- 设备解绑（清空本地绑定信息，恢复出厂设置）。
- OTA 升级入口。
- 帮助文档页面。
- **隐藏调试菜单**：3 秒内连续点击版本号 5 次可解锁，包含：
  - 开启/关闭手机端 AI 对话
  - P2P 连接日志开关
  - RTSP 直播超时时间
  - UVC 模式配置
  - 蓝牙扫描过滤关键词
  - 通话翻译数据回传延时等

---

### 11. upgrade/
相机（KM02G系列芯片）固件升级模块，区别于 bluetoothOta（AK1090系列芯片升级）。
- 通过 P2P/FTP 通道将相机固件文件推送到设备指定目录。
- 发送 OTA 升级指令后监听升级进度回调。
- 升级成功/失败通过AK1090系列芯片指令回调通知 Flutter 层更新 UI。

---

## 五、android/ 目录结构（Android 原生实现）

### 1. app/src/main/kotlin/com/anyka/ai/

| 文件/目录 | 说明 |
|---|---|
| `AiApplication.kt` | Application 初始化，注册 BlankJ Utils 等全局工具库 |
| `ForegroundService.kt` | 前台服务，保活 APP，管理蓝牙连接状态监听 |
| `ServiceManager.kt` | 原生服务管理，协调各子模块的初始化与销毁 |
| `activity/` | MainActivity，注册所有 MethodChannel Handler |
| `bluetooth/` | 原生蓝牙实现（SPP/BLE 的 Android 侧），暂未使用 |
| **`llm/`** | 阿里百炼大模型集成 |
| **`p2p/connection/`** | P2P + FTP 数据通道实现 |
| `utils/` | 原生工具类 |

**llm/ 目录（AI 对话核心）：**
- `BaiLianLLM.kt`：阿里百炼 SDK 封装，管理 License 授权和 SDK 初始化。
- `BaiLianLLMHelper.kt`：AI 对话主控，处理语音 ASR、LLM 问答、TTS 合成全流程；管理 WebSocket 长连接和会话状态。
- `UploadPhotoUtil.kt`：图片上传工具，将设备传来的图片数据上传到百炼服务器进行识图。

**p2p/connection/ 目录（媒体导入核心）：**
- `P2PConnection.kt`：Wi-Fi P2P 连接管理，处理设备搜索、连接、超时重试；通过 MethodChannel 将连接结果和进度回调给 Flutter 层。
- `FTPUtil.kt`：FTP 文件传输封装，处理图片/视频的批量下载，实时更新进度。
- `FTPClientHelper.kt`：底层 FTP 客户端操作封装（连接、上传、下载、列目录、删除等）。

**utils/ 目录（原生工具）：**
- `OpusUtil.kt`：OPUS 音频编解码（调用 JNI 原生库），包括编码器管理、解码为 PCM、多流解码。
- `AudioPlayer.kt`：原生音频播放器，负责 TTS 回复的播放与静音帧插入。
- `MethodChannelUtil.kt`：MethodChannel 原生侧封装，统一注册和分发来自 Flutter 的调用。

---

### 2. videoStabilization/
视频防抖子模块（独立 Library Module）。
- 输入视频文件或目录，识别符合格式要求（分辨率、帧率等）的视频后进行防抖处理。
- 输出防抖后的视频文件，通过 AAR 形式集成到主 app。
- 防抖缩放比例可通过 `AppConstants.stabilizationZoom`（默认 1.25）配置。

---

## 六、国际化（i18n）

使用 **easy_localization** 实现中英文双语。

- 翻译文件位于 `assets/translations/zh.json` 和 `assets/translations/en.json`。
- 使用命名空间组织 key（如 `bt_connect.title`、`eq.set_timeout`、`bt_service.callback_timeout`）。
- 在 Flutter 代码中使用顶层函数 `tr('namespace.key')` 调用（注意：应使用 easy_localization 的 `tr()` 而非 GetX 的 `.tr` 扩展，两者存在冲突）。
- Android 原生侧通过 `values/strings.xml`（英文默认）和 `values-zh/strings.xml`（中文）实现本地化，使用 `Utils.getApp().getString(R.string.xxx)` 读取。
