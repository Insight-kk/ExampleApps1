from typing import override,Callable
from ikkVisualKit import WindowBaseModan, DialogGridSelecter
# ==========================================================
# 
# ==========================================================
class MainWindow(WindowBaseModan):
    # アプリケーション設定ファイル
    CONFIG_FILE = "config.json"
    
    def __init__(self):
        super().__init__(
            title="EsampleApp1",  #アプリ名
            version="1.0.1",       #バージョン
            size=(720, 320),       #ウィンドウサイズ
            icon_path="resources/icon.ico", #アイコンパス（.ico推奨）
            tray_app=False,      #常駐アプリにしたいならTrue
            fixed_size=True     #ウィンドウサイズを固定するならTrue
            )
        self.on_post: Callable = None  #UIからロジック方向への伝搬コールバック
        self.isAlwaysOnTop = False
    #----------------------------------------------
    def _build(self, root):
        super()._build(root)
        #------------------------------------------
        #パーツの配置
        #------------------------------------------
        #中大ボタン
        self.btnRecipe   = self.make_ActionButton(32, 16 , image_key="recipe.dio",size_rank=2,text="レシピ選択")
        self.btnStart    = self.make_ActionButton(176, 16 , image_key="start.dio",size_rank=2,text="検査スタート")
        self.btnStop     = self.make_ActionButton(320, 16 , image_key="stop.dio",size_rank=1,text="中止")
        self.btnSave     = self.make_ActionButton(432, 16 , image_key="save.dio" ,size_rank=1,text="保存")
        self.btnClear    = self.make_ActionButton(544, 16 , image_key="clear.dio",size_rank=1,text="クリア")
        #小ボタン
        self.btnSetting  = self.make_ActionButton(656 ,16+48*0,  image_key="setting.dio")
        self.btnFolder   = self.make_ActionButton(656 ,16+48*1, image_key="folder.dio")
        self.btnHelp     = self.make_ActionButton(656 ,16+48*2, image_key="help.dio")
        self.btnMostTop  = self.make_ActionButton(656 ,16+48*3, image_key="alwaysTop.dio")
        #ラベル＆テキストボックス
        self.tblHINSYU   = self.make_labelTextBox(16, 128  ,"製品名称"   , width=368 ,is_required=True)
        #ドロップダウンリスト
        self.dropdown    = self.make_DropdownList(16, 96, width=620, values=[], default_index=0,justify="right",additional=True)
        # ログビューを作成
        self.logTerminal = self.make_LogTerminal(x=16, y=224, width=624) 
        #ON/OFFステータス
        self.statusReader= self.make_StatusIcon(16, 320, image_key="handyReader.dio", on_tooltip="バーコードリーダー:接続中",off_tooltip="バーコードリーダー:未接続",size_rank=0)
        #------------------------------------------
        #ツールチップ設定（マウスホバー時の説明）
        #------------------------------------------
        self.btnRecipe.tooltip_text = "レシピを選択してアップロードします"
        #------------------------------------------
        #ハンドラ登録
        #------------------------------------------
        self.btnMostTop.OnClicked += lambda: setattr(self, 'isAlwaysOnTop', not self.isAlwaysOnTop)  # 常に最前面の切り替え
        self.logTerminal.OnError += lambda: self.ErrorBlink()      # ログでエラーが出たら点滅させる
        self.logTerminal.OnWarning += lambda: self.WarningBlink()  # ログで警告が出たら点滅させる
    #----------------------------------------------
    @override
    def _loadAppState(self):
        """ウインドウ生成時に呼ばれる関数"""
        try:
            pass #
        except Exception as e:
            pass #
    #----------------------------------------------
    @override
    def _backupAppState(self):
        """ウインドウの状態保存（基底から呼ばれる）"""
        try:
            pass #
        except Exception as e:
            pass #
# ==========================================================
# テスト
# ==========================================================
if __name__ == "__main__":
    ui = MainWindow() #ウインドウ生成
    ui.btnRecipe.OnClicked += lambda: ui.logTerminal.Print("レシピボタンが押されました",level="INFO")
    ui.btnFolder.OnClicked += lambda: ui.logTerminal.Print("フォルダボタンが押されました",level="INFO")
    ui.btnSetting.OnClicked += lambda: ui.logTerminal.Print("設定ボタンが押されました",level="ERROR")

    ui.show_window() #ウインドウ表示
    ui.run() #GUI開始

