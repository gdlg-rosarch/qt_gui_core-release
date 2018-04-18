# Script generated with Bloom
pkgdesc="ROS - qt_gui_cpp provides the foundation for C++-bindings for qt_gui and creates bindings for every generator available. At least one specific binding must be available in order to use C++-plugins."
url='http://ros.org/wiki/qt_gui_cpp'

pkgname='ros-lunar-qt-gui-cpp'
pkgver='0.3.8_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pkg-config'
'qt5-base'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-pluginlib>=1.9.23'
'ros-lunar-python-qt-binding>=0.3.0'
'tinyxml'
)

depends=('ros-lunar-pluginlib>=1.9.23'
'ros-lunar-qt-gui>=0.3.0'
'tinyxml'
)

conflicts=()
replaces=()

_dir=qt_gui_cpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/qt_gui_cpp $srcdir/qt_gui_cpp
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

