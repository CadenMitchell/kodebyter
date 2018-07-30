# Maintainer: Caden Mitchell <sidedvirus@outlook.com>

pkgname="KodeByter"
_pkgname="kodebyter"
pkgver=1.3
pkgrel=1.3
pkgdesc='A program for encrypting and decrypting caesar cypher messages.'
url='https://github.com/CadenMitchell/kodebyter/'
arch=('any')
license=('GPL3')
depends=('python')
source=("${pkgname}-${pkgver}.tar.gz::https://codeload.github.com/CadenMitchell/${_pkgname}/tar.gz/1.0")
package() {
    cd "${srcdir}/${_pkgname}-1.0"

    install -D -m 777 kodebyter \
    	 "${pkgdir}/usr/bin/kodebyter"

    install -D -m 755 kodebyter.desktop \
    	 "${pkgdir}/usr/share/applications/kodebyter.desktop"

    install -D -m 755 kodebyter.svg \
    	 "${pkgdir}/usr/share/kodebyter/kodebyter.svg"
}