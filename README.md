# What is this spec?

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.2+ on RHEL based systems. I have based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.2 and Ruby Enterprise Edition.

### How to install

N.B. The following instructions assume installation on a 32-bit platform. For 64-bit replace i386 with x86_64 (not tested).

#### RHEL/CentOS 5

    yum install -y rpm-build
    cd /usr/src/redhat/SOURCES
    wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.2-p180.tar.gz
    cd /usr/src/redhat/SPECS
    curl https://github.com/robduncan/ruby-1.9.2-rpm/raw/master/ruby19.spec > ruby19.spec
    rpmbuild -bb ruby19.spec
    rpm -Uvh ../RPMS/i386/ruby-1.9.2p180-1.ruby-1.9.2p180-1.i386.rpm
    

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
