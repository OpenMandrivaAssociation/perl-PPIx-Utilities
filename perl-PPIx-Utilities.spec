%define modname	PPIx-Utilities
%define modver	1.001000

Summary:	A problem identified by L<PPIx::Utilities|PPIx::Utilities>
Name:		perl-%{modname}
Version:	%{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://guest@perlcritic.tigris.org/svn/perlcritic/trunk/distributions/PPIx-Utilities
Source0:	https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

%description
This is a collection of functions for dealing with the PPI manpage objects,
many of which originated in the Perl::Critic manpage. They are organized
into modules by the kind of PPI class they relate to, by replacing the
"PPI" at the front of the module name with "PPIx::Utilities", e.g.
functionality related to the PPI::Node manpages is in the
PPIx::Utilities::Node manpage.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*

