# revision 15878
# category Package
# catalog-ctan /info/lshort/dutch
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license gpl
# catalog-version 1.3
Name:		texlive-lshort-dutch
Version:	1.3
Release:	11
Summary:	Introduction to LaTeX in Dutch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/dutch
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Dutch (Nederlands) translation of the Short
Introduction to LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-dutch/LEESMIJ
%doc %{_texmfdistdir}/doc/latex/lshort-dutch/README
%doc %{_texmfdistdir}/doc/latex/lshort-dutch/WIJZIGINGEN
%doc %{_texmfdistdir}/doc/latex/lshort-dutch/lshort-nl-1.3.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-dutch/lshort-nl-1.3.src.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 753467
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718887
- texlive-lshort-dutch
- texlive-lshort-dutch
- texlive-lshort-dutch
- texlive-lshort-dutch

