Name:		palp
Group:		Sciences/Mathematics
License:	GPL
Summary:	A Package for Analyzing Lattice Polytopes
Version:	1.1
Release:	3
Source:		http://hep.itp.tuwien.ac.at/~kreuzer/CY/palp/%{name}-%{version}.tar.gz
Source1:	http://arxiv.org/pdf/math/0204356v1
URL:		http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html

%description
PALP: A Package for Analyzing Lattice Polytopes with Applications to
Toric Geometry.
See also http://arxiv.org/abs/math/0204356

%prep
%setup -q -n %{name}

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
cp -fa class.x cws.x nef.x poly.x %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -fa %{SOURCE1} %{buildroot}%{_docdir}/%{name}/%{name}.pdf

%clean

%files
%{_bindir}/*
%dir %doc %{_docdir}/%{name}
%doc %{_docdir}/%{name}/%{name}.pdf


%changelog
* Thu Mar 26 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1mdv2009.1
+ Revision: 361502
- Initial import o pal version 1.1.
  PALP: A Package for Analyzing Lattice Polytopes
  http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html
- palp

