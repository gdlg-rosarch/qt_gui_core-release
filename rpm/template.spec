Name:           ros-jade-qt-dotgraph
Version:        0.2.31
Release:        0%{?dist}
Summary:        ROS qt_dotgraph package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_dotgraph
Source0:        %{name}-%{version}.tar.gz

Requires:       pydot
Requires:       ros-jade-python-qt-binding
BuildRequires:  python-pygraphviz
BuildRequires:  ros-jade-catkin

%description
qt_dotgraph provides helpers to work with dot graphs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Nov 02 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.31-0
- Autogenerated by Bloom

* Wed Mar 30 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.30-0
- Autogenerated by Bloom

* Sat Sep 19 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.29-0
- Autogenerated by Bloom

* Mon Jun 08 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.28-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.27-0
- Autogenerated by Bloom

