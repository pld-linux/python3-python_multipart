#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A streaming multipart parser for Python
Summary(pl.UTF-8):	Strumieniowy parser formatu multipart dla Pythona
Name:		python3-python_multipart
Version:	0.0.21
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-multipart/
Source0:	https://files.pythonhosted.org/packages/source/p/python-multipart/python_multipart-%{version}.tar.gz
# Source0-md5:	fd24645f1b328d5d328e8b10bc2c596c
URL:		https://pypi.org/project/python-multipart/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-hatchling
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-PyYAML >= 6.0.1
BuildRequires:	python3-pytest >= 8.1.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apache2-licensed streaming multipart parser for Python.

%description -l pl.UTF-8
Ten moduł jest strumieniowym parserem formatu multipart dla Pythona,
wydanym na licencji Apache 2.

%prep
%setup -q -n python_multipart-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.md
# backward compat layer, also proxy to multipart.py module, if installed
%{py3_sitescriptdir}/multipart
%{py3_sitescriptdir}/python_multipart
%{py3_sitescriptdir}/python_multipart-%{version}.dist-info
