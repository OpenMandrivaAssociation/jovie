Summary:	KTTS - KDE Text-to-Speech
Name:		jovie
Version:	15.04.3
Release:	2
Epoch:		2
License:	LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
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
%{_datadir}/appdata/jovie.appdata.xml
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
