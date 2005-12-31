%define tarname iowa
Summary:	Interpreted Objects for Web Applications
Summary(pl):	IOWA - interpretowane obiekty dla aplikacji WWW
Name:		ruby-Iowa
Version:	0.9.2
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1853/%{tarname}_%{version}.tar.bz
# Source0-md5:	cb27f0baa555c9e4f55ebb4a4a593c0a
URL:		http://enigo.com/projects/iowa/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-LOG4R
Requires:	ruby-TMail
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iowa is a framework, written in the Ruby programming language, for the
development of both web based applications and more general dynamic
web content.

%description -l pl
Iowa (Interpreted Objects for Web Applications - interpretowane
obiekty dla aplikacji WWW) to napisany w jêzyku programowania Ruby
szkielet do tworzenia zarówno aplikacji opartych na WWW, jak i
bardziej ogólnej dynamicznej tre¶ci WWW.

%prep
%setup -q -n %{tarname}_%{version}

%build
rdoc --ri --op ri src/ iowa.rb
rm ri/ri/{Object,Array,Hash}/cdesc*
rdoc --op rdoc src/ iowa.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir}/{iowa,apache},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a src/* $RPM_BUILD_ROOT%{ruby_rubylibdir}/iowa
cp -a iowa*.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a mod_iowa.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}/apache
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples utils $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_rubylibdir}/*iowa*
%{ruby_rubylibdir}/apache/*
%{ruby_ridir}/Iowa
%{ruby_ridir}/Crypt
%{ruby_ridir}/Array/*
%{ruby_ridir}/Hash/*
%{ruby_ridir}/Object/*
%{_examplesdir}/%{name}-%{version}
