function Component()
{}

Component.prototype.createOperationsForArchive = function(archive)
{
	component.addOperation("Extract", archive, "@TargetDir@/guis/rivmaker");
}

Component.prototype.createOperations = function()
{
	component.createOperations();

	component.addOperation("CreateShortcut", "@TargetDir@/guis/rivmaker/Rivmaker.exe",
		"@StartMenuDir@/Rivmaker.lnk", "workingDirectory=@TargetDir@/guis/rivmaker");
	component.addOperation("RegisterFileType", "rpro", "@TargetDir@\\guis\\rivmaker\\Rivmaker.exe" + " \"%1\"",
		"RivMaker Project file", "application/rivmaker",
		"@TargetDir@/guis/rivmaker/iconRivMakerFile.ico", "ProgId=RivMakerProject.rpro");
}
