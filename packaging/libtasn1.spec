Name:           libtasn1
Version:        2.14
Release:        0
License:        LGPL-2.1+ and GPL-3.0
Summary:        ASN
Url:            http://ftp.gnu.org/gnu/libtasn1/
Group:          Security/Crypto Libraries
Source:         %{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  info
BuildRequires:  pkg-config

%description
This is the ASN.1 library used in GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%package tools
Summary:        ASN
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description tools
This is the ASN.1 library used in GNUTLS. More up to date information
can be found at http://www.gnu.org/software/gnutls and
http://www.gnutls.org

%package devel
Summary:        ASN
Group:          Development/Libraries
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


%files tools
%defattr(-, root, root)
%{_bindir}/*

%files
%defattr(-, root, root)
%license COPYING COPYING.LIB
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtasn1.pc

%changelog