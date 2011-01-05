%define _mozillaextpath %{firefox_mozillapath}/extensions
%define debug_package %{nil}

Summary: Download Statusbar extension for firefox
Name: firefox-ext-download-statusbar
Version: 0.9.7.2
Release: %mkrel 3
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/fr/firefox/addon/26/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/26/download_statusbar-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
BuildRequires: firefox-devel

%description
Despite its compact size, Download Statusbar packs in more useful features than
the standard download window. The fully customizable interface auto-hides when
not in use, allowing full control without interruption. 

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}


