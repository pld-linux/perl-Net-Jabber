%include	/usr/lib/rpm/macros.perl
Summary:	Jabber perl module
Summary(pl):	Modu³ perla dla protoko³u Jabber
Name:		perl-Net-Jabber
Version:	1.0022
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://www.obelisk.net/jarl/modules/Net-Jabber-%{version}.tar.gz
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
%setup -q -n Net-Jabber-%{version}

%build
echo -e "y\ny\ny\n" |perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitelib}/Net/*

%{_mandir}/man3/*
