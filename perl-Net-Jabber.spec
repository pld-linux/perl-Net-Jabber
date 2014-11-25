#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	Net
%define		pnam	Jabber
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Jabber Perl module - access to the Jabber protocol
Summary(pl.UTF-8):	Moduł Perla Net::Jabber - dostęp do protokołu Jabbera
Name:		perl-Net-Jabber
Version:	2.0
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1fd348fb9a1a6c5a167ae862ed89cd53
URL:		http://search.cpan.org/dist/Net-Jabber/
BuildRequires:	perl-Digest-SHA1 >= 1.02
BuildRequires:	perl-XML-Stream >= 1.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Jabber is a collection of Perl modules that provide a Perl
Developer access to the Jabber protocol. Using OOP modules they
provide a clean interface to writing anything from a full client to a
simple protocol tester.

%description -l pl.UTF-8
Net::Jabber to zbiór modułów Perla dających programiście perlowemu
dostęp do protokołu Jabbera. Zorientowane obiektowo moduły dają czysty
interfejs do pisania wszystkiego od pełnego klienta do prostego
testera protokołu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(use 5.006_)0(01;)(.*)$/$1$2$3/' Jabber/X.pm

%build
echo -e "y\ny\ny\n" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	UNINST=0 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*
