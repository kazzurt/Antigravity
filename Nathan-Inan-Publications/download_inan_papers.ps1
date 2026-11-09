<#
    download_inan_papers.ps1
    Downloads the freely-available publications of Nader A. ("Nathan"/"Nate") Inan
    into the same curated folder as this script.

    Source list: INSPIRE-HEP (https://inspirehep.net/authors/2116927), July 2026.
    15 arXiv preprints + 1 PhD thesis (eScholarship). The only item omitted is a
    2025 Phys. Rev. A "Reply to Comment" that has no open-access version.

    Just double-click "Download-Inan-Papers.bat", or right-click this file ->
    "Run with PowerShell".
#>

$ProgressPreference = 'SilentlyContinue'   # makes Invoke-WebRequest fast on PS 5.1
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}

$UA   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$dest = $root
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Write-Host ""
Write-Host "Downloading Nathan (Nader A.) Inan publications" -ForegroundColor Cyan
Write-Host "  -> $dest" -ForegroundColor Cyan
Write-Host ""

# arXiv papers: Id = arXiv identifier, File = target filename
$papers = @(
    @{ Id='2512.15935'; File='Inan-2025-AC-Stark-Time-Dependent-Aharonov-Bohm-Ring-2512.15935.pdf' }
    @{ Id='2505.11560'; File='Inan-2025-Cosmological-Constant-Bose-Einstein-Distribution-2505.11560.pdf' }
    @{ Id='2502.07613'; File='Inan-2025-Modified-Gravity-Signatures-Gravitational-Aharonov-Bohm-2502.07613.pdf' }
    @{ Id='2409.13780'; File='Inan-2024-Temporal-Pound-Rebka-as-Gravitational-Aharonov-Bohm-2409.13780.pdf' }
    @{ Id='2405.05269'; File='Inan-2024-Modified-Gravity-Entropic-Gravity-Graviton-Mass-2405.05269.pdf' }
    @{ Id='2404.03872'; File='Inan-2024-Graviton-Mass-Dark-Energy-Superconducting-Medium-2404.03872.pdf' }
    @{ Id='2311.07764'; File='Inan-2023-Gravitational-Aharonov-Bohm-Effect-2311.07764.pdf' }
    @{ Id='2309.00795'; File='Inan-2023-Cosmological-Constant-Spacetime-Uncertainty-2309.00795.pdf' }
    @{ Id='2212.03437'; File='Inan-2022-Scalar-Electric-Aharonov-Bohm-Energy-Level-Shift-2212.03437.pdf' }
    @{ Id='2201.12969'; File='Inan-2022-Superconductor-GEM-Meissner-Effects-2201.12969.pdf' }
    @{ Id='2207.08809'; File='Inan-2017-Detecting-GWs-Phonon-Zero-Point-Energy-Superconductor-2207.08809.pdf' }
    @{ Id='2207.08062'; File='Inan-2017-Interaction-of-Gravitational-Waves-with-Superconductors-2207.08062.pdf' }
    @{ Id='1501.07665'; File='Inan-2015-Neutrino-Induced-Decoherence-Nuclear-Decay-Rates-1501.07665.pdf' }
    @{ Id='1411.3627';  File='Inan-2014-Scalar-Aharonov-Bohm-3D-Faraday-Cage-1411.3627.pdf' }
    @{ Id='1301.4270';  File='Inan-2013-Gravitational-Aharonov-Bohm-Parametric-Oscillators-GW-1301.4270.pdf' }
)

# Verify a file exists, is non-trivial, and actually begins with the %PDF magic bytes.
function Test-Pdf($path) {
    if (-not (Test-Path $path)) { return $false }
    if ((Get-Item $path).Length -lt 8KB) { return $false }
    try {
        $fs = [System.IO.File]::OpenRead($path)
        $buf = New-Object byte[] 5
        [void]$fs.Read($buf, 0, 5); $fs.Close()
        return ([System.Text.Encoding]::ASCII.GetString($buf)).StartsWith('%PDF')
    } catch { return $false }
}

function Get-File($url, $path) {
    for ($try = 1; $try -le 3; $try++) {
        try {
            Invoke-WebRequest -Uri $url -OutFile $path -UserAgent $UA -UseBasicParsing `
                -MaximumRedirection 5 -TimeoutSec 180 -ErrorAction Stop
            if (Test-Pdf $path) { return $true }
        } catch {
            if ($try -lt 3) { Start-Sleep -Seconds (2 * $try) }
        }
    }
    if (Test-Path $path) { Remove-Item $path -Force -ErrorAction SilentlyContinue }
    return $false
}

$ok = @(); $fail = @()
$n = 0
foreach ($p in $papers) {
    $n++
    $path = Join-Path $dest $p.File
    Write-Host ("[{0,2}/{1}] {2} ... " -f $n, $papers.Count, $p.Id) -NoNewline
    if (Test-Pdf $path) { Write-Host "already present" -ForegroundColor DarkGray; $ok += $p.File; continue }

    $got = $false
    foreach ($url in @("https://arxiv.org/pdf/$($p.Id)", "https://arxiv.org/pdf/$($p.Id).pdf")) {
        if (Get-File $url $path) { $got = $true; break }
    }
    if ($got) {
        Write-Host ("OK  ({0:N0} KB)" -f ((Get-Item $path).Length/1KB)) -ForegroundColor Green
        $ok += $p.File
    } else {
        Write-Host "FAILED" -ForegroundColor Red
        $fail += $p.Id
    }
    Start-Sleep -Seconds 3   # be polite to arXiv
}

# ---- PhD thesis (eScholarship, open access) ----
Write-Host "[thesis] eScholarship 3kt7z6kw ... " -NoNewline
$thesis = Join-Path $dest 'Inan-2017-PhD-Thesis-GR-Formulations-GWs-and-Superconductors.pdf'
$tgot = $false
foreach ($url in @(
    'https://escholarship.org/content/qt3kt7z6kw/qt3kt7z6kw.pdf',
    'https://escholarship.org/content/qt3kt7z6kw/qt3kt7z6kw_noSplash_d03836a03d6fc991a026e15f2a7b5653.pdf')) {
    if (Get-File $url $thesis) { $tgot = $true; break }
}
if ($tgot) {
    Write-Host ("OK  ({0:N0} KB)" -f ((Get-Item $thesis).Length/1KB)) -ForegroundColor Green
    $ok += (Split-Path $thesis -Leaf)
} else {
    Write-Host "skipped (grab manually: https://escholarship.org/uc/item/3kt7z6kw )" -ForegroundColor Yellow
}

Write-Host ""
Write-Host ("Done. {0} file(s) in {1}" -f $ok.Count, $dest) -ForegroundColor Cyan
if ($fail.Count) {
    Write-Host ("Could not fetch: {0}" -f ($fail -join ', ')) -ForegroundColor Red
    Write-Host "Re-run the script to retry just the missing ones." -ForegroundColor Red
}
Write-Host ""
Read-Host "Press Enter to close"
