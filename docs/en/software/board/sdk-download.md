# SDK Download

The 1.0.0 release candidate uses this repository's Releases page to distribute the core KM02G SDK source and the upstream source archives needed by its build. The links below become usable only after the 1.0.0 release and named assets are published. A missing asset means its release gate is still pending.

Release base: `https://github.com/Anyka-Micro/anykavision-ai-docs-public/releases/download/1.0.0/`

## Included, required and pending inputs

| Input | 1.0.0 candidate state | Use |
|---|---|---|
| `anykavision-km02g-sdk-1.00.tar.gz` and `SHA256SUMS` | Clean-source candidate; publication requires final packaging and validation gates | Core KM02G SDK source, build scripts, middleware headers/libraries and demo application. Extracts to `anykavision-km02g-sdk-1.00/`; the unresolved legacy `rootfs/skeleton/etc/format_tool` artifact is removed |
| `busybox-1.35.0.tar.bz2`, `busybox-1.35.0.tar.bz2.sig`, `busybox-1.35.0.config`, `mtd-utils-2.3.1.tar.bz2`, `mtd-utils-2.3.1.tar.bz2.asc` | Candidate support assets; checksums verified, but detached signatures not independently verified because the public keys were unavailable during preparation | Put the two source archives in the SDK's `tools/` directory. The SDK source already contains the build config it uses |
| `riscv64-anyka-linux-musl.tar.gz` | Required to build, but not approved for public redistribution yet | Obtain the exact checksum-matched archive from Anyka and put it in the SDK's `tools/` directory. A public download can be added only after corresponding-source and licence checks pass |
| Licensed vendor formatter supplied through `FORMAT_TOOL_BIN` | Required for full ramdisk and firmware images; not included | Obtain it separately from Anyka under appropriate licence terms and pass its absolute path. The default fallback is `rootfs/vendor/format_tool`; the build copies the selected tool to image path `/etc/format_tool` |
| `ramfs.img` | Optional reference image; not part of the build input and not approved for publication yet | The clean public SDK cannot build it without the separately supplied licensed vendor formatter. Provenance/licence review and build validation must pass before a prebuilt image is published |
| Factory APP-partition scripts | Required for the factory USB update/UVC environment, but not supplied by this SDK | `/usr/sbin/usb_udc_g.sh` and `/usr/sbin/uvc.sh` must come from matching factory firmware |
| Anyka_Glasses app/source, AK1090 firmware and board design files | Pending | Not included in the 1.0.0 candidate; the developer can add them later |

The clean-source candidate omits the unresolved vendor formatter. Its packaging, SDK build, host tests, flashing, OTA, Wi-Fi and USB webcam operation are still pending validation.

## Developer quick start

Use an x86-64 Linux host. After the 1.0.0 release assets appear on the Releases page, download and verify the source archive and the two upstream source archives:

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

Obtain the required checksum-matched toolchain archive from Anyka while its public redistribution gate remains pending, then place it at `tools/riscv64-anyka-linux-musl.tar.gz`. Follow [Build Environment Setup](build-environment.md) to install it, run the host tests and build the application:

```bash
./scripts/get_toolchain.sh
export PATH="$PATH:/opt/riscv64-anyka-linux-musl/bin"
make test
make app
```

This public path does not produce firmware images. Full `make` and `make install` additionally require all full-image inputs and a separately supplied licensed formatter, passed without restoring the removed legacy artifact:

```bash
FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make
```

The SDK copies the selected formatter to image path `/etc/format_tool`; its default fallback is `rootfs/vendor/format_tool`. Any resulting `update.bin`, `ramfs.img` and `usr.jffs2` remain unverified development outputs until they pass the required board validation.
