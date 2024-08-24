# A puppet code that increases ULIMIT from 15 to 4096

#Increase ULIMIT
exec { 'Increase-ulimt':
    command => '/bin/sed -i \'s/ULIMIT=-n" 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

# restart nginx
exec { 'nginx-restart':
    command => '/usr/sbin/service nginx restart'
}
