%define upstream_name    PPIx-Utilities
%define upstream_version 1.000001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A problem identified by L<PPIx::Utilities|PPIx::Utilities>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Exporter)
BuildRequires: perl(PPI)
BuildRequires: perl(PPI::Document)
BuildRequires: perl(PPI::Document::Fragment)
BuildRequires: perl(PPI::Dumper)
BuildRequires: perl(Readonly)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


