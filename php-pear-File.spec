%define		status		alpha
%define		pearname	File
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Common file and directory routines
Summary(pl.UTF-8):	%{pearname} - Podstawowe sposoby operacji na plikach i katalogach
Name:		php-pear-%{pearname}
Version:	1.4.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	3cf96cff0ae67c495dbc6714b0cb032a
URL:		http://pear.php.net/package/File/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.573
Requires:	php(core) >= 4.2.0
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-File_CSV
Requires:	php-pear-File_Util
Requires:	php-pear-PEAR-core >= 1:1.5.3
Obsoletes:	php-pear-File-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy access to read/write to files along with some common
routines to deal with paths. Also provides interface for handling CSV
files.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Dostarcza prosty dostęp do zapisu/odczytu plików razem z prostymi
metodami operacji na ścieżkach. Dostarcza także interfejsu do plików
CSV.

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/File.php
