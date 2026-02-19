$b64File = "C:\Users\adria\propuestas-mvip\prototipos\b64.txt"
$outFile = "C:\Users\adria\propuestas-mvip\prototipos\semaforo-habilitacion\index.html"
$b64 = Get-Content $b64File -Raw
$bytes = [System.Convert]::FromBase64String($b64.Trim())
[System.IO.File]::WriteAllBytes($outFile, $bytes)
Write-Host "OK: File written to $outFile"
