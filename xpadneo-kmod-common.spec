%global commit0 be65dbb793b09241c4a525ce3363f797672b3301
%global date 20241101
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

%global real_name xpadneo

Name:           %{real_name}-kmod-common
Version:        0.9.6%{!?tag:^%{date}git%{shortcommit0}}
Release:        4%{?dist}
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
install -p -m 644 hid-%{real_name}/etc-udev-rules.d/*.rules %{buildroot}%{_udevrulesdir}/

%files
%license LICENSE
%doc docs/*.md
%{_prefix}/lib/modprobe.d/%{real_name}.conf
%{_udevrulesdir}/60-%{real_name}.rules
%{_udevrulesdir}/70-%{real_name}-disable-hidraw.rules

%changelog
* Mon Nov 04 2024 Simone Caronni <negativo17@gmail.com> - 0.9.6^20241101gitbe65dbb-4
- Update to latest snapshot.
- Add new udev rule to fix misdetection in Steam Input / Steamlink.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 0.9.6^20240923git70ef8ee-3
- Use new packaging guidelines for snapshots.

* Mon May 13 2024 Simone Caronni <negativo17@gmail.com> - 0.9.6-2.20240423git73be2eb
- Update to latest snapshot.

* Sat Feb 17 2024 Simone Caronni <negativo17@gmail.com> - 0.9.6-1
- Update to final 0.9.6.

* Wed Jun 21 2023 Simone Caronni <negativo17@gmail.com> - 0.9.5-2.20230617git5970c4c
- Update to latest snapshot.

* Wed Sep 21 2022 Simone Caronni <negativo17@gmail.com> - 0.9.5-1
- Update to 0.9.5.

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
