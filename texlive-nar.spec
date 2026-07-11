%global tl_name nar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.19
Release:	%{tl_revision}.1
Summary:	BibTeX style for Nucleic Acid Research
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/nar.bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nar.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This BibTeX bibliography style is for the journal Nucleic Acid Research.
It was adapted from the standard unsrt.bst style file.

