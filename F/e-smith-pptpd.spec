Summary: e-smith server and gateway - configure PPTP inbound VPN
%define name e-smith-pptpd
Name: %{name}
%define version 1.12.0
%define release 04
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Packager: e-smith developers <bugs@e-smith.com>
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-pptpd-1.12.0-misc.patch
Patch1: e-smith-pptpd-1.12.0-debug.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-base >= 4.13.16-27
Requires: pptpd
Requires: kmod-ppp
Requires: kmod-ppp-smp
Obsoletes: kernel-module-ppp
Obsoletes: kernel-smp-module-ppp
Requires: kernel => 2.4
Requires: e-smith-lib >= 1.15.1-16
Requires: e-smith-packetfilter >= 1.13.0-22
Requires: e-smith-radiusd
BuildRequires: e-smith-devtools >= 1.13.1-03
BuildArchitectures: noarch

%description
e-smith server and gateway - configure inbound PPTP VPN access

%changelog
* Sat Dec 02 2006 Shad L. Lords <slords@mail.com> 1.12.0-04
- Update requires to reflect new kernel module format

* Sun Apr  9 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-03
- Make pptpd debug logging depend on $pptpd{debug}. [SME: 1224]

* Tue Mar 21 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-02
- Purge Interfaces property of pptpd record on bootup. [SME: 1073]
- Remove multilink setting from pppd configuration used by pptpd. Add
  LCP timeout processing to autodisconnect stale links. [SME: 1064]
- Control "passive" setting by db property - enabled by default. [SME: 1064]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Wed Mar 1 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-22
- Add 'passive' option to /etc/ppp/options.pptpd [SME: 160]

* Wed Feb 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.0-21
- Dynamically calculate remote IP address range - dhcpd.conf won't
  necessarily be expanded before pptpd.conf, so we can't depend on
  a side effect. [SME: 797]

* Sun Feb 12 2006 Charlie Brady <charlieb@e-smith.com> 1.11.0-20
- Resolve some duplication of files included in e-smith-base.
  [SME: 752]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-19
- Bump release number only

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-18]
- Add Requires headers for kernel module RPMs, to ensure that module RPMs are
  added during install/upgrade.

* Wed Jul 27 2005 Shad L. Lords <slords@mail.com>
- [1.11.0-17]
- Add noipparam parameter so that ppp gets called correctly [SF: 1228376]
- Move masq fragment from template to db [SF: 1241414]
- Default sessions to 0 like web panel

* Tue Jul 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-16]
- Patch from Shad. Remove modprobe of ppp_generic (unnecessary). [SF: 1225995]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-15]
- Various options.pptpd config changes to support radius auth. [SF: 1225995]
- Ensure that ppp_generic module is loaded before running pptpd. [SF: 1225995]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-14]
- Add rc7.d startup symlink for pptpd. [SF: 1215401]
- Add Requires: e-smith-radiusd [SF: 1215401]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-13]
- Add missing radius plugin template fragment. [SF: 1215401]

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-12]
- Use radius plugin to access NT hash passwords and obsolete
  domain strip option. [SF: 1215401]

* Tue Mar 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-11]
- Fix path problem in adjust-services action symlinks. [MN00065576]
- Remove explicit links to implicit actions.

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-10]
- Fix more breakage in use of generic_template_expand action.  [MN00064130]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-09]
- Obsolete pptpd-restart by use of generic adjust-services action.
  [MN00065576]

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Fix some breakage in use of generic_template_expand action.  [MN00064130]

* Wed Jan 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-07]
- Use generic_template_expand action in place of pptpd-conf.
  [MN00064130]

* Fri Sep  3 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-06]
- Clean BuildRequires. [charlieb MN00043055]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-05]
- Made pptpd-restart pptpd status aware. [msoulier 4502]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-04]
- Updated pptpd-restart. [msoulier 4502]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-03]
- Removing old inittab fragment. [msoulier 4502]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-02]
- Adding supervision of pptpd. [msoulier 4502]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- rolling to dev - 1.11.0

* Wed Jul  9 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-02]
- Denylog inbound GRE unless pptpd is enabled. This allows
  masquerade to work better. [charlieb 9249]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Wed Jun 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-24]
- Enable ppp multilink, to help Win XP PPTP reliability [charlieb 9059]

* Wed Jun 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-23]
- Back out last change; it's required for address pool sharing. [charlieb 8874]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-22]
- Don't expand /etc/dhcpd.conf here - let the run script do it [gordonr 8883]

* Tue Jun 10 2003 Tony Clayton <apc@e-smith.com>
- [1.9.0-21]
- Fix pptpd.conf/remoteip fragment to use new StartIP property [tonyc 8883]

* Fri Jun  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-20]
- Fix runtime errors in last change, and add comment.  [charlieb 8951]

* Fri Jun  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-19]
- Use esmith::ConfigDB::wins_server method to determine correct
  wins server. [charlieb 8951]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-18]
