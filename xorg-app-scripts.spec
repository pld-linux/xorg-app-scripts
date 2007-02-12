Summary:	Few simple scripts
Summary(pl.UTF-8):	Kilka prostych skryptów
Name:		xorg-app-scripts
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/scripts-%{version}.tar.bz2
# Source0-md5:	08c7f078fc351196c21db3a8206d482d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	awk
Requires:	xorg-app-xauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Few simple scripts.

%description -l pl.UTF-8
Kilka prostych skryptów.

%prep
%setup -q -n scripts-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/fontname.sh
%attr(755,root,root) %{_bindir}/fontprop.sh
%attr(755,root,root) %{_bindir}/xauth_switch_to_sun-des-1
%attr(755,root,root) %{_bindir}/xon
%{_mandir}/man1/xon.1x*
