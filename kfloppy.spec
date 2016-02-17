# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kfloppy
Summary:	Format floppy disks
Version:	15.12.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kfloppy
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

%description
KFloppy is a utility that provides a straightforward graphical means to
format 3.5" and 5.25" floppy disks.

%files
%{_kde_bindir}/kfloppy
%{_kde_iconsdir}/*/*/apps/kfloppy.*
%{_kde_applicationsdir}/KFloppy.desktop
%{_kde_docdir}/HTML/*/kfloppy

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
