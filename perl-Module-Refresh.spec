%define upstream_name	 Module-Refresh
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.17
Release:	3

Summary:	Refresh INC files when the module is updated on disk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Module/Module-Refresh-0.17.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Path::Class)
BuildArch:	noarch

%description
This module is a generalization of the functionality provided by
Apache::StatINC. It's designed to make it easy to do simple iterative
development when working in a persistent environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Module
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 655764
- update to new version 0.16

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 406070
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.13-5mdv2009.0
+ Revision: 257902
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-4mdv2009.0
+ Revision: 245951
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2008.1
+ Revision: 171026
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 20 2007 Michael Scherer <misc@mandriva.org> 0.13-1mdv2008.0
+ Revision: 28863
- Update to new version 0.13

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.12-1mdv2008.0
+ Revision: 20922
- upgrade to 0.12


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-2mdk
- Fix According to perl Policy
	- Source URL

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdk
- New release 0.09
- spec cleanup
- fix directory ownership

* Mon Nov 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-1mdk
- 0.08
- Remove empty dirs in package

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.06-1mdk
- First mandriva package


