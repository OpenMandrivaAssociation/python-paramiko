%define module_name 	paramiko
%define version 1.7.5
%define rel 1

Summary: 	SSH2 protocol for Python
Name: 		python-%module_name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://www.lag.net//paramiko/
License: 	LGPL 2+
Group: 		Development/Python
Source: 	http://www.lag.net/paramiko/download/%{module_name}-%{version}.tar.gz

Requires:   pycrypto
Obsoletes:  %{module_name}
Provides:   %{module_name}
BuildRequires:	python-devel
BuildRequires:	pycrypto
BuildArch:	noarch
Buildroot: 	%_tmppath/%name-%version

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

%prep
%setup -q -n %module_name-%version

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

#%check
#python test.py

%files
%defattr(-,root,root)
%doc docs PKG-INFO README tests demo*
%py_puresitedir/*.egg-info
%py_puresitedir/%module_name


