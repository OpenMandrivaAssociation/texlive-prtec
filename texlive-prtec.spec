Name:		texlive-prtec
Version:	51919
Release:	1
Summary:	A template for PRTEC conference papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prtec
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prtec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prtec.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class, a BibTeX style, and a
LaTeX template to format conference papers for the Pacific Rim
Thermal Engineering Conference (PRTEC). The .tex and .cls files
are commented and should be self-explanatory. The package
depends on newtx.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/prtec
%{_texmfdistdir}/bibtex/bst/prtec
%doc %{_texmfdistdir}/doc/latex/prtec

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
