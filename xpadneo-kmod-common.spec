%global commit0 74ea7c1488f9ccebf3ed6d9aea1319cacb08c625
%global date 20220430
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

%global real_name xpadneo

Name:           %{real_name}-kmod-common
Version:        0.9.4
Release:        1%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPLv3
URL:            https://atar-axis.github.io/%{real_name}

BuildArch:      noarch

%if 0%{?tag:1}
Source0:    https://github.com/atar-axis/%{real_name}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
%else
Source0:    https://github.com/atar-axis/%{real_name}/archive/%{commit0}.tar.gz#/%{real_name}-%{shortcommit0}.tar.gz
%endif

# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.
 
%prep
%if 0%{?tag:1}
%autosetup -p1 -n %{real_name}-%{version}
%else
%autosetup -p1 -n %{real_name}-%{commit0}
%endif

%install
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_prefix}/lib/modprobe.d/

# Aliases:
install -p -m 0644 hid-%{real_name}/etc-modprobe.d/%{real_name}.conf %{buildroot}%{_prefix}/lib/modprobe.d/

# UDev rules:
install -p -m 644 hid-%{real_name}/etc-udev-rules.d/60-%{real_name}.rules %{buildroot}%{_udevrulesdir}/

%files
%license LICENSE
%doc NEWS.md docs/*.md
%{_prefix}/lib/modprobe.d/%{real_name}.conf
%{_udevrulesdir}/60-%{real_name}.rules

%changelog
* Wed Jun 29 2022 Simone Caronni <negativo17@gmail.com> - 0.9.4-1
- Update to 0.9.4.

* Wed Jun 01 2022 Simone Caronni <negativo17@gmail.com> - 0.9.3-1
- Update to release 0.9.3.

* Sun May 01 2022 Simone Caronni <negativo17@gmail.com> - 0.9.1-4.20220430git74ea7c1
- Update to latest snapshot, supports firmware 5.13.

* Sun Mar 20 2022 Simone Caronni <negativo17@gmail.com> - 0.9.1-3.20220306git4fd620c
- Update to latest snapshot, adds support for BLE firmware.

* Mon Aug 16 2021 Simone Caronni <negativo17@gmail.com> - 0.9.1-2
- Add docs.

* Mon Aug 16 2021 Simone Caronni <negativo17@gmail.com> - 0.9.1-1
- First build.
