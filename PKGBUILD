# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=packaging-scripts
pkgver=1.1.3
pkgrel=1
pkgdesc="A set of helper scripts for handling Arch Linux packages"
arch=('any')
license=('MIT')
groups=('pacman-helpers')
depends=('pacman' 'python')
makedepends=('git' 'python-setuptools')
optdepends=('fzf: for the fqo script'
            'mlocate: for the fqo script')
backup=(etc/apparmor.d/usr.bin.{addpkg,delpkg})
source=("git+file:///home/etorres/Projects/packaging-scripts")
sha256sums=('SKIP')
sha512sums=('SKIP')

build() {
    cd "$srcdir/$pkgname"
    python setup.py build
}

package() {
    cd "${srcdir}/${pkgname}"

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
