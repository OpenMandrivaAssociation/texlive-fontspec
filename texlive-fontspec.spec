# revision 30618
# category Package
# catalog-ctan /macros/latex/contrib/fontspec
# catalog-date 2013-03-17 00:29:52 +0100
# catalog-license lppl1.3
# catalog-version v2.3a
Name:		texlive-fontspec
Version:	v2.3a
Release:	4
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
%{_texmfdistdir}/tex/latex/fontspec/fontspec-luatex.sty
%{_texmfdistdir}/tex/latex/fontspec/fontspec-patches.sty
%{_texmfdistdir}/tex/latex/fontspec/fontspec-xetex.sty
%{_texmfdistdir}/tex/latex/fontspec/fontspec.cfg
%{_texmfdistdir}/tex/latex/fontspec/fontspec.lua
%{_texmfdistdir}/tex/latex/fontspec/fontspec.sty
%doc %{_texmfdistdir}/doc/latex/fontspec/README
%doc %{_texmfdistdir}/doc/latex/fontspec/fontspec-example.tex
%doc %{_texmfdistdir}/doc/latex/fontspec/fontspec-testsuite.pdf
%doc %{_texmfdistdir}/doc/latex/fontspec/fontspec.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fontspec/Makefile
%doc %{_texmfdistdir}/source/latex/fontspec/fontspec.dtx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-alias-feature-option.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-alias-feature.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-autofake.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-autoscaling.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-charactervariant.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-colour-basic.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-colour-clash.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-colour-opacity.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-feat-numbers.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-font-selection-bold.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-hyphenchar.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-inner-emph.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-loading-basic.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-loading-external-underdefined.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-loading-nested-scfeat.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-loading-scale.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-loading-sizefeatures.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-optical-sizes.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-ot-cvxx-2.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-ot-cvxx.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-ot-ss06.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-programmers-interface.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-verb-fancyvrb.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-verb-listings.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-verb-moreverb.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-verb-plain.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-verb-verbatim.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/F-wordspace.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/X-new-font-feature.ltx
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/testsuite-listing.tex
%doc %{_texmfdistdir}/source/latex/fontspec/testsuite/testsuite.cls

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
