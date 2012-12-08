Summary:	SCLI - SNMP Command Line Interface
Name:		scli
Version:	0.4.0
Release:	4
License:	GPLv2
#patch was sent upstream (Kharec)
Patch0:		scli-0.4.0-fix-str-fmt.patch 
Group:		Networking/Other
Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/scli/%{name}-%{version}.tar.gz
Url:		http://www.ibr.cs.tu-bs.de/projects/scli/
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	libglib2-devel
BuildRequires:	libgnet2-devel
BuildRequires:	gsnmp-devel

%description
Authors description on the project's home page:

The scli package was written to address the need for small and
efficient command line utilities to monitor and configure network
devices and host systems. The scli package is based on the SNMP
management protocol. It utilizes a MIB compiler called smidump to
generate C stub code. In fact, virtually no SNMP knowledge is required
in order to extend the scli programs with new features.

The programs contained in the scli package try to be very specific
rather than generic. Generic SNMP tools such as MIB browsers or simple
command line tools (e.g. snmpwalk) are hard to use since they expose
too many protocol details. And in most cases, they fail to present the
information in a format that is easy to read and understand.

The scli package was designed to be extensible. Additional modes that
extend the capabilities of the tools can easily be added. The smidump
MIB compiler hides all the SNMP protocol details so that every C
programmer can implement new modes. In fact, we like to encourage
users to write and contribute new modes so that the package becomes
more and more valuable.

To summarize, the slogan for this little package is: "After more than
10 years of SNMP, I felt it is time for really useful command line
SNMP monitoring and configuration tools. ;-)"

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-xmltest
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS NEWS PORTING README TODO 
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdv2011.0
+ Revision: 669962
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2011.0
+ Revision: 607527
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - patch sent

* Sat Mar 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 515301
- fix source to use tar.gz
- fix license
- update to 0.4.0
- drop old patch
- add a patch for fix str fmt and build

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.1-6mdv2010.0
+ Revision: 427062
- rebuild

* Fri Apr 03 2009 Funda Wang <fwang@mandriva.org> 0.3.1-5mdv2009.1
+ Revision: 363651
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new libreadline

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2009.0
+ Revision: 225402
- rebuild

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2008.1
+ Revision: 154151
- do not package big changelog
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 18 2007 Crispin Boylan <crisb@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 65756
- New version


* Thu Sep 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.12-8mdv2007.0
- Rebuild against ncurse

* Wed Sep 20 2006 Till Kamppeter <till@mandriva.com> 0.2.12-7mdv2007.0
- Rebuilt for new NCurses.

* Mon May 08 2006 Stefan van der Eijk <stefan@eijk.nu> 0.2.12-6mdk
- rebuild for sparc

* Fri Jan 21 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.2.12-5mdk
- rebuild for new readline

* Sun Nov 28 2004 Till Kamppeter <till@mandrakesoft.com> 0.2.12-4mdk
- Rebuilt.

