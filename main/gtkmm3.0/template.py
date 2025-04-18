pkgname = "gtkmm3.0"
pkgver = "3.24.10"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dbuild-demos=false", "-Dbuild-tests=true"]
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "atkmm1.6-devel",
    "cairomm1.0-devel",
    "gdk-pixbuf-devel",
    "gtk+3-devel",
    "pangomm1.4-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "C++ bindings for Gtk+3"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = (
    f"$(GNOME_SITE)/gtkmm/{pkgver[: pkgver.rfind('.')]}/gtkmm-{pkgver}.tar.xz"
)
sha256 = "7ab7e2266808716e26c39924ace1fb46da86c17ef39d989624c42314b32b5a76"


@subpackage("gtkmm3.0-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-3.0",
        ]
    )
