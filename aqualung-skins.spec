Summary:	Aqualung - additional skins
Summary(pl):	Aqualung - dodatkowe sk�rki
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
Additional skins for Aqualung.

%description -l pl
Dodatkowe sk�rki dla Aqualunga.

%package dark
Summary:	Dark skin for Aqualung
Summary(pl):	Sk�rka Dark dla Aqualunga
Group:		X11/Applications/Multimedia
Requires:	aqualung

%description dark
Dark, XMMS-like colors. Your eye won't get burned.

%description dark -l pl
Ciemne kolory podobne do XMMS-a. Nie wypal� oczu.

%package metal
Summary:	Metal skin for Aqualung
Summary(pl):	Sk�rka Metal dla Aqualunga
Group:		X11/Applications/Multimedia
Requires:	aqualung

%description metal
Modern looking, shining metal colors.

%description metal -l pl
Nowocze�nie wygl�daj�ce kolory b�yszcz�cego metalu.

%package woody
Summary:	Woody skin for aqualung
Summary(pl):	Sk�rka Woody dla Aqualunga
Group:		X11/Applications/Multimedia
Requires:	aqualung

%description woody
Warm look&feel, for those who like natural surfaces.

%description woody -l pl
Ciep�y wygl�d, dla lubi�cych naturalne powierzchnie.

%prep
%setup -q -c -a1 -a2 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/aqualung/skin

for i in dark metal woody; do
	cp -rf $i $RPM_BUILD_ROOT%{_datadir}/aqualung/skin
done

%clean
rm -rf $RPM_BUILD_ROOT

%files dark
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/dark
%{_datadir}/aqualung/skin/dark/*

%files metal
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/metal
%{_datadir}/aqualung/skin/metal/*

%files woody
%defattr(644,root,root,755)
%dir %{_datadir}/aqualung/skin/woody
%{_datadir}/aqualung/skin/woody/*
