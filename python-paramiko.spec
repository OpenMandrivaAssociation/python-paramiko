%define module_name 	paramiko
%define version 1.10.1

Summary: 	SSH2 protocol for Python
Name: 		python-%module_name
Version: 	%version
Release: 	1
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




%changelog
* Tue Oct 25 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1.7.7.1-3
+ Revision: 707074
- new version 1.7.7.1

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.7.6-2mdv2011.0
+ Revision: 591781
- Rebuild

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.6-1mdv2010.1
+ Revision: 489188
- update to new version 1.7.6

* Thu Sep 17 2009 Michael Scherer <misc@mandriva.org> 1.7.5-1mdv2010.0
+ Revision: 443919
- update to new version 1.7.5

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7.4-3mdv2010.0
+ Revision: 442326
- rebuild

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 1.7.4-2mdv2009.1
+ Revision: 321177
- Rebuild for 2.6

* Fri Aug 15 2008 Michael Scherer <misc@mandriva.org> 1.7.4-1mdv2009.0
+ Revision: 272310
- new version
- new url

* Mon Mar 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.2-1mdv2008.1
+ Revision: 183316
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.6.4-1mdv2008.1
+ Revision: 122368
- New release 1.6.4 and bypass check


* Sun Jan 07 2007 Michael Scherer <misc@mandriva.org> 1.5.2-4mdv2007.0
+ Revision: 105220
- rebuild for python 2.5
- use %%rel scheme for mkrel
- Import python-paramiko

