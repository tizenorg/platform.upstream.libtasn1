Name:           libtasn1
Version:        2.12
Release:        0
License:        LGPL-2.1+ and GPL-3.0
Summary:        ASN
Url:            http://ftp.gnu.org/gnu/libtasn1/
Group:          Productivity/Networking/Security
Source:         %{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  info
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the ASN.1 library used in GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%package devel
Summary:        ASN
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description devel
This is the ASN.1 library used in GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install


%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig


%docs_package

%files
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtasn1.pc

%changelog
