Name:	radeonhd-power
Version:	1.0
Release:	1%{?dist}
Summary:	Configures the radeon open-source driver's power management

Group:		User Interface/X Hardware Support
License:	MIT
URL:		https://github.com/pwnall/radeonhd-power
Source0:	https://github.com/pwnall/radeonhd-power/archive/radeonhd-power-v%{version}.tar.gz

BuildArch: noarch

# BuildRequires:
Requires:	systemd

%description
radeonhd-power is a convenience script for writing to the sysfs
files provided by the radeon open-source driver.

%prep
%setup -q -n radeonhd-power-radeonhd-power-v%{version}


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/usr


%files
%{_bindir}/radeonhd-power
%{_prefix}/lib/systemd/system/radeonhd-power.service
%doc



%changelog
* Mon Mar 25 2013 Victor Costan <victo@costan.us> - 1.0
- Initial release.
