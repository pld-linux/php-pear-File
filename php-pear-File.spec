%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_pearname	%{_class}
Summary:	%{_pearname} - Common file and directory routines
Summary(pl):	%{_pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy access to read/write to files along with some common
routines to deal with paths. Also provides interface for handling CSV
files.

%description -l pl
Dostarcza prosty dostêp do zapisu/odczytu plików razem z prostymi
metodami operacji na ¶cie¿kach. Dostarcza tak¿e interfejsu do plików
CSV.

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/*.php
