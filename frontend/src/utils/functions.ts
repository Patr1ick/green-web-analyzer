export default function convertBytesToString (bytes: number) {
    var i = Math.floor(Math.log(bytes) / Math.log(1024)), sizes = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
    var text = (bytes / Math.pow(1024, i)).toFixed(2)
    return  text + " " + sizes[i];
}