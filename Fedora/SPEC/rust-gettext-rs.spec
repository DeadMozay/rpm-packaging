# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate gettext-rs

Name:           rust-%{crate}
Version:        0.4.1
Release:        1%{?dist}
Summary:        GNU Gettext FFI binding for Rust

License:        MIT
URL:            https://crates.io/crates/gettext-rs
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(gettext-sys/default) >= 0.19.8 with crate(gettext-sys/default) < 0.20.0)
BuildRequires:  (crate(locale_config/default) >= 0.2.0 with crate(locale_config/default) < 0.3.0)

%global _description \
GNU Gettext FFI binding for Rust.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE.txt
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+gettext-system-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gettext-system-devel %{_description}

This package contains library source intended for building other packages
which use "gettext-system" feature of "%{crate}" crate.

%files       -n %{name}+gettext-system-devel
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
* Sun Apr 28 16:31:47 +06 2019 Yuriy Sharov <dead_mozay@nom-it.ru> - 0.4.1-1
- Initial package
