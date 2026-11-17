# 打包与调试说明

```{note}
配套的 Anyka_Glasses APP 尚未随本次版本发布：没有提供安装包和源码。开发者可在后续版本中补充；本页目前仅供参考。
```

## 简介

本文档将指导您如何将 Anyka Glasses APP 的源代码打包成可以在 Android 手机上安装的 APK 文件。

### 什么是 Anyka Glasses APP？

Anyka Glasses APP 是一款用于控制智能眼镜的手机应用程序。通过这个 APP，您可以：
- 连接智能眼镜设备
- 查看眼镜拍摄的照片和视频
- 配置眼镜的各项功能设置

### 技术说明

- **开发框架**：本 APP 使用 Flutter 框架开发。Flutter 是 Google 推出的跨平台开发框架，可以同时开发 Android 和 iOS 应用。
- **发布范围**：本次发布尚未提供 Anyka_Glasses APP 的源码和安装包。开发者可在后续版本中补充。本页说明该 APP（Android 工程）的打包与调试方法，仅供参考。暂不支持 iOS 平台。
- **工程结构说明**：工程代码中可能包含 iOS 相关的配置文件（如 anyBlue 配置），这些是 Flutter 框架自动生成的，不影响 Android 端的编译打包。

---

## 准备工作

在开始前，您需要在电脑上安装以下软件工具。这些工具都是免费的，可以从官方网站下载。

### 1. Flutter SDK（必须）

Flutter SDK 是开发 Flutter 应用的核心工具包。

**版本要求**：3.3.3 或更高版本（推荐 3.19.x 稳定版）

**下载地址**：<https://flutter.dev/docs/get-started/install>

**安装步骤**：
1. 访问上述网址，根据您的操作系统（Windows/Mac/Linux）选择对应的安装包
2. 下载并解压到您电脑上的某个目录（例如 `C:\flutter` 或 `~/flutter`）
3. 将 `flutter/bin` 目录添加到系统的环境变量 PATH 中（具体方法见下文"环境变量配置"部分）

### 2. Android Studio（必须）

Android Studio 是 Google 官方提供的 Android 应用开发工具。

**版本要求**：Hedgehog (2023.1.1) 或更高版本

**下载地址**：<https://developer.android.com/studio>

**安装时需要勾选的组件**：
- ☑ Android SDK
- ☑ Android SDK Platform (API 26-36)
- ☑ Android SDK Build-Tools
- ☑ Android SDK Command-line Tools（命令行工具）

> **提示**：如果您已经安装了 Android Studio，可以通过以下步骤检查/安装缺失的组件：
> 1. 打开 Android Studio
> 2. 点击菜单栏的 `Tools` → `SDK Manager`
> 3. 在 `SDK Platforms` 标签页勾选 API 26-36
> 4. 在 `SDK Tools` 标签页勾选 `Android SDK Build-Tools` 和 `Android SDK Command-line Tools`
> 5. 点击 `Apply` 按钮安装

### 3. JDK（Java Development Kit）（必须）

JDK 是 Java 开发工具包，Android 应用编译需要它。

**版本要求**：JDK 11 或 JDK 17

**安装方式**（二选一）：
- **推荐**：使用 Android Studio 自带的 JDK（无需额外安装）
- 从 <https://adoptium.net/> 下载独立 JDK 并安装

### 4. Android NDK（必须）

NDK 是 Android 原生开发工具包，用于编译一些底层代码。

**版本要求**：27.2.12479018

**安装方式**：
1. 打开 Android Studio
2. 点击菜单栏的 `Tools` → `SDK Manager`
3. 切换到 `SDK Tools` 标签页
4. 勾选 `NDK (Side by side)`，选择版本 `27.2.12479018`
5. 点击 `Apply` 按钮安装

### 5. cmdline-tools（命令行工具）（必须）

cmdline-tools 是 Android SDK 的命令行工具，用于在终端中执行 Android 相关命令。

**安装方式**：
1. 打开 Android Studio
2. 点击菜单栏的 `Tools` → `SDK Manager`
3. 切换到 `SDK Tools` 标签页
4. 找到 `Android SDK Command-line Tools (latest)` 并勾选
5. 点击 `Apply` 按钮安装

