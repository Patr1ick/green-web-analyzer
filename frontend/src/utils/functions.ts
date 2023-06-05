export default function convertBytesToString(bytes: number) {
    if (bytes === 0) {
        return "0 B";
    }
    const endings = [
        "B",
        "KiB",
        "MiB",
        "GiB",
        "TiB",
        "PiB",
        "EiB",
        "ZiB",
        "YiB",
    ];
    var i = Math.floor(Math.log(bytes) / Math.log(1024)),
        sizes = endings;
    var text = (bytes / Math.pow(1024, i)).toFixed(2);
    return text + " " + sizes[i];
}
