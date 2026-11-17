# Build Environment Setup

This page explains the SDK build steps and their caveats. The exact commands are in the SDK README supplied with the developer-provided package; this page does not repeat them. See [SDK Download](sdk-download.md) for the current availability status.

## Build host

- x86-64 Linux, Ubuntu 18.04 or later. The toolchain runs only there; on macOS or Windows use a Linux VM or container. The packages to install are listed under **Host requirements** in the SDK README.
- Clone the SDK into a path **without spaces**: the Makefiles cannot handle them.
- `make test` (host-side unit tests) also needs `linux-libc-dev`.

## Build steps

Follow the **Build** section of the SDK README in order:

1. **Install the toolchain**: run `./scripts/get_toolchain.sh`. When public release assets are available, it downloads the cross toolchain, checks its SHA-256 and unpacks it to `/opt`. Until then, obtain the archive from the developer and put it in `tools/` first; the script checks its SHA-256 and skips the download. Then add `/opt/riscv64-anyka-linux-musl/bin` to your `PATH`. To install elsewhere, pass the directory as the first argument; the script relocates the toolchain there.
2. **Nothing to download for the ramdisk**: `make` builds it from the files in `rootfs/skeleton/`, BusyBox 1.35.0 and `mtd_debug` (mtd-utils 2.3.1) built from source, and your `ai_glass_demo`. The first build downloads the two source archives into `tools/` and checks their SHA-256; to build offline, put them in `tools/` yourself or set `SOURCES_URL` to a mirror.
3. **Set a root password**: the shipped configuration locks root, so the build stops until you set a password. Copy `rootfs/config/shadow` to `rootfs/config.local/` first, then put the password hash in the second field of its `root` line; do not edit the tracked `rootfs/config/shadow`. Files in `rootfs/config.local/` replace those of `rootfs/config/` in the config image, and git ignores the folder, so the hash is never committed. Use a unique strong password for each device or build, never ship a shared development password, and never commit or share the hash.
4. **Optional: set the debug Wi-Fi password**: copy `apps/ai_glass_demo/common/config/app_main_config.ini` to `rootfs/config.local/` and set `password=` under `[DebugAp]` (a WPA2 passphrase, 8 to 63 characters). Leaving it empty keeps the temporary debug AP and RTSP service disabled. Use a unique development-only passphrase rather than a production or corporate Wi-Fi credential. Don't put a comment after the value: everything after `=` is part of it. The other Wi-Fi files in `rootfs/config/` hold placeholders only; the app writes `hostapd.conf` and `wpa_supplicant.conf` at run time.
5. **Build**: run `make`. The results are in `tools/ota/`: `update.bin` (OTA package), `ramfs.img` and `usr.jffs2`. `make app` builds only the application; `make install` packs the images and needs a built application; `make test` runs the host-side tests. BusyBox and `mtd_debug` are built once and kept in `rootfs/build/`; `make distclean` removes them.

```{warning}
If you build an image with no console login using `ALLOW_LOCKED_ROOT=1 make`, be careful: `update.bin` also carries the config partition, so an OTA update built that way locks root on devices already in use.
```

## Known limitations

- Only the default feature switches in `apps/ai_glass_demo/common.mk` compile; turning EIS, RTSP or recording off does not build yet.
- mtd-utils 2.x builds `usr.jffs2` with 8 KiB erase blocks (it refuses the 4 KiB that the old bundled tool used). After flashing, check on your board that the config partition mounts without JFFS2 errors.

## Next step

When the build finishes, follow [Firmware Flashing](firmware-flashing.md) to update the reference board with `update.bin`.
