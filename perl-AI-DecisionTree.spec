%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	DecisionTree
Summary:	AI::DecisionTree -- Automatically Learns Decision Trees
Summary(pl):	AI::DecisionTree -- Automatyczne uczenie drzew decyzyjnych
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "AI::DecisionTree" module automatically creates so-called "decision
trees" to explain a set of training data.  A decision tree is a kind of
categorizer that use a flowchart-like process for categorizing new
instances.  For instance, a learned decision tree might look like that
one in documentation, which classifies for the concept "play tennis".

%description -l pl
Modu³ AI::DecisionTree automatycznie tworzy tak zwane "drzewa
decyzyjne" do obja¶niania zbiorów danych ucz±cych. Drzewo decyzyjne to
rodzaj klasyfikatora u¿ywaj±cego procesu podobnego do przep³ywu do
klasyfikacji nowych przypadków. Na przyk³ad, nauczone drzewo decyzyjne
mo¿e wygl±daæ jak to umieszczone w dokumentacji, klasyfikuj±ce dla
pojêcia "gry w tenisa".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
