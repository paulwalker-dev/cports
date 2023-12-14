# include trigger autodeps
#
# some stuff should always have a dependency on the package
# it triggers, particularly stuff like sysusers/tmpfiles
# as well as typically desktop/mime stuff, add it here so
# that it's not forgotten as it tends to be
#
# TODO: maybe figure out a way to decentralize this?

from cbuild.core import logger

_trigdeps = {
    "etc/ca-certificates/update.d": "ca-certificates",
    "usr/lib/sysusers.d": "systemd-utils",
    "usr/lib/tmpfiles.d": "systemd-utils",
    # TODO: do we want this? it pulls in glib
    # "usr/share/applications": "desktop-file-utils",
    "usr/share/ca-certificates": "ca-certificates",
    # ditto
    # "usr/share/mime": "shared-mime-info",
}


def invoke(pkg):
    if not pkg.options["scantrigdeps"]:
        return

    deps = []
    log = logger.get()

    for key in _trigdeps:
        if (pkg.destdir / key).is_dir():
            pkgn = _trigdeps[key]
            # don't add self-dependency
            if pkg.pkgname == pkgn:
                continue
            deps.append((key, pkgn))

    depl = list(filter(lambda tpl: tpl[1] not in pkg.depends, deps))

    depset = set()
    for path, dep in depl:
        log.out_plain(f"   TRIGGER DEPENDENCY: {path} -> {dep}")
        # add it only once in case several paths add the same dep
        if dep not in depset:
            pkg.depends.append(dep)
            depset.add(dep)
