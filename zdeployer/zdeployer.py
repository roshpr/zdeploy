from zdeployer.commands.download_zip import DownloadZip
from zdeployer.executors.prehook_executor import PreHookExecutor
from zdeployer.core.Invoker import Invoker


def main():
    prehook_recv = PreHookExecutor()
    downloadzip_cmd = DownloadZip()
    invoker = Invoker()
    invoker.store_command(downloadzip_cmd)
    invoker.invoke_executor(prehook_recv)

if __name__ == "__main__":
    main()