- Fix arithmetic in last change. [charlieb 8883]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-17]
- Add comment to dhcpd.conf to show which addresses have been
  "borrowed". Remove template fragment which generates static IP definitions
  for pptpd "hostnames" (these aren't useful).  [charlieb 8883]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-16]
- Convert pptpd-conf script to use esmith::ConfigDB and remove use of
  deprecated CONFREF.
- Expand dhcpd.conf in pptpd-conf script, to ensure that address range
  is configured. [charlieb 8883]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-15]
- Improve explicit subtraction of pptpd addresses from DHCP range. [charlieb 8883]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-14]
- Relocate chap-secrets fragment to e-smith-base [gordonr 8747]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-13]
- Relocate /etc/smbpasswd to /etc/samba/smbpasswd [gordonr 8747]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-12]
- Removed processing of /etc/ppp/chap-secrets, now done in ppp-conf-users [gordonr 8849]
- Removed creation of pptpd record - defaults fragments exist [gordonr 8849]

* Fri May 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-11]
- Fixed createlinks [gordonr 4847]

* Fri May 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-10]
- Reconfigure pptp in user-modify-admin [gordonr 4847]

* Fri May 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-09]
- Rewrote chap-secrets fragment with new DB interface [gordonr 4847]
- Use VPNClientAccess instead of PPTPAccess [gordonr 4847]

* Tue May 13 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-08]
- Skip users unless PPTPAccess property of user is "yes". We don't want the
  no/disabled ambiguity. [charlieb 4847]

* Tue May  6 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-07]
- Call pptpd-conf in user-modify as well as create & delete [markk 4847]
- Skip users with PPTPAccess of 'off' or 'disabled' [markk 4847]

* Thu May  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-06]
- Added conf-masq and adjust-masq to ip-up.pptpd and ip-down events. 
  [msoulier 7695]

* Thu May  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-05]
- Fixed lack of /etc/ppp/ip-down.local file. [msoulier 7695]
- Removed iptables code from pptp-interface-access. It now sets an Interfaces
  parameter in the pptpd record. [msoulier 7695]
- Updated requirements. [msoulier 7695]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-04]
- Deleted ./etc/pptpd.conf/template-begin [lijied 3295]

* Tue Mar 11 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Don't create links to obsoleted pptpd-conf-startup in createlinks.
  [charlieb 7526]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Gracefully handle undefined "sessions" property in hosts.allow fragment
  [charlieb 5650]
- Move some db initiatisation into defaults directory fragments.
  [charlieb 7526]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Roll to development stream to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Thu Oct  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-06]
- Fix buglet in debug template fragment. [charlieb 4278]

* Thu Oct  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-05]
- Add hosts.allow template fragment (for new wrappers enabled pptpd)
  [charlieb 4278]
- Update /etc/ppp/options.pptpd template to match options available
  with CVS version of pppd. Add property driven debug fragment
  while we are at it [charlieb 4278]

* Wed Oct  2 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-04]
- Remove listen directive - all interfaces is the default, and new
  pptpd segfaults on "listen 0.0.0.0". [charlieb 4797]

* Tue Sep 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-03]
- Force re-tag of file from 1.7.0-02 [gordonr 4797]

* Mon Sep 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-02]
- Listen on all interfaces to avoid race condition with external
  interface configuration [gordonr 4797]

* Mon Sep 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-01]
- Forced version update by co2rpm to 1.7.0
- Bumped version number - this is a development stream [gordonr 4501]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.6-04]
- Fix destination address verification rules of gre-in rules. [charlieb 4501]

* Wed Sep 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.6-03]
- Add nomppe-40 option to prevent use of 40 bit encryption [charlieb 4278]

* Wed Sep 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.6-02]
- Roll back all PPP options changes so that we can use orig pppd binary.
  [charlieb 4278]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.6-01]
- Add action script to enable/disable unrestricted traffic on
  an interface when PPTP comes up/goes down. [charlieb 4501]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.5-01]
- Change allow_tcp_in calling sequence, to facilitate non-disruptive
  change. [charlieb 4501]
- Add GRE rules which are run-time switchable [charlieb 4501]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.5-01]
- Use allow_tcp_in() function in masq template fragment. [charlieb 4499]

* Wed Jul 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.4-01]
- Fix a few errors in the pptp PPP configuration. [charlieb 4278]

* Thu Jul 25 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.3-01]
- Use mschap and mppe configuration directives compatible with the latest
  pppd (from CVS).  [charlieb 4278]

* Tue Jul 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Fix iptables usage - on OUTPUT chain, now use -o interface_name, not
  -i interface_name. [charlieb 1268]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Changing version to development stream number - 1.5.0

* Mon May 27 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.5-01]
- Include pptpd-conf action in workgroup-update event, so that WINS setting is
  added/deleted if required. [charlieb 3602]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.4.4-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.3-01]
- Grab samba domain master setting from smb service, not from SambaDomainMaster.
  [charlieb 3160]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.2-01]
- Add missing bootstrap-console-save event directory.

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.1-01]
- Test build to verify CVS conversion.

* Tue Dec 11 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- rollRPM: Rolled version number to 1.4.0-01. Includes patches up to 1.3.0-02.

* Tue Dec 11 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Fix pptpd-restart so that it won't log FAILED when it tries to shut down
  a pptpd which is not running.

