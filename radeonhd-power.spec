Name:	radeonhd-power
Version:	1.0
Release:	1%{?dist}
Summary:	Configures the radeon open-source driver's power management

Group:		User Interface/X Hardware Support
License:	MIT
URL:		https://github.com/pwnall/radeonhd-power
Source0:	https://github.com/pwnall/radeonhd-power/tarball/v%{version}

# BuildRequires:	
Requires:	systemd

%description
radeonhd-power is a convenience script for writing to the sysfs
files provided by the radeon open-source driver.

%prep
tar -xzf %{_sourcedir}/v%{version}
mv pwnall-radeonhd-power-* %{name}-%{version}
%setup -q -T -D -n %{name}-%{version}


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
* Sun May 6 2010 Victor Costan <victo@costan.us> - 1.0
- Initial release.
