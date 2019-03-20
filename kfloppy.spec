# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kfloppy
Summary:	Format floppy disks
Version:	 18.12.3
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kfloppy
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5XmlGui)

%description
KFloppy is a utility that provides a straightforward graphical means to
format 3.5" and 5.25" floppy disks.

%files -f kfloppy.lang
%{_bindir}/kfloppy
%{_datadir}/icons/*/*/apps/kfloppy.*
%{_datadir}/applications/org.kde.kfloppy.desktop
%{_sysconfdir}/xdg/kfloppy.categories
%{_datadir}/metainfo/org.kde.kfloppy.appdata.xml

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang kfloppy --with-html
