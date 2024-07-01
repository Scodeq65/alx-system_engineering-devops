# This manifest kills a process named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -f /bin/bash\ ./killmenow',
  path    => '/usr/bin/',
}