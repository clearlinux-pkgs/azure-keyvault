#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-keyvault
Version  : 4.1.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/99/94/a7cc3a0e794681e049d1882cb041513dd3624be5d6e138ac486cc8415a81/azure-keyvault-4.1.0.zip
Source0  : https://files.pythonhosted.org/packages/99/94/a7cc3a0e794681e049d1882cb041513dd3624be5d6e138ac486cc8415a81/azure-keyvault-4.1.0.zip
Summary  : Microsoft Azure Key Vault Client Libraries for Python
Group    : Development/Tools
License  : MIT
Requires: azure-keyvault-python = %{version}-%{release}
Requires: azure-keyvault-python3 = %{version}-%{release}
Requires: azure-keyvault-certificates
Requires: azure-keyvault-keys
Requires: azure-keyvault-secrets
BuildRequires : azure-keyvault-certificates
BuildRequires : azure-keyvault-keys
BuildRequires : azure-keyvault-secrets
BuildRequires : buildreq-distutils3

%description
This is the Microsoft Azure Key Vault libraries bundle.
        
        This package does not contain any code in itself. It installs a set

%package python
Summary: python components for the azure-keyvault package.
Group: Default
Requires: azure-keyvault-python3 = %{version}-%{release}

%description python
python components for the azure-keyvault package.


%package python3
Summary: python3 components for the azure-keyvault package.
Group: Default
Requires: python3-core
Provides: pypi(azure_keyvault)
Requires: pypi(azure_keyvault_certificates)
Requires: pypi(azure_keyvault_keys)
Requires: pypi(azure_keyvault_secrets)

%description python3
python3 components for the azure-keyvault package.


%prep
%setup -q -n azure-keyvault-4.1.0
cd %{_builddir}/azure-keyvault-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588709617
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
