%{!?cmake_install: %global cmake_install cd build && make install DESTDIR=%{buildroot}}

%if %{undefined suse_version}
%define cmake_custom mkdir -p build && cd build && %cmake ..
%else
%define cmake_custom %cmake
%endif

Summary: Unit testing framework for C with support for mock objects
Name: cmocka
Version: 0.0.0
Release: 1
License: Apache
Group: System Environment/Libraries
URL: https://cmocka.org/
Source0: %{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.8

%description
cmocka is a fork for Google's cmockery unit testing framework to fix
bugs and support it in future.

%package devel
Summary: CMocka development files
Group: Development/Libraries
Requires: cmocka = %{version}-%{release}
%description devel
%{summary}

%prep
%setup -q -n %{name}-%{version}/cmocka

%build
%cmake_custom
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%cmake_install

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/pkgconfig/cmocka.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
