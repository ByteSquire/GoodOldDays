# function for writing content to modstrings file
function Write-Content([string] $path, [string] $filepath, [hashtable] $replacements) {
    $tmpname = $filepath.Replace($path, "")
    $content = (Get-Content -Path $filepath)
    foreach($key in $replacements.Keys)
    {
        $content = $content.Replace($key, $replacements[$key])
    }
    Add-Content -Path $modstringpath -Value "//BEGIN $tmpname"
    Add-Content -Path $modstringpath -Value $content
    Add-Content -Path $modstringpath -Value "//END $tmpname`n"
}

# function for language resource folder
function Write-Modstring([string] $path) {
    $modstringpath = "$path\modstrings.txt"
    if (Test-Path -Path $modstringpath) { Clear-Content -Path $modstringpath }
    else { New-Item -ItemType File $modstringpath }

    $masteries = New-Object Collections.Generic.List[String]
    $defaultFiles = New-Object Collections.Generic.List[String]
    $miscTags = @{}
    # add more lists here for different types

    Get-ChildItem -Path $path -Recurse -File -Filter "*.txt" |

    ForEach-Object {
        $filename = $_.FullName
        switch -Regex ($filename){
            '.*modstrings.txt' {
                # ignore modstrings for specific languages
            }
            '.*masteries.*' { 
                $masteries.Add($filename) 
            }
            '.*MiscTags.txt' {
                $miscFile = $filename
                foreach($line in [System.IO.File]::ReadLines($filename))
                {
                    if ($line -like "//*") {
                        continue
                    }
                    $key = $line.split("=")[0]
                    $value = $line.split("=")[1].split("//")[0]
                    $miscTags[$key] = $value
                }
            }
            default {
                $defaultFiles.Add($filename)
            }
        }
    }

    ForEach ($mastery in $masteries)
    { 
        Write-Content $path $mastery $miscTags
    }

    ForEach ($defaultFile in $defaultFiles)
    {
        Write-Content $path $defaultFile $miscTags
    }

    if ($miscFile)
    {
        Write-Content $path $miscFile @{}
    }
}

# main
if ( $args.count -lt 1 ) { $path = "Text_EN" }
elseif ( $args.count -eq 1 ) { $path = $args[0] }
else {
    Write-Host "Too many arguments"
    Exit 1
}

if (!(Test-Path -Path $path)) {
    Write-Host "Specified path not found"
    Exit 1
}

Get-Childitem -Directory |

ForEach-Object {
    Write-Modstring $_.FullName
}

$modstringpath = "modstrings.txt"
if (Test-Path -Path $modstringpath) { Clear-Content -Path $modstringpath }
else { New-Item -ItemType File $modstringpath }

Add-Content -Path $modstringpath -Value (Get-Content $path\modstrings.txt)
