%define upstream_name    PPIx-Utilities
%define upstream_version 1.001000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	A problem identified by L<PPIx::Utilities|PPIx::Utilities>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(PPI)
BuildRequires:	perl(PPI::Document)
BuildRequires:	perl(PPI::Document::Fragment)
BuildRequires:	perl(PPI::Dumper)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a collection of functions for dealing with the PPI manpage objects,
many of which originated in the Perl::Critic manpage. They are organized
into modules by the kind of PPI class they relate to, by replacing the
"PPI" at the front of the module name with "PPIx::Utilities", e.g.
functionality related to the PPI::Node manpages is in the
PPIx::Utilities::Node manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-4mdv2012.0
+ Revision: 765605
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 676772
- rebuild

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 662944
- new version

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.0.1-2
+ Revision: 658869
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 552602
- import perl-PPIx-Utilities


* Tue Jul 13 2010 cpan2dist 1.000001-1mdv
- initial mdv release, generated with cpan2dist
