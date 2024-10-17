Name:		texlive-lshort-dutch
Version:	15878
Release:	2
Summary:	Introduction to LaTeX in Dutch
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/dutch
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
