# A manifest that kills a process named killmenow.
exec { 'killMeNow':
  command => '/usr/bin/pkill -f killmenow'
}