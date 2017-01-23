#!/bin/bash


rm -rf  /var/www/html/public_ol6_latest.old/public_ol6_latest/getPackage/*
rm -rf /var/www/html/public_ol6_latest.old

cp -rp /var/www/html/public_ol6_latest /var/www/html/public_ol6_latest.old

/usr/bin/reposync -r public_ol6_latest -p /var/www/html
/usr/bin/reposync -r public_ol6_UEK_base -p /var/www/html
/usr/bin/reposync -r puppetlabs-deps -p  /var/www/html
/usr/bin/reposync -r puppetlabs-products -p  /var/www/html

/usr/bin/createrepo -v /var/www/html/public_ol6_latest
/usr/bin/createrepo -v /var/www/html/public_ol6_UEK_base
/usr/bin/createrepo -v /var/www/html/puppetlabs-deps
/usr/bin/createrepo -v /var/www/html/puppetlabs-products
