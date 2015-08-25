function myFunction() {
  var folders = DriveApp.getFoldersByName('XYZ');
  while (folders.hasNext()) {
   var folder = folders.next();
    Logger.log(folder.getName() + ':' + folder.getId());
 }

}

