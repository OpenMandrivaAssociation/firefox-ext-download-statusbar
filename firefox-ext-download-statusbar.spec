Summary: Download Statusbar extension for firefox
Name: firefox-ext-download-statusbar
Version: 0.9.7.2
Release: %mkrel 5
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/fr/firefox/addon/26/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/26/download_statusbar-%{version}-fx.xpi
Patch0:	compat-firefox-4.0b9.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
BuildRequires: firefox-devel
Buildarch: noarch

%description
Despite its compact size, Download Statusbar packs in more useful features than
the standard download window. The fully customizable interface auto-hides when
not in use, allowing full control without interruption. 

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p0

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
# (tv) xpi packaging doesn't work with that extension (UI issues):
#cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"
#zip -9 "%{buildroot}$extdir/$hash.xpi" *
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


