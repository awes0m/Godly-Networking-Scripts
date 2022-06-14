$servers = get-content 'hostlist.txt'
if (Test-Path -Path result.csv)
{
Remove-Item result.csv        
New-Item result.csv
add-content result.csv '"Ip_Number","Status"'
}

else
{
New-Item result.csv
add-content result.csv '"Ip_Number","Status"'
}

foreach ( $server in $servers ) {
		
		if ((test-Connection -ComputerName $server -Count 2 -Quiet) -eq $true ) { 
				
			write-Host "$server is alive and Pinging `n " -ForegroundColor Green
			$OtherContent = [PSCustomObject]@{Ip_Number = $server ; Status = "YES" }
            $OtherContent | Export-CSV -Path result.csv -NoTypeInformation -Append
		
					} else { 
					
					Write-Host "========================= Testing Done for all Servers ========== `n" -ForegroundColor Green
					
					
					write-Host " `"Computer $server not Pinging`" `n`n" -ForegroundColor RED 
					$OtherContent = [PSCustomObject]@{Ip_Number = $server ; Status = "NO" }
                    $OtherContent | Export-CSV -Path result.csv -NoTypeInformation -Append
					}
}
Invoke-Item "result.csv" 