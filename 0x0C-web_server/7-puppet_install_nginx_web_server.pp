# Install Nginx web server with Puppet
include stdlib

$content = "\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"

exec { 'update packages':
  command => '/usr/bin/apt-get update',
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx'],
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages'],
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World',  # Change content here
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $content,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html'],
}

