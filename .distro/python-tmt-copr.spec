Name:           python-tmt-copr
Version:        0.0.0
Release:        %autorelease
Summary:        TMT copr plugin

License:        GPL-3.0-or-later
URL:            https://github.com/LecrisUT/tmt-copr
Source:         %{pypi_source tmt_copr}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A tmt plugin for copr testing framework
}

%description %_description

%package -n python3-tmt-copr
Summary:        %{summary}
%description -n python3-tmt-copr %_description


%prep
%autosetup -n tmt-copr-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tmt_copr


%check
%pytest


%files -n python3-tmt-copr -f %{pyproject_files}
%license LICENSE.md
%doc README.md


%changelog
%autochangelog
