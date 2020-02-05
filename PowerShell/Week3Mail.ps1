function getIP {
(Get-NetIPAddress).IPAddress | Select-String "192*"
}
function getTheDate {
get-date -DisplayHint date
}


$IP = getIP
$User = $env:UserName
$Username = $env:COMPUTERNAME
$Version = $(get-host).Version.Major
$Date = getTheDate
$Body = "This machines IP is $IP. User is $User. Hostname is $Username. Powershell version $Version. Todays date is $Date."

#Write-Host($BODY)


Send-MailMessage -To "mic8786@mail.com" -From "smtp@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

Write-Host("email sent")