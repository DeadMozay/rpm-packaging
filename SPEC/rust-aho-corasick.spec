# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate aho-corasick

Name:           rust-%{crate}
Version:        0.7.3
Release:        1%{?dist}
Summary:        Fast multiple substring searching

# Upstream license specification: Unlicense/MIT
License:        Public Domain and MIT
URL:            https://crates.io/crates/aho-corasick
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(memchr) >= 2.2.0 with crate(memchr) < 3.0.0)
BuildRequires:  (crate(memchr/use_std) >= 2.2.0 with crate(memchr/use_std) < 3.0.0)

%global _description \
Fast multiple substring searching.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE-MIT UNLICENSE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sat Apr 27 17:12:44 +06 2019 Yuriy Sharov <dead_mozay@nom-it.ru> - 0.7.3-1
- Initial package
