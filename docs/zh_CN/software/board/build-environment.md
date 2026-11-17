# 编译环境配置

本页说明 SDK 的编译步骤和注意事项。具体命令以开发者提供的软件包内的 SDK README 中文部分为准，本页不重复这些命令。当前获取状态见[SDK下载](sdk-download.md)。

## 编译主机

- x86-64 Linux，Ubuntu 18.04 或更新版本。工具链只能在这类主机上运行；macOS 或 Windows 用户请使用 Linux 虚拟机或容器。需要安装的软件包见 SDK README 的“编译主机要求”。
- 请把 SDK 克隆到**不含空格**的路径：Makefile 无法处理路径中的空格。
- `make test`（主机端单元测试）还需要 `linux-libc-dev`。

## 编译步骤

按 SDK README 的“编译步骤”依次完成：

1. **安装工具链**：运行 `./scripts/get_toolchain.sh`。公开 Release 附件可用后，脚本会下载交叉工具链，校验 SHA-256 后解压到 `/opt`。在此之前，请向开发者获取压缩包并先放到 `tools/`；脚本会校验其 SHA-256 并跳过下载。然后把 `/opt/riscv64-anyka-linux-musl/bin` 加入 `PATH`。如需安装到其他目录，可将目录作为第一个参数传入，脚本会把工具链重定位到该目录。
2. **ramdisk 无需下载**：`make` 会用 `rootfs/skeleton/` 中的文件、从源码编译的 BusyBox 1.35.0 和 `mtd_debug`（mtd-utils 2.3.1）以及你编译的 `ai_glass_demo` 生成 ramdisk。首次编译会把这两个源码包下载到 `tools/` 并校验 SHA-256；离线编译时，请事先把源码包放到 `tools/`，或设置 `SOURCES_URL` 指向镜像。
3. **设置 root 密码**：发布的配置锁定了 root，设置密码前编译会停止。请先把 `rootfs/config/shadow` 复制到 `rootfs/config.local/`，再把密码哈希填入其中 `root` 行的第二个字段；不要修改受 git 跟踪的 `rootfs/config/shadow`。`rootfs/config.local/` 中的文件会在配置镜像中替换 `rootfs/config/` 的同名文件，且 git 会忽略该目录，密码哈希不会被提交。每台设备或每个构建使用唯一的强密码，不要在设备上发布共用的开发密码，也不要提交或共享密码哈希。
4. **可选：设置调试 Wi-Fi 密码**：把 `apps/ai_glass_demo/common/config/app_main_config.ini` 复制到 `rootfs/config.local/`，在 `[DebugAp]` 中设置 `password=`（WPA2 密码，8 到 63 个字符）。留空会保持临时调试热点和 RTSP 服务关闭。请使用仅供本次开发调试的唯一密码，不要复用生产环境或公司 Wi-Fi 凭据。不要在值后面加注释：`=` 之后的全部内容都属于密码。`rootfs/config/` 中的其他 Wi-Fi 配置文件只包含占位值，应用在运行时写入 `hostapd.conf` 和 `wpa_supplicant.conf`。
5. **编译**：运行 `make`。结果位于 `tools/ota/`：`update.bin`（OTA 升级包）、`ramfs.img` 和 `usr.jffs2`。`make app` 只编译应用；`make install` 打包镜像，需要先编译好应用；`make test` 运行主机端测试。BusyBox 和 `mtd_debug` 只编译一次，保存在 `rootfs/build/` 中；`make distclean` 会删除它们。

```{warning}
如果用 `ALLOW_LOCKED_ROOT=1 make` 生成不能从控制台登录的镜像，请注意：`update.bin` 也包含配置分区，用这种方式生成的 OTA 升级包会把已在使用的设备的 root 也锁定。
```

## 已知限制

- 只有 `apps/ai_glass_demo/common.mk` 中默认的功能开关组合可以编译；关闭 EIS、RTSP 或录像功能目前无法编译。
- mtd-utils 2.x 生成的 `usr.jffs2` 使用 8 KiB 擦除块（它不接受旧版内置工具使用的 4 KiB）。烧写后，请在开发板上确认配置分区挂载时没有 JFFS2 错误。

## 下一步

编译完成后，按[固件烧写](firmware-flashing.md)把 `update.bin` 升级到产品板。
