ure the nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the /var/www/html/index.html file contains the correct content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Ensure the nginx default site configuration is correct
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Ensure the nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
  require   => Package['nginx'],
}

