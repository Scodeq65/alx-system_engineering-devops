# Puppet code that correct a wordpress site 500 error to 200 Ok
# by editing the mistake line of code in /var/www/html/wp-settings.php

exec { 'fix-wp-server-error':
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/bin/'],
    onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
