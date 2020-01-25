#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Parallel
%define		pnam	ForkManager
Summary:	Parallel::ForkManager - A simple parallel processing fork manager
Summary(pl.UTF-8):	Parallel::ForkManager - prosty zarządca tworzenia procesów do równoległego przetwarzania
Name:		perl-Parallel-ForkManager
Version:	0.7.9
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b49dbc6fafb697945d33ffbded0009f7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
URL:		http://search.cpan.org/dist/Parallel-ForkManager/
Requires:	perl-dirs >= 2.1-19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended for use in operations that can be done in
parallel where the number of processes to be forked off should be
limited. Typical use is a downloader which will be retrieving
hundreds/thousands of files.

%description -l pl.UTF-8
Ten moduł jest przeznaczony do używania w operacjach, które można
wykonywać równolegle, kiedy liczba procesów do uruchomienia powinna
być ograniczona. Typowe wykorzystanie to narzędzie do ściągania
plików, które ma ciągnąć setki/tysiące plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Parallel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
