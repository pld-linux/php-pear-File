%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Common file and directory routines
Summary(pl):	%{_pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ba8f020b70fb6a37c6258e0e42033aad
URL:		http://pear.php.net/package/File/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy access to read/write to files along with some common
routines to deal with paths. Also provides interface for handling CSV
files.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza prosty dostêp do zapisu/odczytu plików razem z prostymi
metodami operacji na ¶cie¿kach. Dostarcza tak¿e interfejsu do plików
CSV.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
