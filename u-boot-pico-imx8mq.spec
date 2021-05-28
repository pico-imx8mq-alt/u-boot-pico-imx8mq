%define board pico-imx8mq

Name: u-boot-%board
Version: 2020.04_5.4.70
Release: alt1

Summary: Das U-Boot for TechNexion PICO IMX8MQ board
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

Patch1: pico-imx8mq-do-not-set-mmcblk-and-mmcroot-env-variab.patch
Patch2: pico-imx8mq-on-the-first-boot-expand-rootfs-partitio.patch

BuildRequires: flex bc

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.

This package supports PICO-8M board.

%prep
%setup

%patch1 -p1
%patch2 -p1

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
* Fri May 28 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2020.04_5.4.70-alt1
- updated to use tn-imx_v2020.04_5.4.70_2.3.0-stable upstream branch
- unused patches removed

* Tue Nov 03 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2018.03_4.14.98-alt3
- updated to use tn-imx_v2018.03_4.14.98_2.0.0_ga-stable upstream branch

* Thu Dec 26 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2018.03_4.14.98-alt2
- updated to use tn-imx_v2018.03_4.14.98_2.0.0_ga-wip-bootscript upstream branch

* Tue Jul 09 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2018.03_4.14.98-alt1
- initial build of U-Boot for TechNexion PICO IMX8MQ board
