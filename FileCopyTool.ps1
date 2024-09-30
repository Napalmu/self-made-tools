param (
	[string]$rootFolder,
	[string]$destinationFolder
)

# Define the root folder
#$rootFolder = "C:\Path\To\Folder"

# Define the destination folder
#$destinationFolder = "C:\Path\To\Destination"

# Define desired extensions to copy
$fileExtensions = @(".jpg", ".jpeg", ".png")

# Get all files from the subfolders recursively
$files = Get-ChildItem -Path $rootFolder -Recurse -File  | Where-Object { $fileExtensions -contains $_.Extension.ToLower() }

# Initialize a counter to keep track of the number of files copied
$filesCopied = 0

# Loop through each file and move it to the destination folder
foreach ($file in $files) {
    try {
        Copy-Item -Path $file.FullName -Destination $destinationFolder -Force
	$filesCopied++
    }
    catch {
        Write-Warning "Failed to move $($file.FullName): $($_.Exception.Message)"
    }
}

Write-Output "All files copied to destination folder: $destinationFolder"
Write-Output "$filesCopied files were copied."


Read-Host "Press Enter to exit"
