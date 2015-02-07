Summary:	KTTS - KDE Text-to-Speech
Name:		jovie
Version:	14.12.2
Release:	1
Epoch:		2
License:	LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	speech-dispatcher-devel
Obsoletes:	kdeaccessibility4-core < 2:4.5.71
Obsoletes:	kdeaccessibility4 < 2:4.5.71
Obsoletes:	kttsd < 2:4.5.71

%description
Jovie is a subsystem within the KDE desktop for
conversion of text to audible speech. Jovie is currently under development
and aims to become the standard subsystem for all KDE applications
to provide speech output.
User Features:
 * Speak any text from the KDE clipboard.
 * Speak any plain text file.
 * Speak all or any portion of a text file from Kate.
 * Speak all or any portion of an HTML page from Konqueror.
 * Use as the speech backend for KMouth and KSayIt.
 * Speak KDE notifications (KNotify).
 * Long text is parsed into sentences. User may backup by sentence or
    paragraph, replay, pause, and stop playing.
 * Audio output via GStreamer (version 0.8.7 or later)

%files
%doc %{_kde_docdir}/HTML/en/jovie
%{_kde_bindir}/jovie
%{_kde_applicationsdir}/jovieapp.desktop
%{_kde_libdir}/kde4/kcm_kttsd.so
%{_kde_libdir}/kde4/jovie_stringreplacerplugin.so
%{_kde_libdir}/kde4/jovie_talkerchooserplugin.so
%{_kde_libdir}/kde4/jovie_xmltransformerplugin.so
%{_kde_appsdir}/jovie
%{_kde_iconsdir}/*/*/actions/female.png
%{_kde_iconsdir}/*/*/actions/male.png
%{_kde_iconsdir}/*/*/actions/nospeak.png
%{_kde_iconsdir}/*/*/actions/speak.png
%{_kde_services}/jovie.desktop
%{_kde_services}/jovie_stringreplacerplugin.desktop
%{_kde_services}/jovie_talkerchooserplugin.desktop
%{_kde_services}/jovie_xmltransformerplugin.desktop
%{_kde_services}/kcmkttsd.desktop
%{_kde_services}/kttsd.desktop
%{_kde_servicetypes}/jovie_filterplugin.desktop

#-----------------------------------------------------------------------------

%define kttsd_major 4
%define libkttsd %mklibname kttsd %{kttsd_major}

%package -n %{libkttsd}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkttsd}
KDE 4 library.

%files -n %{libkttsd}
%{_kde_libdir}/libkttsd.so.%{kttsd_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkttsd} = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libkttsd.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0
- Update files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5
- Drop BuildRequires libespeak-devel (no longer needed)

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Tue Jul 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- Add Obeoletes for kttsd, kdeaccessibility4-core and kdeaccessibility4
- Add Epoch 2 for updates purpose
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 762445
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762445
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758036
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744512
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739348
- New upstream tarball

* Wed Nov 30 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 735553
- imported package jovie

