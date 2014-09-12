#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	DecisionTree
Summary:	AI::DecisionTree - automatically learns decision trees
Summary(pl.UTF-8):	AI::DecisionTree - automatyczne uczenie drzew decyzyjnych
Name:		perl-AI-DecisionTree
Version:	0.09
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79ee9671099f498d52571cb91c06ec87
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%{?with_tests:BuildRequires:	perl-GraphViz}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "AI::DecisionTree" module automatically creates so-called
"decision trees" to explain a set of training data. A decision tree is
a kind of categorizer that use a flowchart-like process for
categorizing new instances. For instance, a learned decision tree
might look like that one in documentation, which classifies for the
concept "play tennis".

%description -l pl.UTF-8
Moduł AI::DecisionTree automatycznie tworzy tak zwane "drzewa
decyzyjne" do objaśniania zbiorów danych uczących. Drzewo decyzyjne to
rodzaj klasyfikatora używającego procesu podobnego do przepływu do
klasyfikacji nowych przypadków. Na przykład, nauczone drzewo decyzyjne
może wyglądać jak to umieszczone w dokumentacji, klasyfikujące dla
pojęcia "gry w tenisa".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}/Instance
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/Instance/*.so
%{_mandir}/man3/*
