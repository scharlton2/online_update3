function Component()
{
    // default constructor
}

Component.prototype.createOperations = function()
{
	// call default implementation to actually install files
	component.createOperations();

	if (systemInfo.productType === "windows") {
		install_runtime("2013", "12.0", 21005); // Note: 21005 displays as 30501
		install_runtime("2017", "14.0", 26706);

	}
	delete_runtime("2013");
	delete_runtime("2017");
}

function install_runtime(vs_ver, major_subkey, build)
{
	var executable = "vc" + vs_ver + "_vcredist_x64.exe";  // ie vc2013_vcredist_x64.exe
	var runtime = "Microsoft Visual C++ " + vs_ver + " Runtime Bld " + build.toString();
	var key = "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\VisualStudio\\" + major_subkey + "\\VC\\Runtimes\\x64"

	// check if major version is installed
	var installed = installer.execute("reg", new Array("QUERY", key, "/v", "Installed"))[0];
	if (installed) {
		// check build number
		var bld = installer.execute("reg", new Array("QUERY", key, "/v", "Bld"))[0];
		var elements = bld.split(" ");
		bld = parseInt(elements[elements.length-1])
		var year_string = vs_ver
		if (year_string === "2015" || year_string === "2017") {
			// Note: both 2015 and 2017 use the 14.0 major subkey
			year_string = "2015/2017"
		}
		console.log("Found Microsoft Visual C++ " + year_string + " Runtime Bld " + bld.toString());
		if (bld < build) {
			console.log("Installing " + runtime + ": " + executable + " /quiet /norestart");
			component.addOperation("Execute", "@TargetDir@/" + executable, "/quiet", "/norestart");
		}
		else {
			console.log("No need to install " + runtime);
		}
	}
	else {
		console.log("Installing " + runtime + ": " + executable + " /quiet");
		component.addOperation("Execute", "@TargetDir@/" + executable, "/quiet");
	}
}

function delete_runtime(vs_ver)
{
	var executable = "vc" + vs_ver + "_vcredist_x64.exe";  // ie vc2013_vcredist_x64.exe
	component.addOperation("Delete", "@TargetDir@/" + executable);
}
