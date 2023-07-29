%define module_name 	paramiko

Summary: 	SSH2 protocol for Python
Name: 		python-%module_name
Version:	3.3.1
Release:	1
Url: 		http://www.paramiko.org
License: 	LGPL 2+
Group: 		Development/Python
Source0:        https://github.com/paramiko/paramiko/archive/%{version}/%{module_name}-%{version}.tar.gz

Requires:   python-cryptography
Obsoletes:  %{module_name}
Provides:   %{module_name}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python-cryptography
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
%setup -q -n %module_name-%version

%install
python setup.py install --root=%{buildroot}

%files
%doc README.rst tests demo*
%{py3_puresitedir}/*.egg-info
%{py3_puresitedir}/%module_name
