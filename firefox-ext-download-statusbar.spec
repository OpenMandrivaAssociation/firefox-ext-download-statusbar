Summary: Download Statusbar extension for firefox
Name: firefox-ext-download-statusbar
Version: 0.9.8
Release: 2
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en_US/firefox/addon/26/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/26/download_statusbar-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_version}
Obsoletes: %{name} < %{version}
BuildRequires: firefox-devel
Buildarch: noarch

%description
Despite its compact size, Download Statusbar packs in more useful features than
the standard download window. The fully customizable interface auto-hides when
not in use, allowing full control without interruption. 

%prep
%setup -q -c -n %{name}-%{version}

%install
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

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}




%changelog
* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2011.0
+ Revision: 646530
- new version 0.9.8

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.9.7.2-5
+ Revision: 633585
- remove hard requires

  + Thierry Vignaud <tv@mandriva.org>
    - xpi packaging doesn't work with that extension (UI issues)
    - patch 0: make it compatible with firefox-4b9
    - prevent need to rebuild for every new firefox
    - only package .xpi

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 0.9.7.2-3mdv2011.0
+ Revision: 628863
- rebuild for new firefox

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 0.9.7.2-2mdv2011.0
+ Revision: 597377
- rebuild for new firefox

* Sun Nov 07 2010 Thierry Vignaud <tv@mandriva.org> 0.9.7.2-1mdv2011.0
+ Revision: 594629
- import firefox-ext-download-statusbar

