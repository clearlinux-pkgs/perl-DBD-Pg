#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBD-Pg
Version  : 3.7.4
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBD-Pg-3.7.4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBD-Pg-3.7.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DBD-Pg-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl-DBI
BuildRequires : postgresql-dev

%description
DBD::Pg  --  the DBI PostgreSQL interface for Perl
DESCRIPTION:
------------
This is version 3.7.4 of DBD::Pg, the Perl interface to Postgres using DBI.
The web site for this interface, and the latest version, can be found at:

%package dev
Summary: dev components for the perl-DBD-Pg package.
Group: Development
Requires: perl-DBD-Pg-lib = %{version}-%{release}
Provides: perl-DBD-Pg-devel = %{version}-%{release}

%description dev
dev components for the perl-DBD-Pg package.


%package lib
Summary: lib components for the perl-DBD-Pg package.
Group: Libraries

%description lib
lib components for the perl-DBD-Pg package.


%prep
%setup -q -n DBD-Pg-3.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Bundle/DBD/Pg.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/DBD/Pg.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Bundle::DBD::Pg.3
/usr/share/man/man3/DBD::Pg.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/DBD/Pg/Pg.so
