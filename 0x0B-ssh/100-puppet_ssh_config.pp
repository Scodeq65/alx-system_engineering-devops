#!/usr/bin/env puppet

# Ensure the .ssh directory exists with proper permissions
file { 'etc/ssh/ssh_config':
  ensure => present,
}

# Configure the SSH client to use the private key ~/.ssh/school
file_line { 'Identity_file':
  path    => '/etc/ssh/ssh_config'
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile ',
  replace => true
}

# Configure the SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication ',
  replace => true
}