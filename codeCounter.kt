import java.io.File

fun main() {
    print("please enter the file directory you want to compute: ")
    var targetDir = readLine()
    val f = File(targetDir)
    val rComment = Regex("""^(\/\/|#+ |\/\*|\*\ ).*""")
    val r = Regex("""^[\w\s\{\}\[\]\#\_\(\)\?\:\,\;\"\'\+\-\*\/\@\`\!\$\%\^\&\=\\\|\<\>\.\~]+""")
    var fileNum = 0
    var fileLines = 0

    val fileTreeWalk = f.walk()
    fileTreeWalk.iterator().forEach { file ->
        var flag = false
        if (file.isFile and file.canRead()) {
            file.forEachLine {
                if (rComment.matches(it)){
                    return@forEachLine
                }
                if (r.matches(it)) {
                    flag = true
                    fileLines++
                }
            }
            if (flag){
                fileNum++
                println("file++")
            }
        }
    }
    println("total file num: $fileNum")
    println("total file lines: $fileLines")
}