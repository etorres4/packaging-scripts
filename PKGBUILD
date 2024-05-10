# Maintainer: Eric Torres <eric.torres@its-et.me>
pkgname=packaging-scripts
pkgver=1.7.1
pkgrel=4
pkgdesc="A set of helper scripts for handling Arch Linux packages"
arch=('any')
license=('MIT')
groups=(pacman-helpers)
depends=(gist mlocate pacman python pyalpm)
makedepends=(python-build python-installer python-setuptools)
optdepends=('fzf: for the fqo script'
            'mlocate: for the fqo script')
checkdepends=(python-hypothesis python-pytest)
backup=(etc/apparmor.d/usr.bin.{addpkg,delpkg} etc/packaging-scripts.conf)
source=("${pkgname}::git+file:///home/etorres/Projects/packaging-scripts")
sha256sums=('SKIP')

build() {
    cd "$srcdir/$pkgname"
    python -m build --wheel --no-isolation
}

check() {
    cd "$srcdir/$pkgname"
    pytest
}

package() {
    cd "$srcdir/$pkgname"
    python -m installer --destdir="$pkgdir" dist/*.whl

    # install README
    install -Dm644 README.rst "${pkgdir}/usr/share/doc/${pkgname}/README.rst"

    # install config file
    install -Dm644 'misc/packaging-scripts.conf' "${pkgdir}/etc/packaging-scripts.conf"

    # install AppArmor profiles
    for profile in misc/apparmor/*; do
        install -Dm644 "${profile}" "${pkgdir}/etc/apparmor.d/${profile##*/}"
    done

    # install pug hook
    install -Dm644 'misc/pug.hook' "${pkgdir}/usr/share/libalpm/hooks/pug.hook"

    # install zsh completions
    install -d "${pkgdir}/usr/share/zsh/site-functions"
    for completion in packaging_scripts/zsh-completions/*; do
        install -m644 "${completion}"\
            "${pkgdir}/usr/share/zsh/site-functions/${completion##*/*}"
    done

    # install license
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
