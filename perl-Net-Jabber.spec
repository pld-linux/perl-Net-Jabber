%include	/usr/lib/rpm/macros.perl
Summary:	Jabber perl module
Summary(pl):	Modu� perla dla protoko�u Jabber
Name:		perl-Net-Jabber
Version:	1.0022
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Jabber-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Jabber - Jabber protocol interface.

%description -l pl
Net-Jabber - Obs�uga protoko�u Jabber.

%prep
%setup -q -n Net-Jabber-%{version}

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
