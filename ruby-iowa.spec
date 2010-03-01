#
# Conditional build:
%bcond_without doc	# Build without docs
#
%define pkgname iowa
Summary:	Interpreted Objects for Web Applications
Summary(pl.UTF-8):	IOWA - interpretowane obiekty dla aplikacji WWW
Name:		ruby-%{pkgname}
Version:	0.99.2.17
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/13985/%{pkgname}_%{version}.tar.bz2
# Source0-md5:	97a53f2a83a37e3aea4a2f9afbf79d68
URL:		http://enigo.com/projects/iowa/
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-log4r
Requires:	ruby-mime-types
Requires:	ruby-tmail
Provides:	ruby-Iowa
Obsoletes:	ruby-Iowa
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iowa is a framework, written in the Ruby programming language, for the
development of both web based applications and more general dynamic
web content.

%description -l pl.UTF-8
Iowa (Interpreted Objects for Web Applications - interpretowane
obiekty dla aplikacji WWW) to napisany w języku programowania Ruby
szkielet do tworzenia zarówno aplikacji opartych na WWW, jak i
bardziej ogólnej dynamicznej treści WWW.

%prep
%setup -q -n %{pkgname}_%{version}

%build
cp %{_datadir}/setup.rb .
mv src lib
cp -au microprojects/{LRUCache,DiskCache,LinkedList}/src/iowa/* lib/iowa
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

%if %{with doc}
rdoc --ri --op ri lib/ ext/
rm ri/{Object,Array,Hash,Date,DateTime,FalseClass,TrueClass,Kernel,Mutex,NilClass,Numeric,Time,String}/cdesc*
rdoc --op rdoc lib/ ext/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%if %{with doc}
cp -a ri/* $RPM_BUILD_ROOT/%{ruby_ridir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%if %{with doc}
%doc rdoc
%endif
%{ruby_rubylibdir}/*iowa*
%if %{with doc}
%{ruby_ridir}/Iowa
%{ruby_ridir}/Crypt
%{ruby_ridir}/Array/*
%{ruby_ridir}/Date/*
%{ruby_ridir}/DateTime/*
%{ruby_ridir}/Hash/*
%{ruby_ridir}/Object/*
%{ruby_ridir}/Apache/Iowa
%{ruby_ridir}/FalseClass/*
%{ruby_ridir}/Kernel/*
%{ruby_ridir}/IowaComponentMixins
%{ruby_ridir}/JSON
%{ruby_ridir}/LexerBase
%{ruby_ridir}/LexerText
%{ruby_ridir}/LexerRuby
%{ruby_ridir}/Monorail
%{ruby_ridir}/Mutex/*
%{ruby_ridir}/NilClass/*
%{ruby_ridir}/Numeric/*
%{ruby_ridir}/Time/*
%{ruby_ridir}/String/*
%endif
%{_examplesdir}/%{name}-%{version}
