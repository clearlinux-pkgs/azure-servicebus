#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-servicebus
Version  : 0.50.3
Release  : 17
URL      : https://files.pythonhosted.org/packages/fc/55/a365b0e10809f7ce96a59c54cc16a07cfa947cf95e1a6fb7ceb084be5cc7/azure-servicebus-0.50.3.zip
Source0  : https://files.pythonhosted.org/packages/fc/55/a365b0e10809f7ce96a59c54cc16a07cfa947cf95e1a6fb7ceb084be5cc7/azure-servicebus-0.50.3.zip
Summary  : Microsoft Azure Service Bus Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-servicebus-python = %{version}-%{release}
Requires: azure-servicebus-python3 = %{version}-%{release}
Requires: azure-common
Requires: azure-nspkg
Requires: msrestazure
Requires: uamqp
BuildRequires : azure-common
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : msrestazure
BuildRequires : uamqp

%description
# Microsoft Azure Service Bus SDK for Python
> **NOTE**: Starting with the GA release of version 7.0.0 (currently in preview), this package will be deprecated.
> Users can get a head-start on transitioning by installing or upgrading via `pip install azure-servicebus --pre` and reviewing our [migration guide](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/servicebus/azure-servicebus/migration_guide.md)

%package python
Summary: python components for the azure-servicebus package.
Group: Default
Requires: azure-servicebus-python3 = %{version}-%{release}

%description python
python components for the azure-servicebus package.


%package python3
Summary: python3 components for the azure-servicebus package.
Group: Default
Requires: python3-core
Provides: pypi(azure_servicebus)
Requires: pypi(azure_common)
Requires: pypi(msrestazure)
Requires: pypi(uamqp)

%description python3
python3 components for the azure-servicebus package.


%prep
%setup -q -n azure-servicebus-0.50.3
cd %{_builddir}/azure-servicebus-0.50.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590078014
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