* Mon Nov 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-09.

* Thu Oct 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-09]
- Add conf action to bootstrap-console-save event

* Fri Aug 17 2001 gordonr
- [1.2.0-08]
- Autorebuild by rebuildRPM

* Mon Jul 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-07]
- Don't check for /var/lock/subsys/pptpd - pptp is managed by init
  and this lock file will not always be created

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-06]
- Including GPL license with package

* Sat Apr 28 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-05]
- Only advertise WINS address if configured as Samba Domain Master.

* Tue Apr 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- Fix problem in dhcpd.conf template with non C class addresses.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Add "ipparam pptpd" to ppp options file.
- Remove obsolete post-restore event.
- Removed %postun script.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-29.


* Thu Jan 18 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-29]
- Allow admin to use PPTP 

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-28]
- Users now have a property of PPTPAccess - defaults to allowed
  Set to "off" to disable individual user access to PPTP

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-27]
- Backed out serviceControl() - it doesn't handle non-initscript startup yet

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-26]
- Fix call to serviceControl()

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-25]
- Use serviceControl()

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-24]
- Check pptpd status is defined in masq template

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-23]
- Set listenip to $LocalIP in serveronly mode - thanks Karl Ponsonby

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-22]
- Explictly list users in chap-secrets, but only if their password is set

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-21]
- Added /etc/ppp/ip-up.local

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-20]
- /etc/ppp/chap-secrets is required for pptp

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-19]
- Fixed remoteip calculation - missing pptpd/sessions

* Sun Jan 07 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-18]
- Fix remote address calculation in /etc/pptpd.conf
- Disable deflate and bsdcomp in PPP config - can't combine compression 
  protocols successfully yet.

* Sat Jan 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-17]
- Only run %postun script if in runlevel 7

* Sat Jan 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-16]
- Adjust pptpd configuration to force mppe
- Add chap secrets fragment to look up passwords in smbpasswd file

* Mon Dec 18 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-15]
- Allow packets to traverse PPTPD interfaces :-)

* Thu Dec 14 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-14]
- Added pptpd-restart action, and called this and pptpd-conf in ip-change event

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-13]
- Guard dhcpd.conf fragment in case pptpd is disabled

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-12]
- use emsith::db in pptpd-conf

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-11]
- Added pptpd-conf into remoteaccess-update

- [1.1.0-10]
- Added pptpd-conf-startup to initialise services entry
- Renamed conf-pptpd -> pptpd-conf

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-9]
- Made output format consistent other fragments

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-8]
- Removed closing semi-colon and comment from dhcpd output

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-7]
- Changed to use single option "sessions" instead of ipstart/ipend
- Steal addresses from dhcpd range

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-6]
- Added GRE/PPTP packet filter fragment
- Used range specification for remoteip list

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-5]
- Fixed generation of remoteip list

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-4]
- Run at run level 7
- Revised generation of remoteip list - range format is strange...

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-3]
- Removed comments from output files
- Fixed remoteip generation
- Removed speed.orig file

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-2]
- Fixed inittab fragment

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-1]
- Rolled version and tarball, including patches to 0.1-4

* Tue Dec 12 2000 Charlie Brady <charlieb@e-smith.com>
- Remove .orig file
- Add service configuration database data for pptpd.
- Add configuration event to post-restore.

* Mon Nov 13 2000 Charlie Brady <charlieb@e-smith.com>
- Strip comments from /etc/pptpd.conf file - they are still in
  the templates
- Remove %postun section

* Mon Nov 13 2000 Charlie Brady <charlieb@e-smith.com>
- Change "name" to $SystemName rather than Samba Workgroup
- Add domain setting.

* Mon Nov 13 2000 Charlie Brady <charlieb@e-smith.com>
- Be more verbose in pptpd.conf templates

* Mon Nov 13 2000 Charlie Brady <charlieb@e-smith.com>
- initial

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
for i in console-save \
     post-install \
     post-upgrade \
     bootstrap-console-save \
         ip-up.pptpd \
         ip-down \
         ip-change \
     workgroup-update \
     remoteaccess-update \
     password-modify \
     user-create \
         user-modify \
     user-delete
do
    mkdir -p root/etc/e-smith/events/$i
done
perl createlinks
# Manage supervise and multilog.
mkdir -p root/service
ln -s ../var/service/pptpd root/service/pptpd
mkdir -p root/var/service/pptpd/supervise
touch root/var/service/pptpd/down
mkdir -p root/var/service/pptpd/log/supervise
mkdir -p root/var/log/pptpd

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/pptpd 'attr(01755,root,root)' \
    --file /var/service/pptpd/down 'attr(0644,root,root)' \
    --file /var/service/pptpd/run 'attr(0755,root,root)' \
    --dir /var/service/pptpd/log 'attr(0755,root,root)' \
    --dir /var/service/pptpd/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/pptpd/supervise 'attr(0700,root,root)' \
    --file /var/service/pptpd/log/run 'attr(0755,root,root)' \
    --dir /var/log/pptpd 'attr(2750,smelog,smelog)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
