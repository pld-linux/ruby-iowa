%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Interpreted Objects for Web Applications
Summary(pl):	IOWA - interpretowane obiekty dla aplikacji WWW
Name:		ruby-Iowa
%define tarname iowa
Version:	0.9.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1209/%{tarname}_%{version}.tar.bz
# Source0-md5:	c2f188758cd1576656a54013fa0609c5
URL:		http://enigo.com/projects/iowa/
BuildRequires:	ruby
Requires:	ruby
Requires:	ruby-LOG4R
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
cp -a examples extras utils url_mapping $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
