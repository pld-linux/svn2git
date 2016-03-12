Summary:	Tool for importing existing svn projects into git
Name:		svn2git
Version:	2.3.2
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/nirvdrum/svn2git/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	40c64c24e2d5ba31f16a277e2f9ffddf
URL:		https://github.com/nirvdrum/svn2git
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	git-core-svn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svn2git is a tiny utility for migrating projects from Subversion to
Git while keeping the trunk, branches and tags where they should be.
It uses git-svn to clone an svn repository and does some clean-up to
make sure branches and tags are imported in a meaningful way, and that
the code checked into master ends up being what's currently in your
svn trunk rather than whichever svn branch your last commit was in.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.markdown README.markdown MIT-LICENSE
%attr(755,root,root) %{_bindir}/svn2git
%{ruby_vendorlibdir}/svn2git.rb
%{ruby_vendorlibdir}/svn2git
