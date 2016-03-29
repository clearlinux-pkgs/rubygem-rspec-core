#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec-core
Version  : 3.3.2
Release  : 10
URL      : https://rubygems.org/downloads/rspec-core-3.3.2.gem
Source0  : https://rubygems.org/downloads/rspec-core-3.3.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-rspec-core-bin
BuildRequires : ruby
BuildRequires : rubygem-coderay
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rr
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-thread_order

%description
# rspec-core [![Build Status](https://secure.travis-ci.org/rspec/rspec-core.svg?branch=master)](http://travis-ci.org/rspec/rspec-core) [![Code Climate](https://codeclimate.com/github/rspec/rspec-core.svg)](https://codeclimate.com/github/rspec/rspec-core)

%package bin
Summary: bin components for the rubygem-rspec-core package.
Group: Binaries

%description bin
bin components for the rubygem-rspec-core package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-core-3.3.2
gem spec %{SOURCE0} -l --ruby > rubygem-rspec-core.gemspec

%build
gem build rubygem-rspec-core.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-core-3.3.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-core-3.3.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/.document
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/Changelog.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/License.txt
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/exe/rspec
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/autorun.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/backtrace_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/bisect/coordinator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/bisect/example_minimizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/bisect/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/bisect/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/bisect/subset_enumerator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/configuration_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/drb.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/dsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/example_status_persister.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/filter_manager.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/flat_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/base_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/base_text_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/bisect_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/bisect_progress_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/console_codes.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/deprecation_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/documentation_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/exception_presenter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/fallback_message_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/html_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/html_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/json_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/profile_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/progress_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/protocol.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/formatters/snippet_extractor.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/hooks.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/memoized_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/metadata_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/minitest_assertions_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mocking_adapters/flexmock.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mocking_adapters/mocha.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mocking_adapters/null.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mocking_adapters/rr.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mocking_adapters/rspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/mutex.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/notifications.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/option_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/ordering.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/pending.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/profiler.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/project_initializer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/project_initializer/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/project_initializer/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/rake_task.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/reentrant_mutex.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/ruby_project.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/sandbox.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/set.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/shared_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/shared_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/shell_escape.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/test_unit_assertions_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/warnings.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-core-3.3.2/lib/rspec/core/world.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-core-3.3.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rspec
