Summary:	OpenOffice.org nested in KDE
Name:		cuckooo
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/Office
Source0:	http://artax.karlin.mff.cuni.cz/~kendy/cuckooo/download/cuckooo-0.3.tar.gz
# Source0-md5:	774bacad4574445d163a75e826665a6c
URL:		http://artax.karlin.mff.cuni.cz/~kendy/cuckooo/
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	openoffice-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE Part, which allows OpenOffice.org to be run in a Konqueror window. 

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--with-office-dir=%{_prefix} \
	--with-ODK-dir=%{_prefix} \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/*.la
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*/*/apps/*.png
