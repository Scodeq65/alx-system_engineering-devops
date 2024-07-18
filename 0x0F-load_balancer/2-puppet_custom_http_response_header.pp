#!/usr/bin/env bash
# Create an Ubuntu header using puppet

exec { 'http header':
  command  => '
    apt-get update -y &&
    apt-get install nginx -y &&
    sed -i "/server_name _/a add_header X-Serverd-By HOSTNAME;" /etc/nginx/sites-available/default &&
    service nginx restart',
  provider => 'shell',
}
