# A puppet manuscript to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_edit}",
  path    => ['/bin','/usr/bin']
}
