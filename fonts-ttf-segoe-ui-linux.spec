Name:		fonts-ttf-segoe-ui-linux
Version:	1.0
Release:	1
Summary:	Segoe UI font for linux
License:	Microsoft TrueType Fonts
Group:		System/Fonts/True type
Url:		https://github.com/mrbvrz
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Segoe UI font for linux.

%files
%dir %{_datadir}/fonts/TTF/segoe-ui-linux/
%{_datadir}/fonts/TTF/segoe-ui-linux/*

%prep
autosetup -p

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/segoe-ui-linux
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/segoe-ui-linux/

