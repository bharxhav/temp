// Macro to rotate original images 180 degrees and save them to ./inverted
dir = getDirectory("current");
outputDir = dir + "inverted/";

if (!File.exists(outputDir)) {
    File.makeDirectory(outputDir);
}

list = getFileList(dir);
for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".tif") || endsWith(list[i], ".jpg") || endsWith(list[i], ".png") || endsWith(list[i], ".bmp")) {
        open(dir + list[i]);
        run("Rotate 180 Degrees");
        saveAs("Jpeg", outputDir + list[i]);
        close();
    }
}
