%define board pico-imx8mq

Name: u-boot-%board
Version: 2018.03_4.14.98
Release: alt1

Summary: Das U-Boot for TechNexion PICO IMX8MQ board
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

Patch1: 0001-pico-imx8mq-perform-FEC-and-its-PHY-configuration-mo.patch
Patch2: 0002-pico-imx8mq-do-not-set-mmcblk-and-mmcroot-env-variab.patch
Patch3: 0003-pico-imx8mq-update-boot-settings-to-comply-with-ALT-.patch
Patch4: 0004-pico-imx8mq-double-environment-size.patch
Patch5: 0005-pico-imx8mq-enable-gpt-and-part-commands.patch
Patch6: 0006-pico-imx8mq-on-the-first-boot-expand-rootfs-partitio.patch

BuildRequires: dtc >= 1.4 flex bc

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.

This package supports PICO-8M board.

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%make_build %{board}_defconfig all

%install
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/%{board}/u-boot.bin
install -pm0644 -D u-boot-nodtb.bin %buildroot%_datadir/u-boot/%{board}/u-boot-nodtb.bin
install -pm0644 -D spl/u-boot-spl.bin %buildroot%_datadir/u-boot/%{board}/u-boot-spl.bin
install -pm0644 -D arch/arm/dts/imx8mq-pico-pi.dtb %buildroot%_datadir/u-boot/%{board}/imx8mq-pico-pi.dtb

%files
%doc README
%_datadir/u-boot/*

%changelog
* Tue Jul 09 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2018.03_4.14.98-alt1
- initial build of U-Boot for TechNexion PICO IMX8MQ board
