Summary:	Analyze OpenPGP style keyrings
Summary(pl):	Analiza pier¶cieni kluczów w formacie OpenPGP
Name:		keyanalyze
Version:	200204
Release:	1
License:	GPL	
Group:		Application
Source0:	http://dtype.org/keyanalyze/code/%{name}-%{version}.tar.gz
# Source0-md5:	46c1928c0ed298696f9f06b747fa0e85
Patch0:		%{name}-analyze.sh.patch
Patch1:		%{name}-keyanalyze.c.patch
Patch2:		%{name}-pgpring.patch
Patch3:		%{name}-process_keys.c.patch
URL:		http://dtype.org/keyanalyze/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyanalyze is designed to analyze keyrings in the OpenPGP format (PGP
and GnuPG). It looks at properties of connectivity to generate
strongly-connected set analysis, as well as some arbitrary statistics
including a "mean shortest distance" calculation to show the most
connected keys. This code is also used to create a report based on an
extremely large keyset once per month.

#%description -l pl

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd pgpring
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} 
cd ..
%{__make} keyanalyze process_keys \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
cd pgpring
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..
install keyanalyze process_keys $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{_bindir}/*
