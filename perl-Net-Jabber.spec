%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Jabber
Summary:	Jabber perl module
Summary(pl):	Modu³ perla dla protoko³u Jabber
Name:		perl-Net-Jabber
Version:	1.0022
Release:	3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Jabber - Jabber protocol interface.

%description -l pl
Net-Jabber - Obs³uga protoko³u Jabber.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo -e "y\ny\ny\n" |perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitelib}/Net/*

%{_mandir}/man3/*
