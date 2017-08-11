# Generated from parse-cron-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name parse-cron

# explicitly override gem macros to avoid problems with different
# version and upstream_version
%if 0%{?dlrn} > 0
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{upstream_version}
%global gem_cache   %{gem_dir}/cache/%{gem_name}-%{upstream_version}.gem
%global gem_spec    %{gem_dir}/specifications/%{gem_name}-%{upstream_version}.gemspec
%global gem_docdir  %{gem_dir}/doc/%{gem_name}-%{upstream_version}
%endif

Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: Parses cron expressions and calculates the next occurence
Group: Development/Languages
License: MIT
URL: https://github.com/siebertm/parse-cron
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Parses cron expressions and calculates the next occurence.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%if 0%{?dlrn} > 0
%gem_install -n %{gem_name}-%{upstream_version}.gem
%else
%gem_install
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/License
%{gem_libdir}
%exclude %{gem_instdir}/parse-cron.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Aug 11 2017 Martin Mágr <mmagr@redhat.com> - 0.1.4-1
- Initial package
