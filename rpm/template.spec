Name:           ros-jade-xacro
Version:        1.10.7
Release:        0%{?dist}
Summary:        ROS xacro package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/xacro
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-roslaunch
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-roslint
BuildRequires:  ros-jade-rostest

%description
Xacro (XML Macros) Xacro is an XML macro language. With xacro, you can construct
shorter and more readable XML files by using macros that expand to larger XML
expressions.

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
* Wed Jun 22 2016 Morgan Quigley <morgan@osrfoundation.org> - 1.10.7-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.6-0
- Autogenerated by Bloom

* Wed Aug 12 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.5-0
- Autogenerated by Bloom

* Thu Jun 18 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.4-0
- Autogenerated by Bloom

* Tue Jun 16 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.3-0
- Autogenerated by Bloom

* Sat May 23 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.2-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.1-0
- Autogenerated by Bloom

* Fri Mar 13 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.10.0-0
- Autogenerated by Bloom

