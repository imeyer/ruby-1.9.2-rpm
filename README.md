# What is this spec?

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.2+ on RHEL based systems. I have based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.2 and Ruby Enterprise Edition.

### How to install

#### RHEL/CentOS 5

    yum install -y rpm-build
    cd /usr/src/redhat/SOURCES
    wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.2-p136.tar.gz
    cd /usr/src/redhat/SPECS
    curl https://github.com/imeyer/ruby-1.9.2-rpm/raw/master/ruby19.spec > ruby19.spec
    rpmbuild -bb ruby19.spec
    rpm -Uvh ../RPMS/x86_64/ruby-1.9.2p136-1.x86_64.rpm
    
    [imeyer@XXXX SPECS]$ ruby --version
    ruby 1.9.2p136 (2010-12-25 revision 30365) [x86_64-linux]

**PROFIT!**

### What it does

+ Builds
+ Installs
+ Overwrites/upgrades your currently installed ruby package (**DANGEROUS**)

### What it does **not** do

+ Split packages into ruby-libs, ruby-devel, etc (looking for help here)
+ Install alongside Ruby 1.8.x

### Personal thoughts

This is by no means, correct, or sane. Nor does it follow any sort of policy for packaging. I leave that to the people who are most familiar with such things, and will willingly accept patches that add those features. 
