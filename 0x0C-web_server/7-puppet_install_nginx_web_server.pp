# Configure an Nginx server using Puppet

# Ensure the nginx package is installed
package { 'nginx':
  ensure  => installed,
}
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me htps://wwww.youtube.come/watch?vQH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

service {'nginx':
  ensure  => running,
  require => package['nginx']
}
