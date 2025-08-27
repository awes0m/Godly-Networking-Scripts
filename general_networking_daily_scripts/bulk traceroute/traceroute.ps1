$servers = get-content 'hostlist.txt'
if (Test-Path -Path result_trace.txt)
{
Remove-Item result_trace.txt      
New-Item result_trace.txt
add-content result_trace.txt '"Ip_Host","Tracedata"'
}

else
{
New-Item result_trace.txt
add-content result_trace.txt '"Ip_Host","Tracedata"'
}
foreach ( $server in $servers ) {
		
		if ((test-Connection -ComputerName $server -Count 2 -Quiet) -eq $true ) { 
				
			write-Host "$server is alive and Pinging `n " -ForegroundColor Green
			add-content result_trace.txt "server  is alive and Pinging`n`n" 
			Write-Host "========================= Starting Traceroute for $server ========== `n" -ForegroundColor Yellow
			add-content result_trace.txt "========================= Starting Traceroute for $server ==========`n`n"
			tracert -d  $server
            $t=tracert -d  $server	
			add-content result_trace.txt "$t"
			Write-Host "========================= Traceroute for $server Done ========== `n`n" -ForegroundColor Yellow
			add-content result_trace.txt "========================= Traceroute for $server Done ==========`n "
		
					} else { 
					
					Write-Host "========================= Testing Done for all Servers ========== `n" -ForegroundColor Green
					"`n"
					"`n"
					
					write-Host " `"Computer $server not Pinging, i am going to do traceroute now.`" `n`n" -ForegroundColor RED 
					add-content result_trace.txt "server not Pinging, i am going to do traceroute now `n."
		
					Write-Host "========================= Starting Traceroute for $server ========== `n " -ForegroundColor Yellow
					add-content result_trace.txt "========================= Starting Traceroute for $server ==========`n`n"
					tracert -d  $server 
					$t=tracert -d  $server	
			        add-content result_trace.txt "$t"
					Write-Host "========================= Traceroute for $server Done ========== `n" -ForegroundColor Yellow
			        add-content result_trace.txt "========================= Traceroute for $server Done ==========`n "
					}
}
Write-Host "========================= end of script ========== `n" -ForegroundColor Red
Invoke-Item "result_trace.txt" 