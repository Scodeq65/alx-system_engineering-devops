# This Puppet manifest creates a file at /tmp/school with specific properties.

file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}