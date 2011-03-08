%define rubyver         1.9.2
%define rubyminorver    p136

%{!?ruby_vendorlib:     %global ruby_vendorlib  %{_prefix}/lib/ruby}
%{!?ruby_vendorarch:    %global ruby_vendorarch %{_libdir}/ruby}
%{!?ruby_sitelib:       %global ruby_sitelib    %{ruby_vendorlib}/site_ruby}
%{!?ruby_sitearch:      %global ruby_sitearch   %{ruby_vendorarch}/site_ruby}

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 1.9
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel


%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --with-sitedir='%{ruby_sitelib}' \
  --with-sitearchdir='%{ruby_sitearch}' \
  --with-vendordir='%{ruby_vendorlib}' \
  --with-vendorarchdir='%{ruby_vendorarch}'

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/lib/
rm -rf $RPM_BUILD_ROOT/usr/share/doc/ruby
rm -rf $RPM_BUILD_ROOT/usr/src
#rm -f $RPM_BUILD_ROOT/usr/lib64/libruby-static.a
#rm -f $RPM_BUILD_ROOT/usr/lib64/libruby.so


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog LEGAL ToDo
%{_bindir}
%{_includedir}
%{_prefix}/lib64/
%{_prefix}/share/

%changelog
* Tue Mar 7 2011 Robert Duncan <robert@robduncan.co.uk> - 1.9.2-p136-2
- Update prerequisites to include make

* Sun Jan 2 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p136-1
- Initial spec to replace system ruby with 1.9.2-p136
