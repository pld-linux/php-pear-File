%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_status		alpha
%define		_pearname	%{_class}
%define		subver	alpha1
%define		rel		3
Summary:	%{_pearname} - Common file and directory routines
Summary(pl.UTF-8):	%{_pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	517436d7e68f0b2d3e27b938371e0ff0
URL:		http://pear.php.net/package/File/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.573
Requires:	php-common >= 3:4.2.0
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-File_CSV
Requires:	php-pear-File_Util
Requires:	php-pear-PEAR-core >= 1:1.5.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy access to read/write to files along with some common
routines to deal with paths. Also provides interface for handling CSV
files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza prosty dostęp do zapisu/odczytu plików razem z prostymi
metodami operacji na ścieżkach. Dostarcza także interfejsu do plików
CSV.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
