#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Parallel
%define	pnam	ForkManager
Summary:	Parallel::ForkManager - A simple parallel processing fork manager
Summary(pl):	Parallel::ForkManager - prosty zarz�dca tworzenia proces�w do r�wnoleg�ego przetwarzania
Name:		perl-Parallel-ForkManager
Version:	0.7.5
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec12f36370329e2c235284f5cb4ed427
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended for use in operations that can be done in
parallel where the number of processes to be forked off should be
limited. Typical use is a downloader which will be retrieving
hundreds/thousands of files.

%description -l pl
Ten modu� jest przeznaczony do u�ywania w operacjach, kt�re mo�na
wykonywa� r�wnolegle, kiedy liczba proces�w do uruchomienia powinna
by� ograniczona. Typowe wykorzystanie to narz�dzie do �ci�gania
plik�w, kt�re ma ci�gn�� setki/tysi�ce plik�w.

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

mv $RPM_BUILD_ROOT{%{perl_vendorlib}/Parallel/ForkManager/*.pl,%{_examplesdir}/%{name}-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%dir %{perl_vendorlib}/Parallel
%{perl_vendorlib}/Parallel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}