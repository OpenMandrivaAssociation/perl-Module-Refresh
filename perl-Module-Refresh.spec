%define module	Module-Refresh
%define name	perl-%{module}
%define version 0.13
%define rel     1

Name:		%{name}
Version:	%{version}
Release:	%mkrel 4
Summary:	Refresh %INC files when the module is updated on disk
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is a generalization of the functionality provided by
Apache::StatINC. It's designed to make it easy to do simple iterative
development when working in a persistent environment.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Module
%{_mandir}/man3/*