> **注意**：安装完成后，cmdline-tools 位于 `Android SDK 目录/cmdline-tools/latest/bin/` 下。

---

## 环境变量配置

环境变量是告诉电脑在哪里找到这些工具的配置。配置完成后，您可以在任何目录下使用这些工具的命令。

### Windows 系统配置方法

1. 右键点击"此电脑" → 选择"属性" → 点击"高级系统设置"
2. 点击"环境变量"按钮
3. 在"系统变量"区域点击"新建"，添加以下变量：

| 变量名 | 变量值（根据您的实际安装路径修改） |
|--------|----------------------------------|
| `FLUTTER_HOME` | `C:\flutter` |
| `ANDROID_HOME` | `C:\Users\您的用户名\AppData\Local\Android\Sdk` |
| `JAVA_HOME` | `C:\Program Files\Android\Android Studio\jbr` |

4. 找到 `Path` 变量，点击"编辑"，添加以下条目：
   - `%FLUTTER_HOME%\bin`
   - `%ANDROID_HOME%\platform-tools`
   - `%ANDROID_HOME%\cmdline-tools\latest\bin`

### macOS/Linux 系统配置方法

1. 打开终端
2. 编辑配置文件（根据您的 shell 类型选择）：
   - Bash 用户：`nano ~/.bashrc` 或 `nano ~/.bash_profile`
   - Zsh 用户：`nano ~/.zshrc`
3. 在文件末尾添加以下内容：

```bash
export FLUTTER_HOME=~/flutter
export ANDROID_HOME=~/Library/Android/sdk
export JAVA_HOME=/Applications/Android\ Studio.app/Contents/jbr/Contents/Home
export PATH=$PATH:$FLUTTER_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin
```

4. 保存文件（按 `Ctrl+O`，然后按 `Enter`，再按 `Ctrl+X`）
5. 使配置生效：
   - Bash：`source ~/.bashrc` 或 `source ~/.bash_profile`
   - Zsh：`source ~/.zshrc`

---

## 验证安装

配置完成后，我们需要验证所有工具是否安装正确。

### 1. 检查 Flutter 环境

打开终端（Windows 用户打开 CMD 或 PowerShell，Mac/Linux 用户打开 Terminal），执行以下命令：

```bash
flutter doctor
```

这个命令会检查 Flutter 环境是否配置正确。您应该看到类似以下的输出：

```
[✓] Flutter (Channel stable, 3.x.x, ...)
[✓] Android toolchain - develop for Android devices
[✓] Android Studio (version 2023.x)
[✓] Connected device (可选，仅调试时需要)
```

**注意事项**：
- `[✓]` 表示该项检查通过
- `[✗]` 表示该项有问题，需要根据提示修复
- `[!]` 表示警告，可能不影响基本功能

如果看到 `[✗]` 或 `[!]`，请根据提示信息进行修复。

### 2. 检查环境变量

执行以下命令验证环境变量是否配置正确：

```bash
# Windows
where flutter
where adb

# macOS/Linux
which flutter
which adb
```

如果显示工具的路径，说明配置成功。

---

## 安装项目依赖

### 1. 进入项目目录

打开终端，切换到项目根目录（包含 `pubspec.yaml` 文件的目录）：

```bash
cd /path/to/anyka_ai
```

> 将 `/path/to/anyka_ai` 替换为实际的工程路径

### 2. 下载依赖包

执行以下命令下载项目所需的所有依赖包：

```bash
flutter pub get
```

这个命令会自动读取 `pubspec.yaml` 文件，下载所有必需的 Dart/Flutter 包。下载过程可能需要几分钟，取决于您的网络速度。

**成功标志**：看到 `Got dependencies!` 或类似的提示信息。

---

## 编译 APK

一切准备就绪后，就可以编译生成 APK 文件了。

### 编译命令

在项目根目录（`anyka_ai` 目录）下执行：

```bash
flutter build apk --flavor glasses
```

**编译过程**：
- 首次编译可能需要 5-10 分钟，取决于电脑性能
- 后续编译会更快（约 1-3 分钟）

### 找到生成的 APK 文件

编译成功后，APK 文件位于：
```
build/app/outputs/apk/glasses/release/app-glasses-release.apk
```
