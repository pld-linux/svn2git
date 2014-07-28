Summary:	Tool for importing existing svn projects into git
Name:		svn2git
Version:	2.0.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://github.com/nirvdrum/svn2git/tarball/v%{version}?/%{name}-%{version}.tgz
# Source0-md5:	64f428daca195a9b04e9e4ff39566cc6
URL:		https://github.com/nirvdrum/svn2git
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
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
%setup -qc
mv *-svn2git-*/* .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
cp %{_datadir}/setup.rb .
%{__ruby} setup.rb config \
	--rbdir=%{ruby_vendorlibdir}

%{__ruby} setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.markdown README.markdown MIT-LICENSE
%attr(755,root,root) %{_bindir}/svn2git
%{ruby_vendorlibdir}/svn2git.rb
%dir %{ruby_vendorlibdir}/svn2git
%{ruby_vendorlibdir}/svn2git/blah.rb
%{ruby_vendorlibdir}/svn2git/migration.rb
