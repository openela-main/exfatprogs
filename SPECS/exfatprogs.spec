Name:           exfatprogs
Version:        1.1.3
Release:        3%{?dist}
Summary:        Userspace utilities for exFAT filesystems
License:        GPLv2
URL:            https://github.com/%{name}/%{name}

Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-fsck-fix-memory-leak.patch
Patch1:         0002.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
Utilities for formatting and repairing exFAT filesystems.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/dump.exfat
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/dump.exfat.*
%{_mandir}/man8/exfatlabel.*
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*

%changelog
* Tue May 24 2022 Pavel Reichl <preichl@redhat.com> - 1.1.3-3.test
- Fix some covscan issues

* Mon May 09 2022 Pavel Reichl <preichl@redhat.com> - 1.1.3-2
- Fix memomry leak

* Wed Apr 20 2022 Pavel Reichl <preichl@redhat.com> - 1.1.3-1
- Rebase

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.2-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 1 2021 Pavel Reichl <preichl@redhat.com> - 1.1.2-1
- First build.
