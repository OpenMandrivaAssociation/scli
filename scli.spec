Summary:	SCLI - SNMP Command Line Interface
Name:		scli
Version:	0.3.1
Release:	%mkrel 1
License:	GPL
Group:		Networking/Other

Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/scli/%{name}-%{version}.tar.bz2
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

%build
%configure --disable-xmltest
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS PORTING README TODO 
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
