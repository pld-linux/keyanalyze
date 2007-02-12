Summary:	Analyze OpenPGP style keyrings
Summary(pl.UTF-8):   Analiza pierścieni kluczy w formacie OpenPGP
Name:		keyanalyze
Version:	200204
Release:	3
License:	GPL
Group:		Applications
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

%description -l pl.UTF-8
Keyanalyze służy do analizy pierścieni kluczy w formacie OpenPGP (PGP
i GnuPG). Przegląda własności łączące do wygenerowania analizy silnie
połączonych zbiorów, a także pewnych statystyk, w tym obliczenia
"średniej najkrótszej odległości", aby pokazać najbardziej połączone
klucze. Ten kod służy także do tworzenia raportów miesięcznych w
oparciu o bardzo duże zbiory kluczy.

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
