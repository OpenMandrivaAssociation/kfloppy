# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kfloppy
Summary:	Format floppy disks
Version:	16.04.0
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kfloppy
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

%description
KFloppy is a utility that provides a straightforward graphical means to
format 3.5" and 5.25" floppy disks.

%files
%{_kde_bindir}/kfloppy
%{_kde_iconsdir}/*/*/apps/kfloppy.*
%{_datadir}/applications/org.kde.kfloppy.desktop
%{_kde_docdir}/HTML/*/kfloppy

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
