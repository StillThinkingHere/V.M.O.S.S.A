$iconPath = Join-Path -Path $PSScriptRoot -ChildPath 'pops.ico'
$websiteUrl = "https://ionalegoman.wixsite.com/avocado"
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$notify = New-Object System.Windows.Forms.NotifyIcon
$notify.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($iconPath)
$notify.Visible = $true
$notify.Text = "Py OS"
$notify.Add_Click({
    Start-Process $websiteUrl
    $notify.Dispose()
})
$notify.ShowBalloonTip(10000, 'Help', 'You can get more info on us at https://ionalegoman.wixsite.com/avocado', [System.Windows.Forms.ToolTipIcon]::Info)
