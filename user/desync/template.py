pkgname = "desync"
pkgver = "0.9.6"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/desync"]
hostmakedepends = ["go"]
pkgdesc = "Alternative casync implementation"
license = "BSD-3-Clause"
url = "https://github.com/folbricht/desync"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9d364c8b3b39457501006eb58c454f3a4961b8c3adc92ce11d1556f767a46d72"
# check: needs docker
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
