$ips = get-content hostlist.txt 
$ips

if (Test-Path -Path result_nslookup.csv)
{
Remove-Item result_nslookup.csv      
New-Item result_nslookup.csv
add-content result_nslookup.csv '"Ip_Host","Host_ip"'
}

else
{
New-Item result_nslookup.csv
add-content result_nslookup.csv '"Ip_Host","Host_ip"'
}
Foreach ($ip in $ips) 
{ 
 
[string]$name = nslookup $ip 2> $null | Select-String -pattern "Address:"
if ( ! $name ) { $name = "" } 
 
$name = $name.ToString() 
 
if ($name.StartsWith("Address:")) 
 
{ $name = (($name -Split ":")[-1]).Trim() } 
 
 else 
 
{ $name = "NOT FOUND" }
 
$OtherContent = [PSCustomObject]@{Ip_Host = $ip ; Host_ip = $name }
$OtherContent | Export-CSV -Path result_nslookup.csv -NoTypeInformation -Append

Echo "$ip `t $name" 

}
Invoke-Item "result_nslookup.csv" 