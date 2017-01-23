#!/bin/bash


rm -rf /var/www/html/public_el5_latest.old
cd /var/www/html
cp -rp /var/www/html/public_el5_latest /var/www/html/public_el5_latest.old
/usr/bin/reposync -r public_el5_latest  -p /var/www/html
/usr/bin/reposync -r puppetlabs-deps -p /var/www/html
/usr/bin/reposync -r puppetlabs-products -p /var/www/html

/usr/bin/createrepo -v /var/www/html/public_el5_latest
/usr/bin/createrepo -v /var/www/html/puppetlabs-deps
/usr/bin/createrepo -v /var/www/html/puppetlabs-products
