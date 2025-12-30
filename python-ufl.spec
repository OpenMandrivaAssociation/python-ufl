%global	module ufl
%global fname %(n=%{name}; echo ${n:0:1})

Summary:	Unified Form Language for form-compilers
Name:		python-%{module}
Version:	2019.1.0
Release:	2
License:	LGPLv3+ and GPLv2+
Group:		Development/Python
URL:		https://fenicsproject.org
Source0:	https://bitbucket.org/fenics-project/%{module}/downloads/%{module}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/%{fname}/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

%description
The Unified Form Language (UFL) is a domain specific language for
declaration of finite element discretizations of variational forms. More
precisely, it defines a flexible interface for choosing finite element
spaces and defining expressions for weak forms in a notation close to
mathematical notation.

UFL is part of the FEniCS Project.

%files
%license COPYING
%license COPYING.LESSER
%doc README.rst
%doc AUTHORS
%{py_sitedir}/%{module}/
%{py_sitedir}/fenics_%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

