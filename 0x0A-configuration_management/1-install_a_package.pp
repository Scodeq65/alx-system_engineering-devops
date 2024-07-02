# Install python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}

# Puppet manifest to install Flask 2.1.0 using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

#Install Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider =>  'pip3',
  require  => Package['Flask'],
}