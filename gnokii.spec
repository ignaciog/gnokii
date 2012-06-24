Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narz�dzi dla telefon�w kom�rkowych Nokia
Name:		gnokii
Version:	0.3.3
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.gnokii.org/pub/gnokii/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_gettext_fixes.patch
URL:		http://www.gnokii.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for Nokia's mobile phones, released under the GPL.

%description -l pl
Gnokii jest zestawem narz�dzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefon�w kom�rkowych Nokia, dost�pnym na
licencji GPL.

%package X11
Summary:	Graphical Linux/Unix tool suite for Nokia mobile phones.
Summary(pl):	Zestaw narz�dzi z graficznym interfejsem dla telefon�w kom�rkowych Nokia.
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	%{name} = %{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for Nokia's mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Gnokii-X11 jest zestawem narz�dzi z graficznym interfejsem u�ytkownika
do pracy z telefonami kom�rkowymi Nokia. Pozwalaj� one na edytowanie
spisu telefon�w, wysy�anie/czytanie wiadomo�ci SMS i wiele innych
rzeczy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
aclocal
autoconf
automake -a -c || :
%configure \
	--enable-security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/gnokii} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/{bin,lib/xgnokii},%{_sysconfdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

gzip -9nf Docs/{CREDITS,DataCalls-QuickStart,README{,-{3810,6110}}} \
	Docs/{sample/gnokiirc,gnokii-ir-howto} \
	TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/*.gz Docs/gnokii.nol
%doc *.gz
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_sbindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%config(noreplace) %{_sysconfdir}/gnokiirc

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/xgnokii
#%attr(755,root,root) %{_prefix}/X11R6/bin/xlogos
%{_prefix}/X11R6/lib/xgnokii
