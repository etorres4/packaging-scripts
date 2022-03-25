# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=packaging-scripts
pkgver=1.7.0
pkgrel=1
pkgdesc="A set of helper scripts for handling Arch Linux packages"
arch=('any')
license=('MIT')
groups=(pacman-helpers)
depends=(gist pacman python)
makedepends=(git python-setuptools)
optdepends=('fzf: for the fqo script'
            'mlocate: for the fqo script')
checkdepends=(python-hypothesis python-pytest)
backup=(etc/apparmor.d/usr.bin.{addpkg,delpkg}
    etc/packaging-scripts.conf)
source=("${pkgname}::git+file:///home/etorres/Projects/packaging-scripts")
sha256sums=('SKIP')

pkgver() {
    cd $srcdir/$pkgname
    python setup.py --version
}

build() {
    cd $srcdir/$pkgname
    python setup.py build
}

check() {
    cd $srcdir/$pkgname
    python -m unittest
}

package() {
    cd $srcdir/$pkgname

    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

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
}
