# What is this spec?

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.2+ on RHEL based systems. I have based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.2 and Ruby Enterprise Edition.

### How to install

#### RHEL/CentOS 5/6

    yum install -y rpm-build rpmdevtools readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES
    wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.2-p320.tar.gz
    cd ~/rpmbuild/SPECS
    wget https://raw.github.com/imeyer/ruby-1.9.2-rpm/master/ruby19.spec
    rpmbuild -bb ruby19.spec
    rpm -Uvh ~/rpmbuild/RPMS/x86_64/ruby-1.9.2p320-1.ruby-1.9.2p320-1.i386.rpm

**PROFIT!**

### What it does

+ Builds
+ Installs
+ Overwrites/upgrades your currently installed ruby package (**DANGEROUS**)

### What it does **not** do

+ Split packages into ruby-libs, ruby-devel, etc (looking for help here)
+ Install alongside Ruby 1.8.x

### Requirements

+ EPEL Yum repository (for rpmdev-setuptree)

### Distro support

Tested working (as sane as I could test for) on:

* RHEL 5.x x86_64
* RHEL 6.x x86_64
* RHEL 6.x i686
* CentOS 5.x x86_64
* Scientific Linux 6.x x86_64

### Personal thoughts

This is by no means, correct, or sane. Nor does it follow any sort of policy for packaging. I leave that to the people who are most familiar with such things, and will willingly accept patches that add those features.
