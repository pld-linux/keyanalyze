Summary:	Analyze OpenPGP style keyrings
Summary(pl):	Analiza pier¶cieni kluczy w formacie OpenPGP
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
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyanalyze is designed to analyze keyrings in the OpenPGP format (PGP
and GnuPG). It looks at properties of connectivity to generate
strongly-connected set analysis, as well as some arbitrary statistics
including a "mean shortest distance" calculation to show the most
connected keys. This code is also used to create a report based on an
extremely large keyset once per month.

%description -l pl
Keyanalyze s³u¿y do analizy pier¶cieni kluczy w formacie OpenPGP (PGP
i GnuPG). Przegl±da w³asno¶ci ³±cz±ce do wygenerowania analizy silnie
po³±czonych zbiorów, a tak¿e pewnych statystyk, w tym obliczenia
"¶redniej najkrótszej odleg³o¶ci", aby pokazaæ najbardziej po³±czone
klucze. Ten kod s³u¿y tak¿e do tworzenia raportów miesiêcznych w
oparciu o bardzo du¿e zbiory kluczy.

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

%{__make} -C pgpring install \
	DESTDIR=$RPM_BUILD_ROOT

install keyanalyze process_keys $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
