# Spec file for package orchis-gtk-theme
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:		orchis-gtk-theme
Version:	2.0
Release:	0

Summary:	Orchis GTK Theme
License:    GPL-3.0+ or CC-BY-SA-3.0

Group:      System/GUI/GNOME
Url:        http://www.mokaproject.com/orchis-gtk-theme
Source0:	%{name}-%{version}.tar.gz

Requires:	orchis-gtk-theme, gtk-murrine-engine
BuildArch:	noarch


%description
Orchis GTK3 Theme

%prep
%setup -q

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Orchis/ $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Orchis-Dark/ $RPM_BUILD_ROOT%{_datadir}/themes/

%files
%doc {AUTHORS,LICENSE}
%{_datadir}/themes/Orchis/
%{_datadir}/themes/Orchis-Dark/
