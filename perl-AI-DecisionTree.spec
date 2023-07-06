#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	AI
%define		pnam	DecisionTree
Summary:	AI::DecisionTree - automatically learns decision trees
Summary(pl.UTF-8):	AI::DecisionTree - automatyczne uczenie drzew decyzyjnych
Name:		perl-AI-DecisionTree
Version:	0.11
Release:	6
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab18666204a5363ced7f6a2eafd9da7f
URL:		http://search.cpan.org/dist/AI-DecisionTree/
%{?with_tests:BuildRequires:	perl-GraphViz}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
