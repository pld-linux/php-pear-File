%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Common file and directory routines
Summary(pl):	%{_pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f127f1d26485ac8d1d953b9b648e9d86
URL:		http://pear.php.net/package/File/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}
