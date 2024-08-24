# Increasing the limit of hard and soft of the /etc/security/limits.conf

#Increase limit
exec { 'Increase-hard-limit':
    command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/bin/:/bin/',
}

#Increase soft limit
exec { 'Increase-soft-limit':
    command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/bin/:/bin/',
}
