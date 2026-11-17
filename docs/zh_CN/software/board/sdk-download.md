# SDK下载

1.0.0 候选版本计划通过本仓库的 Releases 页面分发 KM02G SDK 核心源码，以及编译所需的上游源码附件。只有在 1.0.0 Release 和对应附件正式发布后，下方链接才可使用。附件不存在表示其发布门禁尚未通过。

Release 基础地址：`https://github.com/Anyka-Micro/anykavision-ai-docs-public/releases/download/1.0.0/`

## 已包含、必需和待提供的输入

| 输入 | 1.0.0 候选状态 | 用途 |
|---|---|---|
| `anykavision-km02g-sdk-1.00.tar.gz` 和 `SHA256SUMS` | 清洁源码候选包；发布前须通过最终打包和验证门禁 | KM02G SDK 核心源码、编译脚本、中间件头文件/库和示例应用；解压后的顶层目录为 `anykavision-km02g-sdk-1.00/`；已移除来源和许可未解决的旧版 `rootfs/skeleton/etc/format_tool` 文件 |
| `busybox-1.35.0.tar.bz2`、`busybox-1.35.0.tar.bz2.sig`、`busybox-1.35.0.config`、`mtd-utils-2.3.1.tar.bz2`、`mtd-utils-2.3.1.tar.bz2.asc` | 候选辅助附件；校验和已验证，但准备环境缺少公钥，未独立验证分离签名 | 将两个源码压缩包放入 SDK 的 `tools/` 目录；SDK 源码中已包含编译实际使用的配置 |
| `riscv64-anyka-linux-musl.tar.gz` | 编译必需，但尚未获准公开再分发 | 向安凯获取校验和匹配的压缩包，放入 SDK 的 `tools/` 目录。完成对应源码和许可证核验后才能补充公开下载 |
| 通过 `FORMAT_TOOL_BIN` 提供的已获许可厂商格式化工具 | 完整 ramdisk 和固件镜像必需；不包含在内 | 请按适当的许可条款另行向安凯获取并传入其绝对路径。默认回退路径为 `rootfs/vendor/format_tool`；构建时会把选定工具复制到镜像内的 `/etc/format_tool` |
| `ramfs.img` | 可选参考镜像，不是编译输入；尚未获准发布 | 清洁公开 SDK 缺少另行提供的已获许可厂商格式化工具，无法单独生成该镜像。预编译镜像必须先通过来源/许可证审查和编译验证 |
| 出厂 APP 分区脚本 | 出厂 USB 升级/UVC 环境需要，但本 SDK 不提供 | `/usr/sbin/usb_udc_g.sh` 和 `/usr/sbin/uvc.sh` 必须来自匹配的出厂固件 |
| Anyka_Glasses APP/源码、AK1090 固件和产品板设计文件 | 待提供 | 不包含在 1.0.0 候选版本中；开发者可在后续版本补充 |

清洁源码包的打包和源码导出审查已通过。在离线 Ubuntu 22.04 x86-64 内部验证环境中，使用现有但不公开分发的工具链，`make test`（`list_test` 和在 ASan/UBSan 下运行的 `uvc_test`）以及面向 RISC-V 的 `make app` 均已通过。这不代表工具链已获准公开再分发；其许可证门禁仍未通过。由于未提供已获许可的格式化工具，完整 `ALLOW_LOCKED_ROOT=1 make` 按预期在生成镜像前停止。完整镜像、烧写、OTA、Wi-Fi 和 USB 摄像头硬件功能仍未验证。

## 开发者快速开始

请使用 x86-64 Linux 主机。1.0.0 Release 附件出现在 Releases 页面后，下载并校验 SDK 源码包和两个上游源码包：

```bash
release_base=https://github.com/Anyka-Micro/anykavision-ai-docs-public/releases/download/1.0.0
for asset in SHA256SUMS anykavision-km02g-sdk-1.00.tar.gz \
  busybox-1.35.0.tar.bz2 mtd-utils-2.3.1.tar.bz2; do
  curl --fail --location --remote-name "$release_base/$asset"
done
grep -E ' (anykavision-km02g-sdk-1.00.tar.gz|busybox-1.35.0.tar.bz2|mtd-utils-2.3.1.tar.bz2)$' SHA256SUMS | sha256sum --check -
tar -xzf anykavision-km02g-sdk-1.00.tar.gz
mv busybox-1.35.0.tar.bz2 mtd-utils-2.3.1.tar.bz2 anykavision-km02g-sdk-1.00/tools/
cd anykavision-km02g-sdk-1.00
```

交叉工具链公开再分发门禁通过前，请向安凯获取校验和匹配的工具链压缩包，并将其放到 `tools/riscv64-anyka-linux-musl.tar.gz`。按[编译环境配置](build-environment.md)安装工具链、运行主机端测试并编译应用：

```bash
./scripts/get_toolchain.sh
export PATH="$PATH:/opt/riscv64-anyka-linux-musl/bin"
make test
make app
```

此公开流程不生成固件镜像。完整 `make` 和 `make install` 还需要全部完整镜像输入，以及另行提供且已获许可的厂商格式化工具；通过变量传入，不要恢复已移除的旧版文件：

```bash
FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make
```

SDK 会把选定的格式化工具复制到镜像内的 `/etc/format_tool`；默认回退路径为 `rootfs/vendor/format_tool`。生成的 `update.bin`、`ramfs.img` 和 `usr.jffs2` 在通过所需的开发板验证前，均属于未经验证的开发输出。
