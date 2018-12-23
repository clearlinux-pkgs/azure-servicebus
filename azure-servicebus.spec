#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-servicebus
Version  : 0.21.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/82/29/cb0cfd5cc8b7b92b1a67c2fbab55e72792080255498cab7a2bbfe50ce90a/azure-servicebus-0.21.1.zip
Source0  : https://files.pythonhosted.org/packages/82/29/cb0cfd5cc8b7b92b1a67c2fbab55e72792080255498cab7a2bbfe50ce90a/azure-servicebus-0.21.1.zip
Summary  : Microsoft Azure Service Bus Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: azure-servicebus-python = %{version}-%{release}
Requires: azure-servicebus-python3 = %{version}-%{release}
Requires: azure-common
Requires: requests
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : requests

%description
==============================
        
        This is the Microsoft Azure Service Bus Runtime Client Library.
        
        This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

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
%setup -q -n azure-servicebus-0.21.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545578283
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
