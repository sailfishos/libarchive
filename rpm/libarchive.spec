Name:       libarchive
Summary:    A library for handling streaming archive formats
Version:    3.7.4
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/libarchive
Source0:    libarchive-%{version}.tar.gz
Patch1:     0001-rar4-reader-protect-copy_from_lzss_window_to_unp-217.patch
Patch2:     0002-Fix-CVE-2024-26256-2269.patch
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
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n bsdtar
Summary:    Bsdtar is a program to create and read different streaming archive formats
Requires:   %{name} = %{version}-%{release}

%description -n bsdtar
This package contains the bsdtar cmdline utility

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
build/autogen.sh

%configure --disable-static \
	   --disable-bsdcat \
	   --disable-bsdcpio \
	   --disable-bsdunzip

%make_build

%install
%make_install

iconv -f latin1 -t utf-8 < NEWS > NEWS.utf8; cp NEWS.utf8 NEWS
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n bsdtar
%{_bindir}/bsdtar
