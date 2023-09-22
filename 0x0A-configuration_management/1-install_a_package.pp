# Ensure pip3 is installed
package { 'flask':
  ensure   => 'installed',
  provider => 'pip3'
}
