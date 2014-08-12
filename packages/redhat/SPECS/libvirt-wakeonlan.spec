Name:           libvirt-wakeonlan
Version:        %{_version}
Release:        1
Summary:        Starts KVM instances from wake on lan packets

License:        GPLv3+
URL:            http://lvwol.niftiestsoftware.com
Source0:        http://lvwol.niftiestsoftware.com/libvirt-wakeonlan-%{_version}.tar.bz2

BuildArch:      noarch
BuildRequires:  make
Requires:       libvirt-python,libvirt

%description
Daemon that starts KVM instances from wake on lan packets.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%attr(644, root, root) %{_usr}/share/libvirt-wakeonlan/*.py
%attr(644, root, root) %{_usr}/share/libvirt-wakeonlan/testing/*.sh
%attr(744, root, root) %{_sysconfdir}/init.d/libvirt-wakeonlan
%attr(744, root, root) %{_sysconfdir}/sysconfig/libvirt-wakeonlan

%changelog
* Sat Aug 09 2014 Simon Cadman <src@niftiestsoftware.com> 20140809-1)
- RPM package release
