Name:		texlive-lshort-dutch
Version:	1.3
Release:	1
Summary:	Introduction to LaTeX in Dutch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/dutch
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
