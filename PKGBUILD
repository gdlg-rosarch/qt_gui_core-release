# Script generated with Bloom
pkgdesc="ROS - qt_gui provides the infrastructure for an integrated graphical user interface based on Qt. It is extensible with Python- and C++-based plugins (implemented in separate packages) which can contribute arbitrary widgets. It requires either PyQt or PySide bindings."
url='http://ros.org/wiki/qt_gui'

pkgname='ros-lunar-qt-gui'
pkgver='0.3.8_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-pyqt5'
'qt5-base'
'ros-lunar-catkin'
)

depends=('python2-rospkg'
'ros-lunar-python-qt-binding>=0.3.0'
'tango-icon-theme'
)

conflicts=()
replaces=()

_dir=qt_gui
source=()
md5sums=()

prepare() {
    cp -R $startdir/qt_gui $srcdir/qt_gui
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

