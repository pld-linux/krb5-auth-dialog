Summary:	Kerberos Network Authentication Dialog for GNOME
Summary(pl.UTF-8):	Okno dialogowe uwierzytelnienia do sieci Kerberos dla GNOME
Name:		krb5-auth-dialog
Version:	3.20.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/krb5-auth-dialog/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	5eac2f521361e45c818aa9d695dd5902
URL:		http://live.gnome.org/GnomeKeyring
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gtk+3-devel >= 3.14
BuildRequires:	heimdal-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcap-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.14
Requires:	libnotify >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kerberos Authentication Dialog allows you to list your current
Kerberos tickets, and to request a new ticket (authenticate to the
Kerberos Server). It also notifies you when your Kerberos credentials
are about to expire and renews your ticket automatically if possible.

%description -l pl.UTF-8
Kerberos Authentication Dialog pozwala na wypisywanie bieżących
biletów Kerberosa oraz żądanie nowego biletu (uwierzytelnienie do
serwera Kerberosa). Powiadamia także w przypadku zbliżającego się
przedawnienia danych uwierzytelniających Kerberosa oraz automatycznie
odnawia bilet, jeśli jest to możliwe.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-network-manager \
	--disable-silent-rules \
	--disable-static \
	--with-pkcs11=%{_libdir}/opensc/opensc-pkcs11.so

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/krb5-auth-dialog/plugins/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/krb5-auth-dialog
%dir %{_libdir}/krb5-auth-dialog
%dir %{_libdir}/krb5-auth-dialog/plugins
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-afs.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-dummy.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-gnomelock.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-pam.so
%{_datadir}/GConf/gsettings/org.gnome.KrbAuthDialog.convert
%{_datadir}/appdata/krb5-auth-dialog.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_desktopdir}/krb5-auth-dialog.desktop
%{_iconsdir}/hicolor/*/status/krb-*-ticket.*
/etc/xdg/autostart/krb5-auth-dialog.desktop
%{_mandir}/man1/krb5-auth-dialog.1*
