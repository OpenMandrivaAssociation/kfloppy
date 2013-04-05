# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kfloppy
Summary:	Format floppy disks
Version:	4.10.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kfloppy
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

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
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Thu Jul 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758054
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744535
- New upstream tarball

* Mon Dec 12 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-2
+ Revision: 740446
- Workaround a rpm5 new bug
- New upstream tarball

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733057
- Import kfloppy
- Create folder

