#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	DecisionTree
Summary:	AI::DecisionTree -- Automatically Learns Decision Trees
Summary(pl):	AI::DecisionTree -- Automatyczne uczenie drzew decyzyjnych
Name:		perl-%{pdir}-%{pnam}
Version:	0.08
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaed56886a22506b8ed5f6dab88e7060
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%{?with_test:BuildRequires:	perl-GraphViz}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "AI::DecisionTree" module automatically creates so-called "decision
trees" to explain a set of training data.  A decision tree is a kind of
categorizer that use a flowchart-like process for categorizing new
instances.  For instance, a learned decision tree might look like that
one in documentation, which classifies for the concept "play tennis".

%description -l pl
Modu� AI::DecisionTree automatycznie tworzy tak zwane "drzewa
decyzyjne" do obja�niania zbior�w danych ucz�cych. Drzewo decyzyjne to
rodzaj klasyfikatora u�ywaj�cego procesu podobnego do przep�ywu do
klasyfikacji nowych przypadk�w. Na przyk�ad, nauczone drzewo decyzyjne
mo�e wygl�da� jak to umieszczone w dokumentacji, klasyfikuj�ce dla
poj�cia "gry w tenisa".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}/Instance
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/Instance/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/Instance/*.bs
%{_mandir}/man3/*
