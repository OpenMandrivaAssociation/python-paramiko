%define module_name 	paramiko
%define version 1.6.4
%define rel 1

Summary: 	SSH2 protocol for Python
Name: 		python-%module_name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://www.lag.net/~robey/paramiko/
License: 	GPL
Group: 		Development/Python
Source: 	http://www.lag.net/~robey/paramiko/download/%{module_name}-%{version}.tar.bz2

Requires:   pycrypto
Obsoletes:  %{module_name}
Provides:   %{module_name}
BuildRequires:	python-devel
BuildRequires:	pycrypto
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

%prep
%setup -q -n %module_name-%version.orig

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%check
#python test.py

%files
%defattr(-,root,root)
%doc docs PKG-INFO README tests demo*
%py_puresitedir/*.egg-info
%py_puresitedir/%module_name


