%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Common file and directory routines
Summary(pl):	%{_pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{_pearname}
Version:	1.1.0
%define		_suf	RC1
Release:	0.%{_suf}.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_suf}.tgz
# Source0-md5:	32f3ed86f4efa7d3da3b7d66c75ca06e
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
%setup -q -c -n %{name}-%{version}%{_suf}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}%{_suf}/*.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}%{_suf}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_suf}/tests/*
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}
