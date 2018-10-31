Name:		texlive-fontspec
Version:	2.6h
Release:	2
Summary:	Advanced font selection in XeLaTeX and LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontspec
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-iftex
Requires:	texlive-kastrup
Requires:	texlive-l3kernel
Requires:	texlive-l3packages
Requires:	texlive-lm

%description
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an
automatic and unified interface to feature-rich AAT and
OpenType fonts through the NFSS in LaTeX running on XeTeX or
LuaTeX engines. The package requires the l3kernel and xparse
bundles from the LaTeX 3 development team.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fontspec
%doc %{_texmfdistdir}/doc/latex/fontspec
#- source
%doc %{_texmfdistdir}/source/latex/fontspec

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
