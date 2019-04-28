# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate petgraph

Name:           rust-%{crate}
Version:        0.4.13
Release:        1%{?dist}
Summary:        Graph data structure library. Provides graph types and graph algorithms.

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/petgraph
Source:         %{crates_source}
# Initial patched metadata
Patch0:         petgraph-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(fixedbitset/default) >= 0.1.4 with crate(fixedbitset/default) < 0.2.0)
BuildRequires:  (crate(ordermap/default) >= 0.3.0 with crate(ordermap/default) < 0.4.0)
%if %{with check}
BuildRequires:  (crate(defmac/default) >= 0.1.0 with crate(defmac/default) < 0.2.0)
BuildRequires:  (crate(itertools) >= 0.8.0 with crate(itertools) < 0.9.0)
BuildRequires:  (crate(odds/default) >= 0.2.19 with crate(odds/default) < 0.3.0)
BuildRequires:  (crate(rand/default) >= 0.3.0 with crate(rand/default) < 0.4.0)
%endif

%global _description \
Graph data structure library. Provides graph types and graph algorithms.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.rst CONTRIBUTING.rst
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

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+generate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-devel %{_description}

This package contains library source intended for building other packages
which use "generate" feature of "%{crate}" crate.

%files       -n %{name}+generate-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+graphmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+graphmap-devel %{_description}

This package contains library source intended for building other packages
which use "graphmap" feature of "%{crate}" crate.

%files       -n %{name}+graphmap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+ordermap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ordermap-devel %{_description}

This package contains library source intended for building other packages
which use "ordermap" feature of "%{crate}" crate.

%files       -n %{name}+ordermap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+quickcheck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quickcheck-devel %{_description}

This package contains library source intended for building other packages
which use "quickcheck" feature of "%{crate}" crate.

%files       -n %{name}+quickcheck-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-1-devel %{_description}

This package contains library source intended for building other packages
which use "serde-1" feature of "%{crate}" crate.

%files       -n %{name}+serde-1-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages
which use "serde_derive" feature of "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+stable_graph-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stable_graph-devel %{_description}

This package contains library source intended for building other packages
which use "stable_graph" feature of "%{crate}" crate.

%files       -n %{name}+stable_graph-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
* Sun Apr 28 15:53:31 +06 2019 Yuriy Sharov <dead_mozay@nom-it.ru> - 0.4.13-1
- Initial package
