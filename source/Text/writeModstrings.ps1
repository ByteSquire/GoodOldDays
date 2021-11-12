# function for language resource folder
function Write-Modstring([string] $path) {
    $modstringpath = "$path\modstrings.txt"
    if (Test-Path -Path $modstringpath) { Clear-Content -Path $modstringpath }
    else { New-Item -ItemType File $modstringpath }

    $masteries = New-Object Collections.Generic.List[String]
    # add more lists here for different types

    Get-ChildItem -Path $path -Recurse -File -Filter "*.txt" |

    ForEach-Object {
        $filename = $_.FullName
        switch -Wildcard ($filename){
            '*masteries*' { 
                $masteries.Add($filename) 
            }
        }
    }

    ForEach ($mastery in $masteries)
    { 
        $tmpname = $mastery.Replace($path, "")
        Add-Content -Path $modstringpath -Value "//BEGIN $tmpname"
        Add-Content -Path $modstringpath -Value (Get-Content -Path $mastery)
        Add-Content -Path $modstringpath -Value "//END $tmpname`n"
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
    Write-Modstring($_.FullName)
}

$modstringpath = "modstrings.txt"
if (Test-Path -Path $modstringpath) { Clear-Content -Path $modstringpath }
else { New-Item -ItemType File $modstringpath }

Add-Content -Path $modstringpath -Value (Get-Content $path\modstrings.txt)
