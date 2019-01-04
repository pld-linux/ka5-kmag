%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kmag
Summary:	kmag
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a28d279ead36124c41902397513b0afd
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kio-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMag is a small utility for Linux to magnify a part of the screen.
KMag is very useful for people with visual disabilities and for those
working in the fields of image analysis, web development etc.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_desktopdir}/org.kde.kmag.desktop
%{_iconsdir}/hicolor/16x16/apps/kmag.png
%{_iconsdir}/hicolor/32x32/apps/kmag.png
%{_datadir}/kmag
%{_datadir}/kxmlgui5/kmag
%lang(ca) %{_mandir}/ca/man1/kmag.1*
%lang(de) %{_mandir}/de/man1/kmag.1*
%lang(es) %{_mandir}/es/man1/kmag.1*
%lang(et) %{_mandir}/et/man1/kmag.1*
%lang(fr) %{_mandir}/fr/man1/kmag.1*
%lang(it) %{_mandir}/it/man1/kmag.1*
%lang(C) %{_mandir}/man1/kmag.1*
%lang(nl) %{_mandir}/nl/man1/kmag.1*
%lang(pt) %{_mandir}/pt/man1/kmag.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmag.1*
%lang(ru) %{_mandir}/ru/man1/kmag.1*
%lang(sv) %{_mandir}/sv/man1/kmag.1*
%lang(uk) %{_mandir}/uk/man1/kmag.1*
%{_datadir}/metainfo/org.kde.kmag.appdata.xml
