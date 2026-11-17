# 编译环境配置

本页说明 SDK 的编译步骤和注意事项。具体命令以 SDK 源码包内 README 的中文部分为准，本页不重复这些命令。候选附件和发布门禁见[SDK下载](sdk-download.md)。

## 编译主机

- x86-64 Linux，Ubuntu 18.04 或更新版本。工具链只能在这类主机上运行；macOS 或 Windows 用户请使用 Linux 虚拟机或容器。需要安装的软件包见 SDK README 的“编译主机要求”。
- 请把 SDK 解压到**不含空格**的路径：Makefile 无法处理路径中的空格。
- `make test`（主机端单元测试）还需要 `linux-libc-dev`。

## 编译步骤

按 SDK README 的“编译步骤”依次完成：

1. **安装工具链**：工具链公开再分发仍受门禁限制。请向安凯获取校验和匹配的 `riscv64-anyka-linux-musl.tar.gz`，放入 `tools/`，再运行 `./scripts/get_toolchain.sh`。脚本会校验 SHA-256 并解压到 `/opt`。然后把 `/opt/riscv64-anyka-linux-musl/bin` 加入 `PATH`。如需安装到其他目录，可将目录作为第一个参数传入，脚本会把工具链重定位到该目录。
2. **生成完整镜像时准备 ramdisk 源码**：把经过校验的 `busybox-1.35.0.tar.bz2` 和 `mtd-utils-2.3.1.tar.bz2` Release 附件放入 `tools/`。完整 `make` 会校验附件，并用这些源码、`rootfs/skeleton/` 和你编译的 `ai_glass_demo` 生成 ramdisk；也可设置 `SOURCES_URL` 指向已批准的镜像。
3. **生成完整镜像时提供已获许可的格式化工具**：清洁公开源码包已移除来源和许可未解决的旧版 `rootfs/skeleton/etc/format_tool` 文件。请按适当的许可条款另行向安凯获取格式化工具，并传入其绝对路径，例如 `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make`。默认回退路径为 `rootfs/vendor/format_tool`；构建时会把选定工具复制到镜像内的 `/etc/format_tool`。
4. **生成完整镜像时设置 root 密码**：发布的配置锁定了 root，设置密码前镜像打包会停止。请先把 `rootfs/config/shadow` 复制到 `rootfs/config.local/`，再把密码哈希填入其中 `root` 行的第二个字段；不要修改受 git 跟踪的 `rootfs/config/shadow`。`rootfs/config.local/` 中的文件会在配置镜像中替换 `rootfs/config/` 的同名文件，且 git 会忽略该目录，密码哈希不会被提交。每台设备或每个构建使用唯一的强密码，不要在设备上发布共用的开发密码，也不要提交或共享密码哈希。
5. **生成完整镜像时可选设置调试 Wi-Fi 密码**：把 `apps/ai_glass_demo/common/config/app_main_config.ini` 复制到 `rootfs/config.local/`，在 `[DebugAp]` 中设置 `password=`（WPA2 密码，8 到 63 个字符）。留空会保持临时调试热点和 RTSP 服务关闭。请使用仅供本次开发调试的唯一密码，不要复用生产环境或公司 Wi-Fi 凭据。不要在值后面加注释：`=` 之后的全部内容都属于密码。`rootfs/config/` 中的其他 Wi-Fi 配置文件只包含占位值，应用在运行时写入 `hostapd.conf` 和 `wpa_supplicant.conf`。
6. **测试并编译应用**：先运行 `make test`，再运行 `make app`。只有在另行提供的已获许可格式化工具和全部完整镜像输入就绪后，才能运行 `make install` 或完整 `make`。完整镜像结果位于 `tools/ota/`：`update.bin`（OTA 升级包）、`ramfs.img` 和 `usr.jffs2`。BusyBox 和 `mtd_debug` 只编译一次，保存在 `rootfs/build/` 中；`make distclean` 会删除它们。

```{warning}
如果用 `ALLOW_LOCKED_ROOT=1 make` 生成不能从控制台登录的镜像，请注意：`update.bin` 也包含配置分区，用这种方式生成的 OTA 升级包会把已在使用的设备的 root 也锁定。
```

## 已知限制

- 只有 `apps/ai_glass_demo/common.mk` 中默认的功能开关组合可以编译；关闭 EIS、RTSP 或录像功能目前无法编译。
- mtd-utils 2.x 生成的 `usr.jffs2` 使用 8 KiB 擦除块（它不接受旧版内置工具使用的 4 KiB）。烧写后，请在开发板上确认配置分区挂载时没有 JFFS2 错误。

## 下一步

只有在已获许可的格式化工具就绪、完整镜像构建并验证后，才能按[固件烧写](firmware-flashing.md)把 `update.bin` 升级到产品板。
