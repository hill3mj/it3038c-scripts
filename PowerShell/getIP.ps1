function getIP {
(Get-NetIPAddress).IPAddress | Select-String "192*"
}

$IP= getIP

write-host("This machine's IP is $IP")