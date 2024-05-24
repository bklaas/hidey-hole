function removeOldGoogleSheets() {
  // Set the folder ID and the time threshold
  var folderId = 'YOUR_FOLDER_ID'; // Replace with your folder ID
  var twoMonthsAgo = new Date();
  twoMonthsAgo.setMonth(twoMonthsAgo.getMonth() - 2);

  // Get the folder
  var folder = DriveApp.getFolderById(folderId);

  // Get all Google Sheets in the folder
  var files = folder.getFilesByType(MimeType.GOOGLE_SHEETS);

  // Loop through all files and check the last updated date
  while (files.hasNext()) {
    var file = files.next();
    var lastUpdated = file.getLastUpdated();

    // If the file hasn't been updated in the last two months, move it to trash
    if (lastUpdated < twoMonthsAgo) {
      file.setTrashed(true);
      Logger.log('Moved to trash: ' + file.getName());
    }
  }
}
