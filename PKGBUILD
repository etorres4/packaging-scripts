# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=packaging-scripts
pkgver=1.4
pkgrel=1
pkgdesc="A set of helper scripts for handling Arch Linux packages"
arch=('any')
license=('MIT')
groups=('pacman-helpers')
depends=('pacman' 'python>=3.6')
makedepends=('git' 'python-setuptools')
optdepends=('fzf: for the fqo script'
            'mlocate: for the fqo script')
checkdepends=('python-hypothesis')
backup=(etc/apparmor.d/usr.bin.{addpkg,delpkg})
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('7f235f7bc5d500ed2e9ef371678d176d4c9fdff268aac11f52f9fd4891cf8719')
sha512sums=('74fe9fa108fd0acbfcb24ebbfa91e2aadf356f018938c6ba8fe890bb74e23d06cbfeee2114836ad501a71df7dab4460d03c4c75808f1e71e7610bd3c16a754b5')

build() {
    cd "$srcdir"
    python setup.py build
}

check() {
    cd "$srcdir"
    python -m unittest
}

package() {
    cd "$srcdir"

    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

    # install README
    install -Dm644 README.rst "${pkgdir}/usr/share/doc/${pkgname}/README.rst"

    # install AppArmor profiles
    for profile in misc/apparmor/*; do
        install -Dm644 "${profile}" "${pkgdir}/etc/apparmor.d/${profile##*/}"
    done

    # install zsh completions
    install -d "${pkgdir}/usr/share/zsh/site-functions"
    for completion in packaging_scripts/zsh-completions/*; do
        install -m644 "${completion}"\
            "${pkgdir}/usr/share/zsh/site-functions/${completion##*/*}"
    done
}
