// Macro to list all .png images in the current working directory
dir = getDirectory("current");

list = getFileList(dir);
print("PNG Images in PWD:");
for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".png")) {
        print(dir + list[i]);
    }
}
