Name:		texlive-nar
Version:	38100
Release:	2
Summary:	BibTeX style for Nucleic Acid Research
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nar
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nar.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This BibTeX bibliography style is for the journal Nucleic Acid
Research. It was adapted from the standard unsrt.bst style
file.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/nar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
