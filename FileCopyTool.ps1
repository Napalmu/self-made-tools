#Even in 2024, when trying to upload local photos to iCloud, you can't upload folders. This is annoying.
#Imagine having 10 years worth of photos in tens if not hundreds of folders from a camera. You would have to go through every single folder and select the photos in that folder.
#I made this simple script to move all photos from the subfolders to a single folder. This way you can select all the photos at the same time. 

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
