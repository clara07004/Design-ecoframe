# instalar-memoria.ps1
# Copia os arquivos de memoria do repositorio para o diretorio correto do Claude Code
# Rodar uma vez apos clonar o repositorio: .\instalar-memoria.ps1

$projectPath = $PSScriptRoot
# Codificacao do caminho igual a do Claude Code: cada caractere que nao seja
# letra/numero/hifen vira '-' (inclui ':', '\', espaco e '_'). NAO colapsa hifens
# consecutivos (ex.: "C:\" -> "C--"). No Windows o nome e case-insensitive.
$encoded = $projectPath -replace '[^A-Za-z0-9-]', '-'
$destination = "$env:USERPROFILE\.claude\projects\$encoded\memory"

Write-Host ""
Write-Host "Projeto detectado: $projectPath"
Write-Host "Destino da memoria: $destination"
Write-Host ""

if (-not (Test-Path $destination)) {
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    Write-Host "Pasta criada: $destination"
}

$source = Join-Path $projectPath "_memoria"
$files = Get-ChildItem -Path $source -Filter "*.md"

foreach ($file in $files) {
    Copy-Item -Path $file.FullName -Destination $destination -Force
    Write-Host "  copiado: $($file.Name)"
}

Write-Host ""
Write-Host "$($files.Count) arquivos de memoria instalados."
Write-Host "Abra o Claude Code neste repositorio - o agente ja estara calibrado."
Write-Host ""
