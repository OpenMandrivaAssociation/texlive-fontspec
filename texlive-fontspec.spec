%global tl_name fontspec
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9g
Release:	%{tl_revision}.1
Summary:	Advanced font selection in XeLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/fontspec
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontspec.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(euenc)
Requires:	texlive(iftex)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(lm)
Requires:	texlive(xunicode)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an automatic
and unified interface to feature-rich AAT and OpenType fonts through the
NFSS in LaTeX running on XeTeX or LuaTeX engines. The package requires
the l3kernel and xparse bundles from the LaTeX3 development team.

