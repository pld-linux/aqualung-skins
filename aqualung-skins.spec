#
Summary:	Aqualung - additional skins
Summary(pl):	Aqualung - dodatkowe skórki
Name:		aqualung-skins
Version:	0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://aqualung.sf.net/skins/aqualung-dark.tar.gz
# Source0-md5:	4bdfb815875db5bfefaa138c3b93833b
Source1:	http://aqualung.sf.net/skins/aqualung-metal.tar.gz
# Source1-md5:	193ec183c7050cf8f844287953c3d6e8
Source2:	http://aqualung.sf.net/skins/aqualung-woody.tar.gz
# Source2-md5:	d13546c75e5712d9fed880d0e3a7e792
URL:		http://aqualung.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional skins for aqualung

%description -l pl
Dodatkowe skórki

%package -n %{name}-dark
Summary:	Dark skin for aqualung
Summary(pl):	Skórka Dark
Group:		X11/Applications/Multimedia

%description -n %{name}-dark
Dark, XMMS-like colors. Your eye won't get burned.

%package -n %{name}-metal
Summary:	Metal skin for aqualung
Summary(pl):	Skórka Metal
Group:		X11/Applications/Multimedia

%description -n %{name}-metal
Modern looking, shining metal colors.

%package -n %{name}-woody
Summary:	Woody skin for aqualung
Summary(pl):	Skórka Woody
Group:		X11/Applications/Multimedia

%description -n %{name}-woody
Warm look&feel, for those who like natural surfaces.

%prep
%setup -q -n aqualung-skins -c -a 1 -a 2 

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/aqualung/skin/
for i in dark metal woody; do
	cp -rf $i $RPM_BUILD_ROOT%{_datadir}/aqualung/skin/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}-dark
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/dark
%{_datadir}/aqualung/skin/dark/*

%files -n %{name}-metal
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/metal
%{_datadir}/aqualung/skin/metal/*

%files -n %{name}-woody
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/woody
%{_datadir}/aqualung/skin/woody/*
