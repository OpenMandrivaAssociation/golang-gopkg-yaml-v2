%global debug_package %{nil}

# Run tests in check section
%bcond_with check

# https://github.com/go-yaml/yaml
%global goipath		gopkg.in/yaml.v2
%global forgeurl	https://github.com/go-yaml/yaml
Version:			3.0.1

%gometa

Summary:	YAML support for the Go language
Name:		golang-gopkg-yaml-v2

Release:	1
Source0:	https://github.com/go-yaml/yaml/archive/v%{version}/yaml-%{version}.tar.gz
URL:		https://github.com/go-yaml/yaml
License:	GPL
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	golang(gopkg.in/check.v1)
%endif

%description
The yaml package enables Go programs to comfortably encode
and decode YAML values. It was developed within Canonical
as part of the juju project, and is based on a pure Go port
of the well-known libyaml C library to parse and generate
YAML data quickly and reliably.

The yaml package supports most of YAML 1.2, but preserves
some behavior from 1.1 for backwards compatibility.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc NOTICE

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n yaml-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
  install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

%check
%if %{with check}
%gochecks
%endif

