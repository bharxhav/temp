// Macro to crop all images into a square and save them to ./cropped
dir = getDirectory("current");
outputDir = dir + "cropped/";

if (!File.exists(outputDir)) {
    File.makeDirectory(outputDir);
}

list = getFileList(dir);
for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".tif") || endsWith(list[i], ".jpg") || endsWith(list[i], ".png") || endsWith(list[i], ".bmp")) {
        open(dir + list[i]);
        width = getWidth();
        height = getHeight();
        size = min(width, height);
        makeRectangle((width - size) / 2, (height - size) / 2, size, size);
        run("Crop");
        saveAs("Jpeg", outputDir + list[i]);
        close();
    }
}
