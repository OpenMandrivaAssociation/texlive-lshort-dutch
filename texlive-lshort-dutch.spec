%global tl_name lshort-dutch
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Introduction to LaTeX in Dutch
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/dutch
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-dutch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Dutch (Nederlands) translation of the Short Introduction to
LaTeX2e.

