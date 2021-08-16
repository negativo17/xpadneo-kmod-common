Name:           xpadneo-kmod-common
Version:        0.9.1
Release:        1%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPLv3
URL:            https://atar-axis.github.io/xpadneo

BuildArch:      noarch

Source0:        https://github.com/atar-axis/xpadneo/archive/refs/tags/v%{version}.tar.gz#/xpadneo-%{version}.tar.gz

# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       xpadneo-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       xpadneo-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.
 
%prep
%autosetup -p0 -n xpadneo-%{version}

%install
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_prefix}/lib/modprobe.d/

# Aliase:
install -p -m 0644 hid-xpadneo/etc-modprobe.d/xpadneo.conf %{buildroot}%{_prefix}/lib/modprobe.d/

# UDev rules:
install -p -m 644 hid-xpadneo/etc-udev-rules.d/60-xpadneo.rules %{buildroot}%{_udevrulesdir}/

%files
%{_prefix}/lib/modprobe.d/xpadneo.conf
%{_udevrulesdir}/60-xpadneo.rules

%changelog
* Mon Aug 16 2021 Simone Caronni <negativo17@gmail.com> - 0.9.1-1
- First build.
