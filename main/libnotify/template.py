pkgname = "libnotify"
pkgver = "0.8.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Ddocbook_docs=disabled",
    "-Dgtk_doc=false",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "libxslt-progs",
    "docbook-xsl",
    "gobject-introspection",
]
makedepends = [
    "glib-devel",
    "libpng-devel",
    "gdk-pixbuf-devel",
    "gtk+3-devel",
]
checkdepends = ["xwayland-run", "dbus"]
pkgdesc = "Desktop notification library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnotify"
source = f"$(GNOME_SITE)/libnotify/{pkgver[:-2]}/libnotify-{pkgver}.tar.xz"
sha256 = "c5540aaefb60e1d63b1c587c05f2284ebe72ece7d0c0e5e4a778cfd5844b6b58"
# introspection
optiosn = ["!cross"]


@subpackage("libnotify-devel")
def _(self):
    return self.default_devel()
