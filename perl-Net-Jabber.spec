#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Jabber
Summary:	Net::Jabber Perl module - access to the Jabber protocol
Summary(pl):	Modu³ Perla Net::Jabber - dostêp do protoko³u Jabbera
Name:		perl-Net-Jabber
Version:	1.29
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5465efa832cd451cb6066929d51b7b0d
BuildRequires:	perl-devel >= 5.005_03-14
BuildRequires:	perl-Digest-SHA1 >= 1.02
BuildRequires:	perl-XML-Stream >= 1.17
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Jabber is a collection of Perl modules that provide a Perl
Developer access to the Jabber protocol. Using OOP modules they
provide a clean interface to writing anything from a full client to a
simple protocol tester.

%description -l pl
Net::Jabber to zbiór modu³ów Perla daj±cych programi¶cie perlowemu
dostêp do protoko³u Jabbera. Zorientowane obiektowo modu³y daj± czysty
interfejs do pisania wszystkiego od pe³nego klienta do prostego
testera protoko³u.

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

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*
