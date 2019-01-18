import subprocess

def main(input_text):
    #input_text="a.txt"
    output_text="zunda_out.txt"

    command = "echo " + input_text + "| zunda > " +output_text                  #！ここに実行したいコマンドを書く！
    
    proc = subprocess.Popen(
        command,
        shell  = True,                            #シェル経由($ sh -c "command")で実行。
        stdin  = subprocess.PIPE,                 #1
        stdout = subprocess.PIPE,                 #2
        stderr = subprocess.PIPE)                 #3

    stdout_data, stderr_data = proc.communicate() #処理実行を待つ(†1)

    #print(stdout_data.decode("utf8"))  #標準出力の確認
    
if __name__=="__main__":
    input_text="a.txt"
    main(input_text)
    
