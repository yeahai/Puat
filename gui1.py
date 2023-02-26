# 2023/1/28 17:49
# 你好，夜嗨大帅比
import sys
from data_save.text import DB
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QHeaderView,QLineEdit,QMessageBox,QStatusBar
from PyQt5.QtWidgets import QPushButton,QTextBrowser,QTreeWidget,QListWidget,QListWidgetItem,QLabel,QTableWidgetItem,QTableWidget,QStackedWidget


class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        # 文本输入空间
        self.txt_text = None

        # 表格
        self.table_widget = None

        # 窗体标题
        self.setWindowTitle("Puat")
        # 窗体尺寸
        self.setFixedSize(1024,512)

        # 窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 创建布局
        layout = QHBoxLayout()


        # layout.addLayout(self.init_ce_bian())

        # layout.addLayout(self.init_content_area())

        self.list_right_bar = QListWidget()
        self.list_right_bar.insertItem(0,"三")
        self.list_right_bar.insertItem(1,"Home")
        self.list_right_bar.insertItem(2,"Url_Coll")
        self.list_right_bar.insertItem(3,"Analyzer")



        # 给窗体设置元素的排列方式
        self.setLayout(layout)

    def init_ce_bian(self):
        # 1.创建左侧侧边菜单布局
        ce_bian_bar = QVBoxLayout()
        ce_list_bar = QListWidget()

        # 创建侧边按钮
        btn_san = QPushButton("三")
        btn_home = QPushButton("Home")
        btn_analy = QPushButton("Analy")

        # 加入侧边栏
        ce_bian_bar.addWidget(btn_san)
        ce_bian_bar.addWidget(btn_home)
        ce_bian_bar.addWidget(btn_analy)
        ce_bian_bar.addStretch(9)

        return ce_bian_bar

    def text_search(self):
        ## 文本输入
        H_bar = QHBoxLayout()
        txt_text = QLineEdit()
        txt_text.setPlaceholderText("请输入网址，例如：www.baidu.com; 或者要查询的组件漏洞,例如：Ubuntu")
        self.txt_text = txt_text

        ## 搜索按钮
        btn_search = QPushButton("指纹搜索")

        btn_search.clicked.connect(self.event_sec_click)

        # 3.文本空间加入模块
        ## 文本区加入整个模块
        H_bar.addWidget(txt_text)
        H_bar.addWidget(btn_search)
        # content_bar.addWidget(text_content)

        return H_bar

    def init_content_area(self):
        # 创建右侧整体布局
        content_bar = QVBoxLayout()


        # 表格创建
        table_widget = QTableWidget(0,8)
        self.table_widget = table_widget

        table_hearder = [
            {"field": "eid", "text": "Eid", },
            {"field": "title", "text": "Title", },
            {"field": "author", "text": "Author", },
            {"field": "publish_time", "text": "Publish_time", },
            {"field": "platform", "text": "Platform", },
            {"field": "type", "text": "Type", },
            {"field": "exploit_url", "text": "Exp_url", },
            {"field": "download_url", "text": "Down_url", },
        ]


        for idx, info in enumerate(table_hearder):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx,item)

        db =DB()
        result =db.search_all()

        # 获取数据库中的数据,并在表格中显示
        current_row_count = table_widget.rowCount()

        self.content_to_table(result,current_row_count)


        # H_bar的文本区和搜索按钮的Layout 加入content_bar 之上
        content_bar.addLayout(self.text_search())

        # 增加表格区域到布局中
        content_bar.addWidget(table_widget)


        # 加入右侧整个布局
        content_bar.addLayout(self.foot_bar())

        return content_bar


    def foot_bar(self):
        # 底部的信息栏
        foot_bar = QHBoxLayout()

        # author
        foot_content_author = QLabel("By: Yeahii")
        # version
        foot_content_version = QLabel("v1.0")
        # 底部信息
        foot_bar.addWidget(foot_content_author)
        foot_bar.addStretch()
        foot_bar.addWidget(foot_content_version)
        return foot_bar

    # 搜索按钮事件
    def event_sec_click(self):
        # 获取文本框中的内容
        db = DB()
        text = self.txt_text.text()
        text = text.strip()
        if not text:
            result = db.search_all()
            # 把行数清零
            self.table_widget.setRowCount(0)
            # 把内容全部清除，为下面更新数据做准备
            self.table_widget.clear()
            current_row_widget = self.table_widget.rowCount()
            self.table_widget.clearContents()
            self.content_to_table(result,current_row_widget)
            return
        if "www." not in text:
            result1 = db.search_all(text)

            # 把行数清零
            self.table_widget.setRowCount(0)
            # 把内容全部清除，为下面更新数据做准备
            self.table_widget.clear()
            current_row_count = self.table_widget.rowCount()

            self.table_widget.clearContents()
            self.content_to_table(result1,current_row_count)
    def content_to_table(self,result,current_row_count):
        for row_list in result:
            self.table_widget.insertRow(current_row_count)
            # 写入数据
            for i, ele in enumerate(row_list):
                cell = QTableWidgetItem(str(ele))
                # 表格内容不能被修改
                if i in [0, 1, 2, 3, 4, 5]:
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table_widget.setItem(current_row_count, i, cell)
            current_row_count += 1
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    qssStyle = '''
             QPushButton{
                 font-family:"JetBrainMono Nerd Font";
                 text-align:top;
                 background:#6DDF6D;border-radius:5px;
                 border:none;
                 font-size:13px;
             }
             QListWidget {
                 outline: none;
                 font-family:"JetBrainMono Nerd Font";
                 font-size:20px;
                 text-align: center
             }
          '''
    window.setStyleSheet(qssStyle)
    sys.exit(app.exec_())