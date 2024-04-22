#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
Name     : gtk4
Version  : 4.14.3
Release  : 55
URL      : https://download.gnome.org/sources/gtk/4.14/gtk-4.14.3.tar.xz
Source0  : https://download.gnome.org/sources/gtk/4.14/gtk-4.14.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.0 LGPL-2.1
Requires: gtk4-bin = %{version}-%{release}
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-lib = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}
Requires: gtk4-locales = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
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
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pygobject
BuildRequires : pypi-docutils
BuildRequires : shaderc
BuildRequires : shaderc-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains a collection of images of various widgets.
They are created via the shooter command in gtk/docs/tools/, and are
updated semi-regularly. The images are used in both the headers of
individual widgets as well as the visual index of widgets.

%package bin
Summary: bin components for the gtk4 package.
Group: Binaries
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}

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


%package lib
Summary: lib components for the gtk4 package.
Group: Libraries
Requires: gtk4-data = %{version}-%{release}
Requires: gtk4-license = %{version}-%{release}

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
%setup -q -n gtk-4.14.3
cd %{_builddir}/gtk-4.14.3
pushd ..
cp -a gtk-4.14.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713804107
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dintrospection=enabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dintrospection=enabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gtk4
cp %{_builddir}/gtk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gtk4/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/gtk-%{version}/gdk/COPYING %{buildroot}/usr/share/package-licenses/gtk4/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/gtk-%{version}/gtk/roaring/COPYING %{buildroot}/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gtk-%{version}/gtk/timsort/COPYING %{buildroot}/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gtk40
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gtk4-builder-tool
/V3/usr/bin/gtk4-demo
/V3/usr/bin/gtk4-demo-application
/V3/usr/bin/gtk4-encode-symbolic-svg
/V3/usr/bin/gtk4-icon-browser
/V3/usr/bin/gtk4-launch
/V3/usr/bin/gtk4-node-editor
/V3/usr/bin/gtk4-path-tool
/V3/usr/bin/gtk4-print-editor
/V3/usr/bin/gtk4-query-settings
/V3/usr/bin/gtk4-rendernode-tool
/V3/usr/bin/gtk4-update-icon-cache
/V3/usr/bin/gtk4-widget-factory
/usr/bin/gtk4-builder-tool
/usr/bin/gtk4-demo
/usr/bin/gtk4-demo-application
/usr/bin/gtk4-encode-symbolic-svg
/usr/bin/gtk4-icon-browser
/usr/bin/gtk4-launch
/usr/bin/gtk4-node-editor
/usr/bin/gtk4-path-tool
/usr/bin/gtk4-print-editor
/usr/bin/gtk4-query-settings
/usr/bin/gtk4-rendernode-tool
/usr/bin/gtk4-update-icon-cache
/usr/bin/gtk4-widget-factory

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
/usr/share/gtk-4.0/emoji/bn.gresource
/usr/share/gtk-4.0/emoji/da.gresource
/usr/share/gtk-4.0/emoji/de.gresource
/usr/share/gtk-4.0/emoji/es.gresource
/usr/share/gtk-4.0/emoji/et.gresource
/usr/share/gtk-4.0/emoji/fi.gresource
/usr/share/gtk-4.0/emoji/fr.gresource
/usr/share/gtk-4.0/emoji/hi.gresource
/usr/share/gtk-4.0/emoji/hu.gresource
/usr/share/gtk-4.0/emoji/it.gresource
/usr/share/gtk-4.0/emoji/ja.gresource
/usr/share/gtk-4.0/emoji/ko.gresource
/usr/share/gtk-4.0/emoji/lt.gresource
/usr/share/gtk-4.0/emoji/ms.gresource
/usr/share/gtk-4.0/emoji/nb.gresource
/usr/share/gtk-4.0/emoji/nl.gresource
/usr/share/gtk-4.0/emoji/pl.gresource
/usr/share/gtk-4.0/emoji/pt.gresource
/usr/share/gtk-4.0/emoji/ru.gresource
/usr/share/gtk-4.0/emoji/sv.gresource
/usr/share/gtk-4.0/emoji/th.gresource
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
/usr/include/gtk-4.0/gdk/deprecated/gdkpixbuf.h
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
/usr/include/gtk-4.0/gdk/gdkdmabufformats.h
/usr/include/gtk-4.0/gdk/gdkdmabuftexture.h
/usr/include/gtk-4.0/gdk/gdkdmabuftexturebuilder.h
/usr/include/gtk-4.0/gdk/gdkdrag.h
/usr/include/gtk-4.0/gdk/gdkdragsurface.h
/usr/include/gtk-4.0/gdk/gdkdragsurfacesize.h
/usr/include/gtk-4.0/gdk/gdkdrawcontext.h
/usr/include/gtk-4.0/gdk/gdkdrop.h
/usr/include/gtk-4.0/gdk/gdkenums.h
/usr/include/gtk-4.0/gdk/gdkenumtypes.h
/usr/include/gtk-4.0/gdk/gdkevents.h
/usr/include/gtk-4.0/gdk/gdkframeclock.h
/usr/include/gtk-4.0/gdk/gdkframetimings.h
/usr/include/gtk-4.0/gdk/gdkglcontext.h
/usr/include/gtk-4.0/gdk/gdkgltexture.h
/usr/include/gtk-4.0/gdk/gdkgltexturebuilder.h
/usr/include/gtk-4.0/gdk/gdkkeys.h
/usr/include/gtk-4.0/gdk/gdkkeysyms.h
/usr/include/gtk-4.0/gdk/gdkmemorytexture.h
/usr/include/gtk-4.0/gdk/gdkmonitor.h
/usr/include/gtk-4.0/gdk/gdkpaintable.h
/usr/include/gtk-4.0/gdk/gdkpango.h
/usr/include/gtk-4.0/gdk/gdkpopup.h
/usr/include/gtk-4.0/gdk/gdkpopuplayout.h
/usr/include/gtk-4.0/gdk/gdkrectangle.h
/usr/include/gtk-4.0/gdk/gdkrgba.h
/usr/include/gtk-4.0/gdk/gdkseat.h
/usr/include/gtk-4.0/gdk/gdksnapshot.h
/usr/include/gtk-4.0/gdk/gdksurface.h
/usr/include/gtk-4.0/gdk/gdktexture.h
/usr/include/gtk-4.0/gdk/gdktexturedownloader.h
/usr/include/gtk-4.0/gdk/gdktoplevel.h
/usr/include/gtk-4.0/gdk/gdktoplevellayout.h
/usr/include/gtk-4.0/gdk/gdktoplevelsize.h
/usr/include/gtk-4.0/gdk/gdktypes.h
/usr/include/gtk-4.0/gdk/gdkvulkancontext.h
/usr/include/gtk-4.0/gdk/version/gdk-visibility.h
/usr/include/gtk-4.0/gdk/version/gdkversionmacros.h
/usr/include/gtk-4.0/gdk/wayland/gdkwayland.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylanddevice.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylanddisplay.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandglcontext.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandmonitor.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandpopup.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandseat.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandsurface.h
/usr/include/gtk-4.0/gdk/wayland/gdkwaylandtoplevel.h
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
/usr/include/gtk-4.0/gsk/gpu/gskvulkanrenderer.h
/usr/include/gtk-4.0/gsk/gsk.h
/usr/include/gtk-4.0/gsk/gskcairorenderer.h
/usr/include/gtk-4.0/gsk/gskenums.h
/usr/include/gtk-4.0/gsk/gskenumtypes.h
/usr/include/gtk-4.0/gsk/gskglshader.h
/usr/include/gtk-4.0/gsk/gskpath.h
/usr/include/gtk-4.0/gsk/gskpathbuilder.h
/usr/include/gtk-4.0/gsk/gskpathmeasure.h
/usr/include/gtk-4.0/gsk/gskpathpoint.h
/usr/include/gtk-4.0/gsk/gskrenderer.h
/usr/include/gtk-4.0/gsk/gskrendernode.h
/usr/include/gtk-4.0/gsk/gskroundedrect.h
/usr/include/gtk-4.0/gsk/gskstroke.h
/usr/include/gtk-4.0/gsk/gsktransform.h
/usr/include/gtk-4.0/gsk/gsktypes.h
/usr/include/gtk-4.0/gtk/a11y/gtkatspi.h
/usr/include/gtk-4.0/gtk/a11y/gtkatspisocket.h
/usr/include/gtk-4.0/gtk/css/gtkcss.h
/usr/include/gtk-4.0/gtk/css/gtkcssenums.h
/usr/include/gtk-4.0/gtk/css/gtkcssenumtypes.h
/usr/include/gtk-4.0/gtk/css/gtkcsserror.h
/usr/include/gtk-4.0/gtk/css/gtkcsslocation.h
/usr/include/gtk-4.0/gtk/css/gtkcsssection.h
/usr/include/gtk-4.0/gtk/deprecated/gtkappchooser.h
/usr/include/gtk-4.0/gtk/deprecated/gtkappchooserbutton.h
/usr/include/gtk-4.0/gtk/deprecated/gtkappchooserdialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkappchooserwidget.h
/usr/include/gtk-4.0/gtk/deprecated/gtkassistant.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellarea.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellareabox.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellareacontext.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcelleditable.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcelllayout.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrenderer.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrendereraccel.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrenderercombo.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrendererpixbuf.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrendererprogress.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrendererspin.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrendererspinner.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrenderertext.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellrenderertoggle.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcellview.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcolorbutton.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcolorchooser.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcolorchooserdialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcolorchooserwidget.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcombobox.h
/usr/include/gtk-4.0/gtk/deprecated/gtkcomboboxtext.h
/usr/include/gtk-4.0/gtk/deprecated/gtkdialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkentrycompletion.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfilechooser.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfilechooserdialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfilechoosernative.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfilechooserwidget.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfontbutton.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfontchooser.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfontchooserdialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkfontchooserwidget.h
/usr/include/gtk-4.0/gtk/deprecated/gtkiconview.h
/usr/include/gtk-4.0/gtk/deprecated/gtkinfobar.h
/usr/include/gtk-4.0/gtk/deprecated/gtkliststore.h
/usr/include/gtk-4.0/gtk/deprecated/gtklockbutton.h
/usr/include/gtk-4.0/gtk/deprecated/gtkmessagedialog.h
/usr/include/gtk-4.0/gtk/deprecated/gtkrender.h
/usr/include/gtk-4.0/gtk/deprecated/gtkshow.h
/usr/include/gtk-4.0/gtk/deprecated/gtkstatusbar.h
/usr/include/gtk-4.0/gtk/deprecated/gtkstylecontext.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreednd.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreemodel.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreemodelfilter.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreemodelsort.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreeselection.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreesortable.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreestore.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreeview.h
/usr/include/gtk-4.0/gtk/deprecated/gtktreeviewcolumn.h
/usr/include/gtk-4.0/gtk/deprecated/gtkvolumebutton.h
/usr/include/gtk-4.0/gtk/gtk.h
/usr/include/gtk-4.0/gtk/gtkaboutdialog.h
/usr/include/gtk-4.0/gtk/gtkaccelgroup.h
/usr/include/gtk-4.0/gtk/gtkaccessible.h
/usr/include/gtk-4.0/gtk/gtkaccessiblerange.h
/usr/include/gtk-4.0/gtk/gtkaccessibletext.h
/usr/include/gtk-4.0/gtk/gtkactionable.h
/usr/include/gtk-4.0/gtk/gtkactionbar.h
/usr/include/gtk-4.0/gtk/gtkadjustment.h
/usr/include/gtk-4.0/gtk/gtkalertdialog.h
/usr/include/gtk-4.0/gtk/gtkapplication.h
/usr/include/gtk-4.0/gtk/gtkapplicationwindow.h
/usr/include/gtk-4.0/gtk/gtkaspectframe.h
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
/usr/include/gtk-4.0/gtk/gtkcenterbox.h
/usr/include/gtk-4.0/gtk/gtkcenterlayout.h
/usr/include/gtk-4.0/gtk/gtkcheckbutton.h
/usr/include/gtk-4.0/gtk/gtkcolordialog.h
/usr/include/gtk-4.0/gtk/gtkcolordialogbutton.h
/usr/include/gtk-4.0/gtk/gtkcolorutils.h
/usr/include/gtk-4.0/gtk/gtkcolumnview.h
/usr/include/gtk-4.0/gtk/gtkcolumnviewcell.h
/usr/include/gtk-4.0/gtk/gtkcolumnviewcolumn.h
/usr/include/gtk-4.0/gtk/gtkcolumnviewrow.h
/usr/include/gtk-4.0/gtk/gtkcolumnviewsorter.h
/usr/include/gtk-4.0/gtk/gtkconfig.h
/usr/include/gtk-4.0/gtk/gtkconstraint.h
/usr/include/gtk-4.0/gtk/gtkconstraintguide.h
/usr/include/gtk-4.0/gtk/gtkconstraintlayout.h
/usr/include/gtk-4.0/gtk/gtkcssprovider.h
/usr/include/gtk-4.0/gtk/gtkcustomfilter.h
/usr/include/gtk-4.0/gtk/gtkcustomlayout.h
/usr/include/gtk-4.0/gtk/gtkcustomsorter.h
/usr/include/gtk-4.0/gtk/gtkdebug.h
/usr/include/gtk-4.0/gtk/gtkdialogerror.h
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
/usr/include/gtk-4.0/gtk/gtkenums.h
/usr/include/gtk-4.0/gtk/gtkeventcontroller.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerfocus.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerkey.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerlegacy.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollermotion.h
/usr/include/gtk-4.0/gtk/gtkeventcontrollerscroll.h
/usr/include/gtk-4.0/gtk/gtkexpander.h
/usr/include/gtk-4.0/gtk/gtkexpression.h
/usr/include/gtk-4.0/gtk/gtkfiledialog.h
/usr/include/gtk-4.0/gtk/gtkfilefilter.h
/usr/include/gtk-4.0/gtk/gtkfilelauncher.h
/usr/include/gtk-4.0/gtk/gtkfilter.h
/usr/include/gtk-4.0/gtk/gtkfilterlistmodel.h
/usr/include/gtk-4.0/gtk/gtkfixed.h
/usr/include/gtk-4.0/gtk/gtkfixedlayout.h
/usr/include/gtk-4.0/gtk/gtkflattenlistmodel.h
/usr/include/gtk-4.0/gtk/gtkflowbox.h
/usr/include/gtk-4.0/gtk/gtkfontdialog.h
/usr/include/gtk-4.0/gtk/gtkfontdialogbutton.h
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
/usr/include/gtk-4.0/gtk/gtkgraphicsoffload.h
/usr/include/gtk-4.0/gtk/gtkgrid.h
/usr/include/gtk-4.0/gtk/gtkgridlayout.h
/usr/include/gtk-4.0/gtk/gtkgridview.h
/usr/include/gtk-4.0/gtk/gtkheaderbar.h
/usr/include/gtk-4.0/gtk/gtkicontheme.h
/usr/include/gtk-4.0/gtk/gtkimage.h
/usr/include/gtk-4.0/gtk/gtkimcontext.h
/usr/include/gtk-4.0/gtk/gtkimcontextsimple.h
/usr/include/gtk-4.0/gtk/gtkimmodule.h
/usr/include/gtk-4.0/gtk/gtkimmulticontext.h
/usr/include/gtk-4.0/gtk/gtkinscription.h
/usr/include/gtk-4.0/gtk/gtklabel.h
/usr/include/gtk-4.0/gtk/gtklayoutchild.h
/usr/include/gtk-4.0/gtk/gtklayoutmanager.h
/usr/include/gtk-4.0/gtk/gtklevelbar.h
/usr/include/gtk-4.0/gtk/gtklinkbutton.h
/usr/include/gtk-4.0/gtk/gtklistbase.h
/usr/include/gtk-4.0/gtk/gtklistbox.h
/usr/include/gtk-4.0/gtk/gtklistheader.h
/usr/include/gtk-4.0/gtk/gtklistitem.h
/usr/include/gtk-4.0/gtk/gtklistitemfactory.h
/usr/include/gtk-4.0/gtk/gtklistview.h
/usr/include/gtk-4.0/gtk/gtkmain.h
/usr/include/gtk-4.0/gtk/gtkmaplistmodel.h
/usr/include/gtk-4.0/gtk/gtkmediacontrols.h
/usr/include/gtk-4.0/gtk/gtkmediafile.h
/usr/include/gtk-4.0/gtk/gtkmediastream.h
/usr/include/gtk-4.0/gtk/gtkmenubutton.h
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
/usr/include/gtk-4.0/gtk/gtkpaned.h
/usr/include/gtk-4.0/gtk/gtkpasswordentry.h
/usr/include/gtk-4.0/gtk/gtkpasswordentrybuffer.h
/usr/include/gtk-4.0/gtk/gtkpicture.h
/usr/include/gtk-4.0/gtk/gtkpopover.h
/usr/include/gtk-4.0/gtk/gtkpopovermenu.h
/usr/include/gtk-4.0/gtk/gtkpopovermenubar.h
/usr/include/gtk-4.0/gtk/gtkprintdialog.h
/usr/include/gtk-4.0/gtk/gtkprogressbar.h
/usr/include/gtk-4.0/gtk/gtkrange.h
/usr/include/gtk-4.0/gtk/gtkrecentmanager.h
/usr/include/gtk-4.0/gtk/gtkrevealer.h
/usr/include/gtk-4.0/gtk/gtkroot.h
/usr/include/gtk-4.0/gtk/gtkscale.h
/usr/include/gtk-4.0/gtk/gtkscalebutton.h
/usr/include/gtk-4.0/gtk/gtkscrollable.h
/usr/include/gtk-4.0/gtk/gtkscrollbar.h
/usr/include/gtk-4.0/gtk/gtkscrolledwindow.h
/usr/include/gtk-4.0/gtk/gtkscrollinfo.h
/usr/include/gtk-4.0/gtk/gtksearchbar.h
/usr/include/gtk-4.0/gtk/gtksearchentry.h
/usr/include/gtk-4.0/gtk/gtksectionmodel.h
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
/usr/include/gtk-4.0/gtk/gtkstringfilter.h
/usr/include/gtk-4.0/gtk/gtkstringlist.h
/usr/include/gtk-4.0/gtk/gtkstringsorter.h
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
/usr/include/gtk-4.0/gtk/gtktreeexpander.h
/usr/include/gtk-4.0/gtk/gtktreelistmodel.h
/usr/include/gtk-4.0/gtk/gtktreelistrowsorter.h
/usr/include/gtk-4.0/gtk/gtktypebuiltins.h
/usr/include/gtk-4.0/gtk/gtktypes.h
/usr/include/gtk-4.0/gtk/gtkurilauncher.h
/usr/include/gtk-4.0/gtk/gtkversion.h
/usr/include/gtk-4.0/gtk/gtkvideo.h
/usr/include/gtk-4.0/gtk/gtkviewport.h
/usr/include/gtk-4.0/gtk/gtkwidget.h
/usr/include/gtk-4.0/gtk/gtkwidgetpaintable.h
/usr/include/gtk-4.0/gtk/gtkwindow.h
/usr/include/gtk-4.0/gtk/gtkwindowcontrols.h
/usr/include/gtk-4.0/gtk/gtkwindowgroup.h
/usr/include/gtk-4.0/gtk/gtkwindowhandle.h
/usr/include/gtk-4.0/gtk/print/gtkpagesetup.h
/usr/include/gtk-4.0/gtk/print/gtkpapersize.h
/usr/include/gtk-4.0/gtk/print/gtkprintcontext.h
/usr/include/gtk-4.0/gtk/print/gtkprintoperation.h
/usr/include/gtk-4.0/gtk/print/gtkprintoperationpreview.h
/usr/include/gtk-4.0/gtk/print/gtkprintsettings.h
/usr/include/gtk-4.0/unix-print/gtk/gtkunixprint.h
/usr/include/gtk-4.0/unix-print/gtk/print/gtkpagesetupunixdialog.h
/usr/include/gtk-4.0/unix-print/gtk/print/gtkprinter.h
/usr/include/gtk-4.0/unix-print/gtk/print/gtkprintjob.h
/usr/include/gtk-4.0/unix-print/gtk/print/gtkprintunixdialog.h
/usr/lib64/libgtk-4.so
/usr/lib64/pkgconfig/gtk4-atspi.pc
/usr/lib64/pkgconfig/gtk4-unix-print.pc
/usr/lib64/pkgconfig/gtk4-wayland.pc
/usr/lib64/pkgconfig/gtk4-x11.pc
/usr/lib64/pkgconfig/gtk4.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gtk-4.0/4.0.0/media/libmedia-gstreamer.so
/V3/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so
/V3/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-file.so
/V3/usr/lib64/libgtk-4.so.1.1400.3
/usr/lib64/gtk-4.0/4.0.0/media/libmedia-gstreamer.so
/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so
/usr/lib64/gtk-4.0/4.0.0/printbackends/libprintbackend-file.so
/usr/lib64/libgtk-4.so.1
/usr/lib64/libgtk-4.so.1.1400.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk4/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gtk4/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/gtk4/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f gtk40.lang
%defattr(-,root,root,-)

