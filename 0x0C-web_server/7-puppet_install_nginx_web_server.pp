# Puppet manifest to install and configure Nginx

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create the HTML directory
file { '/etc/nginx/html':
  ensure => 'directory',
}

# Configure the index.html file
file { '/etc/nginx/html/index.html':
  content => 'Hello World!',
}

# Configure the Nginx site
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
}

# Create a custom 404 page
file { '/etc/nginx/html/404.html':
  content => 'Ceci n\'est pas une page',
}

# Set up the redirection rule
nginx::resource::location { '/redirect_me':
  location => '~ ^/redirect_me',
  ensure   => 'present',
  proxy    => 'http://cuberule.com/',
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}


