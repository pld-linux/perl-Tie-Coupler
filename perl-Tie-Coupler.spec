#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	Coupler
Summary:	Tie::Coupler - Tie based implementation of coupled scalars
Summary(pl.UTF-8):	Tie::Coupler - implementacja par skalarów bazująca na Tie
Name:		perl-Tie-Coupler
Version:	0.01
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34537d1e9fc070003ea3be50b40fb813
URL:		http://search.cpan.org/dist/Tie-Coupler/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Coupler provides a mechanism by which you can couple two scalars.
That is the value of the coupled scalar would determined by the value
of the scalar to which it is coupled. The code referenced by the
options fconvert and rconvert determine the relation between the two
scalars.

%description -l pl.UTF-8
Moduł Tie::Coupler udostępnia mechanizm, którym można powiązać dwa
skalary. Oznacza to, że wartość powiązanego skalaru będzie określona
przez wartość skalaru, z którym został powiązany. Kod wskazany przez
opcje fconvert i rconvert określa relację między obydwoma skalarami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
