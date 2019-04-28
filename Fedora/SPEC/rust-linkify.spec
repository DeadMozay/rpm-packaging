# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate linkify

Name:           rust-%{crate}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Finds URLs and email addresses in plain text

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/linkify
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(memchr/default) >= 2.0.1 with crate(memchr/default) < 3.0.0)

%global _description \
Finds URLs and email addresses in plain text. Takes care to get the boundaries\
right with surrounding punctuation like parentheses.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md CHANGELOG.md
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Sun Apr 28 13:02:41 +06 2019 Yuriy Sharov <dead_mozay@nom-it.ru> - 0.3.1-1
- Initial package