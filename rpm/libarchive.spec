Name:       libarchive
Summary:    A library for handling streaming archive formats
Version:    3.4.0
Release:    1
License:    BSD
URL:        http://code.google.com/p/libarchive/
Source0:    http://libarchive.googlecode.com/files/libarchive-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  bison
BuildRequires:  sharutils
BuildRequires:  bzip2-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n bsdtar
Summary:    Bsdtar is a program to create and read different streaming archive formats
Group:      Applications/Archiving
Requires:   %{name} = %{version}-%{release}

%description -n bsdtar
This package contains the bsdtar cmdline utility

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
build/autogen.sh

%configure --disable-static \
	   --disable-bsdcat \
	   --disable-bsdcpio

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

iconv -f latin1 -t utf-8 < NEWS > NEWS.utf8; cp NEWS.utf8 NEWS
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n bsdtar
%defattr(-,root,root,-)
%{_bindir}/bsdtar
