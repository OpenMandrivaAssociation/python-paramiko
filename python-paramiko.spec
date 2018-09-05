%define py2_purelibdir %(python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())' 2>/dev/null || echo PYTHON-LIBDIR-NOT-FOUND)
%define py3_purelibdir %(python3 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib())' 2>/dev/null || echo PYTHON-LIBDIR-NOT-FOUND)
%define module_name 	paramiko

Summary: 	SSH2 protocol for Python
Name: 		python-%module_name
Version: 	2.4.1
Release: 	1
Url: 		http://www.lag.net//paramiko/
License: 	LGPL 2+
Group: 		Development/Python
Source0: 	http://pypi.python.org/packages/source/p/paramiko/paramiko-%{version}.tar.gz

Requires:   python-cryptography
Obsoletes:  %{module_name}
Provides:   %{module_name}
BuildRequires:	python2-devel
BuildRequires:	python3-devel
BuildRequires:	python-cryptography
BuildRequires:	python2-cryptography
BuildArch:	noarch

%description
Paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines.  the module works
by taking a socket-like object that you pass in, negotiating with the remote
server, authenticating (using a password or a given private key), and opening
flow-controled "channels" to the server, which are returned as socket-like
objects. you are responsible for verifying that the server's host key is the
one you expected to see, and you have control over which kinds of encryption
or hashing you prefer (if you care), but all of the heavy lifting is done by
the paramiko module.

%package -n python2-%module_name
Summary:	Version of the Paramiko SSH2 module for Python 2.x
Group:		Development/Python
Requires:	python2-cryptography

%description -n python2-%module_name
Paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines.  the module works
by taking a socket-like object that you pass in, negotiating with the remote
server, authenticating (using a password or a given private key), and opening
flow-controled "channels" to the server, which are returned as socket-like
objects. you are responsible for verifying that the server's host key is the
one you expected to see, and you have control over which kinds of encryption
or hashing you prefer (if you care), but all of the heavy lifting is done by
the paramiko module.

%prep
%setup -q -n %module_name-%version

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python3 setup.py install --root=%{buildroot}

%files
%doc python3/README.rst python3/tests python3/demo*
%{py3_puresitedir}/*.egg-info
%{py3_puresitedir}/%module_name

%files -n python2-%module_name
%doc python2/README.rst python2/tests python2/demo*
%{py2_puresitedir}/*.egg-info
%{py2_puresitedir}/%module_name
