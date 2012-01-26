%define		pkg	memcache
Summary:	simple memcache client
Name:		nodejs-%{pkg}
Version:	0.2.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/elbart/node-memcache
Source0:	http://registry.npmjs.org/memcache/-/%{pkg}-%{version}.tgz
# Source0-md5:	297b9a4ef8d96ae9c809b47654a165ac
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure-JavaScript memcached library for Node.js.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a index.js package.json lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
