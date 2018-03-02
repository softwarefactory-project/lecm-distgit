Name:           lecm
Version:        0.0.7
Release:        3%{?dist}
Summary:        Let's Encrypt Certificates Manager

License:        ASL 2.0
URL:            https://github.com/Spredzy/lecm
Source0:        https://github.com/Spredzy/lecm/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       acme-tiny
Requires:       python-prettytable
Requires:       pyOpenSSL
Requires:       PyYAML
Requires:       python2-requests

BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
Let's Encrypt Certificates Manager (lecm) is an utility that allows one
to manage (generate and renew) Let's Encrypt SSL certificates.


%prep
%autosetup -n %{name}-%{version}
rm -f requirements.txt test-requirements.txt
touch requirements.txt


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
install -p -D -m 0755 sample/lecm-simple.conf %{buildroot}%{_sysconfdir}/lecm.conf



%files
%{_bindir}/lecm
%config(noreplace) %{_sysconfdir}/lecm.conf
%{python2_sitelib}/lecm
%{python2_sitelib}/lecm-*.egg-info


%changelog
* Fri Mar 2 2018 Fabien Boucher <fboucher@redhat.com> - 0.0.7-3
- Fix build for sdist source

* Tue Mar 21 2017 Tristan Cacqueray - 0.0.7-2
- Prevent configuration replace

* Fri Mar 17 2017 Tristan Cacqueray - 0.0.7-1
- Initial packaging
