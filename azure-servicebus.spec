#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-servicebus
Version  : 0.50.2
Release  : 11
URL      : https://files.pythonhosted.org/packages/62/8f/d3b4d435323d4eb2234bde3e128073eccc1a5b86a74e3a8c87624c93155d/azure-servicebus-0.50.2.zip
Source0  : https://files.pythonhosted.org/packages/62/8f/d3b4d435323d4eb2234bde3e128073eccc1a5b86a74e3a8c87624c93155d/azure-servicebus-0.50.2.zip
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
Microsoft Azure Service Bus SDK for Python
==========================================

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

%description python3
python3 components for the azure-servicebus package.


%prep
%setup -q -n azure-servicebus-0.50.2
cd %{_builddir}/azure-servicebus-0.50.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576541346
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
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
