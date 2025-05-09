pkgname = "perl-algorithm-diff"
pkgver = "1.201"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
checkdepends = ["perl"]
depends = ["perl"]
pkgdesc = "Compute differences between files/lists"
license = "Artistic-1.0-Perl"
url = "https://metacpan.org/pod/Algorithm::Diff"
source = f"$(CPAN_SITE)/Algorithm/Algorithm-Diff-{pkgver}.tar.gz"
sha256 = "0022da5982645d9ef0207f3eb9ef63e70e9713ed2340ed7b3850779b0d842a7d"
