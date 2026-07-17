import asyncio  #必須
import logging  #必須

from ikkToolKit import (XmlSettingBase,LogReporter,DynamicBindData,AsyncSequencer,
    CsvLookupAutoReload,SerialReceiver,FileExplorer,ImageViewer
)
logger = LogReporter.setup(name="app", logDirctory="./", dumpLevel=logging.DEBUG, reportLevel=logging.INFO)

###############################################################################
class AppSetting(XmlSettingBase):
    """ XMLの要素値利用して、動的にクラス変数を生成する
    書き方  <公開プロパティ名>: (XMLのキー, 型, デフォルト値)
    """
    _PROPERTIES = {
        "RecipeDir": ("RecipeDirectory", str, ""),
        "SaveDir": ("StorageBaseDirectory", str, ""),
        "ComPortNo": ("ComPortNo", str, ""),# 優先するCOMポート
    }
    def __init__(self):
        super().__init__("setting.xml") #ファイル名
        self.load()
###############################################################################
class MainLogic:
    def __init__(self, debug_mode: bool = False):
        self.setting = AppSetting()
    #------------------------------------------------------
    def start(self,root=None):  #必須
        self._tkRoot = root
    #------------------------------------------------------
    def stop(self): #必須
        # self.reader.stop() #バーコードリーダーの受信停止
        pass
    #------------------------------------------------------
    def function1(self):
        logger.error(f"function1実行：エラーレベル")
    #------------------------------------------------------
    def function2(self):
        logger.warning(f"function1実行：ワーニング")
###############################################################################
#
###############################################################################
async def main():
    import msvcrt
    logic = MainLogic()
    logic.start()
    print("\nPress Ctrl+C to stop...")
    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getwche()  # キーを表示しながら取得
                # ここにキーに応じた処理を書く
                if key == 'q':
                    break #終了
                if key == '1':
                    logic.function1()
                if key == '2':
                    logic.function2()
                elif key == 'e':
                    print("\nEditing settings...")
                    logic.setting.show_editor()  #スタンドアロンで設定エディタが開く
                # elif key == '@': #有効なシリアルポート一覧を表示
                #     print(ReaderCH340.PortLists())
            await asyncio.sleep(0.1)  # CPU使用率を抑える
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\nStopping...")
    finally:
        logic.stop()
#-------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
    