#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk4
Version  : 4.8.1
Release  : 27
URL      : https://download.gnome.org/sources/gtk/4.8/gtk-4.8.1.tar.xz
Source0  : https://download.gnome.org/sources/gtk/4.8/gtk-4.8.1.tar.xz
Summary  : Wayland protocol files
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1 OFL-1.1
Requires: gtk4-bin = %{version}-%{release}
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-filemap = %{version}-%{release}
Requires: gtk4-lib = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}
Requires: gtk4-locales = %{version}-%{release}
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord-dev
BuildRequires : cups
BuildRequires : cups-dev
BuildRequires : gi-docgen
BuildRequires : glslang
BuildRequires : gobject-introspection
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(gstreamer-player-1.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pygobject
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markdown)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(pygments)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(toml)
BuildRequires : pypi(typogrify)
BuildRequires : pypi(wheel)

%description
Xwayland keyboard grabbing protocol
Maintainers:
Olivier Fourdan <ofourdan@redhat.com>

%package bin
Summary: bin components for the gtk4 package.
Group: Binaries
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}
Requires: gtk4-filemap = %{version}-%{release}

%description bin
bin components for the gtk4 package.


%package data
Summary: data components for the gtk4 package.
Group: Data

%description data
data components for the gtk4 package.


%package dev
Summary: dev components for the gtk4 package.
Group: Development
Requires: gtk4-lib = %{version}-%{release}
Requires: gtk4-bin = %{version}-%{release}
Requires: gtk4-data = %{version}-%{release}
Provides: gtk4-devel = %{version}-%{release}
Requires: gtk4 = %{version}-%{release}

%description dev
dev components for the gtk4 package.


%package filemap
Summary: filemap components for the gtk4 package.
Group: Default

%description filemap
filemap components for the gtk4 package.


%package lib
Summary: lib components for the gtk4 package.
Group: Libraries
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}
Requires: gtk4-filemap = %{version}-%{release}

%description lib
lib components for the gtk4 package.


%package license
Summary: license components for the gtk4 package.
Group: Default

%description license
license components for the gtk4 package.


%package locales
Summary: locales components for the gtk4 package.
Group: Default

%description locales
locales components for the gtk4 package.


