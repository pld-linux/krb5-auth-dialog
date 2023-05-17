Summary:	Kerberos Network Authentication Dialog for GNOME
Summary(pl.UTF-8):	Okno dialogowe uwierzytelnienia do sieci Kerberos dla GNOME
Name:		krb5-auth-dialog
Version:	43.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/krb5-auth-dialog/43/%{name}-%{version}.tar.xz
# Source0-md5:	a141644febde84b456594d7d755c54e2
URL:		https://gitlab.gnome.org/GNOME/krb5-auth-dialog
BuildRequires:	NetworkManager-devel >= 1.0
BuildRequires:	gettext-tools
BuildRequires:	gcr-ui-devel >= 3.5.5
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gtk+3-devel >= 3.14
BuildRequires:	heimdal-devel
BuildRequires:	libcap-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.58
Requires:	glib2 >= 1:2.58
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
%meson build \
	-Dpkcs11=%{_libdir}/opensc/opensc-pkcs11.so

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome
# --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/krb5-auth-dialog
%dir %{_libdir}/krb5-auth-dialog
%dir %{_libdir}/krb5-auth-dialog/plugins
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-afs.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-dummy.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-gnomelock.so
%attr(755,root,root) %{_libdir}/krb5-auth-dialog/plugins/libka-plugin-pam.so
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_datadir}/metainfo/krb5-auth-dialog.metainfo.xml
%{_desktopdir}/org.gnome.KrbAuthDialog.desktop
%{_iconsdir}/hicolor/*/status/krb-*-ticket.*
/etc/xdg/autostart/krb5-auth-dialog.desktop
%{_mandir}/man1/krb5-auth-dialog.1*
