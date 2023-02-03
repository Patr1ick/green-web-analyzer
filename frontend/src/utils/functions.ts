export default function convertBytesToString(bytes: number) {
    if (bytes === 0) {
        return "0 B";
    }
    const endings = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
    var i = Math.floor(Math.log(bytes) / Math.log(1024)),
        sizes = endings;
    var text = (bytes / Math.pow(1024, i)).toFixed(2);
    return text + " " + sizes[i];
}