%prep
%setup -q -n gtk-4.8.1
cd %{_builddir}/gtk-4.8.1
pushd ..
cp -a gtk-4.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663605088
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gtk4
cp %{_builddir}/gtk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gtk4/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/gtk-%{version}/gdk/COPYING %{buildroot}/usr/share/package-licenses/gtk4/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/gtk-%{version}/gtk/roaring/COPYING %{buildroot}/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gtk-%{version}/gtk/timsort/COPYING %{buildroot}/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/CC-BY-SA-3.0.txt %{buildroot}/usr/share/package-licenses/gtk4/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/gtk4/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gtk4/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/gtk4/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gtk4/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/gtk4/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/gtk4/ca2fd1439eb3e23507f13855e5450c5d617db83d || :
cp %{_builddir}/gtk-%{version}/subprojects/gi-docgen/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/gtk4/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4 || :
cp %{_builddir}/gtk-%{version}/subprojects/wayland-protocols/COPYING %{buildroot}/usr/share/package-licenses/gtk4/9d823228bce4c6977989fdd7b58026cd62fc55e0 || :
cp %{_builddir}/gtk-%{version}/subprojects/wayland/COPYING %{buildroot}/usr/share/package-licenses/gtk4/997b2f1a3639f31f0757b06a15035315baaffadc || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gtk40
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gtk4-builder-tool
/usr/bin/gtk4-demo
/usr/bin/gtk4-demo-application
/usr/bin/gtk4-encode-symbolic-svg
/usr/bin/gtk4-icon-browser
/usr/bin/gtk4-launch
/usr/bin/gtk4-node-editor
/usr/bin/gtk4-print-editor
/usr/bin/gtk4-query-settings
/usr/bin/gtk4-update-icon-cache
/usr/bin/gtk4-widget-factory
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gdk-4.0.typelib
/usr/lib64/girepository-1.0/GdkWayland-4.0.typelib
/usr/lib64/girepository-1.0/GdkX11-4.0.typelib
/usr/lib64/girepository-1.0/Gsk-4.0.typelib
/usr/lib64/girepository-1.0/Gtk-4.0.typelib
/usr/share/applications/org.gtk.Demo4.desktop
/usr/share/applications/org.gtk.IconBrowser4.desktop
/usr/share/applications/org.gtk.PrintEditor4.desktop
/usr/share/applications/org.gtk.WidgetFactory4.desktop
/usr/share/applications/org.gtk.gtk4.NodeEditor.desktop
/usr/share/gettext/its/gtk4builder.its
/usr/share/gettext/its/gtk4builder.loc
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
/usr/share/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
/usr/share/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
/usr/share/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
/usr/share/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml
/usr/share/gtk-4.0/emoji/da.gresource
/usr/share/gtk-4.0/emoji/de.gresource
/usr/share/gtk-4.0/emoji/es.gresource
/usr/share/gtk-4.0/emoji/fr.gresource
/usr/share/gtk-4.0/emoji/hu.gresource
/usr/share/gtk-4.0/emoji/it.gresource
/usr/share/gtk-4.0/emoji/ko.gresource
/usr/share/gtk-4.0/emoji/lt.gresource
/usr/share/gtk-4.0/emoji/ms.gresource
/usr/share/gtk-4.0/emoji/nl.gresource
/usr/share/gtk-4.0/emoji/pl.gresource
/usr/share/gtk-4.0/emoji/pt.gresource
/usr/share/gtk-4.0/emoji/ru.gresource
/usr/share/gtk-4.0/emoji/sv.gresource
/usr/share/gtk-4.0/emoji/uk.gresource
/usr/share/gtk-4.0/emoji/zh.gresource
/usr/share/gtk-4.0/gtk4builder.rng
/usr/share/gtk-4.0/valgrind/gtk.supp
/usr/share/icons/hicolor/scalable/apps/org.gtk.Demo4.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.IconBrowser4.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.gtk4.NodeEditor.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gtk.gtk4.NodeEditor.svg
/usr/share/icons/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gtk.IconBrowser4-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gtk.gtk4.NodeEditor-symbolic.svg
/usr/share/metainfo/org.gtk.Demo4.appdata.xml
/usr/share/metainfo/org.gtk.IconBrowser4.appdata.xml
/usr/share/metainfo/org.gtk.PrintEditor4.appdata.xml
/usr/share/metainfo/org.gtk.WidgetFactory4.appdata.xml
/usr/share/metainfo/org.gtk.gtk4.NodeEditor.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gtk-4.0/gdk/gdk-autocleanup.h
/usr/include/gtk-4.0/gdk/gdk.h
/usr/include/gtk-4.0/gdk/gdkapplaunchcontext.h
/usr/include/gtk-4.0/gdk/gdkcairo.h
/usr/include/gtk-4.0/gdk/gdkcairocontext.h
/usr/include/gtk-4.0/gdk/gdkclipboard.h
/usr/include/gtk-4.0/gdk/gdkconfig.h
/usr/include/gtk-4.0/gdk/gdkcontentdeserializer.h
/usr/include/gtk-4.0/gdk/gdkcontentformats.h
/usr/include/gtk-4.0/gdk/gdkcontentprovider.h
/usr/include/gtk-4.0/gdk/gdkcontentproviderimpl.h
/usr/include/gtk-4.0/gdk/gdkcontentserializer.h
/usr/include/gtk-4.0/gdk/gdkcursor.h
/usr/include/gtk-4.0/gdk/gdkdevice.h
/usr/include/gtk-4.0/gdk/gdkdevicepad.h
/usr/include/gtk-4.0/gdk/gdkdevicetool.h
/usr/include/gtk-4.0/gdk/gdkdisplay.h
/usr/include/gtk-4.0/gdk/gdkdisplaymanager.h
/usr/include/gtk-4.0/gdk/gdkdrag.h
/usr/include/gtk-4.0/gdk/gdkdragsurface.h
/usr/include/gtk-4.0/gdk/gdkdrawcontext.h
/usr/include/gtk-4.0/gdk/gdkdrop.h
/usr/include/gtk-4.0/gdk/gdkenums.h
/usr/include/gtk-4.0/gdk/gdkenumtypes.h
/usr/include/gtk-4.0/gdk/gdkevents.h
/usr/include/gtk-4.0/gdk/gdkframeclock.h
/usr/include/gtk-4.0/gdk/gdkframetimings.h
/usr/include/gtk-4.0/gdk/gdkglcontext.h
/usr/include/gtk-4.0/gdk/gdkgltexture.h
/usr/include/gtk-4.0/gdk/gdkkeys.h
/usr/include/gtk-4.0/gdk/gdkkeysyms.h
/usr/include/gtk-4.0/gdk/gdkmemorytexture.h
/usr/include/gtk-4.0/gdk/gdkmonitor.h
/usr/include/gtk-4.0/gdk/gdkpaintable.h
/usr/include/gtk-4.0/gdk/gdkpango.h
/usr/include/gtk-4.0/gdk/gdkpixbuf.h
/usr/include/gtk-4.0/gdk/gdkpopup.h
/usr/include/gtk-4.0/gdk/gdkpopuplayout.h
/usr/include/gtk-4.0/gdk/gdkrectangle.h
/usr/include/gtk-4.0/gdk/gdkrgba.h
/usr/include/gtk-4.0/gdk/gdkseat.h
/usr/include/gtk-4.0/gdk/gdksnapshot.h
/usr/include/gtk-4.0/gdk/gdksurface.h
/usr/include/gtk-4.0/gdk/gdktexture.h
/usr/include/gtk-4.0/gdk/gdktoplevel.h
/usr/include/gtk-4.0/gdk/gdktoplevellayout.h
/usr/include/gtk-4.0/gdk/gdktoplevelsize.h
/usr/include/gtk-4.0/gdk/gdktypes.h
/usr/include/gtk-4.0/gdk/gdkversionmacros.h
/usr/include/gtk-4.0/gdk/gdkvulkancontext.h
/usr/include/gtk-4.0/gdk/wayland/gdkwayland.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylanddevice.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylanddisplay.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandglcontext.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandmonitor.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandseat.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandsurface.h
/usr/include/gtk-4.0/gdk/x11/gdkx-autocleanups.h
/usr/include/gtk-4.0/gdk/x11/gdkx.h
/usr/include/gtk-4.0/gdk/x11/gdkx11applaunchcontext.h
/usr/include/gtk-4.0/gdk/x11/gdkx11device-xi2.h
/usr/include/gtk-4.0/gdk/x11/gdkx11device.h
/usr/include/gtk-4.0/gdk/x11/gdkx11devicemanager-xi2.h
/usr/include/gtk-4.0/gdk/x11/gdkx11devicemanager.h
/usr/include/gtk-4.0/gdk/x11/gdkx11display.h
/usr/include/gtk-4.0/gdk/x11/gdkx11dnd.h
/usr/include/gtk-4.0/gdk/x11/gdkx11glcontext.h
/usr/include/gtk-4.0/gdk/x11/gdkx11monitor.h
/usr/include/gtk-4.0/gdk/x11/gdkx11property.h
/usr/include/gtk-4.0/gdk/x11/gdkx11screen.h
/usr/include/gtk-4.0/gdk/x11/gdkx11selection.h
/usr/include/gtk-4.0/gdk/x11/gdkx11surface.h
/usr/include/gtk-4.0/gdk/x11/gdkx11utils.h
/usr/include/gtk-4.0/gsk/gl/gskglrenderer.h
/usr/include/gtk-4.0/gsk/gsk-autocleanup.h
/usr/include/gtk-4.0/gsk/gsk.h
/usr/include/gtk-4.0/gsk/gskcairorenderer.h
/usr/include/gtk-4.0/gsk/gskenums.h
/usr/include/gtk-4.0/gsk/gskenumtypes.h
/usr/include/gtk-4.0/gsk/gskglshader.h
/usr/include/gtk-4.0/gsk/gskrenderer.h
/usr/include/gtk-4.0/gsk/gskrendernode.h
/usr/include/gtk-4.0/gsk/gskroundedrect.h
/usr/include/gtk-4.0/gsk/gsktransform.h
/usr/include/gtk-4.0/gsk/gsktypes.h
/usr/include/gtk-4.0/gtk/css/gtkcss.h
/usr/include/gtk-4.0/gtk/css/gtkcssenums.h
/usr/include/gtk-4.0/gtk/css/gtkcssenumtypes.h
/usr/include/gtk-4.0/gtk/css/gtkcsserror.h
/usr/include/gtk-4.0/gtk/css/gtkcsslocation.h
/usr/include/gtk-4.0/gtk/css/gtkcsssection.h
/usr/include/gtk-4.0/gtk/gtk-autocleanups.h
/usr/include/gtk-4.0/gtk/gtk.h
/usr/include/gtk-4.0/gtk/gtkaboutdialog.h
/usr/include/gtk-4.0/gtk/gtkaccelgroup.h
/usr/include/gtk-4.0/gtk/gtkaccessible.h
/usr/include/gtk-4.0/gtk/gtkactionable.h
/usr/include/gtk-4.0/gtk/gtkactionbar.h
/usr/include/gtk-4.0/gtk/gtkadjustment.h
/usr/include/gtk-4.0/gtk/gtkappchooser.h
/usr/include/gtk-4.0/gtk/gtkappchooserbutton.h
/usr/include/gtk-4.0/gtk/gtkappchooserdialog.h
/usr/include/gtk-4.0/gtk/gtkappchooserwidget.h
/usr/include/gtk-4.0/gtk/gtkapplication.h
/usr/include/gtk-4.0/gtk/gtkapplicationwindow.h
/usr/include/gtk-4.0/gtk/gtkaspectframe.h
/usr/include/gtk-4.0/gtk/gtkassistant.h
/usr/include/gtk-4.0/gtk/gtkatcontext.h
/usr/include/gtk-4.0/gtk/gtkbinlayout.h
/usr/include/gtk-4.0/gtk/gtkbitset.h
/usr/include/gtk-4.0/gtk/gtkbookmarklist.h
/usr/include/gtk-4.0/gtk/gtkboolfilter.h
/usr/include/gtk-4.0/gtk/gtkborder.h
/usr/include/gtk-4.0/gtk/gtkbox.h
/usr/include/gtk-4.0/gtk/gtkboxlayout.h
/usr/include/gtk-4.0/gtk/gtkbuildable.h
/usr/include/gtk-4.0/gtk/gtkbuilder.h
/usr/include/gtk-4.0/gtk/gtkbuilderlistitemfactory.h
/usr/include/gtk-4.0/gtk/gtkbuilderscope.h
/usr/include/gtk-4.0/gtk/gtkbutton.h
/usr/include/gtk-4.0/gtk/gtkcalendar.h
/usr/include/gtk-4.0/gtk/gtkcellarea.h
/usr/include/gtk-4.0/gtk/gtkcellareabox.h
/usr/include/gtk-4.0/gtk/gtkcellareacontext.h
/usr/include/gtk-4.0/gtk/gtkcelleditable.h
/usr/include/gtk-4.0/gtk/gtkcelllayout.h
/usr/include/gtk-4.0/gtk/gtkcellrenderer.h
/usr/include/gtk-4.0/gtk/gtkcellrendereraccel.h
/usr/include/gtk-4.0/gtk/gtkcellrenderercombo.h
/usr/include/gtk-4.0/gtk/gtkcellrendererpixbuf.h
/usr/include/gtk-4.0/gtk/gtkcellrendererprogress.h
/usr/include/gtk-4.0/gtk/gtkcellrendererspin.h
/usr/include/gtk-4.0/gtk/gtkcellrendererspinner.h
/usr/include/gtk-4.0/gtk/gtkcellrenderertext.h
/usr/include/gtk-4.0/gtk/gtkcellrenderertoggle.h
/usr/include/gtk-4.0/gtk/gtkcellview.h
/usr/include/gtk-4.0/gtk/gtkcenterbox.h
/usr/include/gtk-4.0/gtk/gtkcenterlayout.h
/usr/include/gtk-4.0/gtk/gtkcheckbutton.h
/usr/include/gtk-4.0/gtk/gtkcolorbutton.h
/usr/include/gtk-4.0/gtk/gtkcolorchooser.h
/usr/include/gtk-4.0/gtk/gtkcolorchooserdialog.h
/usr/include/gtk-4.0/gtk/gtkcolorchooserwidget.h
/usr/include/gtk-4.0/gtk/gtkcolorutils.h
/usr/include/gtk-4.0/gtk/gtkcolumnview.h
/usr/include/gtk-4.0/gtk/gtkcolumnviewcolumn.h
/usr/include/gtk-4.0/gtk/gtkcombobox.h
/usr/include/gtk-4.0/gtk/gtkcomboboxtext.h
/usr/include/gtk-4.0/gtk/gtkconstraint.h
/usr/include/gtk-4.0/gtk/gtkconstraintguide.h
/usr/include/gtk-4.0/gtk/gtkconstraintlayout.h
/usr/include/gtk-4.0/gtk/gtkcssprovider.h
/usr/include/gtk-4.0/gtk/gtkcustomfilter.h
/usr/include/gtk-4.0/gtk/gtkcustomlayout.h
/usr/include/gtk-4.0/gtk/gtkcustomsorter.h
/usr/include/gtk-4.0/gtk/gtkdebug.h
/usr/include/gtk-4.0/gtk/gtkdialog.h
/usr/include/gtk-4.0/gtk/gtkdirectorylist.h
/usr/include/gtk-4.0/gtk/gtkdragicon.h
/usr/include/gtk-4.0/gtk/gtkdragsource.h
/usr/include/gtk-4.0/gtk/gtkdrawingarea.h
/usr/include/gtk-4.0/gtk/gtkdropcontrollermotion.h
/usr/include/gtk-4.0/gtk/gtkdropdown.h
/usr/include/gtk-4.0/gtk/gtkdroptarget.h
/usr/include/gtk-4.0/gtk/gtkdroptargetasync.h
/usr/include/gtk-4.0/gtk/gtkeditable.h
/usr/include/gtk-4.0/gtk/gtkeditablelabel.h
/usr/include/gtk-4.0/gtk/gtkemojichooser.h
/usr/include/gtk-4.0/gtk/gtkentry.h
/usr/include/gtk-4.0/gtk/gtkentrybuffer.h
/usr/include/gtk-4.0/gtk/gtkentrycompletion.h
/usr/include/gtk-4.0/gtk/gtkenums.h
/usr/include/gtk-4.0/gtk/gtkeventcontroller.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerfocus.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerkey.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerlegacy.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollermotion.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerscroll.h
/usr/include/gtk-4.0/gtk/gtkexpander.h
/usr/include/gtk-4.0/gtk/gtkexpression.h
/usr/include/gtk-4.0/gtk/gtkfilechooser.h
/usr/include/gtk-4.0/gtk/gtkfilechooserdialog.h
/usr/include/gtk-4.0/gtk/gtkfilechoosernative.h
/usr/include/gtk-4.0/gtk/gtkfilechooserwidget.h
/usr/include/gtk-4.0/gtk/gtkfilefilter.h
/usr/include/gtk-4.0/gtk/gtkfilter.h
/usr/include/gtk-4.0/gtk/gtkfilterlistmodel.h
/usr/include/gtk-4.0/gtk/gtkfixed.h
/usr/include/gtk-4.0/gtk/gtkfixedlayout.h
/usr/include/gtk-4.0/gtk/gtkflattenlistmodel.h
/usr/include/gtk-4.0/gtk/gtkflowbox.h
/usr/include/gtk-4.0/gtk/gtkfontbutton.h
/usr/include/gtk-4.0/gtk/gtkfontchooser.h
/usr/include/gtk-4.0/gtk/gtkfontchooserdialog.h
/usr/include/gtk-4.0/gtk/gtkfontchooserwidget.h
/usr/include/gtk-4.0/gtk/gtkframe.h
/usr/include/gtk-4.0/gtk/gtkgesture.h
/usr/include/gtk-4.0/gtk/gtkgestureclick.h
/usr/include/gtk-4.0/gtk/gtkgesturedrag.h
/usr/include/gtk-4.0/gtk/gtkgesturelongpress.h
/usr/include/gtk-4.0/gtk/gtkgesturepan.h
/usr/include/gtk-4.0/gtk/gtkgesturerotate.h
/usr/include/gtk-4.0/gtk/gtkgesturesingle.h
/usr/include/gtk-4.0/gtk/gtkgesturestylus.h
/usr/include/gtk-4.0/gtk/gtkgestureswipe.h
/usr/include/gtk-4.0/gtk/gtkgesturezoom.h
/usr/include/gtk-4.0/gtk/gtkglarea.h
/usr/include/gtk-4.0/gtk/gtkgrid.h
/usr/include/gtk-4.0/gtk/gtkgridlayout.h
/usr/include/gtk-4.0/gtk/gtkgridview.h
/usr/include/gtk-4.0/gtk/gtkheaderbar.h
/usr/include/gtk-4.0/gtk/gtkicontheme.h
/usr/include/gtk-4.0/gtk/gtkiconview.h
/usr/include/gtk-4.0/gtk/gtkimage.h
/usr/include/gtk-4.0/gtk/gtkimcontext.h
/usr/include/gtk-4.0/gtk/gtkimcontextsimple.h
/usr/include/gtk-4.0/gtk/gtkimmodule.h
/usr/include/gtk-4.0/gtk/gtkimmulticontext.h
/usr/include/gtk-4.0/gtk/gtkinfobar.h
/usr/include/gtk-4.0/gtk/gtkinscription.h
/usr/include/gtk-4.0/gtk/gtklabel.h
/usr/include/gtk-4.0/gtk/gtklayoutchild.h
/usr/include/gtk-4.0/gtk/gtklayoutmanager.h
/usr/include/gtk-4.0/gtk/gtklevelbar.h
/usr/include/gtk-4.0/gtk/gtklinkbutton.h
/usr/include/gtk-4.0/gtk/gtklistbase.h
/usr/include/gtk-4.0/gtk/gtklistbox.h
/usr/include/gtk-4.0/gtk/gtklistitem.h
/usr/include/gtk-4.0/gtk/gtklistitemfactory.h
/usr/include/gtk-4.0/gtk/gtkliststore.h
/usr/include/gtk-4.0/gtk/gtklistview.h
/usr/include/gtk-4.0/gtk/gtklockbutton.h
/usr/include/gtk-4.0/gtk/gtkmain.h
/usr/include/gtk-4.0/gtk/gtkmaplistmodel.h
/usr/include/gtk-4.0/gtk/gtkmediacontrols.h
/usr/include/gtk-4.0/gtk/gtkmediafile.h
/usr/include/gtk-4.0/gtk/gtkmediastream.h
/usr/include/gtk-4.0/gtk/gtkmenubutton.h
/usr/include/gtk-4.0/gtk/gtkmessagedialog.h
/usr/include/gtk-4.0/gtk/gtkmountoperation.h
/usr/include/gtk-4.0/gtk/gtkmultifilter.h
/usr/include/gtk-4.0/gtk/gtkmultiselection.h
/usr/include/gtk-4.0/gtk/gtkmultisorter.h
/usr/include/gtk-4.0/gtk/gtknative.h
/usr/include/gtk-4.0/gtk/gtknativedialog.h
/usr/include/gtk-4.0/gtk/gtknoselection.h
/usr/include/gtk-4.0/gtk/gtknotebook.h
/usr/include/gtk-4.0/gtk/gtknumericsorter.h
/usr/include/gtk-4.0/gtk/gtkorientable.h
/usr/include/gtk-4.0/gtk/gtkoverlay.h
/usr/include/gtk-4.0/gtk/gtkoverlaylayout.h
/usr/include/gtk-4.0/gtk/gtkpadcontroller.h
/usr/include/gtk-4.0/gtk/gtkpagesetup.h
/usr/include/gtk-4.0/gtk/gtkpaned.h
/usr/include/gtk-4.0/gtk/gtkpapersize.h
/usr/include/gtk-4.0/gtk/gtkpasswordentry.h
/usr/include/gtk-4.0/gtk/gtkpasswordentrybuffer.h
/usr/include/gtk-4.0/gtk/gtkpicture.h
/usr/include/gtk-4.0/gtk/gtkpopover.h
/usr/include/gtk-4.0/gtk/gtkpopovermenu.h
/usr/include/gtk-4.0/gtk/gtkpopovermenubar.h
/usr/include/gtk-4.0/gtk/gtkprintcontext.h
/usr/include/gtk-4.0/gtk/gtkprintoperation.h
/usr/include/gtk-4.0/gtk/gtkprintoperationpreview.h
/usr/include/gtk-4.0/gtk/gtkprintsettings.h
/usr/include/gtk-4.0/gtk/gtkprogressbar.h
/usr/include/gtk-4.0/gtk/gtkrange.h
/usr/include/gtk-4.0/gtk/gtkrecentmanager.h
/usr/include/gtk-4.0/gtk/gtkrender.h
/usr/include/gtk-4.0/gtk/gtkrevealer.h
/usr/include/gtk-4.0/gtk/gtkroot.h
/usr/include/gtk-4.0/gtk/gtkscale.h
/usr/include/gtk-4.0/gtk/gtkscalebutton.h
/usr/include/gtk-4.0/gtk/gtkscrollable.h
/usr/include/gtk-4.0/gtk/gtkscrollbar.h
/usr/include/gtk-4.0/gtk/gtkscrolledwindow.h
/usr/include/gtk-4.0/gtk/gtksearchbar.h
/usr/include/gtk-4.0/gtk/gtksearchentry.h
/usr/include/gtk-4.0/gtk/gtkselectionfiltermodel.h
/usr/include/gtk-4.0/gtk/gtkselectionmodel.h
/usr/include/gtk-4.0/gtk/gtkseparator.h
/usr/include/gtk-4.0/gtk/gtksettings.h
/usr/include/gtk-4.0/gtk/gtkshortcut.h
/usr/include/gtk-4.0/gtk/gtkshortcutaction.h
/usr/include/gtk-4.0/gtk/gtkshortcutcontroller.h
/usr/include/gtk-4.0/gtk/gtkshortcutlabel.h
/usr/include/gtk-4.0/gtk/gtkshortcutmanager.h
/usr/include/gtk-4.0/gtk/gtkshortcutsgroup.h
/usr/include/gtk-4.0/gtk/gtkshortcutssection.h
/usr/include/gtk-4.0/gtk/gtkshortcutsshortcut.h
/usr/include/gtk-4.0/gtk/gtkshortcutswindow.h
/usr/include/gtk-4.0/gtk/gtkshortcuttrigger.h
/usr/include/gtk-4.0/gtk/gtkshow.h
/usr/include/gtk-4.0/gtk/gtksignallistitemfactory.h
/usr/include/gtk-4.0/gtk/gtksingleselection.h
/usr/include/gtk-4.0/gtk/gtksizegroup.h
/usr/include/gtk-4.0/gtk/gtksizerequest.h
/usr/include/gtk-4.0/gtk/gtkslicelistmodel.h
/usr/include/gtk-4.0/gtk/gtksnapshot.h
/usr/include/gtk-4.0/gtk/gtksorter.h
/usr/include/gtk-4.0/gtk/gtksortlistmodel.h
/usr/include/gtk-4.0/gtk/gtkspinbutton.h
/usr/include/gtk-4.0/gtk/gtkspinner.h
/usr/include/gtk-4.0/gtk/gtkstack.h
/usr/include/gtk-4.0/gtk/gtkstacksidebar.h
/usr/include/gtk-4.0/gtk/gtkstackswitcher.h
/usr/include/gtk-4.0/gtk/gtkstatusbar.h
/usr/include/gtk-4.0/gtk/gtkstringfilter.h
/usr/include/gtk-4.0/gtk/gtkstringlist.h
/usr/include/gtk-4.0/gtk/gtkstringsorter.h
/usr/include/gtk-4.0/gtk/gtkstylecontext.h
/usr/include/gtk-4.0/gtk/gtkstyleprovider.h
/usr/include/gtk-4.0/gtk/gtkswitch.h
/usr/include/gtk-4.0/gtk/gtksymbolicpaintable.h
/usr/include/gtk-4.0/gtk/gtktestatcontext.h
/usr/include/gtk-4.0/gtk/gtktestutils.h
/usr/include/gtk-4.0/gtk/gtktext.h
/usr/include/gtk-4.0/gtk/gtktextbuffer.h
/usr/include/gtk-4.0/gtk/gtktextchild.h
/usr/include/gtk-4.0/gtk/gtktextiter.h
/usr/include/gtk-4.0/gtk/gtktextmark.h
/usr/include/gtk-4.0/gtk/gtktexttag.h
/usr/include/gtk-4.0/gtk/gtktexttagtable.h
/usr/include/gtk-4.0/gtk/gtktextview.h
/usr/include/gtk-4.0/gtk/gtktogglebutton.h
/usr/include/gtk-4.0/gtk/gtktooltip.h
/usr/include/gtk-4.0/gtk/gtktreednd.h
/usr/include/gtk-4.0/gtk/gtktreeexpander.h
/usr/include/gtk-4.0/gtk/gtktreelistmodel.h
/usr/include/gtk-4.0/gtk/gtktreelistrowsorter.h
/usr/include/gtk-4.0/gtk/gtktreemodel.h
/usr/include/gtk-4.0/gtk/gtktreemodelfilter.h
/usr/include/gtk-4.0/gtk/gtktreemodelsort.h
/usr/include/gtk-4.0/gtk/gtktreeselection.h
/usr/include/gtk-4.0/gtk/gtktreesortable.h
/usr/include/gtk-4.0/gtk/gtktreestore.h
/usr/include/gtk-4.0/gtk/gtktreeview.h
/usr/include/gtk-4.0/gtk/gtktreeviewcolumn.h
/usr/include/gtk-4.0/gtk/gtktypebuiltins.h
/usr/include/gtk-4.0/gtk/gtktypes.h
/usr/include/gtk-4.0/gtk/gtkversion.h
/usr/include/gtk-4.0/gtk/gtkvideo.h
/usr/include/gtk-4.0/gtk/gtkviewport.h
/usr/include/gtk-4.0/gtk/gtkvolumebutton.h
/usr/include/gtk-4.0/gtk/gtkwidget.h
/usr/include/gtk-4.0/gtk/gtkwidgetpaintable.h
/usr/include/gtk-4.0/gtk/gtkwindow.h
/usr/include/gtk-4.0/gtk/gtkwindowcontrols.h
/usr/include/gtk-4.0/gtk/gtkwindowgroup.h
/usr/include/gtk-4.0/gtk/gtkwindowhandle.h
/usr/include/gtk-4.0/unix-print/gtk/gtkpagesetupunixdialog.h
/usr/include/gtk-4.0/unix-print/gtk/gtkprinter.h
/usr/include/gtk-4.0/unix-print/gtk/gtkprintjob.h
/usr/include/gtk-4.0/unix-print/gtk/gtkprintunixdialog.h
/usr/include/gtk-4.0/unix-print/gtk/gtkunixprint-autocleanups.h
/usr/include/gtk-4.0/unix-print/gtk/gtkunixprint.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libgtk-4.so
/usr/lib64/libgtk-4.so
/usr/lib64/pkgconfig/gtk4-unix-print.pc
/usr/lib64/pkgconfig/gtk4-wayland.pc
/usr/lib64/pkgconfig/gtk4-x11.pc
/usr/lib64/pkgconfig/gtk4.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gtk4

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgtk-4.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libgtk-4.so.1.800.1
/usr/lib64/gtk-4.0/4.0.0/media/libmedia-gstreamer.so
/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so
/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-file.so
/usr/lib64/libgtk-4.so.1
/usr/lib64/libgtk-4.so.1.800.1
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk4/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gtk4/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/gtk4/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/gtk4/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/gtk4/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/gtk4/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/gtk4/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
/usr/share/package-licenses/gtk4/997b2f1a3639f31f0757b06a15035315baaffadc
/usr/share/package-licenses/gtk4/9d823228bce4c6977989fdd7b58026cd62fc55e0
/usr/share/package-licenses/gtk4/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/gtk4/ca2fd1439eb3e23507f13855e5450c5d617db83d
/usr/share/package-licenses/gtk4/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51

%files locales -f gtk40.lang
%defattr(-,root,root,-)

