# Build Environment Setup

This page explains the SDK build steps and their caveats. The exact commands are in the README inside the SDK source archive; this page does not repeat them. See [SDK Download](sdk-download.md) for the published asset list and remaining release gates.

## Build host

- x86-64 Linux, Ubuntu 18.04 or later. The toolchain runs only there; on macOS or Windows use a Linux VM or container. The packages to install are listed under **Host requirements** in the SDK README.
- Extract the SDK into a path **without spaces**: the Makefiles cannot handle them.
- `make test` (host-side unit tests) needs the host packages `gcc`, `libc6-dev` and `linux-libc-dev`.

## Build steps

Follow the **Build** section of the SDK README in order:

1. **Install the toolchain**: public redistribution of the toolchain remains gated. Obtain the exact checksum-matched `riscv64-anyka-linux-musl.tar.gz` from Anyka, put it in `tools/`, then run `./scripts/get_toolchain.sh`. The script checks its SHA-256 and unpacks it to `/opt`. Then add `/opt/riscv64-anyka-linux-musl/bin` to your `PATH`. To install elsewhere, pass the directory as the first argument; the script relocates the toolchain there.
2. **For full images, prepare the ramdisk sources**: put the verified `busybox-1.35.0.tar.bz2` and `mtd-utils-2.3.1.tar.bz2` release assets in `tools/`. Full `make` checks them and builds the ramdisk from those sources, `rootfs/skeleton/` and your `ai_glass_demo`. You can also set `SOURCES_URL` to an approved mirror.
3. **For full images, supply the licensed formatter**: the clean public archive removes the unresolved legacy `rootfs/skeleton/etc/format_tool` artifact. Obtain the approved V1.00 formatter separately from Anyka. It must be an executable file, passed by absolute path, with SHA-256 `6e608235637406349c5da89b0657ee9e3386ba55ee9175140c586d7718f01603`; the build rejects any other byte hash. For example, use `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make`. The default fallback is `rootfs/vendor/format_tool`; the build copies the approved tool to image path `/etc/format_tool`.
4. **For full images, set a root password**: the shipped configuration locks root, so image packaging stops until you set a password. Copy `rootfs/config/shadow` to `rootfs/config.local/` first, then put the password hash in the second field of its `root` line; do not edit the tracked `rootfs/config/shadow`. Files in `rootfs/config.local/` replace those of `rootfs/config/` in the config image, and git ignores the folder, so the hash is never committed. Use a unique strong password for each device or build, never ship a shared development password, and never commit or share the hash.
5. **Optional for full images: set the debug Wi-Fi password**: copy `apps/ai_glass_demo/common/config/app_main_config.ini` to `rootfs/config.local/` and set `password=` under `[DebugAp]` (a WPA2 passphrase, 8 to 63 characters). Leaving it empty keeps the temporary debug AP and RTSP service disabled. Use a unique development-only passphrase rather than a production or corporate Wi-Fi credential. Don't put a comment after the value: everything after `=` is part of it. The other Wi-Fi files in `rootfs/config/` hold placeholders only; the app writes `hostapd.conf` and `wpa_supplicant.conf` at run time.
6. **Test and build the application**: run `make test`, then `make app`. Run `make install` or full `make` only after the separately supplied licensed formatter and all full-image inputs are present. Full-image results are written under `tools/ota/`: `update.bin` (OTA package), `ramfs.img` and `usr.jffs2`. BusyBox and `mtd_debug` are built once and kept in `rootfs/build/`; `make distclean` removes them.

```{warning}
If you build an image with no console login using `ALLOW_LOCKED_ROOT=1 make`, be careful: `update.bin` also carries the config partition, so an OTA update built that way locks root on devices already in use.
```

## Known limitations

- Only the default feature switches in `apps/ai_glass_demo/common.mk` compile; turning EIS, RTSP or recording off does not build yet.
- mtd-utils 2.x builds `usr.jffs2` with 8 KiB erase blocks (it refuses the 4 KiB that the old bundled tool used). After flashing, check on your board that the config partition mounts without JFFS2 errors.

## Next step

Only after the licensed formatter is present and a full image has been built and validated, follow [Firmware Flashing](firmware-flashing.md) to update the reference board with `update.bin`.
